import sys
import urllib2
import json

reload(sys)
sys.setdefaultencoding("utf-8")

def _wunderground(request):
	f = urllib2.urlopen(request)
	json_string = f.read()
	parsed_json = json.loads(json_string) 
	city_date_data = {}
	weather_traits = ["fog", "rain", "snow", "snowfallm", "hail", "thunder", "meantempm", "meanwindspdm", "precipm"]
	for trait in weather_traits:
		city_date_data[trait] = parsed_json["history"]["dailysummary"][0][trait]
	return city_date_data

def _getCityData():
	city_date_data = {}
	cities = ["San_Francisco", "Seattle", "New_York"]
	for city in cities:
		city_date_data[city] = {}
	april = "200604"
	dates = []
	for i in range(1,30):
		if(i <= 9):
			dates.append(april + "0" + str(i))
		else:
			dates.append(april + str(i))
	#for
	print dates
	request = ""
	for city in cities:
		for date in dates:
			request = "http://api.wunderground.com/api/c4829adbdcc45e26/history_" + date + "/q/CA/" + city + ".json"
			city_date_data[city][date] = _wunderground(request)
	print city_date_data

_getCityData()
