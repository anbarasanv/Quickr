from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    # path('', views.EmployeeList.as_view()),
    # path('<int:pk>/',views.EmployeeDetail.as_view() ),
    url(r'', views.EmployeeList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
