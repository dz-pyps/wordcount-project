from django.http import HttpResponse
from django.shortcuts import render
import operator


# def homepage(request):
#     return HttpResponse("Hello")
def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def eggs(request):
    return HttpResponse("<h1>Eggs are great</h1>")


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] = 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sorted_words})


def about(request):
    return render(request, 'about.html', {'name': 'MR.DZ'})




