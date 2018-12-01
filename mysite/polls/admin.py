# Register your models here.
from django.contrib import admin

from .models import Question, Choice


#我们得告诉管理页面，问题 Question 对象需要被管理
# admin.site.register(Question)
'''

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    
    #fileldsets 元组中的第一个元素是字段集的标题,第二个元素是显示的字段内容
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
'''


#class ChoiceInline(admin.StackedInline):每行显示一个字段
#Django 提供了一种表格式的单行显示关联对象的方法。你只需按如下形式修改 ChoiceInline 申明：
#(即一行显示多个字段)
class ChoiceInline(admin.TabularInline):
    model = Choice
    #默认提供 3 个足够的选项字段。
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #使用 list_display 后台选项，它是一个包含要显示的字段名的元组，在更改列表页中以列的形式展示这个对象：
    #https://docs.djangoproject.com/zh-hans/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('question_text', 'pub_date','was_published_recently')
    #过滤器（你可以使用任意多的字段——由于后台使用 LIKE 来查询数据，将待搜索的字段数限制为一个不会出问题大小，会便于数据库进行查询操作。）
    list_filter = ['pub_date']
    #列表的顶部增加一个搜索框
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        #'classes': ['collapse']：表明该字段可以操作隐藏/显示
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #显示对应的行
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)