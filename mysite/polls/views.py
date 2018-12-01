'''
render:载入模板，填充上下文，再返回由它生成的 HttpResponse 对象
例：
render(request, 'polls/index.html', context)

get_object_or_404()¶:尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程
例：
question = get_object_or_404(Question, pk=question_id)

'''


# from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse,HttpResponseRedirect
# from .models import Question,Choice
# from django.urls import reverse
# from django.template import loader
# from django.http import Http404
#
#
# # Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # render():载入模板，填充上下文，再返回由它生成的HttpResponse对象」是一个非常常用的操作流程
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     # try:
#     # question = Question.objects.get(pk=question_id)
#     # get_object_or_404():尝试用get()函数获取一个对象，如果不存在就抛出Http404错误也是一个普遍的流程
#     question = get_object_or_404(Question,pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         # 通过关键字的名字获取提交的数据,request.POST['choice']以字符串形式返回选择的Choice的ID
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         # HttpResponseRedirect只接收一个参数：用户将要被重定向的URL
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

'''我们在这里使用两个通用视图： ListView 和 DetailView'''

''''
对于 DetailView ， question 变量会自动提供—— 因为我们使用 Django 的模型 (Question)， Django 能够为 context 变量决定一个合适的名字。
然而对于 ListView， 自动生成的 context 变量是 question_list。为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用 latest_question_list。作为一种替换方案，你可以改变你的模板来匹配新的 context 变量 —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]

        '''
        returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
        '''
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # template_name属性是用来告诉Django使用一个指定的模板名字，而不是自动生成的默认名字
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
