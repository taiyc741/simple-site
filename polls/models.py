from django.db import models

# Create your models here.
class Question(models):
    question_text = models.CharField('问题内容',max_length=200)
    pub_data = models.DateTimeField('发布时间')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE())
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)




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
