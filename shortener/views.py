from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
from django.shortcuts import get_object_or_404, redirect

@api_view(['POST'])
def create_short_url(request):
    serializer = URLSerializer(data=request.data)

    if serializer.is_valid():
        url = serializer.save()

        short_url = request.build_absolute_uri(f'/{url.short_code}')

        return Response({
            "short_url": short_url,
            "original_url": url.original_url
        })

    return Response(serializer.errors)


def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)

    url.clicks += 1
    url.save()

    return redirect(url.original_url)

from django.shortcuts import render
from .models import URL

def home(request):
    short_url = None

    if request.method == "POST":
        original_url = request.POST.get("original_url")
        url = URL.objects.create(original_url=original_url)

        short_url = request.build_absolute_uri(f'/{url.short_code}')

    return render(request, "shortener/index.html", {"short_url": short_url})