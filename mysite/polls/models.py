# Create your models here.
import datetime
from django.utils import timezone
from django.db import models

'''
模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。

在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。
Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。
models.Model：表示django.db.models.Model 类的子类
'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
