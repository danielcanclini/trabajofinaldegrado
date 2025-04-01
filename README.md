# Comparación de Métodos de Segmentación Automática con Imágenes de Resonancia Magnética de Bajo Campo
Repositorio del Trabajo final de grado "Comparación de Métodos de Segmentación Automática con Imágenes de Resonancia Magnética de Bajo Campo" realizado por el alumno Jose Daniel Canclini para la Univerdad Comunera

Estructura de repositorio:
 - Codigo : Aca esta el codigo de fuente de los metodos utilizados
 - Experimento : Los archivos procesados que contienen las imagenes de resonancia magnetica de bajo campo de los pacientes del trabajo en formato .nii.gz
 - Originales : Los archivos originales sin procesar de las imagenes cerebrales de resonancia magnetica de bajo campo en formato .nii.gz


Se elabora esta guia de instlacion de los metodos utilizados para reproducir los resultados documentados en el trabajo.
# Ejecutar Bet

1. Descargar el script  de instalacion de FSL 
2. Ejecutar el script "python ./fslinstaller.py"
3. Recargar terminal
4. Ejecutar el comando "FSL"
5. Click en Bet2

# Ejecutar Deepbet
1. Descargar carpeta "Codigo/deepbet"
2. ejecutar el siguiente script pyhton:

from deepbet import run_bet

input_paths = ['path/to/sub_1/t1.nii.gz', 'path/to/sub_2/t1.nii.gz']
brain_paths = ['path/to/sub_1/brain.nii.gz', 'path/to/sub_2/brain.nii.gz']
mask_paths = ['path/to/sub_1/mask.nii.gz', 'path/to/sub_2/mask.nii.gz']
tiv_paths = ['path/to/sub_1/tiv.csv', 'path/to/sub_2/tiv.csv']
run_bet(input_paths, brain_paths, mask_paths, tiv_paths, threshold=.5, n_dilate=0, no_gpu=False)

# Ejecutar synthstrip

La forma mas facil es utilizarla con contenedores/docker
1. descargar el wrapper curl -O https://raw.githubusercontent.com/freesurfer/freesurfer/dev/mri_synthstrip/synthstrip-docker && chmod +x synthstrip-docker
2. ejecutar el comando: mri_synthstrip -i input.nii.gz -o stripped.nii.gz


# Ejecutar FAST
1. Descargar el script  de instalacion de FSL 
2. Ejecutar el script "python ./fslinstaller.py"
3. Recargar terminal
4. Ejecutar el comando "FSL"
5. Click en fast

# Ejecutar knn++
1. Descargar el script "codigo/knn/knn_segment"
2. Ejecutar el script knn_segment.py

# Ejecutar synthseg
1. descargar y descomprimir "codigo"synthseg/SynthSeg-master"
2. Crear un ambiente virtual en python e instalar paquetes "conda create -n synthseg_36 python=3.6 tensorflow-gpu=2.0.0 keras=2.3.1 h5py==2.10.0 nibabel matplotlib -c anaconda -c conda-forge"
3. descargar el archivo del modelo entrenado desde "https://liveuclac-my.sharepoint.com/:f:/g/personal/rmappmb_ucl_ac_uk/EtlNnulBSUtAvOP6S99KcAIBYzze7jTPsmFk2_iHqKDjEw?e=rBP0RO" 
4. colocar el archivo del modelo entrenado en la carpeta "models"
5. ejecutar "python ./scripts/commands/SynthSeg_predict.py --i <input> --o <output>"

