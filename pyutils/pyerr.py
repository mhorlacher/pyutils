import sys
import re
import traceback

def exception_as_dict(e):
    edict = dict()

    try:
        exc_info = sys.exc_info()

        edict['type'] = type(e).__name__
        edict['message'] = e.message if hasattr(e, 'message') else None
        edict['errno'] = e.errno if hasattr(e, 'errno') else None
        edict['traceback'] = ''.join(traceback.format_exception(*exc_info))
    except:
        pass
    
    return edict


if __name__ == '__main__':
    """Example exceptions"""

    try:
        1 / 0
    except Exception as e:
        edict = exception_as_dict(e)
        print(edict)

    try:
        1 + "2"
    except Exception as e:
        edict = exception_as_dict(e)
        print(edict)

    try:
        dict()['key']
    except Exception as e:
        edict = exception_as_dict(e)
        print(edict)

    try:
        list()[1]
    except Exception as e:
        edict = exception_as_dict(e)
        print(edict)
        
