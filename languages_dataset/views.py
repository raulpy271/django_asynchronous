from django.shortcuts import render, get_list_or_404
from .models import Language
from .tasks.tasks import save_example


def index(request):
    save_example()
    languages = get_list_or_404(Language)
    context = {'languages': languages}
    return render(request, 'index.html', context)


