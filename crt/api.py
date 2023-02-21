#crt/api.py
#crt.sh parameters

BASE_URL = 'https://crt.sh/?'
OUTPUT = '&output=json'

'''
Search Type
'''
class Type:

    query = 'q='
    
    class Identity:
        identity = 'Identity='
        commonName = 'CN='
        emailAddress = 'E='
        organizationalUnitName = 'OU='
        organizationName = 'o='
        dnsName = 'dNSName='
        rfc822Name = 'rfc822Name='
        ipAddress = 'iPAddress='

    class CA:
        ca = "CA="
        id = 'CAID='
        name = 'CAName='
        
    class Certificate:
        crtID = 'id='
        id = 'ctid='
        serial = 'serial='
        ski = 'ski='
        spkisha1 = 'spkisha1='
        spkisha256 = 'spkisha256='
        subjectsha1 = 'subjectsha1='
        sha1 = 'sha1='
        sha256 = 'sha256='

'''
Match Type
'''
class Match:
    like = '&match=LIKE'
    ilike = '&match=ILIKE'
    equals = '&match=='
    single = '&match=single'
    any = '&match=any'
    full = '&match=fts' # full text search

'''
Exclude Expired
'''
EXPIRED = '&exclude=expired'

'''
Deduplicate
'''
DEDUPLICATE = '&deduplicate=Y'

'''
showSQL
'''
SQL = '&showSQL=Y'