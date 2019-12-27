"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from rest_framework import routers
from quickstart import views
# from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from rest_framework_simplejwt import views as jwt_views#<--JWT

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employe', views.EmployeeViewSet)
router.register(r'project', views.ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('hello/', views.HelloView.as_view(), name='hello'),
    # url('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

    url('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),#<--JWT
    url('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),#<--JWT

    
]

