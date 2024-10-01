from django.contrib import admin

# Register your models here.
from .models import Genre, Book, BookInstance, Author, Language

# admin.site.register(Book)
# admin.site.register(Author)


#Inline BookInstance  to Book model for field form to update models at a single time to improve effeciency
class BookInstanceInline(admin.TabularInline):
    model = BookInstance








admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)







#Inline Book 
class BookInline(admin.TabularInline):
    model = Book


#admin book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    def display_genre(self, obj):
        return ', '.join(genre.name for genre in obj.genre.all()[:3])
    display_genre.short_description = 'Genre'






@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
    fieldsets = (
        (None, {'fields':('book', 'imprint', 'id')}),
        ('Availability', {'fields':('status', 'due_back')}),
    )


#sart_change
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)

#end_change

