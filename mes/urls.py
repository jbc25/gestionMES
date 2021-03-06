"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from api.urls import get_api

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^', include('currency.urls', namespace='currency')),
    url(r'^bpm/', include('simple_bpm.urls', namespace='bpm')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^management/', include('management.urls', namespace='management')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^payments/', include('payments.urls', namespace='payments')),
    url(r'^intercoop/', include('intercoop.urls', namespace='intercoop')),
    url(r'^', include('social_balance.urls', namespace='balance')),
    url(r'^pay/', include('sermepa.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(get_api('v1').urls)),

] + \
  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


