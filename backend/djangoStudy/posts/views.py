from django.shortcuts import render, redirect
from .forms import PostForm
from datetime import datetime
# Create your views here.

def writePost(request):
    if request.method == 'GET':
        return render(request, 'writing.html')
    elif request.method == 'POST':
        form = PostForm(request.POST) #form에 받아온 정보를 담은 form 넘기기
        if form.is_valid(): #검사 한번 돌리기
            post = form.save(commit=False) #post 변수에 정보 담긴 form 전달
            post.wrritenDate = datetime.now() #작성날짜 저장
            post.save() #post 저장
            return redirect('postlist')
        else:
            return redirect('postlist')

def showPostList(request):
    if request.method == 'GET':
        return render(request, 'postlist.html')