from django.conf.urls import patterns, include, url
from django.contrib import admin
from Blogapp.views import blog_detail, ClassificationView, AuthorView, TagView, ArticleYearView, IndexView, ImageView, \
    UserRegisterView, HomePageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/$', blog_list),
    url(r'^$', HomePageView.as_view(), name='homepage_view'),
    url(r'^index/$', IndexView.as_view(), name='index_view'),
    url(r'^article/(?P<year>\d{4})/$', ArticleYearView.as_view(), name="articleyear_view"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/$', blog_detail),
    url(r'^author/(?P<pk>.+)/$', AuthorView.as_view(), name='author-view'),
    url(r'^type/(?P<pk>.+)/$', ClassificationView.as_view(), name='classification_view'),
    url(r'^tag/(?P<pk>.+)/$', TagView.as_view(), name='tag-view'),
    url(r'^image/$', ImageView.as_view(), name='image_view'),
    url(r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}, name='login_view'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout_view'),
    url(r'^account/register/$', UserRegisterView.as_view(), name='user_register_view'),

)
