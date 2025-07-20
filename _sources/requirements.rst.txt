requirements
============

support Hardware


# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it

.. code-block:: Python

    secrets = {
        'hostname' : 'LOLIN S3 with ESP32S3',
        'ssid' : 'mySSID',
        'password' : 'myWIFI_Password',
        'aio_username' : 'my_adafruit_io_username',
        'aio_key' : 'my_adafruit_io_key',
        'timezone' : "Europe/Berlin", # http://worldtimeapi.org/timezone,
        'utc_diff' : 2,
        'ntp_server' : 'de.pool.ntp.org',
        'ap_ssid' : 'my_AP_SSID',
        'auth' : 'None',
        'channel' : 1
        }


.. code-block:: bash

    >>> import webrepl_setup
    WebREPL daemon auto-start status: enabled

    Would you like to (E)nable or (D)isable it running on boot?
    (Empty line to quit)
    > e
    Would you like to change WebREPL password? (y/n) y
    New password (4-9 chars): micro
    Confirm password: micro
    No further action required

.. code-block:: bash

    import mip
    mip.install("github:go2m/s_ilib/micropython/mpyOS/")
    or 
    mip.install("github:go2m/s_ilib/micropython/mpyOS/",target="/")
    for Raspberry PICO W
    mip.install("github:go2m/s_ilib/micropython/mpyOS/",target=".")



mip.install("github:go2m/s_ilib/micropython/mpyOS/")
mip.install("github:go2m/s_ilib/micropython/mpyOS/",target="/temp")
mip.install("github:go2m/s_ilib/micropython/mpyOS/main.py",target="/temp")

.. code-block:: json

    {
    "urls": [
        ["webrepl_cfg.py", "github:go2m/s_ilib/micropython/mpyOS/webrepl_cfg.py"],
        ["boot.py", "github:go2m/s_ilib/micropython/mpyOS/boot.py"],
        ["main.py", "github:go2m/s_ilib/micropython/mpyOS/main.py"],
        ["lib/debug.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/debug.mpy"],
        ["lib/go2m_aes_decrypt_all.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/go2m_aes_decrypt_all.mpy"],
        ["lib/go2m_mpyaes.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/go2m_mpyaes.mpy"],
        ["lib/go2m_os_hw.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/go2m_os_hw.mpy"],
        ["lib/md5.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/md5.mpy"],
        ["lib/microWebCli.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/microWebCli.mpy"],
        ["lib/sccp.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/sccp.mpy"],
        ["lib/urequests.mpy", "github:go2m/s_ilib/micropython/mpyOS/lib/urequests.mpy"],
        [".ilib/l.pya", "github:go2m/s_ilib/micropython/mpyOS/_ilib/l.pya"]
    ],
    "version": "0.12"
    }

if you want to use webrepl, run 

.. code-block:: bash

    import webrepl_setup

.. code-block:: bash

        MPY: soft reboot
        WebREPL server started on http://10.0.1.89:8266/
        Started webrepl in normal mode
        CL: f4:12:fa:cb:21:f0
        Network configuration CL: ('10.0.1.89', '255.255.255.0', '10.0.1.1', '10.0.1.1')
        [Errno 2] ENOENT
        root is empty
        main finsh
        MicroPython v1.19.1-602-g515088ffd3 on 2022-10-13; LOLIN S3 with ESP32S3
        Type "help()" for more information.