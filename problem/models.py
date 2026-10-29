from django.db import models

from exams.models import Assesment

from accounts.models import User

# Create your models here.


class Question(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()
    
    score=models.PositiveIntegerField()

    assesment=models.ForeignKey(Assesment,on_delete=models.CASCADE)

    sampleinput=models.TextField(null=True)

    sampleoutput=models.TextField(null=True)

    createdat=models.DateTimeField(auto_now=True)

    question_num=models.PositiveIntegerField(null=True,default=0)

    updatedat=models.DateTimeField(auto_now=True)

    createdby=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title

    def save(self, *args,**kwargs):

        last_quest_object = Question.objects.filter(assesment=self.assesment).last()

        if last_quest_object:

            self.question_num = last_quest_object.question_num+1

        else:

            self.question_num=1
            
        return super().save()