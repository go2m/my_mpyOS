# version 0.4
# last update 12/15/22
def wifi(_debug=False):
    '''
    WIFI main modul
    need a enviroment file is where you keep secret settings, passwords, and tokens!
    '''
    #from secrets import secrets
    from enviroment import enviroment
    import network
    import time
    import ubinascii
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    try:
        sta_if.config(hostname=enviroment['hostname'])
        sta_if.config(dhcp_hostname=enviroment['hostname']) # set hostname
    except:
        pass
    # Access Point
    #ap_if.active(True)
    #ap_if.active(False)
    if ap_if.active():
        print('AP connected: {}'.format(ap_if.isconnected()))
        print('AP:',(ubinascii.hexlify(ap_if.config('mac'),':').decode()))
        print('Network configuration AP: ', ap_if.ifconfig())
    # client
    sta_if.active(True)
    # Client
    i=0
    while (False == sta_if.isconnected()):
        try:
            #sta_if = network.WLAN(network.STA_IF)        
            print(sta_if.isconnected())
            sta_if.connect(enviroment["ssid"],enviroment['password'])
            if _debug:
                 print('WIFI try counter: {}'.format(i))
            i=i+1
            if i == 2:
                #print('sta reset')
                #sta_if.active(False)
                print('WIFI disconnect')
                sta_if.disconnect()
                time.sleep_ms(1000)
                #sta_if.active(True)
                sta_if.connect(enviroment["ssid"],enviroment['password'])
                print('Try WIFI connect')
                time.sleep_ms(1000)
                i=0
        except:
            pass
        time.sleep_ms(500)
        
            
            
            
    print('CL:',(ubinascii.hexlify(sta_if.config('mac'),':').decode()))    
    print('Network configuration CL . . :', sta_if.ifconfig())
    try:
        print('Hostname . . . . . . . . . . : {}'.format(sta_if.config('hostname')))
        print('DHCP-Hostname  . . . . . . . : {}'.format(sta_if.config('dhcp_hostname')))
    except:
        pass
    #sta_if.active(False)

    
    #return sta_if.isconnected()
    return sta_if.ifconfig()
