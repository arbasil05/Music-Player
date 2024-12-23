from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('selected_song/',views.play_selected_song,name='selected_song'),
    path('upload/',views.upload_song,name='upload'),
    path('find_song/',views.find_song,name='find_song'),
    path('Artists/',views.Artist_page,name='Artists'),
    path('play_select/<int:id>',views.play_select,name='play_select'),
    path('play_next/',views.play_next,name='play_next'),
    path('Artist/',views.explore_artist,name='explore_artist'),
    path('Moods/',views.Mood_Explore,name='Moods'),
]