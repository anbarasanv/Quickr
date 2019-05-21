from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('created_date','employee_code','department','score')
        model = Employee
