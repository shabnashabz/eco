from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from matplotlib.style import available
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# def index(request):
#     return HttpResponse('heloo this is my shopping page')
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1')) 
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
        
    return render(request,"category.html",{'category':c_page,'products': products})
def  proDetail(request,c_slug,product_slug):
    try:
         product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product}) 







# from todoapp.forms import taskform
# from .models import Task
# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import UpdateView,DeleteView



# class TaskListView(ListView):
#     model=Task
#     template_name='home.html'
#     context_object_name='task1'

# class TaskDetailView(DetailView):
#     model=Task
#     template_name='detail.html'
#     context_object_name='task'

# class TaskUpdateView(UpdateView):
#     model=Task
#     template_name='update.html'
#     context_object_name='task'
#     fields=('name','priority','date')
    
#     def get_success_url(self) :
#         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
# class TaskDeleteView(DeleteView):
#     model=Task
#     template_name='delete.html'
#     success_url=reverse_lazy('cbvhome')
#     # fields=('name','priority','date')








# # Create your views here.
# def add(request):
#     task1=Task.objects.all()
#     if request.method=='POST':
#         name=request.POST.get('task','')
#         priority=request.POST.get('priority','')
#         date=request.POST.get('date','')
#         task=Task(name=name,priority=priority,date=date)
#         task.save()
#     return render(request,'home.html',{'task':task1})
# def delete(request,taskid):
#     task=Task.objects.get(id=taskid)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
    
#     return render(request,'delete.html')
# def update(request,id) :
#        task=Task.objects.get(id=id)
#        form=taskform(request.POST or None, instance=task)
#        if form.is_valid():
#            form.save()
#            return redirect('/')
#        return render(request,'edit.html',{'form':form,'task':task})
    
# # def details(request):
# #     task=Task.objects.all()
# #     return render(request,'detail.html',{'task':task})

