from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('edit', views.edit, name='edit'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('search/<str:username>/', views.search, name='search'),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
