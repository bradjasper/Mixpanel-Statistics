#! /usr/bin/env python
#
# Mixpanel, Inc. -- http://mixpanel.com/
#
# Python API client library to consume mixpanel.com analytics data.

import md5
import hashlib
import urllib
import time
import simplejson

class Mixpanel(object):
    
    ENDPOINT = 'http://mixpanel.com/api'
    VERSION = '1.0'
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def request(self, endpoint, method, params, format='json'):
        """
            endpoint - Parent level access point (e.g. events, properties, etc.)
            method - Child level access point (e.g. general, unique, etc.)
            params - Extra parameters associated with method
        """

        if not len(params): return False

        params['api_key'] = self.api_key
        params['expire'] = int(time.time()) + 600 # Grant this request 10 minutes.
        params['format'] = format
        params['sig'] = self.hash_args(params)
        
        request_url = self.ENDPOINT + '/' + endpoint + '/' + str(self.VERSION) + '/' + method + '?' + self.unicode_urlencode(params)
        
        request = urllib.urlopen(request_url)

        return simplejson.loads(request.read())

    def unicode_urlencode(self, params):
        if isinstance(params, dict):
            params = params.items()

        for i, k in enumerate(params):
            if isinstance(k[1], list): 
                params[i] = (k[0], simplejson.dumps(k[1]),) 
        
        return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params])    

    def hash_args(self, args, secret=None):
        """
            Hashes arguments by joining key=value pairs, appending a secret, and then taking the MD5 hex digest.
        """
        for a in args:
            if isinstance(args[a], list): args[a] = simplejson.dumps(args[a])
        
        args_joined = ''.join(['%s=%s' % (isinstance(x, unicode) and x.encode("utf-8") or x, isinstance(args[x], unicode) and 
                      args[x].encode("utf-8") or args[x]) for x in sorted(args.keys())])

        hash = hashlib.md5(args_joined)
        
        if secret:
            hash.update(secret)
        elif self.api_secret:
            hash.update(self.api_secret)
            
        return hash.hexdigest() 

if __name__ == '__main__':

    api = Mixpanel(api_key='c1bf9105ff4ef6429aa355451cbd07b5', api_secret='260bc592536df8b5442485ecb8a39cfa')
    data = api.request('events', 'general', {
        'event' : ['success_view',],
        'unit' : 'hour',
        'interval' : 24,
    })
    print data
