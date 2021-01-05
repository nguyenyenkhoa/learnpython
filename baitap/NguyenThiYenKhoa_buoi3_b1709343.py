#Nguyen Thi Yen Khoa 
#MSSV: B1709343

#---------------------------Cau1---------------------------------------------------------------------------
# class human:
# 	def __init__(self, hoten, namsinh, quequan, nghenghiep):
# 		self.hoten = hoten
# 		self.namsinh = namsinh
# 		self.quequan = quequan
# 		self.nghenghiep = nghenghiep

# 	def live(self,noicutru):
# 		return "{} , song o {}".format(self.hoten,noicutru)
	
# 	def work(self, diachicoquan):
# 		return"{} dang lam nghe {} cong tac tai {}".format(self.hoten,self.nghenghiep,diachicoquan)
# per1 = human("Nguyen Van A", "1999", "Vinh Long", "Front-end dev")


# print(per1.live("Can Tho"))
# print(per1.work("IT company"))
#---------------------------------------------------------------------------------------------------------



#-------------------------------Cau2----------------------------------------------------------------------

# numofPer = int(input("Nhap so luong nguoi nhap: "))
# for i in range(1,numofPer+1):
# 	namePerson = input("Nhap ho ten nguoi thu %d: " %(i))
# 	birthPerson = input("Nhap nam sinh nguoi thu %d: " %(i))
# 	livePerson = input("Nhap que quan nguoi thu %d: " %(i))
# 	workPerson = input("Nhap nghe nghiep nguoi thu %d: " %(i))
# 	addressPerson = input("Nhap dia chi co quan nguoi thu %d: " %(i))
# 	class human:
# 		def __init__(self, hoten, namsinh, quequan, nghenghiep, diachicoquan):
# 			self.hoten = hoten
# 			self.namsinh = namsinh
# 			self.quequan = quequan
# 			self.nghenghiep = nghenghiep
# 			self.diachicoquan = diachicoquan


# 		def work(self):
# 			return"{} dang lam nghe {} cong tac tai {}".format(self.hoten,self.nghenghiep,self.diachicoquan)

# 	per = human(namePerson,birthPerson,livePerson,workPerson,addressPerson)
# 	print(per.work())

#---------------------------------------------------------------------------------------------------------




#------------------------------------------Cau3-----------------------------------------------------------

# class human:
# 	def __init__(self, hoten, namsinh, quequan, nghenghiep):
# 		self.hoten = hoten
# 		self.namsinh = namsinh
# 		self.quequan = quequan
# 		self.nghenghiep = nghenghiep

# 	def live(self,noicutru):
# 		return "{} , song o {}".format(self.hoten,noicutru)
	
# 	def work(self, diachicoquan):
# 		return"{} dang lam nghe {} cong tac tai {}".format(self.hoten,self.nghenghiep,diachicoquan)



# class Student(human):
# 	"""docstring for student"""
# 	def __init__(self,hoten, namsinh, quequan, nghenghiep, MSSV, nganhhoc, diemtb):
# 		super().__init__(hoten, namsinh, quequan,nghenghiep)
# 		self.MSSV = MSSV
# 		self.nganhhoc = nganhhoc
# 		self.diemtb = diemtb
# 	def Study(self,Class):
# 		return"{} co ma so sinh vien {} thuoc nganh {}, dang hoc tai nphong {}.".format(self.hoten, self.MSSV, self.nganhhoc,Class)
# 	def Rank(self):
# 		if self.diemtb < 4:
# 			return"{} co ma so sinh vien, diem trung binh {} xep loai yeu".format(self.hoten,self.MSSV, self.diemtb)
# 		if self.diemtb>=4 and self.diemtb<6:
# 			return"{} co ma so sinh vien, diem trung binh {} xep loai trung binh".format(self.hoten,self.MSSV, self.diemtb)
# 		if self.diemtb>=6 and self.diemtb<8:
# 			return"{} co ma so sinh vien, diem trung binh {} xep loai kha".format(self.hoten,self.MSSV, self.diemtb)
# 		if self.diemtb>=8 and self.diemtb<10:
# 			return"{} co ma so sinh vien, diem trung binh {} xep loai gioi".format(self.hoten,self.MSSV, self.diemtb)

# std = Student("Nguyen Van A", "1999", "Vinh Long", "hoc sinh", "B1234567", "CNTT&TT", 8)
# print(std.Study("phong 1"))
# print(std.Rank())

#---------------------------------------------------------------------------------------------------------


#-------------------------------------------------Cau4----------------------------------------------------
# class human:
# 	def __init__(self, hoten, namsinh, quequan, nghenghiep):
# 		self.hoten = hoten
# 		self.namsinh = namsinh
# 		self.quequan = quequan
# 		self.nghenghiep = nghenghiep

# 	def live(self,noicutru):
# 		return "{} , song o {}".format(self.hoten,noicutru)
	
# 	def work(self, diachicoquan):
# 		return"{} dang lam nghe {} cong tac tai {}".format(self.hoten,self.nghenghiep,diachicoquan)



# class Student(human):
# 	"""docstring for student"""
# 	def __init__(self,hoten, namsinh, quequan, nghenghiep,diemtb, MSSV, nganhhoc):
# 		super().__init__(hoten, namsinh, quequan,nghenghiep)
# 		self.diemtb = float(diemtb)
# 		self.MSSV = MSSV
# 		self.nganhhoc = nganhhoc
	
# 	def Rank(self):
# 		if self.diemtb < 4:
# 			return"{} , sinh nam {}, que o {}, la {} co diem trung binh {} co ma so sinh vien {}, thuoc nganh {} xep loai yeu".format(self.hoten,self.namsinh, self.quequan, self.nghenghiep,self.diemtb,self.MSSV,self.nganhhoc)
# 		if self.diemtb>=4 and self.diemtb<6:
# 			return"{} , sinh nam {}, que o {}, la {} co diem trung binh {} co ma so sinh vien {}, thuoc nganh {} xep loai trung binh".format(self.hoten,self.namsinh, self.quequan, self.nghenghiep,self.diemtb,self.MSSV,self.nganhhoc)
# 		if self.diemtb>=6 and self.diemtb<8:
# 			return"{} , sinh nam {}, que o {}, la {} co diem trung binh {} co ma so sinh vien {}, thuoc nganh {} xep kha".format(self.hoten,self.namsinh, self.quequan, self.nghenghiep,self.diemtb,self.MSSV,self.nganhhoc)
# 		if self.diemtb>=8 and self.diemtb<10:
# 			return"{} , sinh nam {}, que o {}, la {} co diem trung binh {} co ma so sinh vien {}, thuoc nganh {} xep loai gioi".format(self.hoten,self.namsinh, self.quequan, self.nghenghiep,self.diemtb,self.MSSV,self.nganhhoc)

# SV1 = Student("Le Van An", "2005", "Vinh Long", "sinh vien", 7.6, "B12345", "CNTT&TT")
# SV2 = Student("Tran Van Binh", "2007", "Tra Vinh", "sinh vien", 4.5, "B56789", "Tai chinh ngan hang")
# print(SV1.Rank())
# print(SV2.Rank())

#----------------------------------------------------------------------------------------------------------



#--------------------------------------------Cau5----------------------------------------------------------
# hoten = input("Nhap ho ten: ")
# namsinh = str(input("Nhap nam sinh: "))
# quequan = input("Nhap que quan: ")
# nghenghiep = "sinh vien"
# MSSV = input("Nhap MSSV: ")
# nganhhoc = input("Nhap nganh hoc: ")
# diemtb = float(input("Diem trung binh: "))
# class Sinhvien:
# 	def __init__(self,hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,diemtb):
# 		self.hoten = hoten
# 		self.namsinh = str(namsinh)
# 		self.quequan = quequan
# 		self.nghenghiep = nghenghiep
# 		self.MSSV = MSSV
# 		self.nganhhoc = nganhhoc
# 		self.diemtb = float(diemtb)

# 	def hienthi(self):
# 		while len(self.hoten)>25:
# 			hoten = input("Nhap ho ten: ")
# 			self.hoten = hoten
# 		while len(self.namsinh)!=4 or self.namsinh.isalpha():
# 			namsinh = str(input("Nhap nam sinh: "))
# 			self.namsinh = str(namsinh)
# 		while len(self.quequan)>50:
# 			quequan = input("Nhap que quan: ")
# 			self.quequan = quequan
# 		while len(self.MSSV)!=5 or self.MSSV.isalpha():
# 			MSSV = input("Nhap MSSV: ")
# 			self.MSSV = MSSV
# 		while len(self.nganhhoc)>40:
# 			nganhhoc = input("Nhap nganh hoc: ")
# 			self.nganhhoc = nganhhoc
# 		while self.diemtb<0 or self.diemtb>10:
# 			diemtb = float(input("Diem trung binh: "))
# 			self.diemtb = float(diemtb)
# 		return"{} sinh nam {}, que o {} la {} ma so sinh vien la {}, \n hoc nganh {}, co diem trung binh la {}".format(self.hoten, self.namsinh,self.quequan,self.nghenghiep,self.MSSV,self.nganhhoc,self.diemtb)
		
		
# sv = Sinhvien(hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,diemtb)
# print(sv.hienthi())

#---------------------------------------------------------------------------------------------------------





#-----------------------------------------------------Cau6------------------------------------------------

# soluong = int(input("nhap vao so luong sinh vien: "))
# for i in range(1, soluong+1):
# 	print("\t \t \t \t Sinh vien thu %d " %(i))
# 	print("-------------------------------------------------------------------------------------")
	
# 	hoten = input("Nhap ho ten: ")
# 	namsinh = str(input("Nhap nam sinh: "))
# 	quequan = input("Nhap que quan: ")
# 	nghenghiep = "sinh vien"
# 	MSSV = input("Nhap MSSV: ")
# 	nganhhoc = input("Nhap nganh hoc: ")
# 	diemtb = float(input("Diem trung binh: "))
# 	class Sinhvien:
# 		def __init__(self,hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,diemtb):
# 			self.hoten = hoten
# 			self.namsinh = str(namsinh)
# 			self.quequan = quequan
# 			self.nghenghiep = nghenghiep
# 			self.MSSV = MSSV
# 			self.nganhhoc = nganhhoc
# 			self.diemtb = float(diemtb)

# 		def hienthi(self):
# 			while len(self.hoten)>25:
# 				hoten = input("Nhap ho ten: ")
# 				self.hoten = hoten
# 			while len(self.namsinh)!=4 or self.namsinh.isalpha():
# 				namsinh = str(input("Nhap nam sinh: "))
# 				self.namsinh = str(namsinh)
# 			while len(self.quequan)>50:
# 				quequan = input("Nhap que quan: ")
# 				self.quequan = quequan
# 			while len(self.MSSV)!=5 or self.MSSV.isalpha():
# 				MSSV = input("Nhap MSSV: ")
# 				self.MSSV = MSSV
# 			while len(self.nganhhoc)>40:
# 				nganhhoc = input("Nhap nganh hoc: ")
# 				self.nganhhoc = nganhhoc
# 			while self.diemtb<0 or self.diemtb>10:
# 				diemtb = float(input("Diem trung binh: "))
# 				self.diemtb = float(diemtb)
# 			return"Ho ten: {} \n Sinh nam: {} \n Que quan: {} \n Nghe nghiep: {} \n MSSV: {} \n Nganh hoc: {} \n Diem trung binh: {}".format(self.hoten, self.namsinh,self.quequan,self.nghenghiep,self.MSSV,self.nganhhoc,self.diemtb)
			
			
# 	sv = Sinhvien(hoten,namsinh,quequan,nghenghiep,MSSV,nganhhoc,diemtb)
# 	print(sv.hienthi())
# 	print("----------------------------------------------------------------------------------------")


#------------------------------------------------------------------------------------------------------------------------





#-------------------------------------------------------Cau7&Cau8-------------------------------------------------------------
# from decimal import *
# class Exchange:
# 	def __init__(self,Serial,Date,Amount,ExchangeType):
# 		self.Serial = Serial
# 		self.Date = Date
# 		self.Amount = int(Amount)
# 		self.ExchangeType = ExchangeType

# 	def PrintExchange(self):
# 		pass

# 	def CashUp(self):
# 		pass
# class GoldExchange(Exchange):
# 	def __init__(self,Serial,Date,Amount,ExchangeType,GoldType,UnitPrice):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.GoldType = GoldType
# 		self.UnitPrice = Decimal(UnitPrice)
# 	def CashUp(self):
# 		return Decimal(self.Amount * self.UnitPrice)
# 	def PrintExchange(self):
# 		return"{} - {} - {} - {} - {} - {} = {}".format(self.Serial,self.Date,self.Amount,self.ExchangeType,self.GoldType,self.UnitPrice,self.CashUp())
# golden = GoldExchange("134","11/11/2020","32000000","CashUp","18k",3)
# print(golden.PrintExchange())

#------------------------------------------------------------------------------------------------------------------------






#------------------------------------------------------Cau9--------------------------------------------------------------
# class Exchange:
# 	def __init__(self,Serial,Date,Amount,ExchangeType):
# 		self.Serial = Serial
# 		self.Date = Date
# 		self.Amount = int(Amount)
# 		self.ExchangeType = ExchangeType

# 	def PrintExchange(self):
# 		pass

# 	def CashUp(self):
# 		pass

# class CurrencyExchange(Exchange):
# 	"""docstring for CurrencyExchange"""
# 	def __init__(self, Serial,Date,Amount,ExchangeType,CurrencyType,ExchangeRate,Action):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.CurrencyType = CurrencyType
# 		self.ExchangeRate =ExchangeRate
# 		self.Action = Action

# 	def CashUp(self):
# 		if self.Action==1:
# 			return self.Amount*self.ExchangeRate
# 		else:
# 			return float(self.Amount*self.ExchangeRate*1.1)

# 	def PrintExchange(self):
# 		if self.Action==1:
# 			return "Sell Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# 		else:
# 			return "Buy Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# money = CurrencyExchange("115","11/11/2020",100,"money","USD",25000,"ban")
# print(money.PrintExchange())
#------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------Cau10----------------------------------------------------------------------
# from decimal import *
# class Exchange:
# 	def __init__(self,Serial,Date,Amount,ExchangeType):
# 		self.Serial = Serial
# 		self.Date = Date
# 		self.Amount = int(Amount)
# 		self.ExchangeType = ExchangeType

# 	def PrintExchange(self):
# 		pass

# 	def CashUp(self):
# 		pass
# class GoldExchange(Exchange):
# 	def __init__(self,Serial,Date,Amount,ExchangeType,GoldType,UnitPrice):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.GoldType = GoldType
# 		self.UnitPrice = Decimal(UnitPrice)
# 	def CashUp(self):
# 		return Decimal(self.Amount * self.UnitPrice)
# 	def PrintExchange(self):
# 		return"{} - {} - {} - {} - {} - {} = {}".format(self.Serial,self.Date,self.Amount,self.ExchangeType,self.GoldType,self.UnitPrice,self.CashUp())
# golden = GoldExchange("134","11/11/2020","32000000","CashUp","18k",3)
# print(golden.PrintExchange())


# class CurrencyExchange(Exchange):
# 	"""docstring for CurrencyExchange"""
# 	def __init__(self, Serial,Date,Amount,ExchangeType,CurrencyType,ExchangeRate,Action):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.CurrencyType = CurrencyType
# 		self.ExchangeRate =ExchangeRate
# 		self.Action = Action

# 	def CashUp(self):
# 		if self.Action==1:
# 			return self.Amount*self.ExchangeRate
# 		else:
# 			return float(self.Amount*self.ExchangeRate*1.1)

# 	def PrintExchange(self):
# 		if self.Action==1:
# 			return "Sell Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# 		else:
# 			return "Buy Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# money = CurrencyExchange("115","11/11/2020",100,"money","USD",25000,"ban")
# print(money.PrintExchange())


# def TypeofGold(GoldType):
# 	swicth={
# 		1:"18k",
# 		2:"24",
# 		3:"9999"
# 	}
# 	return swicth.get(GoldType,"Invalid day of gold type")
# def TypeofCurrency(CurrencyType):
# 	swicth={
# 		1: "USD",
#         2: "EUR",
#         3: "AUD"
# 	}
# 	return swicth.get(CurrencyType,"Invalid day of currency type")
# def exchangeType(i):
# 	swicth={
# 		1: "Gold Exchange",
#         2: "Currency Exchange"
# 	}
# 	return swicth.get(i,"Invalid day of exchange type")
# def action(Action):
# 	swicth={
# 		1: "Buy Currency",
#         2: "Sell Currency"
# 	}
# 	return swicth.get(Action,"Invalid day of action")
# def Transaction():
# 	Serial = input("Nhap ma giao dich: ")
# 	while Serial:
# 		if len(Serial)>5 or Serial.isalpha():
# 			Serial = input("Serial must be a Number with max length = 5!\nPlease, input again: ")
# 		else:
# 			break
# 	Date = input("Nhap ngay giao dich: ")
# 	while Date:
# 		if len(Date)>10:
# 			Date = input("Date must be a string with max length = 10\nPlease, input again: ")
# 		else:
# 			break
# 	Amount = input("Nhap so luong: ")
# 	while Amount:
# 		if Amount.isalpha():
# 			Amount = input("Amount must be a number\nPlease, input again: ")
# 		else:
# 			break
# 	print("Nhap loai giao dich: ")
# 	print("\t 1: GoldExchange; 2: CurrencyExchange")
# 	i = int(input("\t Ban chon: "))
# 	while i:
# 		if i!=1 or i!=2:
# 			break
# 		else:
# 			i = int(input("You must choose between 1 or 2\tPlease, input again: "))
# 	if i==1:
# 		print("Loai giao dich la 1, ban co 3 su lua chon: ")
# 		print("\t 1: 18k, 2: 24k, 3: 9999")
# 		GoldType = int(input("\t Ban chon: "))
# 		while GoldType:
# 			if GoldType == 1 or GoldType == 2 or GoldType ==3:
# 				break
# 			else:
# 				GoldType = int(input("You must choose correct gold type\nPlease, input again: "))
# 		UnitPrice = input("Nhap don gia: ")
# 		while UnitPrice:
# 			if UnitPrice.isalpha():
# 				UnitPrice = input("UnitPrice / ExchangeRate must be a number")
# 			else:
# 				break
# 		GD = GoldExchange(Serial,Date,int(Amount),exchangeType(i),TypeofGold(GoldType),int(UnitPrice))
# 		# print(GD.)
# 	elif i== 2:
# 		print("Loai giao dich la 2, ban co 3 su lua chon:")
# 		print("\t 1: USD, 2: EUR, 3: AUD")
# 		CurrencyType = int(input("\t Ban chon: "))
# 		while CurrencyType:
# 			if CurrencyType == 1 or CurrencyType == 2 or CurrencyType==3:
# 				break
# 			else:
# 				CurrencyType = int(input("You must choose correct  currency type\nPlease, input again: "))
# 		ExchangeRate = input("Nhap don gia:")
# 		while ExchangeRate:
# 			if ExchangeRate.isalpha():
# 				ExchangeRate = input("UnitPrice/ExchangeRate must be a number")
# 			else:
# 				break
# 		print("Loai giao dich cua ban la 2, ban co 2 su lua chon:")
# 		print("\t \t 1: Buy Currency, 2: Sell Currency")
# 		Action = int(input("\t \t Ban chon: "))
# 		while Action:
# 			if Action == 1 or Action == 2:
# 				break
# 			else:
# 				Action = int(input("You must choose action with your currency\nPlease, input again: "))
# 		GD = CurrencyExchange(Serial,Date,int(Amount),exchangeType(i),TypeofCurrency(CurrencyType),int(ExchangeRate),Action)
# 	print(GD.PrintExchange())
# Transaction()
# print()
#-------------------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------Cau11&Cau12------------------------------------------------------------
# from decimal import *
# ListofTransaction = []
# class Exchange:
# 	def __init__(self,Serial,Date,Amount,ExchangeType):
# 		self.Serial = Serial
# 		self.Date = Date
# 		self.Amount = int(Amount)
# 		self.ExchangeType = ExchangeType

# 	def PrintExchange(self):
# 		pass

# 	def CashUp(self):
# 		pass
# class GoldExchange(Exchange):
# 	def __init__(self,Serial,Date,Amount,ExchangeType,GoldType,UnitPrice):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.GoldType = GoldType
# 		self.UnitPrice = Decimal(UnitPrice)
# 	def CashUp(self):
# 		return Decimal(self.Amount * self.UnitPrice)
# 	def PrintExchange(self):
# 		return"{} - {} - {} - CashUp - {} - {} = {}".format(self.Serial,self.Date,self.Amount,self.GoldType,self.UnitPrice,self.CashUp())
# golden = GoldExchange("134","11/11/2020","32000000",1,"18k",3)
# print(golden.PrintExchange())


# class CurrencyExchange(Exchange):
# 	"""docstring for CurrencyExchange"""
# 	def __init__(self, Serial,Date,Amount,ExchangeType,CurrencyType,ExchangeRate,Action):
# 		super().__init__(Serial,Date,Amount,ExchangeType)
# 		self.CurrencyType = CurrencyType
# 		self.ExchangeRate =ExchangeRate
# 		self.Action = Action

# 	def CashUp(self):
# 		if self.Action==1:
# 			return self.Amount*self.ExchangeRate
# 		else:
# 			return float(self.Amount*self.ExchangeRate*1.1)

# 	def PrintExchange(self):
# 		if self.Action==1:
# 			return "Sell Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# 		else:
# 			return "Buy Exchange: {} - {} - {} - {} - {} - Cash Up = {}.".format(self.Serial,self.Date,self.CurrencyType,self.ExchangeRate,self.Amount,self.CashUp())
# money = CurrencyExchange("115","11/11/2020",100,2,"USD",25000,"ban")
# print(money.PrintExchange())


# def TypeofGold(GoldType):
# 	swicth={
# 		1:"18k",
# 		2:"24",
# 		3:"9999"
# 	}
# 	return swicth.get(GoldType,"Invalid day of gold type")
# def TypeofCurrency(CurrencyType):
# 	swicth={
# 		1: "USD",
#         2: "EUR",
#         3: "AUD"
# 	}
# 	return swicth.get(CurrencyType,"Invalid day of currency type")
# def exchangeType(i):
# 	swicth={
# 		1: "Gold Exchange",
#         2: "Currency Exchange"
# 	}
# 	return swicth.get(i,"Invalid day of exchange type")
# def action(Action):
# 	swicth={
# 		1: "Buy Currency",
#         2: "Sell Currency"
# 	}
# 	return swicth.get(Action,"Invalid day of action")
# def Transaction():
# 	Serial = input("Nhap ma giao dich: ")
# 	while Serial:
# 		if len(Serial)>5 or Serial.isalpha():
# 			Serial = input("Serial must be a Number with max length = 5!\nPlease, input again: ")
# 		else:
# 			break
# 	Date = input("Nhap ngay giao dich: ")
# 	while Date:
# 		if len(Date)>10:
# 			Date = input("Date must be a string with max length = 10\nPlease, input again: ")
# 		else:
# 			break
# 	Amount = input("Nhap so luong: ")
# 	while Amount:
# 		if Amount.isalpha():
# 			Amount = input("Amount must be a number\nPlease, input again: ")
# 		else:
# 			break
# 	print("Nhap loai giao dich: ")
# 	print("\t 1: GoldExchange; 2: CurrencyExchange")
# 	i = int(input("\t Ban chon: "))
# 	while i:
# 		if i!=1 or i!=2:
# 			break
# 		else:
# 			i = int(input("You must choose between 1 or 2\tPlease, input again: "))
# 	if i==1:
# 		print("Loai giao dich la 1, ban co 3 su lua chon: ")
# 		print("\t 1: 18k, 2: 24k, 3: 9999")
# 		GoldType = int(input("\t Ban chon: "))
# 		while GoldType:
# 			if GoldType == 1 or GoldType == 2 or GoldType ==3:
# 				break
# 			else:
# 				GoldType = int(input("You must choose correct gold type\nPlease, input again: "))
# 		UnitPrice = input("Nhap don gia: ")
# 		while UnitPrice:
# 			if UnitPrice.isalpha():
# 				UnitPrice = input("UnitPrice / ExchangeRate must be a number")
# 			else:
# 				break
# 		GD = GoldExchange(Serial,Date,int(Amount),exchangeType(i),TypeofGold(GoldType),int(UnitPrice))
# 	elif i== 2:
# 		print("Loai giao dich la 2, ban co 3 su lua chon:")
# 		print("\t 1: USD, 2: EUR, 3: AUD")
# 		CurrencyType = int(input("\t Ban chon: "))
# 		while CurrencyType:
# 			if CurrencyType == 1 or CurrencyType == 2 or CurrencyType==3:
# 				break
# 			else:
# 				CurrencyType = int(input("You must choose correct  currency type\nPlease, input again: "))
# 		ExchangeRate = input("Nhap don gia:")
# 		while ExchangeRate:
# 			if ExchangeRate.isalpha():
# 				ExchangeRate = input("UnitPrice/ExchangeRate must be a number")
# 			else:
# 				break
# 		print("Loai giao dich cua ban la 2, ban co 2 su lua chon:")
# 		print("\t \t 1: Buy Currency, 2: Sell Currency")
# 		Action = int(input("\t \t Ban chon: "))
# 		while Action:
# 			if Action == 1 or Action == 2:
# 				break
# 			else:
# 				Action = int(input("You must choose action with your currency\nPlease, input again: "))
# 		GD = CurrencyExchange(Serial,Date,int(Amount),exchangeType(i),TypeofCurrency(CurrencyType),int(ExchangeRate),Action)
# 	print(GD.PrintExchange())
# 	ListofTransaction.append(GD)
# n = int(input("nhap so luong giao dich: "))
# for j in range(1,n+1):
# 	Transaction()
# 	print("------------------------------------------------------------------------------------")
# 	print("\t\t\t\t Exchange %d " %(j))
# for j in ListofTransaction:
# 	print(j.PrintExchange())
# 	print("------------------------------------------------------------------------------------")


# countGold = 0
# countCurrency = 0
# for x in ListofTransaction:
# 	if x.ExchangeType==1:
# 		countGold +=1
# 	elif x.ExchangeType==2:
# 		countCurrency+=1
# print("Total of Gold Exchange: ",countGold)
# print("Total of Currency Exchange: ",countCurrency)
#-------------------------------------------------------------------------------------------------------------------------