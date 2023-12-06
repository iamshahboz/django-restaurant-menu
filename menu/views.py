from django.shortcuts import render
from django.views import View 
from .models import Menu 
from django.http import HttpResponse

class IndexView(View):
    template_name = 'menu/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'menus': Menu.objects.all()})


class DrawMenuView(View):
    template_name = 'menu/index.html'

    def get(self,request, *args, **kwargs):
        path = kwargs.get('path','')
        splitted_path = path.split('/')
        assert len(splitted_path) > 0, ('= Draw_menu function failed =')
        print(splitted_path)
        return render(request, self.template_name, {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})