
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


def main(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'main/index.html', context)  #reques, 요청한 페이지, 인자

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'main/detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('main:detail', question_id=question.id) 

def question_create(request):
    if request.method == "POST": # post 방식이면
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) #임시저장
            question.create_date = timezone.now() #create_date 추가
            question.save() # 저장
            return redirect('main:main')
    else: # get 방식이면
        form = QuestionForm()
    context = {"form":form}
    return render(request, 'main/question_form.html', context)