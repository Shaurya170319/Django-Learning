from django.db import models

class Employee(models.Model):
    Employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    photo= models.ImageField(upload_to= 'images')
    email_address=models.EmailField(max_length=100, unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.Employee_id).zfill(4) + ' - ' + self.first_name + ' ' + self.last_name
