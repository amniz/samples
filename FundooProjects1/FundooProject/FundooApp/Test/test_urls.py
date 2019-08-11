from django.urls import reverse,resolve


class UrlTest:


    def test_url_register(self):
        path=reverse('register')
        assert resolve(path).view_name=='register'