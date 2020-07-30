from django.urls import path
from . import views
# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relativ/',views.relativ,name='relativ'),
    path('other/',views.other,name='other'),
]