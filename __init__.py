from flask import Flask, render_template, request
import requests
from utils.db_builder import create_db, add_zip_ll, add_concentration

app = Flask(__name__)

create_db()

def parsecsv():
    ny_ll_zips = []
    csv = open("utils/zip_codes_states.csv", "rb")
    for line in csv:
        line = line.split(",")
        if line[4] == '"NY"':
            ny_ll_zips.append(line)
    return ny_ll_zips

def search_zip(csv, zipcode):
    ll = []
    zipcode = '"%i"'%zipcode
    for line in csv:
        if line[0] == zipcode:
            ll.append(float(line[1]))
            ll.append(float(line[2]))
    return ll

'''
Set the concentration in database
based on zipcode

later: get rid of params
and loop thru copper concentration csv
'''
def set_con_by_zip(zipcode, concentration):
    add_concentration(zipcode, concentration)
    
    
    
def input_zip_latlong(csv):
    for line in csv:
        try:
            zipcode = line[0].replace("'", "")
            add_zip_ll(zipcode, float(line[1]), float(line[2]))
        except:
            pass



#----------------- ROUTES -------------------------
@app.route('/', methods = ['GET','POST'])
def root():
    apikey = open("utils/apikey.txt", "rb").read().strip()
    link = "https://maps.googleapis.com/maps/api/js?key="+apikey+"&callback=initMap&libraries=visualization"

    csv = parsecsv()

    '''
    run command below once after dropping db
    '''
    #input_zip_latlong(csv)

    '''
    tested set_con_by_zip -- works
    next: make set_con_by_zip loop thru concentration csv
    and set concentration
    '''
    #set_con_by_zip("14925", 123425436789867546352413)

    return render_template("home.html", googlelink=link, latlng=[])


if __name__ == '__main__':
    app.debug = True
    app.run()
