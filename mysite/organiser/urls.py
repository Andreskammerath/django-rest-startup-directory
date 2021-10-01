from django.urls import path

from organiser.views import (
    TagAPIDetail, TagAPIList,
    StartupAPIDetail, StartupAPIList,
    NewsLinkAPIDetail, NewsLinkAPIList)

urlpatterns = [
    path("tags/", TagAPIList.as_view(), name='api_tag_list'),
    path("tags/<str:slug>/", TagAPIDetail.as_view(), name='api_tag_detail'),    
    path("startups/", StartupAPIList.as_view(), name='api_startup_list'),
    path("startups/<str:slug>/", StartupAPIDetail.as_view(), name='api_startup_detail'),
    path("newslink/", NewsLinkAPIList.as_view(), name='api_newslink_list'),
    path("newslink/<str:slug>/", NewsLinkAPIDetail.as_view(), name='api_newslink_detail'),
]
