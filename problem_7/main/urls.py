from django.urls import path, include
from .views import Index, EntryCreateView, EntryDeleteView, EntryUpdateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', EntryCreateView.as_view(), name='create_entry'),
    path('update/<int:pk>', EntryUpdateView.as_view(), name='update_entry'),
    path('delete/<int:pk>', EntryDeleteView.as_view(), name='delete_entry'),
]
