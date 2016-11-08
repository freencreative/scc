from django.shortcuts import render
from apitest.forms import NameForm
from django.http import HttpResponse,HttpResponseRedirect

import sys
import requests
import requests.packages.urllib3
import json
import base64
import urllib
from Crypto.Hash import SHA, HMAC

API_SERVER = "p2.sccservice.com:4000"

def get_instance(request):
	form = NameForm()
	return render(request, 'apitest/get_instance.html', {'form':form})

def return_instance(request):
	form = NameForm(request.POST)
	if form.is_valid():
		new_apikey = form.cleaned_data['apikey']
		new_secretkey = form.cleaned_data['secretkey']
		#apikey = request.POST['apikey']
		#secretkey = request.POST['secretkey']
	else:
		message = 'you input wrong / empty data'
		return HttpResponse(message)
	return render(request, 'apitest/return_instance.html', {'apikey':new_apikey, 'secretkey':new_secretkey})

def sccapi_get(request):
        dict_param = {"userApiUrl": "/api/cl/vm"}
        API_APIKEY = request.POST['apikey']
        API_SECRETKEY = request.POST['secretkey']
        method = "GET"
        dict_param.update({
                "userApiKey": API_APIKEY,
        })
        if method in ["PUT", "DELETE"]:
                method = "POST"
                dict_param["_method"] = method
        dict_param["userApiSignature"] = create_signature(dict_param, str(API_SECRETKEY))
        url = "http://%s/userapi" % API_SERVER
        res_data = req(url, dict_param)
#        return HttpResponse(json.dumps(res_data, indent=4))
	return render(request, 'apitest/return_instance.html', {'apikey':API_APIKEY, 'secretkey':API_SECRETKEY, 'res_data':res_data})


def create_signature(dict_param, secret_key):
        list_param = []
        for k in sorted(dict_param):
                list_param.append("%s=%s" % (k, urllib.quote(dict_param[k], safe="")))
        params = "&".join(list_param)
        params_to_sign = params.encode('utf-8').lower()
        hmac = HMAC.new(secret_key, params_to_sign, SHA)
        return base64.b64encode(hmac.digest())
 
def req(url, dict_param):
        res_data = {"code": 900, "data": "unknown"}
        try:
                requests.packages.urllib3.disable_warnings()
                r = requests.request("GET",
                        url,
                        headers={
                                "Accept": "application/json",
                        },
                        params=dict_param,
                        verify=False
                )
                res_data["code"] = r.status_code
                res_data["data"] = r.json()
                res_data["url"] = r.url
        except Exception as e:
                res_data["code"] = 400
                res_data["data"] = repr(e)
        return res_data

 
