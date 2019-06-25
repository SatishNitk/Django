from django.shortcuts import render, redirect
import requests
from news.models import Headline,UserProfile
requests.packages.urllib3.disable_warnings()  # to disable to warnign from bs4
from bs4 import BeautifulSoup
from datetime import timezone,datetime, timedelta
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import os
import math
import shutil

def news_list(request):
	# user can only do once in 24 hour
	user_p = UserProfile.objects.filter(user=request.user).first()
	now = datetime.now(timezone.utc)
	time_diff = now - user_p.last_scrape
	time_diff_in_hour = time_diff/ timedelta(minutes=60)
	next_scrape = 24 - time_diff_in_hour
	if time_diff_in_hour <=24:
		hide_me = True
	else:
		hide_me = False

	headline = Headline.objects.all()
	content = {
	"object_list":headline,
	"hide_me" :hide_me,
	"next_scrape":math.ceil(next_scrape)
	}
	return render(request,"news/home.html", content)

def scrape(request):
	user_p = UserProfile.objects.filter(user=request.user).first()
	user_p.last_scrape =datetime.now(timezone.utc)
	user_p.save()

	session = requests.Session()
	session.headers = {"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"}
	url = "https://www.theonion.com/"
	content = session.get(url, verify= False).content

	soup = BeautifulSoup(content, "html.parser")

	columns = soup.find_all("div",{'class':'curation-module__item__wrapper'}) # return a list

	for columns in columns:
		link = columns.find('a')
		image = columns.find('img')

		url = link['href']
		title = link['title']
		image_source = (image['srcset'].split(" "))[0]

		media_root = "/home/satish/satish_education/django/just_django/dashboard/media_root"
		if not image_source.startswith(("data:image","javascript")):
			local_filename = image_source.split('/')[-1].split("?")[0]
		r = session.get(image_source, stream=True, verify=True)
		with open(local_filename,'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				f.write(chunk)
		current_image_absolute_path = os.path.abspath(local_filename)
		shutil.move(current_image_absolute_path, media_root)

		new_headline = Headline()
		new_headline.title =  title
		new_headline.url = url
		new_headline.image = local_filename
		new_headline.save()
	return redirect('/home/')

