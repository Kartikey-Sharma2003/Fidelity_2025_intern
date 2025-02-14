from django.contrib import admin
from django.urls import path,include
from .views import QuestionPaper
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
        description="API documentation",
        terms_of_service="",
        contact=openapi.Contact(email="kartikeytrench47@example.com"),
        license=openapi.License("open"),
    ),
    public=True
    
)

urlpatterns = [
    path('list/', QuestionPaper.as_view({'get': 'list'})),
    path('create/', QuestionPaper.as_view({'post': 'create'})),
    path('retreive/<int:pk>/', QuestionPaper.as_view({'get': 'retreive'})),
    path('update/<int:pk>/', QuestionPaper.as_view({'put': 'update'})),
    path('delete/<int:pk>/', QuestionPaper.as_view({'delete': 'destroy'})),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
