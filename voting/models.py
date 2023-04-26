from django.db import models
from .ModelManagers import *
# Create your models here.

class Departments(models.Model):
    Department_id = models.CharField(max_length=7,primary_key=True)
    Department_Name = models.Charfield(max_lenght=50)

    def __str__(self):

        return f"Department ID:{self.Department_id}\n Department Name:{self.Department_Name}"
    
    class Meta:

        ordering = ['Position']


class Positions(models.Model):
    Department_id = models.ForeignKey(Departments,on_delete=models.PROTECT,null=True)
    Position = models.CharField(max_length=50)

    def __str__(self):
         
        dept = self.Department_id.Department_Name if self.Department_id else "None"

        return f"Position:{self.Position}\n Department: {dept}\n"

    class Meta:

        ordering = ['Position']


class Users(models.Model):

    FirstName = models.CharField(max_length=50,help_text="John")
    LastName = models.CharField(max_length=50,help_text="Doe")

    RegistrationNumber = models.CharField(max_length=50,help_text="Registration Number DIT/../..")
    Email = models.EmailField(max_length=200,unique=True,help_text="JohnDoe@gmail.com")
    #TODO Validate phone number field in sign in form
    #PhoneNumber = models.CharField(max_length=15)
    Department  = models.ForeignKey(Departments,on_delete=models.PROTECT,help_text="DIT/DBIT/BIT/BBIT")
    Password = models.CharField(max_lenght=100)


    
    def __str__(self):
        return f"Name:{self.FirstName} {self.LastName},\nDept:{self.Department},\nRegistration Number:{self.RegistrationNumber}"
    
    class Meta:
        ordering = ['FirstName']
    

class Voters(models.Model):
    User_id= models.OneToOneField(Users,primary_key=True,on_delete=models.CASCADE)
    Position = models.ForeignKey(Positions,on_delete=models.PROTECT)
    Votes = models.IntegerField()

    def __str__(self):
        Name = self.User_id.FirstName +" "+ self.User_id.LastName
        return f"Name: {Name}\nPosition: {self.Position}\nVotes: {self.Votes}"

    class Meta:
        ordering = ['Votes']
class
