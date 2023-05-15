from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Book list Api",
        default_version="v1",
        description="Library demo project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email='suhrobturaev2004@gmail.com'),
        license=openapi.License(name="demo license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auht/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]
