from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer
from .tasks import read_files


was_processing = False


def index(request):
    global was_processing
    render_table = False
    languages = Language.objects.all()
    if languages and was_processing:
        render_table = True
    else:
        read_files.apply_async(retry=False)
        was_processing = True
    context = {
        'languages': languages, 
        'render_table': render_table}
    return render(request, 'index.html', context)


@api_view(['GET'])
def data(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        languages_data = LanguageSerializer(languages, many=True).data
        return Response(languages_data)


