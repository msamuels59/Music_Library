from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AddAlbum
from django.utils import timezone

# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/home.html', {'albums': albums})

def add_album(request):
    if request.method == 'POST':
        form = AddAlbum(request.POST, request.FILES)
        if form.is_valid():
            add_album = form.save()
            return redirect('home')
    else:
        form = AddAlbum()
    return render(request, 'albums/add.html', {'form' : form})

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_details.html', {'album': album})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AddAlbum(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            album.save()
            return redirect('album_details', pk=album.pk)
    else:
        form = AddAlbum(instance=album)
    return render(request, 'albums/album_edit.html', {'form' : form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home')    
    return render(request,'albums/delete.html', {'album' : album})
