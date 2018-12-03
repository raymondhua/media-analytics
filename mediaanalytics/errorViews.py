from django.shortcuts import render

'''---Errors - Have DEBUG = on and ALLOWED_HOSTS=['*'] in settings.py---
---DON'T UNCOMMENT IT UNLESS IF YOU'RE DEPLOYING---'''

def error404(request):
    return render(request,'error404.html', status=404)

def error500(request):
    return render(request,'error500.html', status=500)