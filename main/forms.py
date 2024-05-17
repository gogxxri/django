from django import forms
from main.models import Question


# ModelForm : model의 db를 연결할 수 있는 form
#               -> Meta라는 inner class 반드시 사용
class QuestionForm(forms.ModelForm): 
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }