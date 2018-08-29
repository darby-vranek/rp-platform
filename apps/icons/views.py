from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import *


class IconCreateView(CreateView):
    model = Icon
    form_class = CreateIconForm
    template_name = 'icons/icon_create_form.html'

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('image')
        print(type(files))
        print(files)
        for f in files:
            Icon.objects.create(
                fc_model=FaceClaim.objects.get(pk=kwargs['pk']),
                tags=request.POST['tags'],
                image=f
            )
        return redirect(reverse('faceclaim-detail', kwargs={'pk': kwargs['pk']}))


class IconListView(ListView):
    model = Icon

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fcs'] = FaceClaim.objects.distinct()
        context['fc_form'] = FaceClaimForm()
        return context


class IconUpdateView(UpdateView):
    model = Icon
    form_class = IconForm
    template_name = 'icons/icon_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Icon'
        return context

    def get(self, request, *args, **kwargs):
        icon = Icon.objects.get(pk=kwargs['pk'])
        return super().get(self)


class IconDeleteView(DeleteView):
    model = Icon
    success_url = "/icons/"


class FaceClaimDetailView(DetailView):
    model = FaceClaim
    template_name = 'icons/fc_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IconForm()
        context['create_icon_form'] = CreateIconForm()
        return context


def create_faceclaim(request):
    post = request.POST
    fc = FaceClaim(name=post['name'])
    fc.save()
    return redirect(f"/icons/fc/{fc.pk}/")


def upload_icons(request, pk):
    fc = FaceClaim.objects.get(pk=pk)
    tags = request.POST['tags']
    for img in request.FILES:
        print(type(img))
    # for file in files:
    #     Icon.objects.create(
    #         fc_model=fc,
    #         image=file,
    #         tags=tags
    #     )
    return redirect(f'/icons/fc/{pk}/')