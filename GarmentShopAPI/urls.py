
from django.urls import path,include
from .views import UserLoginView,CategoryViewSet,CompanyViewSet,ItemViewSet,ItemCodeViewSet,TokenRefreshView,DesignViewSet,PartyViewSet,TaxViewSet
from .views import FinancialYearViewSet

urlpatterns = [
    
    # path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('token/',TokenRefreshView.as_view(),name='getacceesstoken'),
    path('companies/', CompanyViewSet.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyViewSet.as_view(), name='company-detail'),

    # Path for full category details
    path('categories/', CategoryViewSet.as_view(), name='category-list'),
    
    # Path for minimal category details
    path('categories/minimal/', CategoryViewSet.as_view(), name='category-minimal'),

    # Path for category detail by ID
    path('categories/<int:pk>/', CategoryViewSet.as_view(), name='category-detail'),

    # Item URLs
    path('items/', ItemViewSet.as_view(), name='item-list'),  # List items and create a new item
    path('items/<int:pk>/', ItemViewSet.as_view(), name='item-detail'),  # Retrieve, update, or delete an item by ID
    path('items/codes/', ItemCodeViewSet.as_view(), name='item-code-name-list'),  # New endpoint
    
    #Design URLs
    path('designs/', DesignViewSet.as_view()),  # List all designs
    path('designs/<int:pk>/', DesignViewSet.as_view()),  # Get, update, delete specific design

    #Party URLs
    path('party/', PartyViewSet.as_view()),  # For creating and listing parties
    path('party/<int:pk>/', PartyViewSet.as_view()),  # For retrieving, updating, and deleting a specific party
    
    #Tax URLs
    path('taxes/', TaxViewSet.as_view(), name='tax-list'),
    path('taxes/<int:pk>/', TaxViewSet.as_view(), name='tax-detail'),

    #Financial Year URLs
    path('financial-years/', FinancialYearViewSet.as_view()),  # List and Create
    path('financial-years/<int:pk>/', FinancialYearViewSet.as_view()),  # Retrieve, Update, Delete
    
]