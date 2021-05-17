from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer
from .tasks import read_files


def index(request):
    return render(request, 'index.html', {})


@api_view(['GET'])
def data(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        languages_data = LanguageSerializer(languages, many=True).data
        return Response(languages_data)


