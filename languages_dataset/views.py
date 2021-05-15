from django.shortcuts import render, get_list_or_404
from .models import Language
from .tasks import save_dataset


def index(request):
    save_dataset.delay({'name': 'Elixir', 'year': 2015, 
        'paradigm': 'functional', 'site': 'https://aaa.org'})
    languages = get_list_or_404(Language)
    context = {'languages': languages}
    return render(request, 'index.html', context)


