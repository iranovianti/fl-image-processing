from read_roi import read_roi_zip
import numpy as np
import cv2

def roi_to_arrays(path,image_size):

	rois = read_roi_zip(path)
	coordinates = [[v['x'], v['y']] for k,v in rois.items()]
	arrays = []
	for coor in coordinates:
		x,y = np.subtract(coor, 1)
		binary = np.zeros(image_size)
		binary[x,y] = 1
		arrays.append(np.transpose(binary))
	return arrays


def arrays_to_area(a_list,kernel_size=(12,12))
	
	areas = []
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kernel_size)
	for array in a_list:
		border = cv2.dilate(array, kernel)
    	filled = np.where((flood_fill(border, (0,0), 1))==1, 0, 1)
    	filled = np.add(filled, border)
    	areas.append(filled)
    return areas

def roi_to_areas(path,image_size):

	arrays = roi_to_arrays(path,image_size)
	areas = arrays_to_area(arrays)
	return areas