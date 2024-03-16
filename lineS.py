mas = [2,4,3,2,4,6,54,6,54,34,3,5,6,89,0,87,6,4,8,6,5,3,3]
el = 89

def line_search(mas,elem):
	for i in range(len(mas)):
		if mas[i] == elem:
			return i
	return None
print(line_search(mas,el), mas[line_search(mas,el)])
	
