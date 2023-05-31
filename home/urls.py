from.import views
from django.urls import path


urlpatterns=[
    path('',views.base,name='base'),
    path('detailed/<int:id>',views.detailed,name='detailed'),
    path('upload/',views.upload,name='upload'),
]