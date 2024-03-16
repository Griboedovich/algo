mas = [1,2,3,4,5,6,7,8,9,10,1,1,22,33,4,4,5,56,6,7,56,75,67,56,7,56,7,56,7,43543,6,45,856,8,56,]
elem = 67

mas.sort()#для этого способа массив должен быть отсортирован

def binary_search(mas,elem):
	first = 0
	end = len(mas)-1
	
	index  = -1
	
	while first<=end and index == -1:
		mid = (first + end)//2
		
		
		if mas[mid] == elem:
			index = mid 
		elif mas[mid] > elem:
			end = mid -1
		else:
			first = mid +1
	return index
	
print(binary_search(mas,elem), mas[binary_search(mas,elem)])


