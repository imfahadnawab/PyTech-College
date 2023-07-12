from django.db import models

class Contact(models.Model):
    email= models.EmailField()
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField()
    date= models.DateField()

    def __str__(self):        
        return self.fullname


# Create your models here.
