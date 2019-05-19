from django.shortcuts import render
from datetime import date
# Create your views here.
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar

# any month and year accredted   http://127.0.0.1:8000
def index(request):
	t = date.today()
	month = date.strftime(t, '%b')
	year = t.year
	title = "MyClub Event Calendar index- %s %s" % (month, year)
	return HttpResponse("<h1>%s</h1>" % title)

# any month and year accredted   http://127.0.0.1:8000/201229/may/

def index1(request, year, month):
	title = "MyClub Event Calendar index1 without validation of month and year- %s %s" % (month, year)
	return HttpResponse("<h1>%s</h1>" % title)

# any month and year accredted   http://127.0.0.1:8000/2012/05/
#or             http://127.0.0.1:8000/2012/5/

def index2(request, year, month):
	year = int(year)
	month = int(month)
	if year < 2000 or year > 2099:
		year = date.today().year
	month_name = calendar.month_name[month]
	title = "MyClub Event Calendar index2 with validation- %s %s" % (month_name, year)
	return HttpResponse("<h1>%s</h1>" % title)

def index3(request,year,month):
	year = int(year)
	month = int(month)
	if year < 1900 or year > 2099:
		year = date.today().year
	month_name = calendar.month_name[month]
	title = "MyClub Event Calendar index3- %s %s" % (month_name, year)
	cal = HTMLCalendar().formatmonth(year, month)
	return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
