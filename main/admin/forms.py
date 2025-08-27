from django import forms
from home.models import *
from blog.models import *
from subdomain.models import *
from service.models import *
from news.models import *
from shop.models import *
from reviews.models import *
from .widgets import CustomImageWidget
from django_ckeditor_5.widgets import CKEditor5Widget

INPUT_CLASS = "form__controls"

class UploadFileForm(forms.Form):
    file = forms.FileField()

class GlobalSettingsForm(forms.ModelForm):
  """ Form, глобальные и общие настройки сайта(лого, телефон, email)"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  class Meta:
    model = BaseSettings
    fields = "__all__"
    
    widgets = {
        'phone_one': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'phone': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'time_work': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'email': forms.EmailInput(attrs={
            'class': INPUT_CLASS
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_title': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_description': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': INPUT_CLASS
        }),
        'description':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        )
    }
    
class RobotsForm(forms.ModelForm):
  
  class Meta:
    model = RobotsTxt
    fields = "__all__"
    
    widgets = {'content': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 30 }),}

class ShopSettingsForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  
  class Meta:
      model = ShopSettings
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_description': forms.Textarea(attrs={
              'class': 'form__controls',
              "id": "meta_description"
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
      }
      
class BlogSettingsForm(forms.ModelForm):
  class Meta:
      model = BlogSettings
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_title': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'meta_description': forms.Textarea(attrs={
              'class': INPUT_CLASS,
              "id": "meta_description"
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS
          }),
          'text':CKEditor5Widget(
              attrs={'class': 'django_ckeditor_5'},
              config_name='extends'
          )

      }

class PostForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"name",
                "required": "true"
            }),
            'slug': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                "id":"slug",
                "required": "true"
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            "meta_h1": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            "meta_h1": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            "meta_title": forms.TextInput(attrs={
              "class":"form__controls meta_field",
              "id": "meta_title"
            }),
            "meta_description": forms.Textarea(attrs={
              "class":"form__controls meta_field",
              "rows": "5"
            }),
            "meta_keywords": forms.TextInput(attrs={
              "class":INPUT_CLASS,
            }),
            'text': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'},
                config_name='extends'
            )
        }

class BlogCategoryForm(forms.ModelForm):
    """ Form, отвечает за создание категорий постов"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogCategory
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'id':'name'
            }),
            'slug': forms.TextInput(attrs={
              'class': INPUT_CLASS,
              "id": 'slug'
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_title': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),

        }



class CategoryForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = Category
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      'add_menu': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      "description": forms.Textarea(attrs={
        "class":"form__controls",
      }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),
      'description':CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      # Показывать только корневые категории
      self.fields['parent'].queryset = Category.objects.filter(parent__isnull=True).exclude(id=self.instance.id if self.instance.pk else None)

class ProductForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'short_description',
            'description',
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'image',
            'price',
            'price_two',
            'discount',
            'quantity',
            'category',
            'day',
            'branch',
            'image',
            'weight',
            'weight_two',
            'calories',
            'proteins',
            'fats',
            'carbonhydrates',
            'status',
        ]
        labels = {
            'name': 'Название блюда',
            'slug':'URL',
            'short_description':'Короткое описание',
            'description':'Полное описание',
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
            'image':'Изображение',
            'price':'Цена',
            'discount':'Скидка в (%)',
            'quantity':'Количество',
            'category':'Категория',
            'day':'В какой день готовят',
            'branch':'В каком из филлиалов',
            'image': 'Превью изображения',
            'weight':'Грамовка',
            'calories': 'Каллорийность',
            'proteins': 'Белки',
            'fats': 'Жиры',
            'carbonhydrates': 'Углеводы',
            'status': 'Статус публикации'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form__controls',
                "id":"name"
                # 'placeholder': 'Название товара',
            }),
            'branch': forms.CheckboxSelectMultiple,
            'short_description': forms.Textarea(attrs={
                'class': 'form__controls',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form__controls'
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'day': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'price_two': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form__controls',
                "id": "slug"
            }),
            'category': forms.Select(attrs={
                'class': 'form__controls',
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'weight_two': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'discount': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'image': forms.FileInput(attrs={
                'class': 'submit-file',
                'accept': 'image/*'
            }),
            'calories': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'proteins': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'fats': forms.TextInput(attrs={
                'class': "form__controls",
            }),
            'carbonhydrates': forms.TextInput(attrs={
                'class': "form__controls",
            })
        }


class HomeTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = HomeTemplate
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'untitle': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'title': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'title_why': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'left_text':CKEditor5Widget(
              attrs={'class': 'django_ckeditor_5'},
              config_name='extends'
          ),
          'right_text':CKEditor5Widget(
              attrs={'class': 'django_ckeditor_5'},
              config_name='extends'
          ),
          'callback_title': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'callback_text': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
      }

class ContactTemplateForm(forms.ModelForm):
  """ Form, редактирование страницы контакты"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
      model = ContactTemplate
      fields = "__all__"
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'meta_title': forms.TextInput(attrs={
              'class': f"{INPUT_CLASS} meta_field",
          }),
          'meta_description': forms.Textarea(attrs={
              'class': f"{INPUT_CLASS} meta_field",
              'rows': 5
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': INPUT_CLASS,
          }),
          'activate_page': forms.CheckboxInput(attrs={
            'class': 'form__controls-checkbox',
          }),
      }

class AboutTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
    model = AboutTemplate
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
      }),
      'meta_h1': forms.TextInput(attrs={
          'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
          'class': f"{INPUT_CLASS} meta_field",
      }),
      'meta_description': forms.Textarea(attrs={
          'class': f"{INPUT_CLASS} meta_field",
          'rows': 5
      }),
      'meta_keywords': forms.TextInput(attrs={
          'class': INPUT_CLASS,
      }),
      'about_text': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
     ),
  }
           
class StockPage(forms.ModelForm):
  class Meta:
    model = StockSettings
    fields = "__all__"

    widgets = {
        'text': CKEditor5Widget(
           attrs={'class': 'django_ckeditor_5'},
           config_name='extends'
        ),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        })
    }

class StockForm(forms.ModelForm):
  """ Form, добавление и редактирование акций"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Stock
    fields = "__all__"
    widgets = {
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'validity': forms.DateInput(attrs={
        'class':INPUT_CLASS,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'slider_status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description': CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      )
    }

class ServicePageForm(forms.ModelForm):
  """ Поля настроек старницы услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = ServicePage
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':INPUT_CLASS,
        "id": "slug"
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
              'class': INPUT_CLASS,
            }),
      'meta_description': forms.Textarea(attrs={
        'class': INPUT_CLASS,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': INPUT_CLASS
      })
    }  
    
class ServiceForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""

  # Переопределяем template_type, чтобы вставить "Выберите шаблон"
  template_type = forms.ChoiceField(
    choices=[('', '— Выберите шаблон —')] + Service.TEMPLATE_CHOICES,
    required=True,
    label="Выбор шаблона страницы",
    widget=forms.Select(attrs={
        'class': 'form__controls-select',
    })
  )

  class Meta:
    model = Service
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={
          'class': INPUT_CLASS,
          'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
          'class': INPUT_CLASS,
          "id": "slug"
      }),
      'description': CKEditor5Widget(
          attrs={'class': 'django_ckeditor_5'},
          config_name='extends'
      ),
      'subtitle': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      ),
      'status': forms.CheckboxInput(attrs={
          'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
          'class': INPUT_CLASS,
      }),
      'meta_title': forms.TextInput(attrs={
          'class': INPUT_CLASS,
      }),
      'meta_description': forms.Textarea(attrs={
          'class': INPUT_CLASS,
          'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
          'class': INPUT_CLASS
      }),
      'left_text': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      ),
      'right_text': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      ),
      'price': forms.TextInput(attrs={
          'class': INPUT_CLASS
      }),
      'first_text_title': forms.TextInput(attrs={
          'class': INPUT_CLASS
      }),
      'first_text_text': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      ),
      'second_text_title': forms.TextInput(attrs={
          'class': INPUT_CLASS
      }),
      'second_text_text': CKEditor5Widget(
         attrs={'class': 'django_ckeditor_5'},
         config_name='extends'
      ),
      'text_one': CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text_two': CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text_three': CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),
      'text_four': CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'},
        config_name='extends'
      ),

    }

  def clean_template_type(self):
    """Не позволяем сохранить пустой выбор"""
    value = self.cleaned_data.get('template_type')
    if not value:
        raise forms.ValidationError("Сначала выберите шаблон.")
    return value

class ServiceCategoryForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
    model = ServiceCategory
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }

class ServiceProductForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  service_type = forms.ChoiceField(
    choices=[('', '— Выберите услугу —')] + Service.TEMPLATE_CHOICES,
    required=True,
    widget=forms.Select(attrs={
        'class': 'form__controls-select',
    })
  )
  class Meta:
    model = ServiceProduct
    fields = "__all__"
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'price': forms.TextInput(attrs={
        'class':'form__controls',
      }),
      'subtitle': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      }),
      'service': forms.Select(attrs={
        'class': 'form__controls'
      }),
      'category': forms.Select(attrs={
        'class': 'form__controls'
      })
    }

    def clean_template_type(self):
      """Не позволяем сохранить пустой выбор"""
      value = self.cleaned_data.get('service_type')
      if not value:
          raise forms.ValidationError("Сначала выберите шаблон.")
      return value

class SubdomainForm(forms.ModelForm):
  class Meta:
    model = Subdomain
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'geotag': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'subdomain': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
    }

class SubdomainContactForm(forms.ModelForm):
  class Meta:
    model = SubdomainContact
    fields = "__all__"
    widgets = {
        'phone': forms.TextInput(attrs={
          'class': INPUT_CLASS
        }),
        'phone_two': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'time': forms.DateInput(attrs={
            'class': INPUT_CLASS,
        }),
        'address': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'subdomain': forms.Select(attrs={
            'class': "form__controls-select",
        }),
    }

""" Новости """
class NewsPage(forms.ModelForm):
  class Meta:
    model = NewsSettings
    fields = "__all__"

    widgets = {
        'text':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        ),
        'meta_h1': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_title': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_description': forms.Textarea(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        })
    }

class NewsForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
    model = News
    fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form__controls',
            "id":"name"
        }),
        'text':CKEditor5Widget(
            attrs={'class': 'django_ckeditor_5'},
            config_name='extends'
        ),
        'meta_h1': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_title': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_description': forms.Textarea(attrs={
            'class': INPUT_CLASS,
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': INPUT_CLASS,
        }),
        'slug': forms.TextInput(attrs={
            'class': INPUT_CLASS,
            "id": "slug"
        }),
        'image': forms.FileInput(attrs={
            'class': 'submit-file',
            'accept': 'image/*'
        })
    }


class FillialForm(forms.ModelForm):
  """ Form, отвечает за добавление филлиала и редактирование филлиала"""
  class Meta:
    model = Branch
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
      }),
      "address_fillial": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name",
          "placeholder": "г.Томск, ул.Ленина 111"
      }),
      "phone": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "time_work": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "weekend": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "number_seats": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "hall_rental": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "hall_rental_hollyday": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "scheme_payment": forms.TextInput(attrs={
          "class": "form__controls",
      }),
      "map_code": forms.Textarea(attrs={
          "class": "form__controls",
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
      })
    }


class VacancyForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
    model = Vacancy
    fields = [
      'name',
      'slug',
      'description',
      'meta_h1',
      'meta_title',
      'meta_description',
      'meta_keywords',
      'price',
      'status',
    ]
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        "id":"name"
        # 'placeholder': 'Название товара',
      }),
      'description': forms.Textarea(attrs={
        'class': 'form__controls'
      }),
      'price': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
      'slug': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
      'meta_h1': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
      'meta_title': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
      'meta_description': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
      'meta_keywords': forms.NumberInput(attrs={
         'class': 'form__controls',
      }),
    }


class VacancySettingsForm(forms.ModelForm):
  """ Form, отвечает за создание товара и редактирование товара"""
  # description = forms.CharField(label='Описание производителя', required=False, widget=CKEditorUploadingWidget)
  # description = forms.CharField(widget=TinyMCE())
  class Meta:
    model = ShopSettings
    fields = "__all__"
    widgets = {
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        "id": "meta_description"
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
    }


class ReviewsForm(forms.ModelForm):
  """ Form, добавление и редактирование отзыва"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())

  class Meta:
    model = Reviews
    fields = "__all__"

    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'date': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'text': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }

    
