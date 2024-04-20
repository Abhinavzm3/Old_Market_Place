from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('add/', views.add_product, name='add_product'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('signout/', views.signout, name='signout'), 
    path('remove/<int:product_id>/', views.remove_product, name='remove_product'),
        path('remove-product/<int:product_id>/', views.admin_remove_product, name='admin_remove_product'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
