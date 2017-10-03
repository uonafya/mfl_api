#!/home/elon/.virtualenv/mfl_api python2.7

import requests
import base64
import psycopg2

hostname = 'localhost'
username = 'mfl'
password = 'mfl'
database = 'mfl'


def get_org_unit_ids(payload):
    r = requests.get(
        "http://test.hiskenya.org/api/25/organisationUnits",
        headers={
            "Authorization": "Basic "+base64.b64encode("healthit:hEALTHIT2017"),
            "Accept": "application/json"
        },
        params={
            "parent.id": payload["parent_id"],
            "filter": "name:eq:"+payload["name"],
            "fields": "[name, id]",
            "paging": "false"
        }
    )
    # print("Get Org Unit ID Response", r.json())
    print("Raw Response: "+str(r.json()))
    response = {
        "dhis_name": str(r.json()["organisationUnits"][0]["name"]),
        "dhis_id": str(r.json()["organisationUnits"][0]["id"])
    }
    return response
# HfVjCurKxh2


def update_counties(conn):

    """

    :param conn:
    :return:

    *TODO:
    Update mfl_name of the following:

    THARAKA-NITHI , id 414 TO THARAKA NITHI
    MURANG'A , id 422 TO MURANGA
    TRANS NZOIA , id  427 TO TRANS-NZOIA
    ELEGEYO-MARAKWET id,  429 TO ELGEYO-MARAKWET

    """

    cur_select = conn.cursor()

    cur_select.execute("SELECT id, mfl_name FROM common_countymapping")

    for id, name in cur_select.fetchall():

        name=str(name).lower()+" County"
        name = name.title()

        print("Processing "+name+"...")

        payload = {
            "name": name,
            "parent_id": "HfVjCurKxh2" # uid for Kenya
        }
        print("Payload: "+str(payload))

        response = get_org_unit_ids(payload)
        print("Response: "+str(response))

        cur_update = conn.cursor()
        cur_update.execute("UPDATE common_countymapping SET "+
                                  "dhis_name = '"+str(response["dhis_name"])+"', "+
                                  "dhis_id = '"+str(response["dhis_id"])+"' "+
                                  "WHERE id = '"+str(id)+"'")
        conn.commit()
        print("Updated "+name+"\n\n")
        cur_update.close()

    cur_select.close()
    print("Done.")


conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
update_counties(conn)