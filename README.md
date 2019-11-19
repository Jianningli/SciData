# Skull-Data-Processing
Python/Matlab scripts to segment human skull bone from CT scan , clean the segmented skull, convert the skull volume to mesh and inject holes to the healthy skull.
* **_Python 3.6_**
* **_MATLAB R2018b_**
* **_MeshLab v2016.12_**
* **_ITK-SNAP 3.6.0_**
* **_3D Slicer 4.8.1 r26813_**
* **_Meshmixer 3.5.474_**

## segment skull from CT scan
* **_dependency :_**   [pynrrd](https://pypi.org/project/pynrrd/), [pydicom](https://pydicom.github.io/pydicom/). 
* **_installation :_**   `pip install pynrrd` , `pip install -U pydicom`
* **_usage :_** \
**_1._** change the directory \
**_2._** run in the command window:   `python segmentation.py`
* **_note :_** the script can read dicom files exported directly from CT machine for segmentation and can also read nrrd files converted from dicom files using 3D Slicer.  You need to specify the threshold for the skull segmentation, usually _100--max_ is recommended. 

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
* **_dependency :_**  [Open3D](http://www.open3d.org/), [scikit-image](https://scikit-image.org/), [PyMCubes](https://github.com/pmneila/PyMCubes).
* **_installation :_**    `pip install open3d`  `pip install scikit-image`  `pip install --upgrade PyMCubes`
* **_usage :_** \
`python nrrd2mesh.py`

## voxelization : create voxel grid from mesh (matlab/python)

* **_dependency :_**  [Polygon2Voxel](https://www.mathworks.com/matlabcentral/fileexchange/24086-polygon2voxel), [stlread](https://www.mathworks.com/matlabcentral/fileexchange/6678-stlread). 
* **_usage :_** \
`[F,V] = stlread('skullmesh.stl');`  \
`FV.faces=F;` \
`FV.vertices=V;` \
`Volume=polygon2voxel(FV,512,'none',true);` \
_save Volume.mat to nrrd_  \
`import scipy.io as sio, import nrrd ` \
`volume=sio.loadmat('Volumen.mat')['Volume']` \
`nrrd.write('volume.nrrd',volume.astype(float64))` 

## STL files dimension calculation
* **_dependency :_**  [Open3D](http://www.open3d.org/), [numpy-stl](https://pypi.org/project/numpy-stl/)
* **_installation :_**    `pip install open3d`  `pip install numpy-stl`
* **_usage :_** \
`python stl_dimension.py`
* **_note:_**  calculate the actual size of the STL files in millimeter (mm), which is the size of the 3D printed model.



***
Contact **_Jianning Li_** if you have any inquiries.








