from django.shortcuts import render
from .forms import ImageUploadForm
import random

def predict(request):
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})
        
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data['image']
            prediction = random.choice(["猫", "犬"])

            return render(request, 'home.html', {'form': form, 'prediction': prediction})

        else:
            form = ImageUploadForm()
            return render(request, 'home.html', {'form': form})