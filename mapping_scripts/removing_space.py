import requests
import base64


def weka(payload):
    r = requests.put(
        "http://test.hiskenya.org/api/25/organisationUnits/"+payload["id"],
        headers={
            "Authorization": "Basic " + base64.b64encode("healthit:hEALTHIT2017"),
            "Accept": "application/json"
        },
        json=payload["data"]
    )
    print(r.json())


def sahihisha(jina):
    return str(jina).strip().replace("  ", " ")


r = requests.get(
        "http://test.hiskenya.org/api/25/organisationUnits",
        headers={
            "Authorization": "Basic "+base64.b64encode("healthit:hEALTHIT2017"),
            "Accept": "application/json"
        },
        params={
            "paging": "false",
            "level" : 4,
            "fields" : '[id,name,openingDate,shortName]'
        }
    )

orgunits = r.json()['organisationUnits']

total = len(orgunits)
percentage_complete = 0
counter = 0

for orgunit in orgunits:
    counter += 1
    percentage_complete = (float(counter) / float(total)) * 100.0

    print ("\033[0mProcessing " + orgunit['name'] + " ({}% Completed)...\n".format(str(percentage_complete)))

    payload = {
        "id": orgunit["id"],
        "data": {
            "name": sahihisha(orgunit["name"]),
            "shortName": sahihisha(orgunit["shortName"]),
            "openingDate": orgunit["openingDate"]
        }
    }

    if sahihisha(orgunit["name"]) != orgunit["name"]:
        weka(payload)
        print ("\033[92mFinished Processing " + orgunit['name'] + "...\n")
    else:
        print ("\033[91mSkipped Processing " + orgunit['name'] + "...\n")



print ("\033[92mDone!\033[0m")
