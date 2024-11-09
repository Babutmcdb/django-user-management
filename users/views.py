from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from django.shortcuts import render, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Custom User List View with permissions

class UserListView(ListView):
    """
    View for displaying a list of users.

    This view fetches all users from the database and displays them in a table.
    """
    model = get_user_model()
    template_name = 'users/user_list.html'
    context_object_name = 'users'

# Create User View (Class-Based)
class UserCreateView(CreateView):
    """
    View for creating a new user.

    This function will create a new user through a form. Upon successful creation,
    the user is redirected to the user list page, and a success message is displayed
    and handled exception if we get any issue.
    """
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'users/create_user.html' # html template which will show the fileds of models to create user.
    success_url = reverse_lazy('user_list')  # Redirect to user list after successful creation

    def form_valid(self, form):
        """
        If the form is valid, save the new user and display a success message.
        """
        try:
            # Attempt to save the form (create user)
            messages.success(self.request, 'User created successfully!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Error creating user: {e}')
            return self.form_invalid(form)

# Edit User View (Class-Based)
class UserUpdateView(UpdateView):
    """
    View for updating an existing user's information.

    This function will update the user details through a form. Upon successful update,
    the user is redirected to the user list page, and a success message is displayed.
    """
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'users/edit_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):

        try:
            # Attempt to save the form (update user)
            messages.success(self.request, 'User updated successfully!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Error updating user: {e}')
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        try:
            # Retrieve user object by primary key
            return get_object_or_404(get_user_model(), pk=self.kwargs['pk'])
        except Http404:
            messages.error(self.request, 'User not found!')
            raise Http404("User not found")

# Delete User View (Class-Based)
class UserDeleteView(DeleteView):
    """
    View for deleting a user from the system.

    After deletion, the user is redirected to the user list page.
    """
    model = get_user_model()
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        try:
            # Attempt to delete the user
            messages.success(self.request, 'User deleted successfully!')
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(self.request, f'Error deleting user: {e}')
            return self.render_to_response(self.get_context_data())
