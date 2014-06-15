import urllib2                                  #import library to do http requests:
from xml.dom.minidom import parseString         #import easy to use xml parser called minidom: 
import redis                                    #import redis
import tornado.ioloop                           #import tornado web server
import tornado.web


#PRINT TO TORNADO 
class MetarHandler(tornado.web.RequestHandler):
    def initialize(self, db):           #configuration of a factory, what data it will be manipulating
        self.db = db
        
    def get(self):
        station_name = self.get_argument('station')
        metar_uri = 'data.metar.{}'.format(station_name)
        metar_report = self.db.get(metar_uri)
        if metar_report != None:
            self.write(metar_report)
        else:
            self.write('No METAR for station {}'.format(station_name))

class TafHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        station_name = self.get_argument('station')
        taf_uri = 'data.taf.{}'.format(station_name)
        taf_report = self.db.get(taf_uri)
        if taf_report != None:
            self.write(taf_report)
        else: 
            self.write('No TAF for startion {}'.format(station_name))


if __name__ == "__main__":

    database = redis.Redis(host='localhost', port=6379, db=0)       #create database object in redis
    my_dict = {'db':database}       #create database within redis 

    application = tornado.web.Application([
        (r'/metar', MetarHandler, my_dict), 
        (r'/taf', TafHandler, my_dict)   
    ])
    application.listen(8898)
    tornado.ioloop.IOLoop.instance().start()
