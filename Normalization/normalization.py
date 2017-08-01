import math

def input_data():
	number_of_elements = int(input('Enter no of Elements: '))
	data = list(map(int,input('Enter Elements: ').split()))
	return number_of_elements,data

def min_max_normalization(data):

	new_min = int(input('Enter new_min'))
	new_max = int(input('Enter new_max'))
	max_in_data = max(data)
	min_in_data = min(data)
	number_of_elements = len(data)

	for i in range(0,number_of_elements):
		data[i]= ((data[i]-min_in_data)/(max_in_data-min_in_data)) * (new_max-new_min) + new_min
		data[i]= round(data[i],2)

	return data

def variance(data):
	if len(data)==0:
		return None
	number_of_elements = len(data)
	mean_of_data = sum(data)/number_of_elements	
	_sum=0
	for i in range(0,number_of_elements):
		_sum+=(data[i]-mean_of_data)**2
	data_variance = (1/(number_of_elements-1) * _sum)
	return data_variance
	

def standard_deviation(data):
	data_variance = variance(data)
	return data_variance**0.5


def z_score_normalization(data):
	number_of_elements = len(data)
	mean_of_data = sum(data)/number_of_elements
	data_standard_deviation = standard_deviation(data)
	
	for i in range(0,number_of_elements):
		data[i]= (data[i]-mean_of_data)/data_standard_deviation
		data[i]= round(data[i],2)

	return data


def main():
	number_of_elements,data = input_data()
	print('Data Inserted')
	print(data)	
	data = z_score_normalization(data)
	print('z-score Normalized Data')
	print(data)


	return None

main()
