from is_it_rick import errors

class URL:
    '''A class storing a URL'''
    def __init__(self, url: str):
        self.url = url
    
    def domain_name_and_path(self):
        '''Get domain name and file path of URL. EG: google.com/somevalue/'''
        return self.url.split('://', 1)[1]
    
    def domain_name(self):
        '''Get domain name of URL. EG: google.com'''
        return self.domain_name_and_path().split('/', 1)[0]
    
    def is_sub_url(self, other_url):
        '''Return whether this is a sub-url of other_url'''
        print(self.domain_name_and_path(), other_url.domain_name_and_path())
        return self.domain_name_and_path() in other_url.domain_name_and_path()

class RickRoll:
    '''A class storing a Rick Roll'''
    def __init__(self, url: URL = None, verified=bool, url_str: str = None):
        if url is not None:
            self.url = url
        elif url_str is not None:
            self.url = URL(url_str)
        else:
            raise errors.NoUrlProvided()
        self.verified = verified
    
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