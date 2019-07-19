from django.views.generic import View
from django.http import HttpResponse
"""
class PostListView1(View):
    def get(self, request):
        name = "늘한"
        html = '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>장고를 배우는 늘한입니다</p>
        '''.format(name=name)
        return HttpResponse(html)


class PostListView2(object):
    pass


class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass
"""