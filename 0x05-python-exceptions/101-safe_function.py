#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {:s}".format(str(ex)), file=sys.stderr)
        return None
