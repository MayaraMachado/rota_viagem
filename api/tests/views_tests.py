import pytest
import json
from django.urls import reverse

# def test_view_get_best_source_view(client):
#    url = reverse('best-route')
#    queryparams = "?from=GRU&to=CGD"
#    response = client.get(url+queryparams)
#    assert response.status_code == 200

def test_view_get_best_source_with_non_valid_route(client):
   url = reverse('best-route')
   queryparams = "?from=GRU&to=CG"
   response = client.get(url+queryparams)
   assert response.status_code == 400

def test_view_get_best_source_without_query_params(client):
   url = reverse('best-route')
   queryparams = "?from=GRU&to=CG"
   response = client.get(url+queryparams)
   assert response.status_code == 400

def test_view_post_new_route_value_view(client):
    url = reverse('route')
    data = {
		"origin" : "ORIGIN",
		"end"    : "END",
		"cost"   : 0
    }
    response = client.post(url, data=data)   
    assert response.status_code == 201

