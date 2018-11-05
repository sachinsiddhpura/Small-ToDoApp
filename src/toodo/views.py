from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo,Category
from django.conf import settings

def index(request):
    todos = Todo.objects.all() 
    categories = Category.objects.all() 
    if request.method == "POST": 
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"]) 
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category 
            contact=request.POST['contact_number']
            Todoo = Todo(title=title, 
            	content=content, 
            	due_date=date, 
            	category=Category.objects.get(name=category),
            	contact_number=contact,
                )
            Todoo.save() 
            return redirect("/") 
        if "taskDelete" in request.POST: 
            checkedlist = request.POST["checkedbox"] 
            for todo_id in checkedlist:
                todo = Todo.objects.get(id=int(todo_id)) 
                todo.delete()
    return render(request, "index.html", {"todos": todos, "categories":categories})
