from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import *
from cart.models import Cart
from news.models import *
from home.forms import CallbackForm, OknaForm, ContactForm, OrderForm, ReviewsPopupForm
from home.callback_send import email_callback
from blog.models import Post
from shop.models import Category, Product
from reviews.models import Reviews
from django.http import JsonResponse
from django.db.models import Q
import datetime

def callback(request):
  if request.method == "POST":
    form = CallbackForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']

      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n"

      email_callback(messages, title)

      return JsonResponse({"success": "success"})
    else:
      return JsonResponse({'status': "error", 'errors': form.errors})

  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def order_form(request):
  if request.method == "POST":
    form = OrderForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      product = form.cleaned_data['product']

      title = 'Заявка с заказом'
      messages = "Заявка с заказом:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n" + "Товар: " + str(product) + "\n"

      email_callback(messages, title)

      return JsonResponse({"success": "success"})
    else:
      return JsonResponse({'status': "error", 'errors': form.errors})

  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def contact_form(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n"

      email_callback(messages, title)

      return JsonResponse({"success": "success"})
    else:
      return JsonResponse({'status': "error", 'errors': form.errors})

  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def okna_form(request):
   if request.method == "POST":
      form = OknaForm(request.POST)
      if form.is_valid():
        name  = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        page_name = form.cleaned_data['page_name']
        title = 'Форма получения скидки'
        messages = "Форма получения скидки:" + "\n" + "Имя: " +str(name) + "\n" + "Номер телефона: " + str(phone) + "\n" + "Скидка: " + str(page_name)

        email_callback(messages, title)

        return JsonResponse({"success": "success"})
      else:
        return JsonResponse({'status': "error", 'errors': form.errors})

   return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def index(request):
  page = request.GET.get('page', 1)
  home_page = HomeTemplate.objects.first()
  settings = BaseSettings.objects.first()

  print(home_page.meta_h1)
  stock = Stock.objects.filter(status=True)
  articles = Post.objects.filter(status=True).order_by('-date_creation')[:4]
  news = News.objects.filter(status=True)[:4]
  reviews = Reviews.objects.filter(status=True)

  # Получаем из GET параметра page для пагинации
  category = Category.objects.all().exclude(slug="bez-kategorii")
#   service = Service.objects.filter(status=True)

  # Получаем текущую дату
  current_date = datetime.datetime.now()

  # Получаем номер дня недели (0 для понедельника, 1 для вторника и т.д.)
  day_of_week = current_date.weekday()

  try:
      products = Product.objects.filter(day=day_of_week)
  except:
      pass

#   paginator = Paginator(products, 8)
#   current_page = paginator.page(int(page))
#   current_slug = request.GET.get("slug")

  context = {
      "categorys": category,
#       "current_slug": current_slug,
      "home_page": home_page,
#       "products": current_page,
      "settings": settings,
      "reviews": reviews,
#       "services": service,
      "stocks": stock,
      "articles": articles,
      "news": news,
  }
  return render(request, 'pages/index.html', context)

def about(request):
  try:
    about_page = About.objects.get()
  except:
    about_page = About()


  context = {
    "about_page": about_page
  }

  return render(request, "pages/about.html", context)


def contact(request):
  try:
    contact_page = ContactTemplate.objects.get()
  except:
    contact_page = ContactTemplate()


  context = {
    "contact_page": contact_page
  }

  return render(request, "pages/contact.html", context)


def production(request):
  try:
    settings = Production.objects.get()
  except:
    settings = Production()

  context = {
    "settings": settings,
  }

  return render(request, "pages/production.html", context)

def works(request):
    try:
      work_page = GalleryCategory.objects.get()
    except:
      work_page = GalleryCategory()

    works = Gallery.objects.filter(is_active=True)
    works_list = Works.objects.filter(is_active=True)
    context = {
      "work_page": work_page,
      "works": works,
      "works_list":works_list
    }

    return render(request, "pages/works.html", context)

def delivery(request):
  try:
    delivery_page = Delivery.objects.get()
  except:
    delivery_page = Delivery()

  context = {
    "delivery_page": delivery_page,
  }
  return render(request, "pages/delivery.html", context)

def politika(request):
  return render(request, "pages/politika.html")

def cookie(request):
  return render(request, "pages/cookie.html")

def robots_txt(request):
  try:
      robots_txt = RobotsTxt.objects.first()  # Получаем первую запись, т.к. нам нужен только один robots.txt
      content = robots_txt.content if robots_txt else "User-agent: *\nDisallow: /admin/"
  except RobotsTxt.DoesNotExist:
    content = "User-agent: *\nDisallow: /admin/"

  return HttpResponse(content, content_type="text/plain")


def stock(request):
    stocks = Stock.objects.filter(status=True)

    try:
      stock = StockSettings.objects.get()
    except:
      stock = StockSettings()

    context = {
        "stocks": stocks,
        "stock": stock
    }

    return render(request, "pages/stock/stock.html", context)

def stock_detail(request, slug):
    stock = Stock.objects.get(slug=slug)

    context = {
        "stock": stock
    }

    return render(request, "pages/stock/stock_detail.html", context)

def vacancies(request):
  vacancy = Vacancy.objects.filter(status=True)

  context = {
    "vacancy": vacancy
  }
  return render(request, "pages/vacancies/vacancies.html", context)

def gallery(request):
    gallery = Gallery.objects.all()
    try:
        gallery_settings = GallerySettings.objects.get()
    except:
        gallery_settings = GallerySettings()

    context = {
        "gallery_settings": gallery_settings,
        "gallerys": gallery
    }

    return render(request, "pages/gallery.html", context)