from django.urls import path
# from .views import (home, animales, armas, construcciones, 
#                     consumibles, enemigos, flora, forowiki, historia,
#                     inicio_sesion_wiki, logros, lugares, micuentatf, 
#                     recuperarcontra, registrarse_wiki, registro, inicio)
from .views import (vista_thread, modificar_thread, vista_comentario, modificar_comentario)

urlpatterns = [
   path('vista_thread', vista_thread, name="vista_thread"),
   path('modificar_thread/<id>', modificar_thread, name="modificar_thread"),
   path('vista_comentario', vista_comentario, name="vista_comentario"),
   path('modificar_comentario/<id>', modificar_comentario, name="modificar_comentario"),
]