from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404


def home(request):
    Music_data = Music_Database.objects.all()
    Artist_data = Artist.objects.all()
    Moods_data = Moods.objects.all()
    return render(request,'home.html',{'Music_data': Music_data,'Artist_data':Artist_data,'Moods_data': Moods_data})

def play_selected_song(request):
    Music_seleted = Music_Database.objects.filter()
    return redirect('home')

def upload_song(request):
    if request.method == "POST":
        Musc_name = request.POST.get("music_name")
        Musc_artist = request.POST.get("music_artist")
        Musc_criteria = request.POST.get("music_criteria")
        Musc_banner = request.FILES['music_banner']
        Musc_file = request.FILES['music_file']

        fs = FileSystemStorage()

        musc_banner_file = fs.save(Musc_banner.name,Musc_banner)

        musc_music_file = fs.save(Musc_file.name,Musc_file)

        existing_item_music = Music_Database.objects.filter(Music_Name = Musc_name ).first()
        existing_item_artist = Artist.objects.filter(Name = Musc_artist ).first()

        if not existing_item_music:
            if not existing_item_artist:
                existing_item_artist = Artist.objects.create(Name=Musc_artist)
            Music_Database.objects.create(
                Music_Name=Musc_name,
                Music_Artist=existing_item_artist,
                Music_Criteria=Musc_criteria,
                Music_Banner=musc_banner_file,
                Music_File=musc_music_file
            )
            return redirect('home')
    return render(request,'home.html')

def find_song(request):
    if request.method == "POST":
        song_name = request.POST.get("find_name")
        
        # Using icontains for case-insensitive and partial match
        found_song = Music_Database.objects.filter(Music_Name__icontains=song_name)
        found_artist = Music_Database.objects.filter(Music_Artist__icontains=song_name)
        
        return render(request, 'search.html', {
            'found_song': found_song,
            'found_artist': found_artist,
            'title_name': song_name.title()
        })
    
    return render(request, 'home.html')

def Artist_page(request):
    Artist_data = Artist.objects.all()
    return render(request,'Artist.html',{'Artist_data':Artist_data})

def explore_artist(request):
    if request.method == "POST":
        artist_name = request.POST.get("artist_name").title()
        # print(f"Artist Name: {artist_name}")
        # return HttpResponse(f"Artist Name: {artist_name}")
        founded = Music_Database.objects.filter(Music_Artist = artist_name)
        return render(request,'Explore.html',{'founded':founded,'Artist_Name':artist_name,'selected_artist_name':artist_name})

    return redirect('Artist_page')

def play_select(request,id):
    play_select = Music_Database.objects.get(id=id)
    print(play_select.id)
    Music_data = Music_Database.objects.all()
    Aritst_data = Artist.objects.all()
    Moods_data = Moods.objects.all()
    return render(request,'home.html',{'play_select':play_select,'Music_data': Music_data,'Artist_data':Aritst_data,'Moods_data':Moods_data})


# def play_next(request):
#     total_list = list(Music_Database.objects.all())
#     random_int = random.choice(total_list)
#     play_nexts = Music_Database.objects.get(id=random_int)
#     Music_data = Music_Database.objects.all()
#     return render(request,'home.html',{'Music_data':Music_data,'play_next':play_nexts})

def play_next(request):
    total_list = list(Music_Database.objects.all())
    if not total_list:
        return render(request, 'home.html', {'Music_data': [], 'play_next': None})
    
    play_nexts = random.choice(total_list)
    Music_data = Music_Database.objects.all()
    Aritst_data = Artist.objects.all()
    Moods_data = Moods.objects.all()
    return render(request, 'home.html', {'Music_data': Music_data, 'play_next': play_nexts,'Artist_data':Aritst_data,'Moods_data':Moods_data})

# def play_next(request,current_song):
#     current_id = current_song
#     total_list = list(Music_Database.objects.all())
#     for i in current_id:
#         i.current_id+1
#         if i.current_id in total_list:
#             break
#     play_nexts = Music_Database.objects.get(id=current_id)
#     Music_data = Music_Database.objects.all()
#     return render(request,'home.html',{'Music_data':Music_data,'play_next':play_nexts})

# def play_next(request, current_song):
#     current_song_obj = get_object_or_404(Music_Database, id=current_song)
#     total_list = list(Music_Database.objects.order_by('id'))
#     current_index = next((index for (index, d) in enumerate(total_list) if d.id == current_song_obj.id), None)
#     if current_index is not None and current_index + 1 < len(total_list):
#         next_song = total_list[current_index + 1]
#     else:
#         next_song = None
#     Music_data = Music_Database.objects.all()
#     return render(request, 'home.html', {'Music_data': Music_data, 'play_next': next_song})

def Mood_Explore(request):
    if request.method=='POST':
        Mood_Name = request.POST.get("Moods_name").title()
        Mood_found = Music_Database.objects.filter(Music_Criteria=Mood_Name)
        return render(request,'Moods.html',{'Mood_found':Mood_found})
