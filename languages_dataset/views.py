from django.shortcuts import render, get_list_or_404
from .models import Language


def index(request):
    languages = get_list_or_404(Language)
    context = {'languages': languages}
    return render(request, 'index.html', context)


