#make sure to have numpy
#pip install numpy

import csv
import numpy as np

def read_csv():
	with open('log.csv','r', encoding='utf-8') as dest_f:
		data_iter = csv.reader(dest_f, delimiter = ",")
		data = [data for data in data_iter]

	data_array = np.asarray(data)
	data_array.reshape(-1,5)
	ds = []

	for i in range(1, data_array.shape[0]):
		temp = []
		for j in range(len(data_array[i])):
			try:
				temp.append(data_array[i][j])
			except:
				continue

		if len(temp) == 5:
			ds.append(temp)

	size_list = min(10, len(ds))
	ds.reverse()
	ds = ds[:size_list]

	return ds