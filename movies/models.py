from django.db import models

# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    rating=models.FloatField()
    runtime=models.IntegerField()
    image=models.ImageField(upload_to="movies",null=True)


from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    phone=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=20,null=True)