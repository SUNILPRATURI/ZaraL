from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='notes'),
    path('add/',views.add_notes,name='add_notes'),
    path('view/<int:id>/',views.view_notes,name='view_notes'),
    path('student/view/<int:id>/',views.view_student_notes,name='view_student_notes'),
    path('update/<int:id>/',views.edit_notes,name='edit_notes'),

]
