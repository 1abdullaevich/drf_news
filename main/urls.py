from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CategoryView.as_view()),
    path('user/', UserView.as_view()),
    path('article/', ArticleView.as_view()),
]
