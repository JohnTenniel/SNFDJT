from django.shortcuts import render


def photo(request):
    return render(request, "gallery/photo.html")


def video(request):
    return render(request, "gallery/videos.html")
