
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("todo/",views.todo,name="todo"),
   
    path("add_todo/",views.add_todo,name="add_todo"),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:todo_id>',views.update_todo,name='update_todo'),
    path('mark_complete/<int:todo_id>',views.mark_complete,name='mark_complete'),
    path('upload_profile/',views.profile,name="upload_profile"),
     path('about/',views.about,name="about")
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)