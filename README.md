# Django_blog
:+1: 基于python3.x,django1.x,mysql的博客系统
## 主要功能
- 用户的登录与注册
- 博客的创建,修改,删除和查看功能
- 可进行博客的分类查询
- 可进行博客的全站检索
- 增加了博客的分页功能

## 安装须知
在项目文件夹下打开命令窗口
输入 `pip3 install -r requirements.txt` 下载项目所需依赖
如果没有pip请自行下载

## 数据库配置
在mysql中创建名为 djangoblog 的数据库
`create database djangoblog`

## 配置
修改`Django_blog/settings.py` 中的配置
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'HOST': '127.0.0.1',
        'POST': 3306,
        'USER': 'root',
        'PASSWORD': '' #此密码为数据库的登录密码,如没有设置则为''.
    }
}```

在`Django_blog/settings.py`添加以下语句
```STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]```

## 问题相关
如有问题请将问题发送至邮箱liuhc1995@aliyun.com,转载请评论告知,很高兴能帮助大家



