from django.urls import path
from . import views

app_name = 'exhibition'

urlpatterns = [
    path('', views.direct_shop_view, name='exhibition_list'),
    path('list/', views.ExhibitionListView.as_view(), name='exhibition_list_class'),
    path('<int:pk>/', views.ExhibitionDetailView.as_view(), name='exhibition_detail'),
    path('debug/', views.debug_view, name='debug'),
    path('simple/', views.simple_list_view, name='simple_list'),
] 