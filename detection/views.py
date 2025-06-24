from django.shortcuts import render
import base64
from PIL import Image
from io import BytesIO
from django.http import JsonResponse
import json
from .utils import detect_expression
from django.views.decorators.csrf import csrf_exempt

def upload_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        emotions = detect_expression(image)
        return render(request, "detection/result.html", {"emotions": emotions})
    return render(request, "detection/upload.html")

def analyze_frame(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Frame received!")
            image_data = data['image'].split(',')[1]
            image_bytes = base64.b64decode(image_data)
            image = BytesIO(image_bytes)

            emotions = detect_expression(image)
            print("Emotions:", emotions)

            # Convert float32 to float
            if "error" not in emotions:
                emotions = {k: float(v) for k, v in emotions.items()}
            return JsonResponse(emotions)
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"error": str(e)})
        

def webcam_view(request):
    return render(request, "detection/webcam.html")

