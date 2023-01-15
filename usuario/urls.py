from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='usuario'),
    path('<letter>', views.index, name='usuario'),
    #path('view/<int:id>', views.view, name='usuario_view'),
    #path('edit/<int:id>', views.edit, name='usuario_edit'),
    #path('create/', views.create, name='usuario_create'),
    #path('delete/<int:id>', views.delete, name='usuario_delete')
]