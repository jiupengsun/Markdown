from django.conf.urls import url

from markdown.views import index, document


urlpatterns = [
  url(r'^', index),
  url(r'doc', document),
]