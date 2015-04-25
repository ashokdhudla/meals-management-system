from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime
import os
from django.contrib import admin

STATUS_CHOICES = (
	('A','Active'),
	('I','Inactive'),
	)
GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),        
	)
EMP_TYPE = (
	('QP', 'Qatar Petroleum'),
	('NQP', 'Non Qatar Petroleum'),
	('VIS', 'Visitor')
	)
LOCATION_CHOICES = (
	('HEN','Halul Entry'),
	('HEX','Halul Exit'),
	('PS2EN','PS2 Entry'),
	('PS2EX','PS2 Exit'),
	('PS3EN','PS3 Entry'),
	('PS3EX','PS3 Exit'),
	('MEN','Mess Entry'),
	('AEN','Accommodation Entry'),
	('AEX','Accommodation Exit'),
	('MAINEN','Main Entry'),
	('MAINEX','Main Exit'),
	('NEWSSQE','New SSQ Entry'),
	('NEWSSQX','New SSQ Exit'),
	('ELS1E','ELS1 Entry'),
	('ELS1X','ELS1 Exit'),
	('ELS1B1E','ELS1 Block1 Entry'),
	('ELS1B1X','ELS1 Block1 Exit'),
	('ELS1B2E','ELS1 Block2 Entry'),
	('ELS1B2X','ELS1 Block2 Exit'),
	('ELS1B3E','ELS1 Block3 Entry'),
	('ELS1B3X','ELS1 Block3 Exit'),
	('NEWELS2E','NewELS2 Entry'),
	('NEWELS2X','NewELS2 Exit'),
	('NEWELS2B1E','NewELS2Block1 Entry'),
	('NEWELS2B1X','NewELS2Block1 Exit'),
	('NewELS2B2E','NewELS2Block2 Entry'),
	('NewELS2B2X','NewELS2Block2 Exit'),
	('NewELS2B3E','NewELS2Block3 Entry'),
	('NewELS2B3X','NewELS2Block3 Exit'),
	('NewELS3E','NewELS3 Entry'),
	('NewELS3X','NewELS3 Exit'),
	('NEWELS3B1E','NewELS3Block1 Entry'),
	('NEWELS3B1X','NewELS3Block1 Exit'),
	('NEWELS3B2E','NewELS3Block2 Entry'),
	('NEWELS3B2X','NewELS3Block2 Exit'),
	('NEWELS3B3E','NewELS3Block3 Entry'),
	('NEWELS3B3X','NewELS3Block3 Exit'),
	('NEWELS3B4E','NewELS3Block4 Entry'),
	('NEWELS3B4X','NewELS3Block4 Exit'),
	('NEWELS3B5E','NewELS3Block5 Entry'),
	('NEWELS3B5X','NewELS3Block5 Exit'),
	('OLDSAFTE','Old Safety Entry'),
	('OLDSAFTX','Old Safety Exit'),
	('NEWSAFTE','New Safety Entry'),
	('NEWSAFTX','New Safety Exit'),
	('OLDSSQE','Old SSQ Entry'),
	('OLDSSQX','Old SSQ Exit'),
	('OLDELS2E','Old ELS2 Entry'),
	('OLDELS2X','Old ELS2 Exit'),
	('OLDELS3E','Old ELS3 Entry'),
	('OLDELS3X','Old ELS3 Exit'),
	('CONTRAE','Contractors Entry'),
	('CONTRAX','Contractors Exit'),
	('CONTRAB1E','Contractors Block1 Entry'),
	('CONTRAB1X','Contractors Block1 Exit'),
	('CONTRAB2E','Contractors Block2 Entry'),
	('CONTRAB2X','Contractors Block2 Exit'),
	('CONTRAB3E','Contractors Block3 Entry'),
	('CONTRAB3X','Contractors Block3 Exit'),
	('CONTRAB4E','Contractors Block4 Entry'),
	('CONTRAB4X','Contractors Block4 Exit'),
	('CONTRAB5E','Contractors Block5 Entry'),
	('CONTRAB5X','Contractors Block5 Exit')
	)
class associative_company(models.Model):
	company_name = models.CharField('Company Name', max_length=50)
	company_location = models.CharField('Location', max_length=50, null=True)
	contract_no = models.CharField('Contract No', max_length=50, null=True)
	contracy_title = models.CharField('Contract Title', max_length=50, null=True, blank=True)
	def __unicode__(self):
		return smart_unicode(self.company_name)
class qpusers(models.Model):
	username = models.CharField('UserName', max_length=60, null=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	user_id = models.CharField('User_ID', max_length=50, blank=False, unique=True)
	password1 = models.CharField('Password', max_length=30)
	email_id = models.EmailField('Email_ID', max_length=254, null=False)
	resident_location = models.CharField('Resident Location', max_length=50)
	contact_no = models.CharField('Contact No.', max_length=30, blank=True)
	status = models.CharField('Status', max_length=10,choices=STATUS_CHOICES, null=True)
	role = models.ForeignKey('role')
	date_time=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.email_id)

class role(models.Model):
	rolename = models.CharField(max_length=30)        
	status = models.CharField(max_length=40, choices=STATUS_CHOICES)
	def __unicode__(self):
		return smart_unicode(self.rolename)
	# class Admin:
	# 	pass
	# def __str__(self):
	# 	return '%s' %(self.rolename)
class employee_details(models.Model):
	first_name = models.CharField('First Name', max_length=50, null=True)
	last_name = models.CharField('Last Name', max_length=50, null=True)
	employee_id = models.CharField('Employee ID', max_length=50, null=True)
	rfidcardno = models.CharField(max_length=64, null=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	email_id = models.EmailField('Email_ID', max_length=254, null=False)
	contact_no = models.CharField('Contact No.', max_length=30)
	date_time=models.DateTimeField(auto_now=True)
	employee_type = models.CharField(max_length=20, choices=EMP_TYPE)
	company = models.ForeignKey('associative_company', null = True)
	department = models.ForeignKey('department',null = True)
	def __unicode__(self):
		return smart_unicode(self.employee_id)
class department(models.Model):
	department_name = models.CharField('Department Name', max_length=50,blank=False)
	dept_contact_no = models.CharField('Dept Contact No', max_length=50,null=True)
	def __str__(self):
		return '%s' %(self.department_name)
class emp_breakfast(models.Model):
	rfidcardno = models.CharField(max_length=64, null=True)
	employee_id = models.ForeignKey('employee_details', null=True)
	breakfast_count = models.IntegerField(max_length=50)
	date_time = models.DateTimeField(auto_now=True,null=True)
	def __unicode__(self):
		return smart_unicode(self.rfidcardno)
class emp_lunch(models.Model):
	rfidcardno = models.CharField(max_length=64, null=True)
	employee_id = models.ForeignKey('employee_details', null=True)
	lunch_count = models.IntegerField(max_length=50)
	date_time = models.DateTimeField(auto_now=True,null=True)
	def __unicode__(self):
		return smart_unicode(self.lunch_count)
class emp_dinner(models.Model):
	rfidcardno = models.CharField(max_length=64, null=True)
	employee_id = models.ForeignKey('employee_details', null=True)
	dinner_count = models.IntegerField(max_length=50)
	date_time = models.DateTimeField(auto_now=True,null=True)
	def __unicode__(self):
		return smart_unicode(self.dinner_count)
class emp_stay(models.Model):
	rfidcardno = models.CharField(max_length=64, null=True)
	date_time = models.DateTimeField(auto_now=True,null=True)
	ip_addr = models.CharField(max_length=30, null=True)
	status = models.CharField(max_length=10, null=True)
	def __unicode__(self):
		return smart_unicode(self.rfidcardno)
class emp_accommodation(models.Model):
	rfidcardno = models.CharField(max_length=64, null=True)
	# ip_addr = models.CharField(max_length=30, null=True)
	status = models.CharField(max_length=64, null=True)
	# date_time = models.DateTimeField(auto_now=True,null=True)
	# block_no = models.CharField('Block Number', max_length=50, null=True)
	# room_no = models.CharField('Room Number', max_length=50, null=True)
	# checkin_date_time = models.DateTimeField(auto_now=True,null=True)
	# checkout_date_time = models.DateTimeField(auto_now=True,null=True)
	# status = models.CharField('Status', max_length=10,choices=STATUS_CHOICES, null=True)
	def __unicode__(self):
		return smart_unicode(self.rfidcardno)
class meal_timing(models.Model):
	breakfast_start = models.DateTimeField(blank=True, null=True)
	breakfast_end = models.DateTimeField(blank=True, null=True)
	lunch_start = models.DateTimeField(blank=True, null=True)
	lunch_end = models.DateTimeField(blank=True, null=True)
	dinner_start = models.DateTimeField(blank=True, null=True)
	dinner_end = models.DateTimeField(blank=True, null=True)
	published = models.DateTimeField(blank=True, null=True)
	def __unicode__(self):
		return smart_unicode(self.published)
class device_info(models.Model):
	device_id = models.CharField(max_length=80, unique=True)
	device_location = models.CharField(max_length=50,choices=LOCATION_CHOICES)
	Installation_Date= models.DateTimeField(null=True,blank=True)
	def __unicode__(self):
		return smart_unicode(self.device_location)

class userlogin(models.Model):
	username = models.CharField(max_length=30)
	userid = models.CharField(max_length=30)
	role = models.ForeignKey('role')
	logintime  = models.DateTimeField()
	def __unicode__(self):
		return smart_unicode(self.userid)         
	# class Admin:
	# 	pass
	# def __str__(self):
	# 	return '%s' %(self.username)

class userlogout(models.Model):
	username = models.CharField(max_length=30)
	userid = models.CharField(max_length=30)
	role = models.ForeignKey('role')    
	logouttime  = models.DateTimeField() 
	def __unicode__(self):
		return smart_unicode(self.userid)           
	# class Admin:
	# 	pass
	# def __str__(self):
	# 	return '%s' %(self.username)
class mess_device(models.Model):
	rfidcardid = models.CharField(max_length=30)
	datetime = models.DateTimeField() 
	def __unicode__(self):
		return smart_unicode(self.rfidcardid)
class price_configure(models.Model):
	 emp_type = models.CharField(max_length=40,choices=EMP_TYPE)
	 company_name = models.ForeignKey('associative_company', null = True)
	 breakfast_price = models.CharField(max_length=40,null=True)
	 lunch_price = models.CharField(max_length=40,null=True)
	 dinner_price = models.CharField(max_length=40,null=True)
	 accommodation_price = models.CharField(max_length=40,null=True)
	 datetime = models.DateTimeField(null=True,blank=True)
	 def __unicode__():
	  return smart_unicode(self.datetime)
# Bhanu's models
class emp_entry(models.Model):
	empid= models.CharField(max_length=64,null=True)
	rfidcardno = models.CharField(max_length=64, null=True)
	ip_addr = models.CharField(max_length=64, null=True)
	date_time =models.DateTimeField(auto_now=True,null=True)
	device_location = models.CharField(max_length=30)
	def __unicode__(self):
		return smart_unicode(self.rfidcardno)
class emp_exit(models.Model):
	empid= models.CharField(max_length=64,null=True)
	rfidcardno = models.CharField(max_length=64, null=True)
	ip_addr = models.CharField(max_length=64, null=True)
	date_time =models.DateTimeField(auto_now=True,null=True)
	device_location = models.CharField(max_length=30)
	def __unicode__(self):
		return smart_unicode(self.rfidcardno)
	# class Admin:
	# 	pass
	# def __str__(self):
	# 	return '%s' %(self.rfidcardid)
# class emp_accommodation(models.Model):
#  rfidcardno = models.CharField(max_length=64, null=True)
#  employee_id = models.CharField(max_length=64, null=True)
#  #fromdate=models.DateTimeField(max_length=64, null=True)
#  #todate=models.DateTimeField(max_length=64, null=True)

#  #block_no = models.CharField('Block Number', max_length=50, null=True)
#  #room_no = models.CharField('Room Number', max_length=50, null=True)
#  #checkin_date_time = models.DateTimeField(auto_now=True,null=True)
#  #checkout_date_time = models.DateTimeField(auto_now=True,null=True)
#  #tatus = models.CharField('Status', max_length=10,choices=STATUS_CHOICES, null=True)
#  def __unicode__(self):
#   return smart_unicode(self.status)




	

