from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from blog.views import registration

handler403 = 'pages.views.csrf_failure'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', 'blog')),
    path('pages/', include('pages.urls', 'pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', registration, name='registration'),
    path(
        'auth/password_change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change',
    ),
]
