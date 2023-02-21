from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Book, Author

from django.template import loader
#V1:returnam pe pagina un simplu mesaj
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

#V2: incarcam un template (o pag HTML) si returnam pagina
# def index(request):
#     template = loader.get_template('biblioteca/index.html')
#
#     return HttpResponse(template.render({}, request))

#V3: randam(render) pagina HTML
# def index(request):
#     return render(request, 'biblioteca/index.html', {})


#V4:index care trimite date catre pagina html
def index(request):
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request, 'biblioteca/index.html', context)

# def detail(request, book_id):
#     book = Book.objects.get(id = book_id)
#     return HttpResponse(f"You're looking at Book {book.title}" )


#V2 pt detail
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'biblioteca/detail.html', {'book': book})
# Create your views here.
class BookCreate(generic.CreateView):
    model = Book
    template_name = "biblioteca/form.html"
    success_url = reverse_lazy("index")
    fields = ['title', 'published_year','number_of_pages','genre', 'author','cover']

class BookUpdate(generic.UpdateView):
    model = Book
    template_name = "biblioteca/form.html"
    success_url = reverse_lazy("index")
    fields = ['title', 'published_year','number_of_pages','genre', 'author','cover']

class BookDelete(generic.DeleteView):
    model = Book
    template_name = "biblioteca/confirm_delete.html"
    success_url = reverse_lazy("index")

# class BookSearch(generic.DetailView):
#     model = Book
#     template_name = "biblioteca/detail.html"
#     def get_queryset(self):
#         # suprascriem functia care practic ruleaza sql query-ul pe DB pt a returna carti
#         # filtram dupa titlu, inlocuind cu valoarea primita in URL (pe get request)
#         # valoarea primita se incarca pe kwargs sub cheia definita in URL, in cazul nostru book_title (vezi urls.py)
#          # SELECT * FROM Book WHERE title=?
#         return Book.objects.get(title=self.kwargs['book_title'])

class BookSearch(generic.View):
    def get(self,request):
        try:
           b = Book.objects.get(title = request.GET['q'])
        except Book.DoesNotExist:
            return render(request,'biblioteca/error.html', {'book_title': request.GET['q']} )

        return render(request,'biblioteca/detail.html', {'book': b})