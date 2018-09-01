from django.contrib import admin
from django.urls import path, include
import market.views
import mods.views, games.views, textures.views, skins.views

urlpatterns = [
    # ADMIN PAGE URL ROUTING
    path('admin/', admin.site.urls),
    # TRENDING PAGE URL ROUTING
    #path('trending/', include(trends.urls)),
        #   Future trending urls will be
        #   ¬ trending/mods
        #   ¬ trending/games
        #   ¬ trending/textures
        #   ¬ trending/skins
    
    # AUTHOR, MODS, MOD REFERENCE NAME.
    path('<str:author>/mods/<slug:slug>', mods.views.check),
    path('<str:author>/mods/', mods.views.index),
    
    # AUTHOR, GAMES, GAME REFERENCE NAME.
    path('<str:author>/games/<slug:slug>', games.views.check),
    path('<str:author>/games/', games.views.index),
    
    # AUTHOR, SKINS, SKIN REFERENCE NAME.
    path('<str:author>/skins/<slug:slug>', skins.views.check),
    path('<str:author>/skins/', skins.views.index),
    
    # AUTHOR, TEXTURES, TEXTURE REFERENCE NAME.
    path('<str:author>/textures/<slug:slug>', textures.views.check),
    path('<str:author>/textures/', textures.views.index),
    
    # USER PROFILE. PLACEHOLDER UNTIL DATABASE IS SETUP.
    #path('<str:author>/', accounts.views.check),

    # NORMAL FRONT PAGE VIEW
    path('', market.views.index),
]
