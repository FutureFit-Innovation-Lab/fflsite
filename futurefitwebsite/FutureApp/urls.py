from django.urls import path
from . import views
from .views import contact_view, apply_program

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view), 
    path('about/', views.about_us_view, name='about_us'),
    path('services/', views.our_service_view, name='our_service'),
    path('programs/', views.programs_view, name='programs'),
    path('study-abroad/', views.study_abroad_view, name='study_abroad'),
   
    path('energy-solution/', views.energy_solution_view, name='energy_solution_view'),
    
    path('store/', views.store_view, name='store'),
    path('news/', views.news_update_view, name='news_update'), 
    path('news/<slug:slug>/', views.news_detail_view, name='news_detail'), 
    path('contact/', contact_view.as_view(), name='contact'),
    path('subscribe/', views.newsletter_subscribe_view, name='newsletter_subscribe'), 
    path('store/<slug:slug>/', views.store_detail, name='store_detail'),
    path('store/id/<int:pk>/', views.store_detail, name='store_detail_by_id'), 
    path('ai/', views.ai_page, name='ai'),
    path('emb/', views.emb, name='emb'),
    path('three_d/', views.three_d, name='three_d'),
    path('python/', views.python_page, name='python'),
    path('apply/', apply_program, name='apply_program'),
]