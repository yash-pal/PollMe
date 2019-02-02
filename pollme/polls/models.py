from django.db import models

# Create your models here.
class Poll(models.Model):
    text = models.CharField(max_length=255)
    pub_date =models.DateField()

    def __str__(self):
        return self.text
       

class Choice(models.Model):
    questions = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return "{} . {}".format(self.questions.text[:25], self.choice_text[:25]) # format strings in python each one maps with place holders
