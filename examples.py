from crt.api import *
from crt.crtlib import crt

'''
Enter an Identity (Domain Name, Organization Name, etc),
a Certificate Fingerprint (SHA-1 or SHA-256) or a crt.sh ID:
'''
# basic search
print(crt('reddit').search())

'''
Params:
Search(self, type, match=None, 
        expired=None, deduplicate=None, showSQL=None)
'''
# advanced search
print(crt('reddit').advanced(Type.Identity.identity, Match.like, DEDUPLICATE))
