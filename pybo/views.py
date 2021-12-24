
from django.shortcuts import render
from pybo.models import Question


def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') # 질문 목록 데이터를 question_list라는 변수에 넣어줌
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
