#tables.py
import django_tables2 as tables
from .models import Usr_Urls

class UsrTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input":{"onclick": "toggle(this)"}})
    
    class Meta:
        model = Usr_Urls
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        empty_text = "There is no Short URLs, Start building alternative routes "
        exclude = ['short_id']
        
