"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from blog import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
# router.register(r'<slug:slug>/', views.PostDetail, name='post_detail'),


# wiring up our API using automatic URL routing.
# Also including login URLs for the browsable API.
# probably deleting some of this stuff, just going through the quickstart before jumping into my real needs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
