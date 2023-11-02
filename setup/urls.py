from django.contrib import admin
from django.urls import path
from django.urls import include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/cursos/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/alunos/', ListaAlunosMatriculados.as_view()),
    path('auth/', include('rest_framework.urls')),
]
