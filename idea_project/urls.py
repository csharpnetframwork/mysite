from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ideas/', include('ideas.urls')),  # Include the URLs from the 'ideas' app
    path('', lambda request: HttpResponseRedirect('ideas/')),  # Redirect root URL to 'ideas/'
]
