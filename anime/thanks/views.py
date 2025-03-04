from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.
def thanks(request):
    return render(request, 'thanks/thanks.html')


def serve_video(request):
    video_path = os.path.join(settings.BASE_DIR, "thanks/static/thanks/video/lovechoice.mp4")
    return FileResponse(open(video_path, "rb"), content_type="video/mp4")

def so_close_so_far(request):
    return render(request, 'thanks/so_close_so_far.html')

def memorable(request):
    return render(request, 'thanks/memorable.html')