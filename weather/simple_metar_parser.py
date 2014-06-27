import redis
import urllib2
from lxml import etree
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
metar_location = urllib2.urlopen('http://weather.aero/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&startTime=2014-06-27T01:45:55Z&endTime=2014-06-27T01:51:00Z')
#metar_location = urllib2.urlopen('http://weather.aero/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KDEN%20KSEA,PHNL&hoursBeforeNow=2')

metar_xml = metar_location.read()


root = etree.fromstring (metar_xml)

count = 0

for tags in root.iter('METAR'):
	icao_code = tags.find('icao_code').text.lower()
	raw_text = tags.find('raw_text').text
	observation_time = tags.find('observation_time').text

	station_metar = {'icao_code': icao_code, 
					 'raw_text': raw_text, 
					 'observation_time': observation_time}
	json_metar = json.dumps(station_metar)

	r.set(icao_code, json_metar)

	count += 1

print r.keys('*')


