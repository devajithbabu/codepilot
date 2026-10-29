from django.db import models

from accounts.models import User

from datetime import datetime,timedelta

# Create your models here.

class Assesment(models.Model):

            title=models.CharField(max_length=100)
            
            batch=models.CharField(max_length=100)

            LANGUAGE_CHOICES = [
                                ('Python', 'Python'),
                                ('Java', 'Java'),
                                ('JavaScript', 'JavaScript'),
                                ('SQL', 'SQL')
                            ]

            language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)

            examdate=models.DateField()

            duration=models.PositiveIntegerField()

            starttime=models.TimeField()

            endtime=models.TimeField(null=True)

            createdby=models.ForeignKey(User,on_delete=models.CASCADE)

            STATUS_CHOICES = [
                            ('scheduled', 'Scheduled'),
                            ('ongoing', 'Ongoing'),
                            ('completed', 'Completed')
                        ]

            status=models.CharField(max_length=100,choices=STATUS_CHOICES)

            def save(self,*args,**kwargs):

                    end_date_time = datetime.combine(self.examdate,self.starttime)+timedelta(hours=self.duration)

                    self.endtime=end_date_time.time()

                    
                    return super().save(*args,**kwargs)

