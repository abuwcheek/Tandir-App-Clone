from django.db import models




class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True



class ProgrammLanguage(BaseModel):
     nomi = models.CharField(max_length=50)
     icon = models.ImageField(upload_to='programm_images/')


     def __str__(self):
          return self.nomi



class Questions(BaseModel):
     ball = models.IntegerField(default=0)
     savol = models.TextField()
     vaqt = models.DateTimeField(auto_created=True)
     is_published = models.BooleanField(default=False)


     def __str__(self):
          return self.savol


