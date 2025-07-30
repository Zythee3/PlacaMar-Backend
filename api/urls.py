from django.urls import path, include
from . import views

urlpatterns = [
    path('placas/', include('api.placas.urls')),
    path('choices/', views.get_choices_view, name='choices'),
    path('cidades-por-estado/<int:estado_id>/', views.get_cidades_por_estado_view, name='cidades_por_estado'),
    path('registrar-acesso-qr/', views.registrar_acesso_qr, name='registrar_acesso_qr'),
    path('conteudo-educativo/<int:conteudo_id>/quiz/<int:question_index>/get/', views.get_quiz_question, name='get_quiz_question'),
    path('conteudo-educativo/<int:conteudo_id>/quiz/<int:question_index>/submit/', views.submit_quiz_answer, name='submit_quiz_answer'),
    path('conteudo-educativo/<int:conteudo_id>/', views.get_conteudo_educativo_details, name='get_conteudo_educativo_details'),
]

