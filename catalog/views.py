from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Welcome to the Catalog!")

#Creating sample index view for teh example
from .models import Book, Author, BookInstance, Genre
from django.db.models import Count


def index(request):
    # code to get word from user and replying no.of books and count of genre, a challenge given in the mdn_doc's
    #start- challenge part 5
    word = request.GET.get('word', '').lower()

    num_books_that_requested = Book.objects.filter(title__icontains=word).count()
    num_genres = Genre.objects.annotate(num_books=Count('book')).filter(book__title__icontains=word).count()
    #end


    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        #start_challenge_part-5
        'num_books_that_requested': num_books_that_requested,
        'num_genres':num_genres,
        #end

    }


    # This part is implemented with the reference of part 7 from mdn doc, here we implement the visit counts.
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
#start challenge part 6

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

    
# part -6 challange

class AuthorListView(generic.ListView):
    model = Author
    # context_object_name = 'author_list'

class AuthorDetailView(generic.DetailView):
    model=Author

    