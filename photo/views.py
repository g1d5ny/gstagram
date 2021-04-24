from django.shortcuts import render
from .models import Photo
from django.shortcuts import render, redirect
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

# class PhotoListView(ListView):
#     # model = Photo
#     context_object_name = 'photo_list'
#     # queryset = Photo.objects.all()
#     template_name = 'photo/list.html'
#
#     def get_queryset(self, request,*args, **kwargs):
#         queryset = Photo.objects.all()
#         return queryset


# class PhotoDetailView(DetailView):
#     template_name = "photo/detail.html"
#     model = Photo
#     context_object_name = "photo"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = OrderForm(self.request)
#         return context


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        return self.render_to_response({'form': form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
