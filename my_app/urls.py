from django.urls import path
from . import views
app_name = 'my_app'
urlpatterns=[
    path('uploadsensordata',views.uploadsensordata,name='uploadsensordata'),
    path('blrfan/<int:id>/',views.blrfanstatus,name='blrfanstatus'),
    path('blrlight/<int:id>/',views.blrlightstatus,name='blrlightstatus'),
    path('vancfan/<int:id>/',views.vancfanstatus,name='vancfanstatus'),
    path('vanclight/<int:id>/',views.vanclightstatus,name='vanclightstatus'),
]
