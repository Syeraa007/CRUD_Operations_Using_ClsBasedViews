from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from App.models import *

class TopicList(ListView):
    model=Topic
    # template_name='App/topic_list.html'
    # templates will be directly rendered by ListView implicitly
    context_object_name='ATO'
    # queryset=Topic.objects.all()
    ordering=['id']

class WebpageList(ListView):
    model=Webpage
    # template_name='App/webpage_list.html'
    # templates will be directly rendered by ListView implicitly
    context_object_name='AWO'
    # queryset=Webpage.objects.all()
    ordering=['id']

class TopicDetail(DetailView):
    model=Topic
    context_object_name='DOSTI'
    # template_name='App/topic_detail.html'

class WebpageDetail(DetailView):
    model=Webpage
    context_object_name='DOSWI'
    # template_name='App/webpage_detail.html'

class TopicCreate(CreateView):
    model=Topic
    fields='__all__'

class WebpageCreate(CreateView):
    model=Webpage
    fields='__all__' 

class TopicUpdate(UpdateView):
    model=Topic
    fields='__all__'

class WebpageUpdate(UpdateView):
    model=Webpage
    fields='__all__'

class TopicDelete(DeleteView):
    model = Topic
    context_object_name='DOSTI'
    # success_url=reverse_lazy('SchoolList')

class WebpageDelete(DeleteView):
    model = Webpage
    context_object_name='DOSWI'
    # success_url=reverse_lazy('StudentList')
