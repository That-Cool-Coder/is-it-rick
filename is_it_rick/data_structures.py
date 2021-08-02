import time

from is_it_rick import errors

class URL:
    '''A class storing a URL'''
    def __init__(self, url: str):
        self.url = url

        # Try and get the attributes to make sure the URL is valid
        try:
            self.domain_name()
            self.path()
        except:
            raise errors.InvalidUrl()
    
    def domain_name_and_path(self):
        '''Get domain name and file path of URL. EG: google.com/somevalue/'''
        domain_name_and_path = self.url.split('://', 1)[1]
        if domain_name_and_path.startswith('www.'):
            domain_name_and_path = domain_name_and_path.replace('www.', '', 1)
        return domain_name_and_path
    
    def domain_name(self):
        '''Get domain name of URL. EG: google.com'''
        return self.domain_name_and_path().split('/', 1)[0]
    
    def path(self):
        '''Get path of url. EG: pages/main/hello.js'''
        sections = self.domain_name_and_path().split('/', 1)
        if len(sections) == 1:
            return ''
        else:
            return sections[1]
    
    def is_sub_url(self, other_url):
        '''Return whether this is a sub-url of other_url.
        Similar to checking if a string is a substring.
        '''
        domain_name_matches = self.domain_name() == other_url.domain_name()
        path_matches = self.path() in other_url.path()
        return domain_name_matches and path_matches

class RickRoll:
    '''A class storing a Rick Roll'''
    def __init__(self, url: URL = None, url_str: str = None, verified=bool,
        description: str = ''):
        if url is not None:
            self.url = url
        elif url_str is not None:
            self.url = URL(url_str)
        else:
            raise errors.NoUrlProvided()
        self.verified = verified
        self.description = description
    
    def contains(self, rick_roll=None, url: URL = None, url_str: str = None):
        '''Whether rick_roll/URL leads to this RickRoll'''
        if rick_roll is not None:
            return self.url.is_sub_url(rick_roll.url)
        elif url is not None:
            return self.url.is_sub_url(url)
        elif url_str is not None:
            return self.url.is_sub_url(URL(url_str))
        else:
            raise errors.NoUrlProvided()

class User:
    '''A class storing a user of the application.
    Currently only admin users have any abilities.
    '''
    def __init__(self, name: str, password_hash: str,
        join_timestamp: int = None, is_admin: bool = False):
        self.name = name
        self.password_hash = password_hash
        if join_timestamp is None:
            join_timestamp = time.time()
        self.join_timestamp = join_timestamp
        self.is_admin = is_admin

class SessionId:
    '''A class storing a session id.

    Session ids are obtained by signing in and are then used to perform actions.

    In addition to the id itself, this class contains information on who the id
    belongs to and when it expires.
    '''
    def __init__(self, value: str, user_name: str, expiry_time: float):
        self.value = value
        self.user_name = user_name
        self.expiry_time = expiry_time
    
    def has_expired(self):
        return time.time() > self.expiry_time