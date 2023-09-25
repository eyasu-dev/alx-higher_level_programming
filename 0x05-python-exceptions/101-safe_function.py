#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret_fn = fct(*args)
        return ret_fn
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
