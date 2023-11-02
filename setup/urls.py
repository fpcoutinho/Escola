from django.contrib import admin
from django.urls import path
from django.urls import include
from escola.views import alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos),
    path('api-auth/', include('rest_framework.urls'))
]
