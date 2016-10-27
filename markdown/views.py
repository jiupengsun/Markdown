from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  if request.method == "GET":
    return render(request, 'index.html')

def document(request):
  if request.method == "GET":
    context = {
      'flag': 1,
      'message' : 'success',
      'data': {}
    }
    return JsonResponse(context)
