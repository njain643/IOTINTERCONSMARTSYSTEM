from django.urls import path
from . import views
app_name = 'my_app'
urlpatterns=[
    path('uploadsensordata',views.uploadsensordata,name='uploadsensordata'),
    path('getsensordata/',views.getsensordata, name='getsensordata'),
    # path('blrfan/laststatus/',views.BlrFan.as_view(),name='BlrFan'),
    path('blrfan/<int:status>/',views.blrfanstatus,name='BlrFan'),
    # path('blrlight/<int:id>/',views.blrlightstatus,name='blrlightstatus'),
    # path('vancfan/<int:id>/',views.vancfanstatus,name='vancfanstatus'),
    # path('vanclight/<int:id>/',views.vanclightstatus,name='vanclightstatus'),
]
