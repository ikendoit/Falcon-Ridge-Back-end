from django.urls import path
from . import APIViews

urlpatterns = [
    path('news', APIViews.get_news_info, name='langara-news'),
    path('transfer', APIViews.get_transfer, name='langara-transfers'),
    path('rooms', APIViews.get_room, name='langara-rooms'),
    path('avail', APIViews.get_avail, name='langara-availale'),
    path('', APIViews.get_courses_info, name='langara'),
]
