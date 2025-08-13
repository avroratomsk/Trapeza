from django.urls import path

from home import views

urlpatterns = [
    path("o-nas/", views.about, name="about"),
    path("production/", views.production, name="production"),
    path("works/", views.works, name="works"),
    path('contacts/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('vacancies/', views.vacancies, name="vacancies"),
    path('gallery/', views.gallery, name="gallery"),
#     path('gallery-category/<slug:slug>/', views.gal_cat_detail, name="gal_cat_detail"),
    path('delivery/', views.delivery, name="delivery"),
    path('politika/', views.politika, name="politika"),
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