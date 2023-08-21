from.import views
from django.urls import path,include

app_name='shop'
# from .views import TaskListView

urlpatterns = [
    
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    # path('category/<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
    
  
] 


   # path('delete/<int:taskid>/',views.delete,name='delete'),
    # path('update/<int:id>/',views.update,name='update'),
    # path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    # path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    # path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    # path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
