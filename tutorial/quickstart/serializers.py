

from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'eid', 'ename','eemail','econtact']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'projectname']

# Hi sir,
   
#    i created a employee CURD django-rest application based on employe model this are the screenshots related to the CURD application.

# Proof: https://www.dropbox.com/s/5y5hwaxjs52qwmk/insertemployeedetails.PNG?dl=0
# 	     https://www.dropbox.com/s/gblovqr7mcnz0jj/employeeoptions.PNG?dl=0
#        https://www.dropbox.com/s/kpbcjyog2hwbxyy/employeelist.PNG?dl=0
#        https://www.dropbox.com/s/yyg2ca6xhvjmrdm/employeejsondata.PNG?dl=0
#        https://www.dropbox.com/s/v7z408t9llo704y/employeedelete.PNG?dl=0

 