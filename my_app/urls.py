from django.urls import path
from . import views
app_name = 'my_app'
urlpatterns=[
    path('uploadsensordata',views.uploadsensordata,name='uploadsensordata'),
    path('getsensordata/',views.getsensordata, name='getsensordata'),
    # path('blrfan/laststatus/',views.BlrFan.as_view(),name='BlrFan'),
    path('blrfan/<int:status>/',views.blrfanstatus,name='BlrFan'),
    path('blrlight/<int:status>/',views.blrlightstatus,name='BlrLight'),
    path('vancfan/<int:status>/',views.vancfanstatus,name='VancFan'),
    path('vanclight/<int:status>/',views.vanclightstatus,name='VancLight'),
]
