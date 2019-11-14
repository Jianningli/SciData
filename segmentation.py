# python scripts for skull segmentation from CT scan
# The scripts 

import cc3d
import numpy as np
import nrrd
from glob import glob



if __name__ == '__main__':
    # directory of original nrrd files
    data_dir = "D:/skull-nrrd"
    data_list=glob('{}/*.nrrd'.format(data_dir))
    # directory to save the cleaned nrrd file
    save_dir = "D:/skull-nrrd/cleaned/"

	for i in range(len(data_list)):
		print('current data to clean:',data_list[i])
		# read nrrd file. data: skull volume. header: nrrd header
		data,header=nrrd.read(data_list[i])
		# Get all the connected components in data 
		labels_out = cc3d.connected_components(data.astype('int32'))
		# select the index of the second largest connected component 
		# in the data (the largest connected component is the background).
		skull_label=skull_id(labels_out)
        # keep only the second largest connected components(and remove other components)
		skull=(labels_out==skull_label)
		skull=skull+1-1
		# file name of the cleaned skull
		filename=save_dir+data_list[i][-10:-5]+'.nrrd'
		print('writing the cleaned skull to nrrd...')
		nrrd.write(filename,skull,h)
		print('writing done...')



