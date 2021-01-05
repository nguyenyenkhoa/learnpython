#Nguyen Thi Yen Khoa
#MSSV: B1709343

#----------------Cau1---------------------
# print("Nhap cau: ")
# s = input()

# digits = 0
# letters = 0

# for i in s:
# 	if i.isdigit():
# 		digits+=1
# 	elif i.isalpha():
# 		letters+=1
# 	else:
# 		pass
# print("So chu cai la: ", letters)
# print("So chu so la: ", digits)
#-----------------------------------------



#-----------------Cau2--------------------
# print("Nhap cau: ")
# s = input()

# upper = 0
# lower = 0

# for i in s:
# 	if i.isupper():
# 		upper+=1
# 	elif i.islower():
# 		lower+=1
# 	else:
# 		pass
# print("So chu hoa la: ", upper)
# print("So chu thuong la: ", lower)
#-----------------------------------------




#-----------------------Cau3--------------
# print("Nhap cau: ")
# s = input()

# print("Chu in hoa la: ", s.upper())

#------------------------------------------


#---------------------Cau4-----------------
# print("Tim so chan")
# string=[]
# for i in range(100, 301):
# 	s = str(i)
# 	if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0:
# 		string.append(s)
# print(', '.join(string))
#------------------------------------------




#-------------------Cau5-------------------
# print("Hay nhap vao mot day so:")
# array = []
# numbers = [int(x) for x in input().split(',')]
# for i in numbers:
# 	if i%2!=0:
# 		array.append(str(i))
# print("Day so le la: ",', '.join(array))

#------------------------------------------



#---------------------Cau6-----------------
# def binhphuong():
# 	d=dict()
# 	for i in range(1,21):
# 		d[i]=i**2
# 	print(d)
# binhphuong()
#-------------------------------------------



#---------------------Cau7-------------------
# my_list = ['12','24','35','70','88','120','155']
# value1 = my_list.pop(5)
# value2 = my_list.pop(4)
# vallue3 = my_list.pop(0)

# print(my_list)
#--------------------------------------------



#-----------------------Cau8-----------------
# list1 = set([12,3,6,78,35,55,120] )
# list2 = set([12,24,35,78,88,120,155])

# list1 &= list2
# giao = list(list1)
# print(giao)

#--------------------------------------------



#------------------------Cau9----------------
# def printList():
# 	listfisrt = list()
# 	for i in range(1,21):
# 		listfisrt.append(i**2)
# 	print(listfisrt[:5])
# printList()
#--------------------------------------------



#-------------------------Cau10--------------
# lst = []
# s = int(input("Nhap vao so luong gia tri can in: "))
# count = 0

# for i in range(0,s):
# 	ele = (input())
# 	while ele.isalpha():
# 		s = int(input("Nhap vao so luong gia tri can in: "))
# 		for i in range(0,s):
# 			ele = (input())
# 	lst.append(ele)
# tupl = tuple(lst)


# li = list()
# for j in range(1,len(tupl)):
# 	if j%2==0:
# 		li.append(j)
# 		tp2 = tuple(li)
# print(tp2)
#--------------------------------------------



#----------------------Cau11-----------------
# d = dict()
# string = input("Nhap vao mot cau: ")

# for i in string:
# 	d[i] = d.get(i,0)+1
# print('\n'.join(['%s,%s' % (k,v) for k,v in d.items()]))
#--------------------------------------------



#-----------------------Cau12-------------------
# string = input("Moi nhap cau: ")
# string = string[::-1]

# print(string)
#-----------------------------------------------


#------------------------Cau13------------------
# string = input("Moi nhap chuoi: ")
# while len(string)<2:
# 	string = input("Moi nhap lai: ")
# def printList():
# 	li = []

# 	for i in string:
# 		li.append(str(i))
# 	print(str(li[:2]),str(li[-2:]))
# printList()
#-----------------------------------------------


#--------------------------Cau14-----------------
# string1 = input("Nhap chuoi thu nhat: ")
# string2 = input("Nhap chuoi thu hai: ")

# def chars_mix_up(string1, string2):
# 	new_string1 = string2[:2] + string1[2:]
# 	new_string2 = string1[:2] + string2[2:]

# 	return new_string1 + ', ' + new_string2
# print(chars_mix_up(string1, string2))
#----------------------------------------------


#----------------------Cau15--------------------
# string = input("Nhap chuoi: ")
# lst = list(string)

# array = []
# for i in range(1,len(lst)):
# 	if lst[i]==lst[0]:
# 		lst.insert(i, '@')
# 		lst.pop(i+1)
# 		break
# print(''.join(lst))

#------------------------------------------------------------------------

