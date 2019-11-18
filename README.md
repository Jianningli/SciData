# Skull-Data-Processing
Python/Matlab scripts to segment human skull bone from CT scan , clean the segmented skull, convert the skull volume to mesh and inject holes to the complete skull.
* **_Python 3.6.8_**



## skull data segmentation
* **_dependency :_**   [pynrrd](https://pypi.org/project/pynrrd/), [pydicom](https://pydicom.github.io/pydicom/). 
* **_installation :_**   `pip install pynrrd` , `pip install -U pydicom`
* **_usage :_** \
**_1._** change directory \
**_2._** run in the command window:   `python segmentation.py`
* **_note :_** the script can read dicom files exported directly from CT machine for segmentation and can also read nrrd files converted from dicom files using 3D Slicer. 

## skull data cleaning
* **_dependency :_**   [3D connected component analysis](https://pypi.org/project/connected-components-3d/).
* **_installation :_**   `pip install connected-components-3d`
* **_usage :_** \
**_1._** change  **_data_dir_**  and  **_save_dir_**  to where you stored the original nrrd files and where you want to save the cleaned   nrrd files to. \
**_2._** run in the command window:   `python denoising.py`


## artificial defect injection
* **_dependency :_**   [PyMRT](https://pypi.org/project/pymrt/).
* **_installation :_**   `pip install pymrt`
* **_usage :_** \
**_1._**  change  **_pair_list_ :** where you storied the cleaned nrrd files (it's recommended that **_skull data cleaning_** performed before defect injection). **_defected_dir_ :**  where to store the skull with defect to. **_implant_dir_ :**  where to store the removed part (i.e., the implant) to. \
**_2._** specify the size of defect to be injected into the skull, 128 recommended. \
**_3._** run in the command window: `python defectinject.py`
* **_note:_** the current code provide functionalities to generate cubic defect  `generate_cude(defect_size)` and spherical dfects `generate_sphere(defect_size)`.

## create skull mesh model from .nrrd files

## create voxel grid from mesh (matlab/python)

* **_dependency :_**  [Polygon2Voxel](https://www.mathworks.com/matlabcentral/fileexchange/24086-polygon2voxel), [stlread](https://www.mathworks.com/matlabcentral/fileexchange/6678-stlread). 
* **_usage :_** \
`[F,V] = stlread('oc_from_pcl2.stl'); \
` `FV.faces=F;` \
`FV.vertices=V;` \
`Volume=polygon2voxel(FV,512,'none',true);` \
_save Volume.mat to nrrd_  \
`import scipy.io as sio `








