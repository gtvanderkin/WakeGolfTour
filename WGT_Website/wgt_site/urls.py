"""wgt_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from golf_course import urls as golf_course_urls
from golfer import urls as golfer_urls
from tournament import urls as tournament_urls
from golfer_polls import urls as golfer_polls_urls

from . views import homepage

urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('golfer/', include(golfer_urls)),
    path('tournament/', include(tournament_urls)),
    path('golf_course/', include(golf_course_urls)),
    path('golfer_polls', include(golfer_polls_urls)),
]

admin.site.site_header = 'Wake Golf Tour'
admin.site.index_title = 'WGT Site Administration'
