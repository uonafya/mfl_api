from rest_framework import serializers
from common.serializers import AbstractFieldsMixin

from .models import AdminOffice, AdminOfficeContact


class AdminOfficeContactSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):
    contact_type_name = serializers.ReadOnlyField(
        source='contact_type.name')

    class Meta:
        model = AdminOfficeContact


class AdminOfficeSerializer(
        AbstractFieldsMixin, serializers.ModelSerializer):

    county_name = serializers.ReadOnlyField(source='county.name')
    job_title_name = serializers.ReadOnlyField(source='job_title.name')
    sub_county_name = serializers.ReadOnlyField(source='sub_county.name')
    contacts = AdminOfficeContactSerializer(many=True, required=False)

    def update_or_create_contacts(self, instance, contacts):
        for contact in contacts:
            contact['admin_office'] = instance
            if 'id' in contact:

                contact_obj = AdminOfficeContactSerializer(data=contact)
                contact_obj.update()
            else:
                AdminOfficeContact.objects.create(**contact)

    def create(self, validated_data):
        contacts = self.initial_data.pop('contacts', [])
        instance = super(AdminOfficeSerializer, self).create(validated_data)
        self.update_or_create_contacts(instance, contacts)
        return instance

    def update(self, instance, validated_data):
        contacts = self.initial_data.pop('contacts', [])
        self.update_or_create_contacts(instance, contacts)
        return super(AdminOfficeSerializer, self).update(
            instance, validated_data)

    class Meta:
        model = AdminOffice
        fields = [
            "id", "first_name", "last_name", "county_name","county","sub_county",
            "sub_county_name", "sub_county_name","sub_county","job_title",
            "job_title_name","phone_number","email","is_national","contacts"
        ]
