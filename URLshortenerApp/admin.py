from django.contrib import admin

from URLshortenerApp.models import Usr_Urls
# Register your models here.

#the below code registers the Usr_Urls model that created to Django Admin.
class UrlsAdmin(admin.ModelAdmin):
      list_display = ( 'short_id','short_url','description','httpurl','pub_date', 'count', 'user')
      ordering = ('-pub_date',)

admin.site.register(Usr_Urls, UrlsAdmin) # Register the Urls model
