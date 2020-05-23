from django.contrib import admin
from django.forms import TextInput, ModelForm
from suit.admin import SortableModelAdmin
from .models import MarqueeMessage


class MarqueeMessageForm(ModelForm):
    class Meta:
        widgets = {
            'message': TextInput(attrs={'class': 'input-xxlarge'}),
        }


class MarqueeMessageAdmin(SortableModelAdmin):
    form = MarqueeMessageForm
    sortable = 'order'
    list_editable = ('display', 'order')
    list_display = ('message', 'display', 'order')


admin.site.register(MarqueeMessage, MarqueeMessageAdmin)
