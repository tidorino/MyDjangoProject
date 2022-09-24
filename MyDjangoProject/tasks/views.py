from django.http import HttpResponse
from django.shortcuts import render

from MyDjangoProject.tasks.models import Task


# Create your views here.


def home(request):
    items = ''.join(f'<li>{i}</li>' for i in range(4))
    html = f'''
<h1>It works!</h1>
<ul>
    {items}
</ul>
    '''
    return HttpResponse(html)


def show_all_tasks(request):
    all_tasks = Task.objects\
        .order_by('id')\
        .all()
    # [name(id), name(id)]
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)

    return HttpResponse(result)


def index(request):
    all_tasks = Task.objects \
        .order_by('id') \
        .all()

    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)
