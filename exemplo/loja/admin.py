#admin
from django.contrib import admin
from .models import *

admin.site.register(filmes)
admin.site.register(atores)
admin.site.register(elenco)