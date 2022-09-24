from django.urls import path

from MyDjangoProject.tasks.views import show_all_tasks, index, home

urlpatterns = (
    # http://localhost:8000/tasks/
    path('', index),
    # http://localhost:8000/tasks/it-works/
    path('it-works/', home),
    # http://localhost:8000/tasks/all/
    path('all/', show_all_tasks)
)
