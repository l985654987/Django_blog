from django import forms
from blog import models
from django.core.exceptions import ValidationError


class RegForm(forms.ModelForm):
    username = forms.CharField(
        label='用户名',
        min_length=6,
        error_messages={'min_length': '用户名过短'}
    )
    password = forms.CharField(
        label='密码',
        min_length=6,
        error_messages={'min_length': '密码过短'}
    )
    re_password = forms.CharField(
        label='确认密码',
        min_length=6,
        error_messages={'min_length': '密码过短'}
    )

    class Meta:
        model = models.User
        fields = ['username', 'password', 're_password']

        # widgets = {
        # 'password': forms.widgets.PasswordInput(attrs={"class": 'form-control'}),
        # 'password': forms.widgets.PasswordInput(attrs={"class": 'form-control'}),
        # 're_username': forms.widgets.PasswordInput(attrs={"class": 'form-control'}),
        #     }

    def clean_re_password(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = models.Blogs
        fields = ['blog_title', 'blog_matter', 'blog_type_id', 'user_id']
        error_messages = {
            'blog_matter': {'required': '内容不能为空'},
            'blog_title': {'required': '标题不能为空'},
            'blog_type_id': {'required': '博客类别为必选项'}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 限制发表人是当前的用户
        self.fields['user_id'].widget.choices = [(self.instance.user_id.id, self.instance.user_id)]
