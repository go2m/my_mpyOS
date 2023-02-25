'''
**Check Size ESP(RAM) Memory**

*to do's*

#. debug - is Standard debug (Userlevel).
#. debug 1 is equivalent to True.
#. debug 2 os debug decoding.
'''
def version():
    '''
    version of mem
    '''
    return '(c) 2022 go2m.eu command <mem> version 0.3.4 22/10/28'

def mem(_debug=False):
    """
    Check ESP(RAM) Memory.
    
    :param _debug: app debug Flag, default is disabled.
    
    
    mpyOS :~>
    Input::
    
        mem
        
    Answer::
    
        `Memory
           total ............: 8004.38 KB
           usage ............: 9.44 KB (0.12%)
           free .............: 7994.86 KB (99.88%)

        (c) 2022 go2m.eu command <mem> version 0.3.3 22/10/28
        Status:successful``
    
    """
    if _debug:
        print('debug is on')
        import debug
        #debug.vl()
        #debug.vg()
    import gc
    mem_total = gc.mem_alloc()+gc.mem_free()
    free_percent = gc.mem_free()/mem_total*100.0
    alloc_percent = gc.mem_alloc()/mem_total*100.0
    print("Memory")
    print("   total ............: {:.2f} KB".format(mem_total/1024))
    print("   usage ............: {:.2f} KB ({:.2f}%)".format(gc.mem_alloc()/1024,alloc_percent))
    print("   free .............: {:.2f} KB ({:.2f}%)".format(gc.mem_free()/1024,free_percent))
    print()
    return_code='successful'
    return return_code
#
#Main


def main(parameters={'_debug':False}):    
    '''
    main program
    '''
    #print('__name__:',__name__)
    _debug=parameters['_debug']
    '''
    debug setting from the command processor
    '''
 
    return 0

# Main
if __name__ == '__main__':
    parameters={'_debug':False} 
    '''
    parameters from the secure command processor(SCCP).
    
    mpyOS :~>
    Input::
    
        <app>.
 
    :param _debug: app debug Flag, default is disabled.
    
    '''


main(parameters)
"""
#__name__='builtins'
print('__name__:',__name__)
if __name__ == '__main__':
    main()
if __name__ == 'builtins':
    print('------------------- globals ------------------->APP')
    d = dict(globals())
    '''
    debug helper variable
    '''
    print('number of variables:',len(d))
    for name in d:
        if name != 'd':
            print('{}{} : {}'.format(name,'.'*(27-len(name)),globals()[name]))
    main(parameters)
"""