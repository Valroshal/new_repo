from django.contrib import admin
from django.urls import include, path
#from reviews.views import ProductViewSet, ImageViewSet - need to change to my directories
# from rest_framework.routers import DefaultRouter
# from django.conf import settings
# from django.conf.urls.static import static
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('admins.urls')),
]


    #path('admins/', include('django.contrib.auth.urls')), # new
    # path('get_user_details', views.GetUserDetails)
    # path('_user', views.GetUserDetails)
    # path('doLogin', views.doLogin)
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    #REST framework URLS
    #path('admins/students/', include('admins.urls', 'students_api'))
    #path('admins/teachers/', include('admins.urls', 'teachers_api'))
    #path('admins/admins/', include('admins.urls', 'admins_api'))