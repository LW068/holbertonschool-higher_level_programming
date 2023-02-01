#!/usr/bin/python3
def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

  	alist = list(obj.__dict__.keys())
	alist.extend(x for x in dir(obj) if x not in alist)
	alist.sort()
	return alist 
