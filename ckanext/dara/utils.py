from functools import wraps


def memoize(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def author_name_split(name):
    """
    dara expects firstname, lastname.
    as long as we don't have an author implementation, we have to hack ;-)
    we simply assume (for now) that name is given as FirstName (Middlename)
    LastName. It's ugly...
    """

    #XXX leaving middlename out for now
    all = name.split()
    firstname = all[0]
    lastname = 'None'
    if len(all) >=2:
        lastname = all[-1]

    return dict(
            firstname = firstname,
            lastname = lastname
            )


