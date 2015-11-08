from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import json



def init():
	with open("service_account_creds.json") as creds:
		credJson = json.load(creds)

	credentials = client.SignedJwtAssertionCredentials(credJson["client_email"], credJson["private_key"], "https://www.googleapis.com/auth/drive")
	authedHttp = httplib2.Http()
	credentials.authorize(authedHttp)
	return discovery.build('drive', 'v2', http=authedHttp)
