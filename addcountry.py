import os
import django
import time
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country, City

url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data = raw_data[1]

country_id = list(data['countries']['id'])
country_name = list(data['countries']['name'])
coutries = zip(country_id,country_name)

for country in coutries :
	temp = Country(name=country[1], country_id=country[0])
	temp.save()

# countries = Country.objects.all()
# print(countries)
# print("Done!")