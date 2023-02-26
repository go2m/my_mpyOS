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
    if _debug:
        print('debug is on')
        import debug
        debug.ptt('f_dir',f_dir)
        #debug.vl()
        #debug.vg()
    if p == '--version' or p == '-v':
        #print(version())
        return version()
    import go2m_os_hw
    root=go2m_os_hw.whatisroot()
    #_debug=True
    _debug=False
    if _debug:
        print('debug is on level: [{}]'.format(_debug))
        import debug
        if _debug == 2:
            debug.vl()
            debug.vg()
    import gc
    print('parameter:{}'.format(parameters))
    if len(parameters) == 1:
        return_code=version()
    print('anzahl der parameter:{}'.format(len(parameters)))
    for value in parameters:
        print('{}:{}'.format(value,parameters[value]))
        #pt(value)
        #pt(parameters[value])

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
