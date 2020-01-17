import random 
from collections import Counter
import math


def mean(data):
	leng = len(data)
	sum = 0
	for x in data:
		sum = sum + x
	return sum/float(leng)


def median(data):
	data.sort()
	leng = len(data)
	if leng%2 != 0:
		return data[leng/2]
	else:
		sum = data[leng/2] + data[(leng/2)+1]
		return sum/float(2)


def mode(data):
	n = len(data)
	data_1 = Counter(data)
	get_mode = dict(data_1)
	mode = [k for k, v in get_mode.items() if v==max(list(data_1.values()))]
	if len(mode) == n:
		get_mode = "No mode avaliable"
	else:
		get_mode = mode
	return get_mode


def variance(data):
	leng = len(data)
	avg = mean(data)
	sum = 0
	for i in data:
		sum = sum + (i-avg) * (i-avg)
	return sum/float(leng)


def std_deviation(data):
	num = variance(data)
	num = math.sqrt(num)
	return num


def range(data):
	data.sort()
	leng = len(data)
	value = data[leng-1]-data[0]
	return value

# A  percentile  is a comparison score between a particular score and the scores of the rest of a group. 
# It shows the percentage of scores that a particular score surpassed.
def percentile(data, value):
	leng = len(data)
	data.sort()
	index = data.index(value)
	index += 1
	value = (index*100)/leng
	return value














#data = [random.randrange(25) for i in range(50)]
data = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4 ]
print("Printing data")
print(data)
print("Mean of data")
print(mean(data))
print("Median of data")
print(median(data))
print("Mode of data")
print(mode(data))
print("variance of data")
print(variance(data))
print("Standard deviatio  of data")
print(std_deviation(data))
print("Range of data")
print(range(data))
print("the percentile of 9 is")
print(percentile(data, 9))
