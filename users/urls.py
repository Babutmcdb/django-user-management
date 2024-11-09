from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDeleteView,UserListView

urlpatterns = [
    # To list users
    path('list/', UserListView.as_view(), name='user_list'),

    # To create users
    path('create/', UserCreateView.as_view(), name='create_user'),

    # To update users based on the primary id
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='edit_user'),

    # To delete users based on the primary id
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),

]
