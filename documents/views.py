from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

@login_required(login_url="login")
def documents(request):
    context = {}
    documents = Document.objects.filter(owner__user_id=request.user)

    # page = 1
    # results = 6
    # paginator = Paginator(documents, results)

    # documents = paginator.page(page)

    context['documents'] = documents
    return render(request, 'documents/documents.html', context )

def document(request, pk):
    documentObj = Document.objects.get(id=pk)
    return render(request, 'documents/single-document.html', {'document': documentObj})

@login_required(login_url="login")
def createDocument(request):
    form = DocumentForm()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        
        if form.is_valid():
            example = form.save(commit=False)
            example.owner = Profile.objects.get(user=request.user)
            example.save()
            return redirect('documents')
        
    context = {'form': form}
    return render(request, 'documents/document_form.html', context)

@login_required(login_url="login")
def updateDocument(request, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('documents')

    context = {'form': form}
    return render(request, 'documents/document_form.html', context)

@login_required(login_url="login")
def deleteDocument(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('documents')
    context = {'object':document}
    return render(request, 'documents/delete_template.html', context)

# LEAVE SECTION
@login_required(login_url="login")
def leave(request):  
    context = {}
    leaves = Leave.objects.filter(student__user_id=request.user)
    context['leaves'] = leaves
    return render(request, 'documents/leave.html', context)

@login_required(login_url="login")
def applyLeave(request):
    form = LeaveForm()

    if request.method == 'POST':
        
        form = LeaveForm(request.POST)
        email = request.POST.get('email')
        mess = 'One of your student have made a leave request. Please go and check the leave request.'
        from_email = settings.EMAIL_HOST_USER
        
        if form.is_valid():
            
            send_mail(
                "Student Leave Request",
                mess, 
                from_email, 
                ['12190024.gcit@rub.edu.bt', 'sonam12190024@gmail.com'],
                fail_silently=False,
            )
            
            message = form.save(commit=False)
            message.student = Profile.objects.get(user=request.user)
            message.save()

            messages.success(request, 'Leave applied successfully! ')
            return redirect('leave')

        else:
            print("Not valid!")
            print(form.errors)

    context = {'form': form}
    return render(request, 'documents/applyleave.html', context)

@login_required(login_url="login")
def editLeave(request, pk):
    leaves = Leave.objects.get(id=pk)
    form = LeaveForm(instance=leaves)

    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leaves)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave updated successfully! ')
            return redirect('leave')
        else:
            print()

    context = {'form': form}
    return render(request, 'documents/applyleave.html', context)

@login_required(login_url="login")
def deleteLeave(request, pk):
    leaves = Leave.objects.get(id=pk)
    if request.method == 'POST':
        leaves.delete()
        messages.success(request, 'Leave deleted successfully! ')
        return redirect('leave')
    context = {'object':leaves}
    return render(request, 'documents/delete_leave.html', context)


