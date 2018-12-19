from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # 首页polls
    path('', views.index, name='index'),
    # 首页 问题列表polls/index
    path('index', views.index, name='index'),
    # 问题详情页 polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 投票结果页 polls/1/results
    path('<int:question_id>/results/', views.results, name='results'),
    # 去投票，选项计数加一 /polls/1/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    # 通用视图示例
    path('simple/', views.SimpleView.as_view(), name='simple')
]
# (注意)django1.x路由写法 正则风格
# from django.conf.urls import url
# urlpatterns = [
#     # /polls/
#     url(r'^$', views.index, name='index'),
#     # /index/
#     url(r'^index$', views.index, name='index'),
#     # /index/1/
#     url(r'^(?P<question_id>[0-9]+)/$'),
# ]
#
# @app.route('/')
# def index():
#     pass


# 先引入视图函数
# path()函数定义的路由最终都会在项目启动是加载
