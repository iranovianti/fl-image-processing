from read_roi import read_roi_zip
import numpy as np
from skimage.draw import polygon

"""Some functions to process ImageJ roi files.
Taking roi for borders (like freehand, ellips, etc.) and return the binary files with filled area"""

def roi_to_arrays(path,image_size):
#making roi into numpy arrays with several channels corresponding to the number of rois
	rois = read_roi_zip(path)
	coordinates = {k: [v['y'], v['x']] for k,v in rois.items() if v['type'] == 'freehand'}
	masks = {}

	for k, coor in coordinates.items():
		r, c = coor
		rr, cc = polygon(r, c)
		binary = np.zeros(image_size)
		binary[rr, cc] = 1
		masks[k] = binary
	return masks
