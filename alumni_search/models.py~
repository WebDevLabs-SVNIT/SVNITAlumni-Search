from django.db import models

# Create your models here.

class Alumni(models.Model):
	lName=models.CharField(max_length='30')
	fName=models.CharField(max_length='30')
	yop=models.IntegerField(default=0)
	branch=models.CharField(max_length='30')
	uid=models.CharField(max_length='15')
	phOffice=models.CharField(max_length='100')
	phCell=models.CharField(max_length='100')
	phRes=models.CharField(max_length='100')
	email=models.EmailField(max_length='200')
	posHeld=models.CharField(max_length='100')
	address=models.CharField(max_length='250')
	landmark=models.CharField(max_length='250')
	street=models.CharField(max_length='250')
	city=models.CharField(max_length='100')
	pincode=models.CharField(max_length='10')
	state=models.CharField(max_length='50')
	country=models.CharField(max_length='100')
	resAddress=models.CharField(max_length='250')
	resLandmark=models.CharField(max_length='250')
	resCity=models.CharField(max_length='100')
	resPincode=models.CharField(max_length='10')
	resState=models.CharField(max_length='100')
	resCountry=models.CharField(max_length='100')
	
	def __unicode__(self):
		return self.lName+self.fName	
	 #b=Alumni(lName=s.cell(row,1).value,fName=s.cell(row,2).value,yop=s.cell(row,3).value,branch=s.cell(row,4).value,uid=s.cell(row,5).value,phOffice=s.cell(row,6).value,phCell=s.cell(row,7).value,phRes=s.cell(row,8).value,email=s.cell(row,9).value,posHeld=s.cell(row,10).value,address=s.cell(row,11).value,landmark=s.cell(row,12).value,street=s.cell(row,13).value,city=s.cell(row,14).value,pincode=s.cell(row,15).value,state=s.cell(row,16).value,country=s.cell(row,17).value,resAddress=s.cell(row,18).value,resLandmark=s.cell(row,19).value,resCity=s.cell(row,20).value,resPincode=s.cell(row,21).value,resState=s.cell(row,22).value,resCountry=s.cell(row,23).value)

