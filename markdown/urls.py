from django.conf.urls import url

from markdown.views import index


urlpatterns = [
  url(r'^', index)
]