from django.db import models

# Create your models here.
class filims(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.FloatField(null=True)
    image = models.CharField(max_length=2000, null=True)

    def __str__(self):
      return f"{self.name}-{self.id}"
class details(models.Model):
    about= models.CharField(max_length=1500)
    director=models.CharField(max_length=255)
    fname=models.ForeignKey(filims,on_delete=models.CASCADE,default='0')
    def __str__(self):
      return f"{self.fname}{self.id}"