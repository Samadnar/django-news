from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import News, Category, Tags
from django.urls import reverse_lazy, reverse
from .forms import AddNewForms, ContactForm
from django.views import View   
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView , UpdateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from typing import Any
from hitcount.views import HitCountDetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User

class SearchView(ListView):
    template_name = 'search.html'
    model = News
    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(category__name__icontains=query) | Q(tags__name__icontains=query)
        )
        object_list = set(object_list)
        return object_list
    def get_context_data(self, **kwargs: Any): #-> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        
        return context
    


class AddNewView(CreateView):
    model = News
    form_class = AddNewForms
    template_name = 'add_new.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    


# class Test(View):
    
def categoryPage(request):
        category = Category.objects.all()
        tag = Tags.objects.all()
        last_news = News.objects.latest("update_at")
        context = {
            "category" : category,
            "tag" : tag,
            "last_news" :last_news
        }
        return render(request, 'index.html', context)
    
class CategoryView(View):
    def get(self, request, pk):
        new = Category.objects.get(id=pk)
        category = News.objects.filter(category=new)

        context = {
            "cat" : category,
        }
        return render(request, '123.html', context)
    
class TagView(View):
    def get(self, request, pk):
        tag = Tags.objects.get(id=pk)
        context = {
            "tag" : tag.tag_news.all()
        }
        return render(request, 'tag.html', context)


def ContactPage(request):
    contactform = ContactForm(request.POST)
    if request.POST and contactform.is_valid:
        contactform.save()
    context = {}
    return render(request, 'contact.html', context)
        
def singleview(request):
    user = get_object_or_404(User, id=request.user.id)
    news = News.objects.filter(user = user)
    context = {
        "user": news,   
    }
    return render(request, 'single-page.html', context)


class DetailViewRecom(View):
    def get(self, request, pk):
        tag_new = {"color" : []}
        new = News.objects.get(id=pk)
        category_new = News.objects.filter(category=new.category)
        for i in new.tags.all():
            a = News.objects.filter(tags=i)
            tag_new["color"].append(a)

        context = {
            "new" : new,
            "category_new" : category_new,
            "tag_new" : tag_new["color"]
        }
        return render(request, 'detail_page.html', context)

class NewsUpdate(UpdateView):
    model = News
    form_class = AddNewForms
    template_name = "new_update.html"
    
class NewsDelete(DeleteView):
    model = News
    success_url = reverse_lazy("home")