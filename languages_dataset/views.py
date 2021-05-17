from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer
from .tasks import read_files


was_rendering = False


def index(request):
    return render(request, 'index.html', {})


@api_view(['GET'])
def data(request):
    global was_rendering
    if request.method == 'GET':
        if not was_rendering:
            read_files.delay()
            was_rendering = True
        languages = Language.objects.all()
        languages_data = LanguageSerializer(languages, many=True).data
        return Response(languages_data)


