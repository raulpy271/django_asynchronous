from django.shortcuts import render
from .models import Language
from .tasks import read_files


was_processing = False


def index(request):
    global was_processing
    render_table = False
    languages = Language.objects.all()
    if languages and was_processing:
        render_table = True
    else:
        read_files.delay()
        was_processing = True
    context = {
        'languages': languages, 
        'render_table': render_table}
    return render(request, 'index.html', context)


