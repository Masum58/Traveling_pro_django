from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.home,name='name'),
   path('add',views.add,name='add')
]