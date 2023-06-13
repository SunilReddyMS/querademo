
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postApp/', include('postApp.urls')),
    path('quera123/', include('quera123.urls')),
]

