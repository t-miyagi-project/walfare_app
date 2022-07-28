from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

app_name = "jigosho"
urlpatterns = [

    # TOP
    path('', TemplateView.as_view(template_name='base/top.html'), name='top'),
    # 事業所リスト
    path("jigosho/list", views.jigo_MstListView.as_view(), name='jigo_mst_list_view'),
    path("jigosho/new", views.jigo_MstCreateView.as_view(), name='jigo_mst_new'),

    # # 一覧
    # path("prduct/list/", views.ProductListView.as_view(), name="list"),
    # # 
    # path('prduct/new/', views.ProductCreateView.as_view(), name='new'),
    # # 
    # path('prduct/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    # # 
    # path('prduct/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),

    # # 一覧
    # path("category/list/", views.CategoryListView.as_view(), name="category_list"),
    # # 
    # path('category/new/', views.CategoryCreateView.as_view(), name='category_new'),
    # # 
    # path('category/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    # # 
    # path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]