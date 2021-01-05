#Nguyen Thi Yen Khoa 
# MSSV: B1709343

#---------------Cau1-----------------
#print("Hello ! welcome to python!")
#------------------------------------


#--------------------------------Cau2----------------------
#print("Nhap ten cua ban: ")
#x = input()
#print("Hello " + x + " Welcome to Python")
#----------------------------------------------------------



#---------------------------------Cau3---------------------

#print("Nhap so b: ")
#b = float(input())
#print("Nhap so a: ")
#a = float(input())

#while b == 0:
#	print("Moi nhap lai b")
#	b = float(input())

#tong = a+b
#print("tong la: ", tong)
#tru = a-b
#print("Hieu la: ", tru)
#tich = a*b
#print("Tich la: ", tich)
#thuong = a/b
#print("Thuong la: ", thuong)
#sodu = a%b
#print("Phep du la: ", sodu)
#luythua = a**b
#print("Luy thua la: ", luythua)
#------------------------------------------------------------



#-------------------------Cau4-------------------------------
# print("Nhap r: ")
# r = float(input())
# pi = 3.14

# chuvi = 2*r*pi
# print("Chu vi hinh tron la: ", chuvi)

# dientich = pi*r*r
# print("Dien tich hinh tron la: ", dientich)
#------------------------------------------------------------



#--------------------------Cau5------------------------------
# print("Nhap so nguyen n: ")
# n = int(input())
# while(n<0) :
# 	print("Moi ban nhap lai")
# 	n = int(input())
# def giaithua(n) :
# 	if n==0:
# 		return 1
# 	return n*giaithua(n-1)

# print("Giai thua la: ", giaithua(n))

#--------------------------------------------------------------


#--------------------------Cau6-------------------------------------------------------------
# import math
# print("Nhap a: ")
# a = float(input())
# print("Nhap b: ")
# b = float(input())
# print("Nhap c: ")
# c = float(input())


# if a==0:
# 	print("Phuong trinh co nghiem la: ", (0-c)/b)
# if a!=0:
# 	delta = (b*b) - 4*a*c
# 	print ("delta = ", delta)
# 	if delta==0:
# 		print("Phuong trinh co nghiem kep: ", (-b)/(2*a))
# 	if delta < 0:
# 		print("Phuong trinh vo nghiem")
# 	if delta > 0:
# 		print("Phuong trinh co hai nghiemn")
# 		print("x1= ", ((-b)+math.sqrt(delta))/(2*a), "\nx2= ", ((-b)-math.sqrt(delta))/(2*a))
#-----------------------------------------------------------------------------------------------






#----------------------------Cau7---------------------------------------------------------------
# numbers = []
# for i in range(5000,7001):
# 	if i%7==0 and i%5!=0:
# 		numbers.append(str(i))
# print(", ". join(numbers))
	
#-----------------------------------------------------------------------------------------------







#----------------------------------Cau8----------------------------------------------------------
# print("Nhap so nguyen: ")
# n = int(input())
# while n < 0:
# 	print("Moi ban nhap lai:")
# 	n = int(input())
# print("Doi sang nhi phan: ", int(bin(n)[2:]))
	

#------------------------------------------------------------------------------------------------




#------------------------------------Cau9--------------------------------------------------------
# print("Nhap so a:")
# a = int(input())
# print("Nhap so b:")
# b = int(input())

# def UCLN(a,b):
# 	while a!=b:
# 		if a>b:
# 			a = a - b
# 		else :
# 			b = b - a
# 	return a

# print("UCLN la: ",UCLN(a,b))


# def BCNN(a,b):
# 	result = UCLN(a,b)
# 	return int ((a*b)/result)
# print("BCNN la: ", BCNN(a,b))


#------------------------------------------------------------------------------------------------







#---------------------------------------Cau10-----------------------------------------------------
# import math

# print("Nhap so n: ")
# n = int(input())


# def isPrimeNumber(n) :
# 	if n<2:
# 		return False
# 	else :
# 		squarenumber = int(math.sqrt(n))
# 		for i in range(2,squarenumber+1):
# 			if n%i==0:
# 				return False
# 		return True

# print("So nguyen to nho hon", n, "la: ")
# result=""

# if n>=2:
# 	result = result + "2" + " "
# for i in range(3,n+1):
# 	if isPrimeNumber(i):
# 		result = result + str(i) + " "
# 	i = i + 2
# print(result)
#-------------------------------------------------------------------------------------------------









#------------------------------------------------Cau11--------------------------------------------
# import math
# def isPrimeNumber(n) :
# 	if n<2:
# 		return False
# 	else :
# 		squarenumber = int(math.sqrt(n))
# 		for i in range(2,squarenumber+1):
# 			if n%i==0:
# 				return False
# 		return True

# print("Nhung so nguyen to co 4 chu so la: ")
# result = ""
# for i in range(1001,9999):
# 	if isPrimeNumber(i):
# 		result = result + str(i) + " "
# print(result)
#-------------------------------------------------------------------------------------------------








#-------------------------------------------Cau12-------------------------------------------------
# print("Nhap vao so nguyen n: ")
# n = int(input())
# def SumN(n):
# 	sum = 0
# 	while n>0:
# 		sum = sum + (n%10)
# 		n = int(n/10)
# 	return sum

# print("Tong cac chu so trong ", n, " la: ", SumN(n))
#-------------------------------------------------------------------------------------------------






#-----------------------------------------------Cau13---------------------------------------------
# values = []
# for i in range(1000,2001):
# 	n = str(i)
# 	if (int(n[0])%2!=0) and (int(n[1])%2!=0) and (int(n[2])%2!=0) and (int(n[3])%2!=0):
# 		values.append(n)
# print(", ".join(values))
#-------------------------------------------------------------------------------------------------





#------------------------------------------Cau14---------------------------------------------------
# print("Nhap n: ")
# n = int(input())
# while n < 0:
# 	print("Moi nhap lai n: ")
# 	n = int(input())
# sum = 0
# for i in range(1,n+1):
# 		sum = sum + float(i/(i+1))
# print(sum)
		
#--------------------------------------------------------------------------------------------------





#------------------------------------------------Cau15---------------------------------------------

# print("Nhap n: ")
# n = int(input())

# def fibonaci(n):
# 	if n==0:
# 		return 0
# 	if n==1:
# 		return 1
# 	else :
# 		return fibonaci(n-1) + fibonaci(n-2)
# print("Day fibonaci la: ",fibonaci(n))
#--------------------------------------------------------------------------------------------------

# print(1,2,3,4,sep='*')

print(3>=3)