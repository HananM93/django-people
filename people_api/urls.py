from django.urls import path
from .views import People , PersonDetail

urlpatterns = [
    path('', People.as_view(), name='people'),
    path('<int:pk>', PersonDetail.as_view(), name='person_detail')
]
