from django.shortcuts import render
from api.models import AuthorDeatils, BookDetails, PublicationDetails
from .forms import AuthorForm,PublicationForm,BookForm
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def Home(request):
    content = {}
    content['form'] = AuthorForm()
    content["Action"] = "Author"
    return render(request, "Author.html", content)

def Author(request):
    if request.method == "POST":
        AuthorName = request.POST['AuthorName'].capitalize()
        if AuthorDeatils.objects.filter(AuthorName=AuthorName).exists():
            return Home(request)

        else:

            Authors = AuthorDeatils(AuthorName = AuthorName)
            Authors.AuthorSave()
            content = {}
            content['form'] = PublicationForm()
            content["Action"] = "Publication"
            return render(request, "Author.Html", content)
    else:
        return render(request,"Author.html")


def Book(request):
    content = {}
    content['form'] = BookForm()
    content["Action"] = "Book"
    if request.method == 'POST':
        BookName = request.POST['BookName'].capitalize()
        Pub_id = request.POST['Pub_id'].capitalize()
        Author_id = request.POST["Author_id"].capitalize()
        Genre = request.POST["Genre"].capitalize()
        Launch_Year = request.POST['Launch_Year'].capitalize()
        Desc = request.POST["Desc"].capitalize()

        item_id = AuthorDeatils.objects.get(Author_id = Author_id)
        p_id = PublicationDetails.objects.get(Pub_id = Pub_id)

        if BookDetails.objects.filter(BookName = BookName).exists() and BookDetails.objects.filter(
            Author_id=item_id).exists():
            return render(request, "Author.html", content)
        else:
            book = BookDetails(BookName = BookName, Author_id = item_id,Pub_id = p_id, Genre= Genre,Launch_Year=Launch_Year, Desc = Desc)
            book.BookSave()

            return HttpResponse("BooK Details Save")

    else:
        return render(request,'Author.html', content)

def Publication(request):
    content = {}
    content['form'] = PublicationForm()
    content["Action"] = "Publication"
    if request.method == "POST":
        PubName = request.POST["PubName"].capitalize()
        if PublicationDetails.objects.filter(PubName = PubName).exists():
            return render(request,'Author.html',content)
        else:
            pub = PublicationDetails(PubName = PubName)
            pub.PublicationSave()
            content = {}
            content['form'] = BookForm()
            content["Action"] = "Book"
            return render(request, "Author.html", content)


    else:
        return render(request,'Author.html', content)

def SearchResult(request):
    if request.method == 'GET':
        Name = request.GET.get('Name').strip()
        Category = request.GET.get('Category').strip()
        if Category == 'Author':
            try:
                item_id = AuthorDeatils.objects.filter(Q(AuthorName__icontains=Name))
                namelist = []
                for i in item_id:
                    item_id = AuthorDeatils.objects.get(AuthorName=i).Author_id
                    namelist.append(item_id)


                    key = BookDetails.objects.filter(Author_id__in=namelist).select_related('Author_id').select_related('Pub_id')
            except ObjectDoesNotExist:
                return render(request, '404.html')

        elif Category == "Publication":
            try:
                publist = []
                item_id = PublicationDetails.objects.filter(Q(PubName__icontains= Name))
                for i in item_id:
                    item_id = PublicationDetails.objects.get(PubName=i).Pub_id
                    publist.append(item_id)

                key = BookDetails.objetcs.filter(Pub_id__in=publist).select_related('Author_id').select_related('Pub_id')

            except ObjectDoesNotExist:
                return render(request, '404.html')

        else:
            key = BookDetails.objects.filter(Q(BookName__icontains=Name)).select_related('Author_id').select_related('Pub_id')

        return render(request, 'SearchResult.html', {'key': key, 'Name': Name})

    else:
        return HttpResponse("No Result Found")

def Filter(request):
    return render(request, 'Filter.html')