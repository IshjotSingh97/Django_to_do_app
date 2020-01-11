from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addtask',views.addtask,name="addtask"),
    path('deletetask/<int:id>',views.deletetask,name="deletetask"),
    path('listalltask',views.listalltask,name="listalltask"),
    path('edittask/<int:id>',views.edittask,name="edittask"),
    path('updatetask/<int:id>',views.updatetask,name="updatetask"),
    path('404',views.error_404,name="error_404"),
    path('about',views.about,name='about')
]