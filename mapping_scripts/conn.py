import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'therealsam'
database = 'mfl'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)