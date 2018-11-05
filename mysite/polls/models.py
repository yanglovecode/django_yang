# Create your models here.
from django.db import models


# 在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。
# Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。
# models.Model：表示django.db.models.Model 类的子类
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
