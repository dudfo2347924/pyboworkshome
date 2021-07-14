from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #외래키의 제약 조건을 무시하고 삭제됨
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return str(self.question)