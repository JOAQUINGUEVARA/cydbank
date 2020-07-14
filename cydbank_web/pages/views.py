from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page,PageImage,GrupoPage,Faq,ListaTecnica,GrupoTecnico
from .forms import PageForm
from django.shortcuts import get_object_or_404,render
from .tables import VitrinaTable

class MenuPpalView(ListView):
    model=GrupoPage
    template_name = "pages/menu_ppal.html"

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
""" class PageListView(ListView):
    model = Page

    def get(self, request, *args, **kwargs):
        pages = Page.objects.filter(grupo=kwargs['pk'])
        context = {'pages':pages}
        return render(request, 'pages/page_list.html', context) """

""" class PageDetailView(DetailView):
    model = Page
    form_class = PageForm """

class FAQTitleView(ListView):
    model = Faq

    def get(self, request, *args, **kwargs):
        faq = Faq.objects.all()
        context = {'faq':faq}
        return render(request, 'pages/faq.html', context)

class FAQDetailView(ListView):
    model = Faq

    def get(self, request, *args, **kwargs):
        faq = Faq.objects.get(id=kwargs['id'])
        context = {'faq':faq}
        return render(request, 'pages/faq_detail_list.html', context)
  

class PageDetailView(DetailView):
    
    def get(self, request, *args, **kwargs):
        pages = get_object_or_404(Page, pk=kwargs['pk'])
        #pages = Page.objects.filter(order=orden)
        limages = PageImage.objects.prefetch_related('page').filter(page_id=kwargs['pk'])
        context = {'pages':pages,'limages': limages}
        return render(request, 'pages/paginas.html', context)


@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

""" class VitrinaView(ListView):
    Model = ListaTecnica
    template_name ='pages/vitrina.html'

    def get_queryset(self, **kwargs):
        parametro = self.kwargs.get('id',None)
        queryset = ListaTecnica.objects.filter(uso=parametro)
        
    def get_context_data(self, **kwargs):
        context=super(VitrinaView, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None) 
        context['parametro'] = parametro
        return context """

class VitrinaView(ListView):

    model = ListaTecnica
    template_name ='pages/vitrina.html'
    context_object_name='injertos'
    #paginate_by = 2  # if pagination is desired

    def get_queryset(self, **kwargs):
        parametro = self.kwargs.get('id',None)
        queryset = ListaTecnica.objects.filter(uso=parametro).order_by('grupo')
        return queryset
          
    def get_context_data(self, **kwargs):
        context=super(VitrinaView, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None) 
        grupos = GrupoTecnico.objects.filter(grupo_tecnico__uso=parametro).distinct()
        context['grupos'] = grupos
        return context


def DetalleInjertoView(request,id):

    lista = ListaTecnica.objects.get(id=id)
    return render(request,'pages/injerto_detalle.html',context={'lista':lista})

""" def VitrinaView(request,id):
    table =VitrinaTable(ListaTecnica.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=3)
    return render(request,'pages/vitrina.html',context={'table':table}) """