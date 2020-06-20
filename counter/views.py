from .models import Counter
from django.shortcuts import render
from django.shortcuts import redirect


def current(request):
    instance, created = Counter.objects.get_or_create(id=1)
    return render(request, 'current.html', {'instance': instance})


def increment(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return redirect('http://127.0.0.1:8000/', {'instance': instance})


def decrement(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value -= 1
    instance.save()
    return redirect('http://127.0.0.1:8000/', {'instance': instance})
