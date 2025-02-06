def month(name):
    """This function returns number of days in a month and takes month name as a argument"""
    if name in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
        return('31 days are there in these month ')
    elif name in ['april', 'june', 'september', 'november']:
        return('30 days are there')
    else:
        return('28 days are there')

 

