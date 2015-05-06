import os

from django.conf import settings

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from .test_views import LoginMixin

from rest_framework.exceptions import ValidationError
from common.models import County
from model_mommy import mommy
from common.renderers import _write_excel_file


class TestExcelRenderer(LoginMixin, APITestCase):
    def test_get_excel_from_end_point(self):
        url = reverse('api:common:counties_list')
        excel_url = url + "?format=excel"
        mommy.make(County)
        mommy.make(County)
        response = self.client.get(excel_url)
        self.assertEquals(200, response.status_code)
        file_path = os.path.join(settings.BASE_DIR, 'download.xlsx')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)
        self.assertFalse(os.path.exists(file_path))

    def test_write_excel_file(self):
        mommy.make(County)
        mommy.make(County)
        url = reverse('api:common:counties_list')
        response = self.client.get(url)
        _write_excel_file(response.data)
        file_path = os.path.join(settings.BASE_DIR, 'download.xlsx')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)
        self.assertFalse(os.path.exists(file_path))

    def test_download_view_file_exists(self):
        mommy.make(County)
        mommy.make(County)
        url = reverse('api:common:counties_list')
        response = self.client.get(url)
        _write_excel_file(response.data)
        file_name = "download"
        file_extension = "xlsx"
        kwargs = {
            "file_name": file_name,
            "file_extension": file_extension
        }
        url = reverse("api:common:download_file", kwargs=kwargs)
        resp = self.client.get(url)
        self.assertEquals(200, resp.status_code)
        file_path = os.path.join(settings.BASE_DIR, 'download.xlsx')
        os.remove(file_path)
        self.assertFalse(os.path.exists(file_path))

    def test_download_view_file_does_not_exist(self):
        file_name = "download"
        file_extension = "xlsx"
        kwargs = {
            "file_name": file_name,
            "file_extension": file_extension
        }
        url = reverse("api:common:download_file", kwargs=kwargs)
        with self.assertRaises(ValidationError):
            self.client.get(url)
