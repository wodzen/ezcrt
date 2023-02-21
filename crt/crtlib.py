#crt/crtlib.py

from . import session
from .api import *
import json

class crt():
    
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
    
    def getCertificateData(self, path):

        print('Getting data from %s.' % (path))

        try:
            response = session.get(path)
        except:
            print(e)
            print('\n\nFailed to establish session...')

        try:
            data = response.content.decode('utf-8')
            data = json.loads(data)
        except Exception as e:
            print(e)
            print('\n\nResponse Code: ' + str(response.status_code))

        return data


    def search(self):
        path = BASE_URL+Type.query+self.searchTerm+OUTPUT
        data = self.getCertificateData(path)

        return data

    def advanced(self, type, match='', expired='', deduplicate='',
                    showSQL=''):
        path = BASE_URL+type+self.searchTerm+OUTPUT+match+expired+deduplicate+showSQL
        data = self.getCertificateData(path)

        return data