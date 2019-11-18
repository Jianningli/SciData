# Skull-Data-Processing
Python/Matlab scripts to segment human skull bone from CT scan , clean the segmented skull, convert the skull volume to mesh and inject holes to the complete skull.

## skull data segmentation


## skull data cleaning
* dependency:   [3D connected component analysis](https://pypi.org/project/connected-components-3d/).
* installation:  pip install connected-components-3d
* usage: **_1._** change  **_data_dir_** and **_save_dir_** to where you stored the original nrrd files and where you want to save the cleaned   nrrd files to. **_2._** run in the command window:  python denoising.py


## artificial defect injection
* dependency:   [PyMRT](https://pypi.org/project/pymrt/).
* installation:  pip install pymrt
* usage: **_1._**  change  **_pair_list_:** where you storied the cleaned nrrd files (it's recommended that **_skull data cleaning_** performed before defect injection). **_defected_dir_:**  where to store the skull with defect to. **_implant_dir_:**  where to store the removed part (i.e., the implant) to. **_2._** run in the command window:  'python defectinject.py'


## skull data segmentation

> asdfds





