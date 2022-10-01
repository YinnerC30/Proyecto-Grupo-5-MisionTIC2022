
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Books, Categorias
from .forms import AddBookform
from django.http import HttpResponseRedirect


class IndexView(ListView):
    model = Books
    template_name = 'index.html'
    ordering = ['-fecha']

    def get_context_data(self, *args, **kwargs):

        categories_menu = Categorias.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu

        return context


class BookdetailsView(DetailView):
    model = Books
    template_name = 'book_details.html'


class Add_BookView(CreateView):
    form_class = AddBookform

    model = Books
    template_name = 'add_book.html'

    def form_valid(self, form):
        form.instance.usuario_id = self.request.user.pk
        return super().form_valid(form)


class Update_bookView(UpdateView):
    form_class = AddBookform
    model = Books
    template_name = 'update_book.html'


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'delete_book.html'
    success_url = reverse_lazy('index')


def CategoryView(request, cat):
    categories_menu = Categorias.objects.all()

    category_books = Books.objects.filter(categoria=cat.replace('-', " "))
    return render(request, 'categories.html', {'cat': cat,
                                               'category_books': category_books,
                                               'categories_aside': categories_menu})


def Likeview(request, pk):
    book = get_object_or_404(Books, id=request.POST.get('book_id'))
    book.likes.add(request.user)

    return HttpResponseRedirect(reverse('book_details', args=[str(pk)]))