from django.http import HttpResponse
from django.http import Http404
# from django.template import loader
from django.shortcuts import render,get_object_or_404  
from .models import Album

def index(request):
	all_album = Album.objects.all()
	# html=''
	# for album in all_album:
	# 	url ='/music/'+str(album.id)+'/'
	# 	html += '<a href="'+url+'">'+album.album_title+'</a><br>'
	# template = loader.get_template("music/index.html")
	context ={'all_album' : all_album}
	# return HttpResponse(template.render(context,request))
	return render(request, "music/index.html",context)


# Create your views here.
def detail(request,album_id):
	# return HttpResponse('<h2> Detail of Album no is: '+str(album_id)+'</h2>')
	# try:
	# 	album = Album.objects.get(id=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does not exists")
	album = get_object_or_404(Album,id=album_id)
	return render(request, "music/details.html",{'album' : album})

