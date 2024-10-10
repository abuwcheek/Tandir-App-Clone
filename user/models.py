from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True



class User(BaseModel, AbstractUser):
     username = models.CharField(max_length=50)
     name = models.CharField(max_length=50)
     surname = models.CharField(max_length=50)
     programming_language = models.CharField(max_length=50)
     photo = models.ImageField(upload_to='user_image/')

     @property
     def full_name(self):
          return f'{self.surname} {self.name}'


     def __str__(self):
          return self.username



class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_count = models.IntegerField(default=0)
    win_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    lose_count = models.IntegerField(default=0)


    def __str__(self):
     return self.user