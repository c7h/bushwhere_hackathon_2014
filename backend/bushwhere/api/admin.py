from django.contrib import admin
from polls.models import Place, User, Hint

admin.site.register(Places)
admin.site.register(User)
admin.site.register(Hint)