# arr=[]
# for i in range(2000,3201):
# 	if i%7==0 and i%5!=0:
# 		arr.append(str(i))
# print(', '.join(arr))
# ------------------------------------
# number=int(input("So nhap vao: "))
# def giaithua(number):
# 	if number==0:
# 		return 1
# 	return number*giaithua(number-1)
# print(giaithua(number))
# ------------------------------
# number=int(input("Nhap vao mot so: "))
# d = dict()
# for i in range(1,number+1):
# 	d[i]=i*i
# print(d)
# --------------------------------
# li = input("Nhap vao mot danh sach: ")
# tp = li.split(',')

# tpl = tuple(tp)

# print(tp)
# print(tpl)
# ----------------------------------
# class InputOutString(object):
# 	"""docstring for ClassName"""
# 	def __init__(self):
# 		self.s = ""

# 	def getString(self):
# 		self.s=input("Nhap vao mot chuoi: ")
# 	def printstring(self):
# 		print(self.s.upper())
# strObject = InputOutString()
# strObject.getString()
# strObject.printstring()
# ----------------------------------
# number = int(input("Nhap vao mot so: "))
# def binhphuong(number):
# 	return number*number
# print(binhphuong(number))
# -----------------------------------	
# import math
# c = 50
# h = 30
# values=[]
# d = [x for x in input("Nhap day gia tri d: ").split(',')]
# for i in d:
# 	values.append(str(int(round(math.sqrt(2*c*float(i)/h)))))
# print(', '.join(values))
# -----------------------------------
# alphabet = [x for x in input("Nhap vao mot chuoi: ").split(',')]
# alphabet.sort()
# print(', '.join(alphabet))
# ------------------------------------
# lines = []
# while True:
# 	string = input("Nhap vao mot chuoi: ")
# 	if string:
# 		lines.append(string.upper())
# 	else:
# 		break
# for x in lines:
# 	print(x)
# -------------------------------------
# string = input("Nhap vao mot chuoi: ")
# values = [word for word in string.split(" ")]
# print(" ".join(sorted(list(set(values)))))
# -------------------------------------
# values=[]
# nhiphan = [x for x in input("Nhap vao cac so nhi phan: ").split(',')]
# for i in nhiphan:
# 	numbers = int(i,2)
# 	if not numbers%5:
# 		values.append(i)
# print(', '.join(values))
# ----------------------------------
# a = input("Nhap vao mot so a: ")
# n1 = int("%s"%a)
# n2 = int("%s%s"%(a,a))
# n3 = int("%s%s%s"%(a,a,a))
# n4 = int("%s%s%s%s"%(a,a,a,a))

# print("Tong la: ",n1+n2+n3+n4)
# -----------------------------------
# values=input("Nhap vao mot mang: ")
# numbers=[x for x in values.split(',')if int(x)%2!=0]
# print(', '.join(numbers))
# ------------------------------------
# import re
# values=[]
# items = [x for x in input("Nhap mat khau: ").split(',')]
# for i in items:
# 	if len(i)<6 or len(i)>12:
# 		continue
# 	else:
# 		pass
# 	if not re.search("[a-z]",i):
# 		continue
# 	elif not re.search("[0-9]",i):
# 		continue
# 	elif not re.search("[A-Z]",i):
# 		continue
# 	elif not re.search("[$#@]",i):
# 		continue
# 	else:
# 		pass
# 	values.append(i)
# print(', '.join(values))
# -------------------------------
# from operator import itemgetter, attrgetter
# lst = []
# while True:
# 	string = input()
# 	if not string:
# 		break
# 	lst.append(tuple(string.split(',')))
# print(sorted(lst,key=itemgetter(0,1,2)))
# ---------------------------------------
# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7
# def numbers(x):
# 	i=0
# 	while i<x:
# 		j=i
# 		i=i+1
# 		if j%7==0:
# 			yield j
# for n in numbers(99):
# 	print(n)
# ----------------------------------------
# import math #Robot
# pos = [0,0]

# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
# print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# ----------------------------------------------------
#Noi chuoi
# def addstring(s1,s2):
# 	print(s1+s2)
# addstring("3","4")
#-----------------------------------------------------
# s1 = str(input("Nhap chuoi thu nhat: "))
# s2 = str(input("Nhap chuoi thu hai: "))
# def addstring(s1,s2):
# 	return s1+s2
# print(addstring(s1,s2))