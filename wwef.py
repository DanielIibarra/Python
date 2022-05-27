import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "Monterrey",
               "short_name" : "Monterrey",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Nuevo Leon",
               "short_name" : "N.L.",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "Mexico",
               "short_name" : "MX",
               "types" : [ "country", "political" ]
            }
         ],
         "formatted_address" : "Monterrey, Nuevo Leon, Mexico",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 25.7974005,
                  "lng" : -100.1841891
               },
               "southwest" : {
                  "lat" : 25.5001894,
                  "lng" : -100.4220032
               }
            },
            "location" : {
               "lat" : 25.6866142,
               "lng" : -100.3161126
            },
            "location_type" : "APPROXIMATE",
            "viewport" : {
               "northeast" : {
                  "lat" : 25.7974005,
                  "lng" : -100.1841891
               },
               "southwest" : {
                  "lat" : 25.5001894,
                  "lng" : -100.4220032
               }
            }
         },
         "place_id" : "ChIJ9fg3tDGVYoYRlJjIasrT06M",
         "types" : [ "locality", "political" ]
      }
   ],
   "status" : "OK"
}