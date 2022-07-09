from django.contrib import admin

# Register your models here.

from .models import Recipe, RecipeIngredient


# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['user', 'name']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(RecipeIngredient)
admin.site.register(Recipe, RecipeAdmin)
