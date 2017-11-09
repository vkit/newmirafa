from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^book_list/$', views.BookList.as_view(), name="book_list"),
    url(r'^add_book/$', views.AddBook.as_view(), name="add_book"),
    url(r'^(?P<pk>\d+)/detail/$', views.BookDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>\d+)/comment/$', views.BookCommentView.as_view(),
        name='comment'),
    url(r'^(?P<pk>\d+)/update/$', views.BookupdateStatusView.as_view(),
        name='update'),
    url(r'^(?P<pk>\d+)/rating/$', views.BookUpdateRatingView.as_view(),
        name='rating'),
    url(r'^(?P<pk>\d+)/like/$', views.BookLikeView.as_view(),
        name='like'),
    

    
]