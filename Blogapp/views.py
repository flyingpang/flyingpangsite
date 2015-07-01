#coding=utf-8
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from Blogapp.form import RegisterForm
from Blogapp.models import Article, Tag
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, YearArchiveView, FormView


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        blogs = Article.objects.all().order_by('-publish_time')

        context.update({'blogs': blogs})

        return context

# def blog_list(request):
#     blogs = Article.objects.all().order_by('-publish_time')
#     return render_to_response('index.html', {'blogs': blogs}, context_instance=RequestContext(request))


def blog_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id', '')
        try:
            blog = Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404
        return render_to_response('detail.html', {'blog': blog}, context_instance=RequestContext(request))
    else:
        raise Http404


class ClassificationView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ClassificationView, self).get_context_data(**kwargs)
        blogs = Article.objects.filter(classification=self.kwargs.get('pk', None))
        context.update({'blogs': blogs})
        return context


class AuthorView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        blogs = Article.objects.filter(author=self.kwargs.get('pk', None))
        context.update({'blogs': blogs})
        return context


class TagView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        blogs = Article.objects.filter(tags=self.kwargs.get('pk', None))
        context.update({'blogs': blogs})
        return context


class ArticleYearView(YearArchiveView):
    template_name = 'articleyearview.html'
    # context_object_name = 'list'
    queryset = Article.objects.all()
    date_field = "publish_time"
    make_object_list = True
    allow_future = True
    model = Article


class ImageView(TemplateView):
    template_name = 'image.html'


class UserRegisterView(FormView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = '/account/login'

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        return HttpResponseRedirect(self.get_success_url())

