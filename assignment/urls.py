from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='assignments'),
    path('add/',views.add_assignment,name='add_assignment'),
    path('view/<int:id>/',views.view_assignment,name='view_assignment'),
    path('edit/<int:id>/',views.edit_assignment,name='edit_assignment'),
    path('manage/<int:id>/',views.deactivate_assignment,name='deactivate_assignment'), 
    
]
