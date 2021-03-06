from django.contrib import admin

# Register your models here.


from .models import DetailFromReact,ValueFromMl,ImageModel


admin.site.register(DetailFromReact)
admin.site.register(ValueFromMl)
admin.site.register(ImageModel)