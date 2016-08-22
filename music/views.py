from django.http import HttpResponse
from .models import Album

def index(request):
	all_album = Album.objects.all()
	html=''
	for album in all_album:
		url ='/music/'+str(album.id)+'/'
		html += '<a href="'+url+'">'+album.album_title+'</a><br>'
	return HttpResponse(html)

# Create your views here.
def detail(request,album_id):
	return HttpResponse('<h2> Detail of Album id is:'+str(album_id)+'</h2>')
