from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. "
                        "pybo.py의 views.py에서 작성된 내용입니다."
                        "조용재는 바보입니다.")
