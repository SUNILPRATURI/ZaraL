from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='courses'),
    path('add/',views.add_course,name='add_course'),
    path('view/<str:id>/',views.view_course,name='view_course'),
    path('edit/<str:id>/',views.edit_course,name='edit_course'),
    path('manage/<str:id>/',views.deactivate_course,name='deactivate_course'), 
    
]
