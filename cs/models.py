from datetime import date
from operator import truediv
from django.db import models

# Create your models here.
class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=50)
    password = models.CharField("password",max_length=25)
    role = models.CharField("role",max_length=25)

class employee(models.Model):
    employeeid=models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name=models.CharField("name",max_length=30)
    address=models.CharField("address",max_length=50)
    gender=models.CharField("gender",max_length=20)
    mobileno=models.CharField("mobileno",max_length=50)
    place=models.CharField("place",max_length=25)
    email=models.CharField("email",max_length=30)

class vehicle(models.Model):
    vehicleid=models.AutoField(primary_key=True)
    vehiclename=models.CharField("vehiclename",max_length=30)
    registrationno=models.CharField("registrationno",max_length=20)
    source=models.CharField("source",max_length=30)
    destination=models.CharField("source",max_length=40)
    capacity=models.CharField("capacity",max_length=30)
    date=models.DateField("date",max_length=10)

class couriertype(models.Model):
    couriertypeid=models.AutoField(primary_key=True)
    courier=models.CharField("courier",max_length=40)

class cargo(models.Model):
    cargoid=models.AutoField(primary_key=True)
    couriertypeid=models.ForeignKey(couriertype,on_delete=models.CASCADE,null=True)
    weight=models.CharField("weight",max_length=20)
    price=models.CharField("price",max_length=20)
    paymenttype=models.CharField("paymenttype",max_length=30)
    fromaddress=models.CharField("fromaddress",max_length=50)
    toddress=models.CharField("toaddress",max_length=50)
    landmark=models.CharField("landmark",max_length=30)
    sendingdate=models.DateField("sendingdate",max_length=20)
    currentdate=models.DateField("currentdate",max_length=20)
    status=models.CharField("status:",max_length=100)

class route(models.Model):
    routeid=models.AutoField(primary_key=True)
    vehicle=models.ForeignKey(vehicle,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(employee,on_delete=models.CASCADE,null=True)
    route=models.CharField("route",max_length=50)
    date=models.DateField("date",max_length=20)

class allotedjobs(models.Model):
    allotedjobsid=models.AutoField(primary_key=True)
    employee=models.ForeignKey(employee,on_delete=models.CASCADE,null=True)
    couriertypeid=models.ForeignKey(couriertype,on_delete=models.CASCADE,null=True)
    date=models.DateField("date",max_length=10)
    comments=models.CharField("comments",max_length=100)
    status=models.CharField("status:",max_length=100)


