from __future__ import print_function
import os
import numpy as np
import nibabel as nib
from sklearn.cluster import KMeans

def create_patient_ids (base):
    patient_ids = []
    for folder in os.listdir(base):
        patient_ids.append(folder)
    return patient_ids

# Define function to create directory if it doesn't exist
def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# Define function to load NIfTI file
def load_nii(path):
    nii = nib.load(path)
    return nii.get_fdata(), nii.affine

# Define function to save NIfTI file
def save_nii(data, path, affine):
    nib.save(nib.Nifti1Image(data, affine), path)

# Define function to extract features
def extract_features(data):
    x_idx, y_idx, z_idx = np.where(data > 0)
    features = []
    for x, y, z in zip(x_idx, y_idx, z_idx):
        features.append([data[x, y, z], x, y, z])
    return np.array(features)

# Define function for KMeans clustering
def kmeans_cluster(data, n_clusters):
    features = extract_features(data)
    intensities = features[..., 0].reshape((-1, 1))
    kmeans_model = KMeans(n_clusters=n_clusters, init="k-means++",
                          random_state=7,
                          max_iter=1000, tol=1e-6).fit(intensities)

    labels = np.zeros(data.shape)
    for l, f in zip(kmeans_model.labels_, features):
        labels[int(f[1]), int(f[2]), int(f[3])] = l

    return labels

# Define function to segment NIfTI file
def segment(src_path, output_dir, n_clusters):
    print("Segment on: ", src_path)
    data, affine = load_nii(src_path)
    labels = kmeans_cluster(data, n_clusters)
    labels_path = os.path.join(output_dir, os.path.basename(src_path).replace(".nii.gz", f"_model_{n_clusters-2}.nii.gz"))
    
    # Save segmented labels as NIfTI file
    labels_img = nib.Nifti1Image(labels, affine)
    nib.save(labels_img, labels_path)
    print("Segmentation complete. Labels saved to:", labels_path)

def base_segment(patient_ids):
    # Define paths
    base_directory = os.getcwd()
    input_dir = os.path.join(base_directory, "Data\Patients")  # Input directory containing NIfTI files
    output_dir = os.path.join(base_directory, "Data\Kelsey")  # Output directory to save segmented NIfTI files
    create_dir(output_dir)

    # Define models (number of clusters)
    models = {"T2_Axial": [3, 4], "FLAIR_Axial": [3, 4]}

    # Iterate over models
    for modality, clusters_list in models.items():
        # Iterate over patient IDs
        for patient_id in patient_ids:
            for clusters in clusters_list:
                patient_dir = os.path.join(input_dir, patient_id)
                modality_dir = os.path.join(patient_dir, modality, "Original_nii")
                output_dir = os.path.join(patient_dir, modality, "Segment_Mask_nii")
                # Iterate over NIfTI files
                for file_name in os.listdir(modality_dir):
                    src_path = os.path.join(modality_dir, file_name)
                    segment(src_path, output_dir, clusters)