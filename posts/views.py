from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
 

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

def index_wrong(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        render(request, "index.html", {"posts": latest})

# Хороший вариант: промежуточные переменные полезны
def index_ok(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        response = render(request, "index.html", {"posts": latest})
        return response

# Хороший вариант: без промежуточных переменных - короче
def index_ok_too(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        return render(request, "index.html", {"posts": latest})

 

# # view-функция для страницы сообщества
def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных 
    # или возвращант сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})