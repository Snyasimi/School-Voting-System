from django.db import models

# Create your models here.




class Users(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    #Department  = models.ForeignKey(Departments,on_delete=models.PROTECT)
    

class Voters(models.Model):
    User_id= models.OneToOneField(Users,primary_key=True,on_delete=models.CASCADE )
    Votes = models.IntegerField()

