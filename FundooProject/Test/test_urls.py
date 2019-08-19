from django.urls import reverse,resolve


class TestUrl:
    #  class for testing the url


    def test_url_register(self):
        # function for testing the register url
        path=reverse('register')
        assert resolve(path).view_name=='register'


    def test_url_login(self):
        # function for testing the login url

        path=reverse('login')
        assert resolve(path).view_name=='login'


    def test_url_loginsocial(self):
        # function for testing the login url


        path=reverse('loginsocial')
        assert resolve(path).view_name=='loginsocial'