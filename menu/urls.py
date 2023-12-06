from django.urls import path

from .views import IndexView, DrawMenuView

urlpatterns = [
    path('', IndexView.as_view(), name='main_menu'),
    path('<path:path>/', DrawMenuView.as_view(), name='draw_menu'),
]