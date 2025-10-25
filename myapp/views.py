from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def classes(request):
    return render(request, 'pages/class.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def team(request):
    return render(request, 'pages/team.html')

def blog(request):
    return render(request, 'pages/blog.html')
