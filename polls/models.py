import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题内容', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text




"""
    类最终被翻译成sql执行
    CREATE TABLE question IF NOT EXISTS(
        id INT PRIMARY KEY INCREASE,
        question_text VARCHAR(200) comment "问题内容"，
        pub_data DATETIME comment "发布时间"
    )
"""

# django自带orm框架，用法类似sqlalchemy
# 继承models类
