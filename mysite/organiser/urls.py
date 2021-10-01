from django.urls import path

from organiser.views import TagAPIDetail, TagAPIList

urlpatterns = [
    path("tags/", TagAPIList.as_view(), name='api_tag_list'),
    path("tags/<int:pk>/", TagAPIDetail.as_view(), name='api_tag_detail'),    
]
