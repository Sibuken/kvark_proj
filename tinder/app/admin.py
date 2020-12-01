from django.contrib import admin
from .models import User
from .models import Slide
from .models import Startup
from .models import InvestorsChoice


@admin.register(User, Slide, Startup)
class UserAdmin(admin.ModelAdmin):
    pass    # ??????????


admin.site.register(InvestorsChoice)




