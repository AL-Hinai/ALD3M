from django.conf.urls import url 
from ALD3M import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'), 
]
