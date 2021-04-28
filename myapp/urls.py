from django.urls import include,path,re_path
from .views import EmplyoeeRUDView,EmplyoeeView

urlpatterns = [
    re_path(r'^api/emplyoees/(?P<pk>[0-9]+)$', EmplyoeeRUDView.as_view(), name='emplyoee_rud'),

    path('api/emplyoees/', EmplyoeeView.as_view(), name='emplyoee_view')
]
