from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^start', start, name='start'),
    url(r'^success', display_successFactor, name="display_successFactor"),
    url(r'^performanceIndicator$', display_performanceIndicator, name="display_performanceIndicator"),

    url(r'^add_successFactors$', add_successFactor, name="add_successFactor"),
    url(r'^add_performanceIndicator$', add_performanceIndicator, name="add_performanceIndicator"),

    url(r'^laptops/edit_item/(?P<pk>\d+)$', edit_successFactor, name="edit_successFactor"),
    url(r'^desktops/edit_item/(?P<pk>\d+)$', edit_performanceIndicator, name="edit_performanceIndicator"),
]
