from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction, File
import pandas as pd
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
import time

# Create your views here.
def home(request):
    return render(request , 'index.html')
    
    
    
def upload(request):
    if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file = file)
        create_db(obj.file)
        #display_data()
    #return HttpResponse("Thanks for the response")
    return display_data(request)
    
    
    
def create_db(file_path):
    df =    pd.read_csv(file_path,delimiter=',')
    print(df.values)
    list_of_csv = [list(row) for row in df.values]
    
    for l in list_of_csv:
        Transaction.objects.create(time = l[0], v1 = l[1])
        
        
def display_data_with_checkbox(request):
    objects = Transaction.objects.all()
    processed_data =[]
    for obj in objects:
            print(obj)
            processed_data.append(obj)
    return render(request , 'checkbox_uploaded_data.html',{'processed_data': processed_data})
    
    
def display_data(request):
    objects = Transaction.objects.all()
    processed_data =[]
    for obj in objects:
            print(obj)
            processed_data.append(obj)
    time.sleep(5)
    return render(request , 'uploaded_data.html',{'processed_data': processed_data})
    
    
def show_objects(request):
    objects = Transaction.objects.all()
    context = {'objects': objects}
    return render(request, 'display_objects.html', context)
    
    
def delete_all_objects(request):
    # Delete all objects of the Transaction model
    Transaction.objects.all().delete()
    File.objects.all().delete()
    return redirect(home)
    
    
def delete_selected_objects(request):
    if request.method == 'POST':
        # Get the list of selected object ids
        object_ids = request.POST.getlist('selected_items')
        # Delete the objects with the specified ids
        Transaction.objects.filter(pk__in=object_ids).delete()
    return redirect('home')
    
    
'''class MyModelDeleteView(DeleteView):
    model = Transaction
    template_name = 'checkbox_uploaded_data.html'  '''
