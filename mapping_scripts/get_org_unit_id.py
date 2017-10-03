#!/home/elon/.virtualenv/mfl_api python2.7

import requests
import base64


def get_org_unit_ids(dict_params):
    r = requests.get(
        "http://test.hiskenya.org/api/25/organisationUnits",
        headers={
            "Authorization": "Basic "+base64.b64encode("healthit:hEALTHIT2017"),
            "Accept": "application/json"
        },
        params={
            "filter": "name:ilike:kileleshwa",
            "fields": "[id]",
            "filter": "parent:ilike:dagoretti north sub county",
            "paging": "false"
        }
    )
    # print("Get Org Unit ID Response", r.json())
    return r.json()


response = get_org_unit_ids("Hello")
print("RESPONSE:", response)