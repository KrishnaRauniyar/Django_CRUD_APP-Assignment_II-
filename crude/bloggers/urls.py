from django.urls import path
from .views import list_all_user, detail_view_of_users, create_user_info, update_user_info, delete_user_info


urlpatterns = [
    path('list/', list_all_user),
    path('create/', create_user_info),
    path('detail/<int:user_id>/', detail_view_of_users),
    path('delete/<int:user_id>/', delete_user_info),
    path('update/<int:user_id>/', update_user_info),

]