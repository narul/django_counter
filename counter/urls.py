from django.urls import path
from .views import current, increment, decrement


urlpatterns = [
    path('', current),
    path('increment/', increment, name='increment'),
    path('decrement/', decrement , name='decrement')
]
