from django.contrib import admin
from django.urls import path
from auapp.views import home, usignup, uwelcome, ulogout, urnpassword, create, remove, result, place
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("usignup/", usignup, name="usignup"),
    path("uwelcome/", uwelcome, name="uwelcome"),
    path("ulogout/", ulogout, name="ulogout"),
    path("urnpassword/", urnpassword, name="urnpassword"),
    path("create/", create, name="create"),
    path("place/", place, name="place"),
    path("remove/<int:id>", remove, name="remove"),
    path("result/<int:id>", result, name="result"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
