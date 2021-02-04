from django.contrib import admin
from django.urls import include, path
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
    path('admins/', include('django.contrib.auth.urls')), # new
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
