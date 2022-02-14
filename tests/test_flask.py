import sys
from backend import project

flask_app = project.create_app('flask_test.cfg')

"""
Tests homepage by asserting a status code of 200 to ensure appliation is reachable and running
"""
def test_homepage():
   with flask_app.test_client() as test_client:
      response = test_client.get('/')
      assert response.status_code == 200
