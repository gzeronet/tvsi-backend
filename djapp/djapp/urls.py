from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_registration.api.views import register, login, logout
from tvsi.views import EpisodeViewSet, BookmarkedEpisodeViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="TV Show Information",
      default_version='v1',
      description="Information REST API With Swagger Document",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

user_urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

router = SimpleRouter(trailing_slash=False)
router.register(r'episode', EpisodeViewSet, basename='episode')
router.register(
    r'bookmarked-episode',
    BookmarkedEpisodeViewSet, basename='bookmarked_episode')

urlpatterns = [
    path('user/', include(user_urlpatterns)),
    path('tvsi/', include(router.urls)),
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    # just for db data check, feel free to remove admin page
    path('admin/', admin.site.urls),
]
