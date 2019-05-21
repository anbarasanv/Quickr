from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from . models import  Employee
from . serializers import EmployeeSerializer
#userdefined
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime, timedelta

class EmployeeList(APIView):

    def get(self, request):
        params = request.GET.get("chunk")
        if params:
            end = int(params)*20
            start = (int(params)-1)*20
            print(start,end)
            queryset = Employee.objects.order_by()[start:end]
            serializer = EmployeeSerializer(queryset, many= True)
            return Response(serializer.data)
        else:
            normal_queryset = Employee.objects.order_by('score').reverse()
            now = datetime.now().date()
            days = timedelta(days=14)
            #Query set without deparment 'Waltzz' and more than 14 days
            queryset = Employee.objects.order_by('score').reverse().exclude(department='Waltzz').exclude(created_date__lt=now-days)
            #Query set with deparment 'Waltzz'
            f_days_old = Employee.objects.order_by('score').filter(created_date__lt=now-days)
            #Query set older than 14 days
            s_department = Employee.objects.order_by('score').filter(department='Waltzz')
            # s_five = 6
            # s_six = 7
            # lst = iter(s_department)
            # for i in lst:
            #     try:
            #         x = i
            #         y = next(lst)
            #         queryset.insert(s_five,x)
            #         queryset.insert(s_six,y)
            #         s_five = s_five + 5
            #         s_six = s_six + 5
            #     except StopIteration:
            #         break
            serializer = EmployeeSerializer(normal_queryset, many= True)
            return Response(serializer.data)
