from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, RedirectView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from libros.models import Autor, Libro
from libros.forms import AutorForm, LibroForm

"""
def index(request):
    autores = Autor.objects.exclude(libro__isnull=True)
    context = {'autores_list': autores}
    return render(request, 'libros/index.html', context)


def autor_detail(request, autor_id):
    try:
        autor = Autor.objects.get(pk=autor_id)
    except Autor.DoesNotExist:
        raise Http404
    return render(request, 'libros/autor_detail.html', {'autor': autor})
"""

class GoogleBookInfoRedirectView(RedirectView):
    
    url = "https://www.google.com/search"
    query_string = True
    
    def get_redirect_url(self, *args, **kwargs):
        libro = get_object_or_404(Libro, pk=int(kwargs['pk']))
        self.url +=  "?q=%s" % libro.titulo
        return super(GoogleBookInfoRedirectView, self).get_redirect_url(*args, **kwargs)
        

class AutorDetailView(DetailView):
    
    model = Autor
    template_name = "libros/autor_detail.html"
    context_object_name = "autor"
    

class AutorListView(ListView):
    
    model = Autor
    template_name = "libros/index.html"
    context_object_name = "autores_list"
    
"""
class AutorFormView(FormView):
    
    template_name = 'libros/autor_form.html'
    form_class = AutorForm
    success_url = '/libros/'

    def form_valid(self, form):
        # no hace nada
        return super(AutorFormView, self).form_valid(form)

    
class LibroFormView(FormView):
    
    template_name = 'libros/libro_form.html'
    form_class = LibroForm
    success_url = '/libros/'

    def form_valid(self, form):
        # no hace nada
        return super(LibroFormView, self).form_valid(form)
"""

class AutorCreateView(CreateView):
    
    form_class = AutorForm
    template_name = 'libros/autor_form.html'
    success_url = '/libros/'
    

class AutorUpdateView(UpdateView):
    
    model = Autor
    template_name = 'libros/autor_edit.html'
    success_url = '/libros/'
    
    def form_valid(self, form):
        self.success_url = '/libros/autor/%s/' % self.get_object().id
        return super(AutorUpdateView, self).form_valid(form)
    
    
class AutorDeleteView(DeleteView):
    
    model = Autor
    success_url = '/libros/'
    
    