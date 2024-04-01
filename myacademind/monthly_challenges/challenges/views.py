from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


monthly_challenges = {
    'January':'month of Janary',
    'February':'month of February',
    'March':'month of March',
    'April':'month of April',
    'May':'month of May',
    'June':'month of June',
    'July':'month of July',
    'August':'month of August',
    'September':'month of September',
    'October':'month of October',
    'November':'month of November',
    'December':None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })

def february(request):
    return HttpResponse("This is for february page!")

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month Not Found")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("monthly-challenge", args=[redirect_month]) # challenge/January
        return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month":month.capitalize()
        })
    except:
        raise Http404()


