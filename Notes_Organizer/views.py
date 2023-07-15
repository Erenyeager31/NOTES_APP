from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Notes_Organizer.models import web_users,note

g_email = ""
Auth = ""
g_name = ""
# Create your views here.
def login(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"sign_up.html")

def signuphandle(request):
    print("called succesfully ")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        allusers = web_users.objects.values()
        for i in allusers:
            # print(i.get("email"))
            if email == i.get("email"):
                return HttpResponse("Email-ID alredy exists")

        myuser = web_users(name=name,email=email,password=password)
        myuser.save()
        return HttpResponse("Account created succesfully for"+" "+name+".\n"+"Please go to login page")
    
    else:
        return HttpResponse("Sorry ! could not process the data")
    
def loginhandle(request):
    # print("calling login")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        allusers = web_users.objects.values()
        for i in allusers:
            if email == i.get("email"):
                # print(i.get("password"))
                if password == i.get("password"):
                    global Auth    #This is used for accessing the global varible
                    Auth = "yes"
                    global g_email  #same purpose
                    g_email = email
                    global g_name
                    g_name = i.get("name")
                    return HttpResponse("Success")
                else:
                    
                    return HttpResponse("Invalid Password")

        return HttpResponse("Email ID does not exist")

def home(request):
    global Auth
    global g_email
    global g_name
    # print(g_email+"this mail")
    # print(Auth)
    # Auth = "No"
    # Auth = "yes"

    credentials = {
        "name":g_name,
        "email":g_email,
    }
    # users = web_users.objects.values()
    notes = note.objects.filter(email=g_email).values() #only fetching the data where the email is equal to logged user's email
    # notes = note.objects.values()

    c_user = web_users.objects.get(email = g_email)
    # print(c_user.theme_c1)
    theme = {
        "col1":c_user.theme_c1,
        "col2":c_user.theme_c2,
        "col3":c_user.theme_c3,
        "col4":c_user.theme_c4,
    }

    context={
        "notes":notes,
        "credentials":credentials,
        "theme":theme
    }
    # print(notes)
    # print(context["notes"])
    if(Auth == "yes"):
        return render(request,"home.html",{"context":context})
    else:
        return render(request,"index.html")
    
def savenotes(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        email = request.POST.get("email")
        # print(email)

        try:
            new_note = note.objects.get(title=title,email=email)    #if the note already exists then just change the content
            new_note.content = content
        except:
            new_note = note.objects.create(title=title,email=email,content=content)
        new_note.save()
        # notes = note.objects.values()
        # print(notes)
        return HttpResponse("Your Note is Saved")
    else:
        return HttpResponse("There was some error in Saving your notes")
    # return HttpResponse("hi")


def delete(request):
    if request.method == "POST":
        title = request.POST.get("title")
        note_to_del = note.objects.get(title=title)
        note_to_del.delete()
        return HttpResponse("Note deleted Succesfully")
    else:
        return HttpResponse("Please try Again later !")
    
def theme(request):
    if request.method == "POST":
        col1 = request.POST.get("col1")
        col2 = request.POST.get("col2")
        col3 = request.POST.get("col3")
        col4 = request.POST.get("col4")

        c_user = web_users.objects.get(email = g_email)
        # print(c_user.theme_c1)
        c_user.theme_c1 = col1
        c_user.theme_c2 = col2
        c_user.theme_c3 = col3
        c_user.theme_c4 = col4
        c_user.save()
        return HttpResponse("done")
    else:
        return HttpResponse("Error")
    
def logout(request):
    global Auth
    Auth = "No"
    return render(request,"index.html")

def profile(request):
    c_user = web_users.objects.get(email = g_email)

    theme = {
        "col1":c_user.theme_c1,
        "col2":c_user.theme_c2,
        "col3":c_user.theme_c3,
        "col4":c_user.theme_c4,
    }
    return  render(request,"profile.html",{"theme":theme})