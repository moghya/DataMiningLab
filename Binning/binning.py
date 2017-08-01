import math

'''
Implemented binning techniques - Equal Depth and Equal Width. 
Smoothing techniques - Smoothing by Means and Smoothing by Boundaries.
'''


def input_data():
	number_of_elements = int(input('Enter no of Elements: '))
	data = list(map(int,input('Enter Elements: ').split()))
	number_of_bins = int(input('Enter number of bins: '))
	return number_of_elements,data,number_of_bins

def equal_depth_bining(number_of_elements,data,number_of_bins):
	bins = []
	bin_size = math.ceil(number_of_elements/number_of_bins)
	data.sort()
	for i in range(0,number_of_elements,bin_size):
		x_bin = data[i:min(i+bin_size,number_of_elements)]
		bins.append(x_bin)
	return bins

def equal_width_bining(number_of_elements,data,number_of_bins):
	data.sort()
	max_value = max(data)
	min_value = min(data)
	width = math.ceil((max_value-min_value)/number_of_bins)
	bins = []
	j = 0
	for i in range(0,number_of_bins):
		max_value_for_bin = (i+1)*width
		x_bin = []		
		while j<number_of_elements and data[j] <= max_value_for_bin:
			x_bin.append(data[j])
			j+=1
		bins.append(x_bin)
	return bins

def smoothing_by_means(bins):
	new_bins = []
	for x_bin in bins:
		new_bin_by_mean = [sum(x_bin)/len(x_bin)]*len(x_bin)
		new_bins.append(new_bin_by_mean)
	return new_bins

def smoothing_by_boundaries(bins):
	new_bins = []	
	for x_bin in bins:
		new_bin_by_boundary = []
		for element in x_bin:			
			if abs(x_bin[0]-element)<=abs(x_bin[-1]-element):
				new_bin_by_boundary.append(x_bin[0])
			else:
				new_bin_by_boundary.append(x_bin[-1])
		new_bins.append(new_bin_by_boundary)
	return new_bins


def print_bins(bins):
	for x_bin in bins:
		print(x_bin)



def main():

	number_of_elements,data,number_of_bins = input_data()

	print('Equal Depth Bining')
	bins = equal_depth_bining(number_of_elements,data,number_of_bins)
	print_bins(bins)

	print('Smoothing by Means')
	new_bins = smoothing_by_means(bins)	
	print_bins(new_bins)


	print('Smoothing by Boundaries')
	new_bins = smoothing_by_boundaries(bins)
	print_bins(new_bins)

	

main()
