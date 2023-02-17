from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order_downloader.scripts.download_sample_script import run_download_sample_routine


@api_view(['POST'])
def download_sample(request):
    print(request.data['order'])
    result = run_download_sample_routine(request.data['order'])
    print(result)
    return Response({ "result": "OK" })


def index(request):
    return render(request, "index.html")
