from django.contrib import admin

from .models import Movie
from news.models import News 
from movie.models import Review

admin.site.register(Movie)
admin.site.register(News)
admin.site.register(Review)





