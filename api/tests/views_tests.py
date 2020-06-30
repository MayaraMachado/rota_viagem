import pytest
import json
from django.urls import reverse

def test_view_get_best_source_view(client):
   url = reverse('best-route')
   queryparams = "?from=GRU&to=CDG"
   response = client.get(url+queryparams)
   assert response.status_code == 200

def test_view_get_best_source_with_non_valid_route(client):
   url = reverse('best-route')
   queryparams = "?from=GRU&to=CG"
   response = client.get(url+queryparams)
   assert response.status_code == 400

def test_view_get_best_source_without_query_params(client):
   url = reverse('best-route')
   response = client.get(url)
   assert response.status_code == 400

def test_view_post_new_route_invalid_value_view(client):
    url = reverse('route')
    data = {"routes":[{"origin" : "ORIGIN", "end" : "NewDestinatENDion","cost" : "invalid"}]}
    response = client.post(url, data=data)   
    assert response.status_code == 400
