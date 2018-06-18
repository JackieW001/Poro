import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os

DIR = os.path.dirname(__file__) or '.'
DIR += '/../data/poro.db'

def create_db():
    if not os.path.isfile(DIR):
        db = sqlite3.connect(DIR) #open if f exists, otherwise create
        c = db.cursor()         #facilitates db ops

        users_table = 'CREATE TABLE copper (zipcode TEXT, lat REAL, long REAL, concentration REAL);'
        c.execute(users_table)

        print "created db"
        db.commit()
        db.close()

def add_zip_ll(zipcode, lat, lng):
    db = sqlite3.connect(DIR) #open if f exists, otherwise create
    c = db.cursor()         #facilitates db ops
    
    command = 'INSERT INTO copper VALUES (%s,%f,%f,%f)'%(zipcode, lat, lng, 0)
    
    c.execute(command)
    db.commit()
    db.close()

def add_concentration(zipcode, concentration):
    db = sqlite3.connect(DIR) #open if f exists, otherwise create
    c = db.cursor()         #facilitates db ops
    command = "UPDATE copper SET concentration = %f WHERE zipcode = %s"%(concentration, zipcode)
    print command
    db.execute(command)
    db.commit()
    db.close
    
