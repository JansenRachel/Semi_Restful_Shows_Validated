from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.display_all_shows),

    path('shows/new', views.add_show_form),
    path ('shows/createShow', views.create_new_show),

# this path is for '<int:show_id>'
    path('show_details/<int:show_id>', views.display_show_info),

    path('shows/<int:show_id>/destroy', views.delete_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),

]