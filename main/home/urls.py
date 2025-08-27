from django.urls import path

from home import views

urlpatterns = [
    path("o-nas/", views.about, name="about"),
    path('contacts/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('vacancies/', views.vacancies, name="vacancies"),
    path('gallery/', views.gallery, name="gallery"),
    path('privacy/', views.policy, name="privacy"),
    path('cookie/', views.cookie, name="cookie"),
    path('callback/', views.callback, name="callback"),
    path('writetous/', views.writetous, name="writetous"),
    path('contacform/', views.contacform, name="contacform"),
    path('consultation/', views.consultation, name="consultation"),
    path('reviewsform/', views.reviewsform, name="reviewsform"),
    path('robots.txt', views.robots_txt),
    # path('uslugi/', views.about, name="about"),
    # path('valancy/', views.about, name="about"),
    
    path('', views.index, name="home"),
]