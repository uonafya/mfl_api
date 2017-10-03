#!/home/elon/.virtualenv/mfl_api python2.7

import requests
import base64

from conn import myConnection


def get_org_unit_ids(name, level=2):
    r = requests.get(
        "http://test.hiskenya.org/api/25/organisationUnits",
        headers={
            "Authorization": "Basic "+base64.b64encode("healthit:hEALTHIT2017"),
            "Accept": "application/json"
        },
        params={
            "filter": "name:eq:"+name,
            "fields": "[name,id,parent]",
            "paging": "false",
            "level" : level
        }
    )
    # print("Get Org Unit ID Response", r.json())
    print("Raw Response: "+str(r.json()))

    if len (r.json()['organisationUnits']) < 1:
        return False
    else:
        response = {
            "dhis_name": str(r.json()["organisationUnits"][0]["name"]),
            "dhis_id": str(r.json()["organisationUnits"][0]["id"])
        }
        return response
# HfVjCurKxh2

# correct the county names
def correct_county_names(conn):
    tharaka = "UPDATE common_countymapping SET mfl_name = 'THARAKA NITHI' WHERE mfl_name LIKE '%THARAKA%'"
    muranga = "UPDATE common_countymapping SET mfl_name = 'MURANGA' WHERE mfl_name LIKE 'MURANG%'"
    trans = "UPDATE common_countymapping SET mfl_name = 'TRANS-NZOIA' WHERE mfl_name LIKE 'TRANS%'"
    elgeyo = "UPDATE common_countymapping SET mfl_name = 'ELGEYO-MARAKWET' WHERE mfl_name LIKE 'ELEGEYO%'"
    queries = [tharaka, muranga, trans, elgeyo]

    count = 3
    for query in queries:
        cur_update = conn.cursor()
        cur_update.execute(query)
        conn.commit()
        print ("Rem : " + str (count))
        count -= 1


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

        response = get_org_unit_ids(name, 2)
        cur_update = conn.cursor()
        cur_update.execute("UPDATE common_countymapping SET "+
                                  "dhis_name = '"+str(response["dhis_name"])+"', "+
                                  "dhis_id = '"+str(response["dhis_id"])+"' "+
                                  "WHERE id = '"+str(id)+"'")
        conn.commit()
        print("Updated "+name+"\n\n_________________________\n\n")
        cur_update.close()

    cur_select.close()
    print("Done.")

'''
Correct errors occuring in the local mapping of subcounties

    *TODO
    correct the following:
    
    Mfl - Banisa, DHIS2 Banissa : Modify the banisa query as appropriate MFL_CODE 
'''

# def correct_sub_county_names (conn):
#     awendo = "DELETE FROM common_subcountymapping WHERE mfl_code = '3125'"
#     banisa = ""
#
#     cur_correct = conn.cursor()
#     cur_correct.execute (awendo)
#     print ("-----------\nDeleted redundant Awendo\n--------------")
#     conn.commit()

'''
Fetch all sub-counties from local mapping table and get their org unit IDs and DHIS2 name from DHIS2
-- Two occurences of Awendo sub county in MFL, I have ignored the one with MFL code 3125
-- Two occurences of Banisa (One Banisa and the other Banissa) sub county in MFL, I have ignored the one with MFL code 3125
'''

def update_subcounties (conn):
    """

    :param conn:
    :return:

    """

    cur_select = conn.cursor()
    cur_select.execute ("SELECT id, mfl_name, mfl_code FROM common_subcountymapping")
    ignored = []
    for id, name, code in cur_select.fetchall():

        name = str(name).lower() + " Sub County"
        name = name.title()

        print("Processing " + name + "...")
        response = get_org_unit_ids(name, 3)
        # print ("Response " + str (response))





        print ("\n\n----------------\n\n")

# correct_county_names(myConnection)
# update_counties(myConnection)
# correct_sub_county_names(myConnection)
# update_subcounties(myConnection)

r = get_org_unit_ids("banisa sub county", 3)