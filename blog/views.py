from django.shortcuts import render, redirect, reverse
from django.shortcuts import render_to_response
from blog.forms import RegForm, BlogModelForm
from utils.pagination import Pagination
from django.contrib import auth
from blog import models


# Create your views here.


# 注册
def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 创建新用户
            form_obj.cleaned_data.pop('re_password')
            user = form_obj.save()
            user.set_password(user.password)
            user.save()
            return redirect(reverse('blog_login'))
    return render(request, 'blog/reg.html', {'form_obj': form_obj})


# 登录
def login(request):
    my_error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect(reverse('blog_home'))
        else:
            my_error = '用户名或密码错误'
    return render(request, 'blog/login.html', {'my_error': my_error})


# 主页
def home(request):
    blogs = models.Blogs.objects.all().order_by('-write_time')
    page = Pagination(request, blogs.count())
    return render(request, 'blog/home.html', {
        'blogs': blogs[page.start:page.end],
        'pagination': page.show_li
    })


# 新建博客
def add(request):
    if request.user.is_authenticated():
        obj = models.Blogs(user_id=request.user)
        form_obj = BlogModelForm(instance=obj)
        if request.method == 'POST':
            form_obj = BlogModelForm(request.POST, instance=obj)
            if form_obj.is_valid():
                form_obj.save()
                return redirect(reverse('blog_home'))
        return render(request, 'blog/add.html', {'form': form_obj})
    return redirect(reverse('blog_login'))

#编辑博客
def edit(request, id):
    blog = models.Blogs.objects.filter(id=id).first()
    form_blog = BlogModelForm(instance=blog)
    if request.method == 'POST':
        form_obj = BlogModelForm(request.POST, instance=blog)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('my_blogs'))
    return render(request, 'blog/edit_blog.html', {'form': form_blog})


def delete(request, id):
    blog = models.Blogs.objects.filter(id=id).delete()
    return redirect(reverse('my_blogs'))


# 注销
def logout(request):
    auth.logout(request)
    return redirect(reverse('blog_home'))


# 我的博客
def myblogs(request):
    if request.user.is_authenticated():
        username = '{}'.format(request.user)
        blogs = models.Blogs.objects.filter(user_id__username=username)
        page = Pagination(request, blogs.count())
        return render(request, 'blog/myblogs.html', {
            'blogs': blogs[page.start:page.end],
            'pagination': page.show_li
        })
    return redirect(reverse('blog_login'))


# 博客详细
def content(request, id):
    blog = models.Blogs.objects.filter(id=id)[0]
    return render(request, 'blog/post.html', {'blog': blog})


# 博客分类
def sortblog(request, str):
    blogs = models.Blogs.objects.filter(blog_type_id__b_type=str)
    page = Pagination(request, blogs.count())
    return render(request, 'blog/sort_blog.html', {'str': str + '类',
                                                   'blogs': blogs[page.start:page.end],
                                                   'pagination': page.show_li
                                                   })

