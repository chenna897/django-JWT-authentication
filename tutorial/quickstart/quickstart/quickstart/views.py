from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




# I created a simple API to allow admin users to view and edit the users and groups in the system.
# Proof:  https://www.dropbox.com/s/tcp7i0ol55sccg2/restloginpage.PNG?dl=0
#         https://www.dropbox.com/s/92i9m9btm4rdk3f/createnewuser.PNG?dl=0
#         https://www.dropbox.com/s/e4sa0qix48scm5w/userlist.PNG?dl=0
#         https://www.dropbox.com/s/jdtcjgvf4y8fpfo/edituserdetails.PNG?dl=0
#         https://www.dropbox.com/s/262unhcmsvujsko/deleteuser.PNG?dl=0
#         https://www.dropbox.com/s/oy55359yrf543bu/jsondata.PNG?dl=0

# Bellow i have provided the django-rest-api github source code link
#         https://github.com/chenna897/django-rest-api