from django.db import models
from user.models import User



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



class Quiz(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name



class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(blank=True, null=True)
    time_limit = models.IntegerField(default=20)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.text



class Participant(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.quiz.name}"



class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.text




class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def is_correct(self):
        return self.selected_answer.is_correct

    def __str__(self):
        return f"Participant: {self.participant.user.username}, Question: {self.question.text}, Selected Answer: {self.selected_answer.text}"