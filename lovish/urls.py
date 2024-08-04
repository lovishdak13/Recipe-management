from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vege.views import receipes, delete_receipe, update_receipe, Register_page, Login_page

urlpatterns = [
    path('receipes/', receipes, name="receipes"),
    path('admin/', admin.site.urls),
    path('delete-receipe/<int:id>/', delete_receipe, name="delete_receipe"),
    path('update-receipe/<int:id>/', update_receipe, name="update_receipe"),
    path('register/', Register_page, name="register"),
    path('login/', Login_page, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
