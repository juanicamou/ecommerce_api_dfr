from django.urls import path
from apps.users.api.api import user_get_all_api_view, user_create_api_view, user_detail_api_view, user_update_api_view, user_delete_api_view 


urlpatterns = [
    path('all/', user_get_all_api_view, name = 'user_all'),
    path('create/', user_create_api_view, name = 'user_create'),
    path('detail/<int:pk>/', user_detail_api_view, name = 'user_details'),
    path('update/<int:pk>/', user_update_api_view, name = 'user_update'),
    path('delete/<int:pk>/', user_delete_api_view, name = 'user_delete'),
]
