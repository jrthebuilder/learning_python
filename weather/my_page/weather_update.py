#this script updates the weather database


import urllib2
import redis 
from lxml import etree





#update Metar data 

#get METAR from weather.aero and updates the database
download_metar = urllib2.urlopen('http://weather.aero/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KDAB&hoursBeforeNow=1')
metar_xml = download_metar.read()

#parse METAR XML 





print metar_xml
#update Taf data
'''get TAF from weather.aero and updates the database'''
#update everything eslse that they have 