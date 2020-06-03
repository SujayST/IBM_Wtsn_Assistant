from django.urls import path
from .views import CommentView

urlpatterns = [

    path('watson/', CommentView, name='comment'),
]

