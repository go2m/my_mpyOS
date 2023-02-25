def version():
    '''
    version von para
    '''
    return '(c) 2022 go2m.eu command <para> version 0.5.2 22/10/28'

def para(p='-v',_debug=False):
    '''
    display all parameters
    '''
    print()
 
    return_code='successful'

# Main
#_debug=True
#_debug=False
try:
    if _debug:
        _debug=True

except Exception as e:
    #print(e)
    _debug=False
if _debug:
    print('debug is on of main')
    import debug
if 'parameters' in locals():
    #print('parameters exist in locals')
    pass
else:
    print('parameters not exist in locals')
    
if 'parameters' in globals():
    #print('parameters exist in globals')
    pass
else:
    print('parameters not exist in globals')

  # myVar exists.
if 'parameters' in locals():
    pass
else:
    parameters={} #for parameters debug

    #parameters={'para1': '/ilib'}
    #parameters={'para1': '/lib'}
    #parameters={'para1': '/'}
    #parameters={'para1': '/.ilib'}

if _debug:
    print('parameter:{}'.format(parameters))
    print('anzahl der parameter:{}'.format(len(parameters)))
    for value in parameters:
        print('{}:{}'.format(value,parameters[value]))
#
if len(parameters) == 1:
    return_code=para()
else:
    para(parameters)
