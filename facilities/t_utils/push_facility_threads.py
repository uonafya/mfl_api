import threading, re

from random import randint

abc = 'abcdefghijklmnopqrstuvwxyz'
letters = abc+abc.upper()

ALLOWED_CHARS = '0123456789'+letters
NUMBER_OF_CODE_POINTS = len(ALLOWED_CHARS)-1
NUMBER_OF_SUB_CODE_POINTS = len(letters)-1
CODE_SIZE = 15
CODE_PATTERN = re.compile(r"[a-zA-Z]{1}[a-zA-Z0-9]{14}")


def generate_uid():
    """
        Courtesy of DHIS2 src ('https://dhis2.github.io/d2/src_uid.js.html)
    """
    random_chars = letters[randint(0, NUMBER_OF_SUB_CODE_POINTS)]

    for i in range(1, CODE_SIZE):
        random_chars += ALLOWED_CHARS[randint(0, NUMBER_OF_CODE_POINTS)]

    return random_chars


class TPushNewFacility(threading.Thread):
    def __init__(self, dhis2_api_auth, facility, facility_coordinates,
                 thread_name='TPushNewFacility_' + str(generate_uid())):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.dhis2_api_auth = dhis2_api_auth
        self.facility = facility
        self.facility_coordinates = facility_coordinates

    def run(self):
        print("Starting THREAD " + self.thread_name + '\n')

        dhis2_parent_id = self.dhis2_api_auth.get_parent_id(self.facility.ward_name)

        new_facility_payload = {
            "code": str(self.facility.code),
            "name": str(self.facility.name),
            "shortName": str(self.facility.name),
            "displayName": str(self.facility.official_name),
            "parent": {
                "id": dhis2_parent_id
            },
            "openingDate": self.facility.date_established.strftime("%Y-%m-%d"),
            "coordinates": self.dhis2_api_auth.format_coordinates(
                re.search(r'\((.*?)\)', str(self.facility_coordinates.objects.values('coordinates')
                                            .get(facility_id=self.facility.id)['coordinates'])).group(1))
        }

        print("New Facility Push Payload => ", new_facility_payload)
        self.dhis2_api_auth.push_facility_to_dhis2(new_facility_payload)

        print("Exiting THREAD " + self.thread_name + '\n')


class TAssignOrgUnitGroups(threading.Thread):
    def __init__(self, dhis2_api_auth, facility, owner, owner_type, _facility_type,
                 thread_name='TAssignOrgUnitGroups_' + str(generate_uid())):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.dhis2_api_auth = dhis2_api_auth
        self.facility = facility
        self.owner = owner
        self.owner_type = owner_type
        self._facility_type = _facility_type

    def run(self):
        print("Starting THREAD " + self.thread_name + '\n')

        try:
            facility_type = self._facility_type.objects.values("sub_division").get(
                name__exact=str(self.facility.facility_type_name))
            facility_type = str(facility_type["sub_division"])
            print("Facility Type: " + facility_type + "-")
        except self._facility_type.DoesNotExist:
            facility_type = {"sub_division": "Stand Alone"}
            facility_type = str(facility_type["sub_division"])
            print("Facility Type @ Except: " + facility_type)

        facility_type_details = str(self.facility.facility_type_name)
        if facility_type_details is None:
            facility_type_details = "Some New Type"
        print("Facility Type Details: "+facility_type_details+"-")

        facility_regulatory_body = str(self.facility.regulatory_body)
        if facility_regulatory_body is None:
            facility_regulatory_body = "Other"
        print("Facility Regulatory Body: " + facility_regulatory_body+"-")

        facility_owner = str(self.facility.owner_name)
        if facility_owner is None:
            facility_owner = "NOT IN LIST"
        print("Facility Owner: " + facility_owner+"-")

        facility_owner_type = "Other"
        try:
            facility_owner_type_id = str(self.owner.objects.values("owner_type_id").get(name__exact=facility_owner)["owner_type_id"])
            facility_owner_type = str(self.owner_type.objects.values("name").get(id=facility_owner_type_id)["name"])
        except self.owner.DoesNotExist:
            pass
        print("Facility Owner Type: " + facility_owner_type + "-")

        facility_keph_level = str(self.facility.keph_level)
        print("Facility KEPH Level: "+facility_keph_level)

        from common.models import OrgUnitGroupsMapping
        facility_type_dhis_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
            mfl_name__exact=facility_type)
        facility_type_details_dhis_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
            mfl_name__exact=facility_type_details)
        facility_regulatory_body_dhis_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
            mfl_name__exact=facility_regulatory_body)
        facility_owner_dhis_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
            mfl_name__exact=facility_owner)
        facility_owner_type_dhis_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
            mfl_name__exact=facility_owner_type)

        facility_keph_level_id = None

        if facility_keph_level is not None:
            facility_keph_level_id = OrgUnitGroupsMapping.objects.values("dhis_id").get(
                mfl_name__exact="KEPH "+facility_keph_level)

        # print(facility_type_dhis_id["dhis_id"])

        org_unit_id = self.dhis2_api_auth.get_org_unit_id(self.facility.code)

        print("Assigning Group Facility Type")
        self.dhis2_api_auth.add_org_unit_to_group(facility_type_dhis_id["dhis_id"], org_unit_id)
        print("Assigned Group Facility Type")

        print("Assigning Group Facility Type Details")
        self.dhis2_api_auth.add_org_unit_to_group(facility_type_details_dhis_id["dhis_id"], org_unit_id)
        print("Assigned Group Facility Type Details")

        print("Assigning Group Facility Regulatory Body")
        self.dhis2_api_auth.add_org_unit_to_group(facility_regulatory_body_dhis_id["dhis_id"], org_unit_id)
        print("Assigned Group Facility Regulatory Body")

        print("Assigning Group Facility Owner")
        self.dhis2_api_auth.add_org_unit_to_group(facility_owner_dhis_id["dhis_id"], org_unit_id)
        print("Assigned Group Facility Owner")

        print("Assigning Group Facility owner Type")
        self.dhis2_api_auth.add_org_unit_to_group(facility_owner_type_dhis_id["dhis_id"], org_unit_id)
        print("Assigned Group Facility owner Type")

        if facility_keph_level_id is not None:
            self.dhis2_api_auth.add_org_unit_to_group(facility_keph_level_id["dhis_id"], org_unit_id)

        print("Exiting THREAD " + self.thread_name + '\n')


class TPushFacilityUpdates(threading.Thread):
    def __init__(self, dhis2_api_auth, facility, facility_coordinates, thread_name='TPushFacilityUpdates_' + str(generate_uid())):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.dhis2_api_auth = dhis2_api_auth
        self.facility = facility
        self.facility_coordinates = facility_coordinates

    def run(self):
        print("Starting THREAD " + self.thread_name + '\n')

        dhis2_parent_id = self.dhis2_api_auth.get_parent_id(self.facility.ward_name)
        dhis2_org_unit_id = self.dhis2_api_auth.get_org_unit_id(self.facility.code)
        new_facility_updates_payload = self.dhis2_api_auth.get_org_unit(dhis2_org_unit_id)

        new_facility_updates_payload["code"] = str(self.facility.code)
        new_facility_updates_payload["name"] = str(self.facility.name)
        new_facility_updates_payload["shortName"] = str(self.facility.name)
        new_facility_updates_payload["displayName"] = str(self.facility.official_name)
        new_facility_updates_payload["parent"]["id"] = dhis2_parent_id
        new_facility_updates_payload["openingDate"] = str(self.facility.date_established.strftime("%Y-%m-%d"))
        new_facility_updates_payload["coordinates"] = self.dhis2_api_auth.format_coordinates(
            re.search(r'\((.*?)\)', str(self.facility_coordinates.objects.values('coordinates')
                                        .get(facility_id=self.facility.id)['coordinates'])).group(1))

        print("Facility Updates Push Payload => ", new_facility_updates_payload)
        self.dhis2_api_auth.push_facility_updates_to_dhis2(dhis2_org_unit_id, new_facility_updates_payload)

        print("Exiting THREAD " + self.thread_name + '\n')