from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def test_page(request):
    return HttpResponse("<h1>Test page.</h1>")
