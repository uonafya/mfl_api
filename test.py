import requests
import base64

url = "https://geoalign.datim.org/api/organisationUnits/"
cred = base64.b64encode("OliverM:Nooliverhere2050#")
headers = {
            "Authorization": "Basic " + cred,
            "Accept": "application/json"
        }
parent_id = "ZqLCPqjFIWZ"

def delete_org_unit(payload):
    r = requests.delete(
        url=url+payload['uid'],
        headers = headers ,
        json = payload
    )

    # print(r.json())


def get_children(uid):
    r = requests.get(
        url = url + uid,
        headers = headers,
        params = {
            "paging" : "false",
            "fields" : "[children]"
        }
    )

    # return r.json()

if __name__ == "__main__":
   children = get_children(parent_id)
#    print(children)


