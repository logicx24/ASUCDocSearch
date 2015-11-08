from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import json

asucFolderId = "0B7_j_4L-LvIWd0pIaldkVFBMRDg"

def init():

	with open("service_account_creds.json") as creds:
		credJson = json.load(creds)

	credentials = client.SignedJwtAssertionCredentials(credJson["client_email"], credJson["private_key"], "https://www.googleapis.com/auth/drive")
	authedHttp = httplib2.Http()
	credentials.authorize(authedHttp)
	return discovery.build('drive', 'v2', http=authedHttp)


def printFilesInFolder(service, folder_id):
  page_token = None
  while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      children = service.children().list(
          folderId=folder_id, **param).execute()

      for child in children.get('items', []):
        print(child)
      page_token = children.get('nextPageToken')
      if not page_token:
        break
    except errors.HttpError, error:
      print ("An error occurred:")
      break
