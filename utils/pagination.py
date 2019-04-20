"""
分页器
"""

from django.utils.safestring import mark_safe
from django.http import QueryDict

class Pagination:
    
    def __init__(self, request, all_count, query_params=QueryDict(), per_num=10, max_show=11):
        # 基本的URL
        self.base_url = request.path_info
        
        # 查询条件 query = 'tiaojian'
        self.query_params = query_params
        # _mutable改为True就可以修改
        self.query_params._mutable = True
        # 当前页码
        try:
            self.current_page = int(request.GET.get('page', 1))
            if self.current_page <= 0:
                self.current_page = 1
        except Exception as e:
            self.current_page = 1
        # 最多显示的页码数
        self.max_show = max_show
        half_show = max_show // 2
        
        # 每页显示的数据条数
        self.per_num = per_num
        # 总数据量
        self.all_count = all_count
        
        # 总页码数
        self.total_num, more = divmod(all_count, per_num)
        if more:
            self.total_num += 1
        
        # 总页码数小于最大显示数：显示总页码数
        if self.total_num <= max_show:
            self.page_start = 1
            self.page_end = self.total_num
        else:
            # 总页码数大于最大显示数：最多显示11个
            if self.current_page <= half_show:
                self.page_start = 1
                self.page_end = max_show
            elif self.current_page + half_show >= self.total_num:
                self.page_end = self.total_num
                self.page_start = self.total_num - max_show + 1
            else:
                self.page_start = self.current_page - half_show
                self.page_end = self.current_page + half_show
    
    @property
    def start(self):
        return (self.current_page - 1) * self.per_num
    
    @property
    def end(self):
        return self.current_page * self.per_num
    
    @property
    def show_li(self):
        # 存放li标签的列表
        html_list = []
        
        self.query_params['page'] = 1 # query='tianjian' page=1
        # query=alex&page=1
        
        first_li = '<li><a href="{}?{}">首页</a></li>'.format(self.base_url, self.query_params.urlencode())
        html_list.append(first_li)
        
        if self.current_page == 1:
            prev_li = '<li class="disabled"><a><<</a></li>'
        else:
            self.query_params['page'] = self.current_page - 1
            prev_li = '<li><a href="{0}?{1}"><<</a></li>'.format(self.base_url, self.query_params.urlencode())
        html_list.append(prev_li)
        
        for num in range(self.page_start, self.page_end + 1):
            self.query_params['page'] = num
            if self.current_page == num:
                li_html = '<li class="active"><a href="{0}?{1}">{2}</a></li>'.format(self.base_url,
                                                                                     self.query_params.urlencode(), num)
            else:
                li_html = '<li><a href="{0}?{1}">{2}</a></li>'.format(self.base_url,
                                                                      self.query_params.urlencode(), num)
            html_list.append(li_html)
        
        if self.current_page == self.total_num:
            next_li = '<li class="disabled"><a>>></a></li>'
        else:
            self.query_params['page'] =self.current_page + 1
            next_li = '<li><a href="{0}?{1}">>></a></li>'.format(self.base_url,self.query_params.urlencode())
        
        html_list.append(next_li)
        
        self.query_params['page'] = self.total_num
        last_li = '<li><a href="{0}?{1}">尾页</a></li>'.format(self.base_url,self.query_params.urlencode())
        html_list.append(last_li)
        
        return mark_safe(''.join(html_list))
