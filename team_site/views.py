from django.shortcuts import render
from .models import Team

# teams = [
#     {'name': 'Atlanta United FC',
#      'city': 'Atlanta, Georgia',
#      'stadium': 'Mercedes-Benz Stadium',
#      'capacity': 42500,
#      'joined': 2017,
#      'conference': 'Eastern'},
#     {'name': 'Chicago Fire',
#      'city': 'Bridgeview, Illinois',
#      'stadium': 'SeatGeek Stadium',
#      'capacity': 20000,
#      'joined': 1998},
#     {'name': 'FC Cincinnati',
#      'city': 'Cincinatti, Ohio',
#      'stadium': 'Nippert Stadium',
#      'capacity': 32250,
#      'joined': 2019,
#      'conference': 'Eastern'},
#     {'name': 'Columbus Crew SC',
#      'city': 'Columbus, Ohio',
#      'stadium': 'Mapfre Stadium',
#      'capacity': 19968,
#      'joined': 1996,
#      'conference': 'Eastern'},
#     {'name': 'DC United',
#      'city': 'Washington, DC',
#      'stadium': 'Audi Field',
#      'capacity': 20000,
#      'joined': 1996,
#      'conference': 'Eastern'},
#     {'name': 'Montreal Impact',
#      'city': 'Montreal, Quebec',
#      'stadium': 'Saputo Stadium',
#      'capacity': 20801,
#      'joined': 2012,
#      'conference': 'Eastern'},
#     {'name': 'New England Revolution',
#      'city': 'Foxborough, Massachusets',
#      'stadium': 'Gilette Stadium',
#      'capacity': 20000,
#      'joined': 1996,
#      'conference': 'Eastern'},
#     {'name': 'New York City FC',
#      'city': 'New York City, New York',
#      'stadium': 'Yankee Stadium',
#      'capacity': 30321,
#      'joined': 2015,
#      'conference': 'Eastern'},
#     {'name': 'New York Red Bulls',
#      'city': 'Harrison, New Jersey',
#      'stadium': 'Red Bull Arena',
#      'capacity': 25000,
#      'joined': 1996,
#      'conference': 'Eastern'},
#     {'name': 'Orlando City SC',
#      'city': 'Orlando, FL',
#      'stadium': 'Exploria Stadium',
#      'capacity': 25500,
#      'joined': 2015,
#      'conference': 'Eastern'},
#     {'name': 'Philadelphia Union',
#      'city': 'Chester, Pennsylvania',
#      'stadium': 'Talen Energy Stadium',
#      'capacity': 18500,
#      'joined': 2010,
#      'conference': 'Eastern'},
#     {'name': 'Toronto FC',
#      'city': 'Toronto, Ontario',
#      'stadium': 'BMO Field',
#      'capacity': 30991,
#      'joined': 2007,
#      'conference': 'Eastern'},
#     {'name': 'Colorado Rapids',
#      'city': 'Commerce City, CO',
#      'stadium': 'Dicks Sporting Goods Park',
#      'capacity': 18061,
#      'joined': 1996,
#      'conference': 'Western'},
#     {'name': 'FC Dallas',
#      'city': 'Frisco, Texas',
#      'stadium': 'Toyota Stadium',
#      'capacity': 20500,
#      'joined': 1996,
#      'conference': 'Western'},
#     {'name': 'Houston Dynamo',
#      'city': 'Houston, Texas',
#      'stadium': 'BBVA Stadium',
#      'capacity': 22039,
#      'joined': 2006,
#      'conference': 'Western'},
#     {'name': 'LA Galaxy',
#      'city': 'Carson, California',
#      'stadium': 'Dignity Health Sports Park',
#      'capacity': 27000,
#      'joined': 1996,
#      'conference': 'Western'},
#     {'name': 'Los Angeles FC',
#      'city': 'Los Angeles, California',
#      'stadium': 'Banc of California Stadium',
#      'capacity': 22000,
#      'joined': 2018,
#      'conference': 'Western'},
#     {'name': 'Minnesota United FC',
#      'city': 'Saint Paul, Minnesota',
#      'stadium': 'Allianz Field',
#      'capacity': 19400,
#      'joined': 2017,
#      'conference': 'Western'},
#     {'name': 'Portland Timbers',
#      'city': 'Portland, Oregon',
#      'stadium': 'Providence Park',
#      'capacity': 25218,
#      'joined': 2011,
#      'conference': 'Western'},
#     {'name': 'Real Salt Lake',
#      'city': 'Sandy, Utah',
#      'stadium': 'Rio Tinto Stadium',
#      'capacity': 20213,
#      'joined': 2005,
#      'conference': 'Western'},
#     {'name': 'San Jose Earthquakes',
#      'city': 'San Jose, California',
#      'stadium': 'Avaya Stadium',
#      'capacity': 18000,
#      'joined': 1996,
#      'conference': 'Western'},
#     {'name': 'Seattle Sounders FC',
#      'city': 'Seattle, Washington',
#      'stadium': 'CenturyLink Field',
#      'capacity': 39419,
#      'joined': 2009,
#      'conference': 'Western'},
#     {'name': 'Sporting Kansas City',
#      'city': 'Kansas City, Kansas',
#      'stadium': 'Childrens Mercy Park',
#      'capacity': 18467,
#      'joined': 2011,
#      'conference': 'Westen'},
#     {'name': 'Vancouver Whitecaps FC',
#      'city': 'Vancouver, British Columbia',
#      'stadium': 'BC Place',
#      'capacity': 22120,
#      'joined': 2011,
#      'conference': 'Westen'},
#     {'name': 'Austin FC',
#      'city': 'Austin, Texas',
#      'stadium': 'Austin FC Stadium',
#      'capacity': 20500,
#      'joined': 2021,
#      'conference': 'Future'},
#     {'name': 'Inter Miami CF',
#      'city': 'Fort Lauderdale, Florida',
#      'stadium': 'New Fort Lauderdale Stadium',
#      'capacity': 18000,
#      'joined': 2020,
#      'conference': 'Future'},
#     {'name': 'Nashville SC',
#      'city': 'Nashville, Tennessee',
#      'stadium': 'Nissan Stadium',
#      'capacity': 69143,
#      'joined': 2020,
#      'conference': 'Future'}
# ]


def home(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/home.html', context)


def about(request):
    return render(request, 'team_site/about.html', {'title': 'About'})


def original(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/original.html', context)


def western(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/western.html', context)


def eastern(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/eastern.html', context)


def future(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/future.html', context)


def big(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/big.html', context)


def new(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team_site/new.html', context)
