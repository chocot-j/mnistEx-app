from django.shortcuts import render
from .models import GetImage
from .img_guess import guess_img, make_plot

# Create your views here.
def index(request):
    return render(request, 'mnistEx/mainPage.html')


def guess(request):
    if request.method == "POST":
        predict, predictions = guess_img(request.POST['img'])
        image = make_plot(predictions)
        context = {'predict': predict, 'image': image}
    return render(request, 'mnistEx/mainPage.html', context)