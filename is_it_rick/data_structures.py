from is_it_rick import errors

class RickRoll:
    '''A class storing a Rick Roll'''
    def __init__(self, url: str, verified: bool = False):
        self.url = url
        self.verified = verified
    
    def __eq__(self, other):
        '''Equals method for easy checking'''
        return self.__dict__ == other.__dict__
    
    @staticmethod
    def from_dict(data: dict):
        return RickRoll(data['url', data['verified']])