from django.urls import path
from .views import get_main,get_sub,get_calorie,post_main,put_sub,post_calorie,image_response,get_weight


urlpatterns = [
    path('postimage/', image_response),
    path('getmain/', get_main),
    path('postmain/', post_main),
    path('getsub/', get_sub),
    path('getweight/', get_weight),

    path('putsub/', put_sub),
    path('getcalorie/', get_calorie),
    path('postcalorie/', post_calorie),

]

# urlpatterns = format_suffix_patterns(urlpatterns)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
