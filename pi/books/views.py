# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('请输入书名!')
        elif len(q) > 20:
            errors.append('哪有20个字以上的书名?请不要浪费服务器资源!')
        elif q=='ouhui':
            errors.append('<ouhui>是禁书,请不要做违法的事情!')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('booksapp/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('booksapp/search_form.html',{'errors': errors})