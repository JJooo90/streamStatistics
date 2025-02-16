from django.db import models

# Chzzk 에서 작업하는 모델들
class Chzzk(models.Model):     
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class stremerVideo(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    name = models.CharField(null=False,max_length=20)
    views=models.IntegerField(null=False,max_length=20)