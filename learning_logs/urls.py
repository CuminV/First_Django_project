# learning_logs/urls.py

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all topics
    path('topics/', views.topics, name='topics'),
    #Page that shows a single topic and all its entries
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    #Page that allows users to add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page that allows users to add a new entry for a particular topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Page that allows users to edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]