from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# def index(request):
#     return HttpResponse("""
#         <html>
#             <head></head>
#             <body>
#                 <h1>helloword</h1>
#             </body>
#         </html>
#     """)

# def index(request):
#     """
#     展示问题列表
#     :return:
#     """
#     question_list_obj = Question.objects.all().order_by('-pub_date')[0:5]
#     # print(question_list) <QuerySet [<Question: 晚上吃瓦罐？>, <Question: 第一次使用Django这玩意真坑>]>
#     question_list = [question for question in question_list_obj]
#     print(type(question_list[0]))
#     template = loader.get_template('polls/index.html')
#     context = {
#         'question_list': question_list
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    question_list_obj = Question.objects.all().order_by('-pub_date')[0:5]
    content = {
        "question_list_obj": question_list_obj
    }
    return render(request, 'polls/index.html', content)

def detail(request, question_id):
    """
    显示一个问题的详细信息，问题内容、问题发布时间、
    选项内容、每个选项投票数。
    :param request:
    :param question_id:
    :return:
    """
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("404 网页不存在")
    question = get_object_or_404(Question, id=question_id)
    # chioces = question.choice_set.all()  反向查询可在前端直接写
    # context = {
    #     "question": question
    # }
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    """
    投票结果
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, "polls/results.html", context)

def vote(request, question_id):
    """
    投票
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, id=question_id)
    try:
        print(f"用户选择的选项id：{request.POST['choice']}")
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print("出错了")
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "问题对应的选项不存在"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# 通用模板
class SimpleView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list_obj'

    def get_queryset(self):
        return Question.objects.all()



"""
时间
    TIME_ZONE = "UTC"
    USE_TZ = True
    不带时区的时间aware_time,带时区的时间local_time(本地时间)。
    
    为了避免上面提到的场景，django的解决方案是。
        基于三方包pytime_tz, 由time_zone()生成带时区的时间，
        根据TIME_ZONE设置转换UTC时间存入数据库，html渲染时从UTC时间，根据访问者的时区
        换成访问者当地的时间。
    最佳实践：
    1、国内访问， USE_TZ = False TIME_ZONE = 'UTC'  datetime.now() time_zone()都行
    2、多国访问，USE_TZ = True TIME_ZONE = 'Asia/Shanghi'
    
    可能出现的错误：
         
"""
"""
i18n
i18n意为国际化。网站上的菜单不同国家人访问展示不同的语言。原理有个翻译的配置文件。
i18n = True 默认开启
"""
