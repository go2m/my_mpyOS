supported Hardware
==================

The first step is to install the current version of MicroPython on the chip.


Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/ttyUSB0 erase_flash

And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin

Notes:

* You might need to change the "port" setting to something else relevant for your
  PC
* You may need to reduce the baudrate if you get errors when flashing
  (eg down to 115200 by adding ``--baud 115200`` into the command)
* For some boards with a particular FlashROM configuration you may need to
  change the flash mode (eg by adding ``-fm dio`` into the command)
* The filename of the firmware should match the file that you have

If the above commands run without error then MicroPython should be installed on
your board!

ESP32
-----

Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/ttyUSB0 erase_flash

And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
    
D1 Mini ESP32 WiFi with Display
-------------------------------
.. image:: /ESP32/tft_2.4_v1.0.0_1_16x16.jpg
   :scale: 15%
   
more Information over Hardware `MH-ET-LIVE`_.

.. _MH-ET-LIVE: https://forum.mhetlive.com/topic/8/mh-et-live-minikit-for-esp32
   
.. image:: /ESP32/D1_mini_ESP32_pinout.webp
   :scale: 60%

more Information over Hardware `TFT 2.4 Touch Shields`_.

.. _TFT 2.4 Touch Shields: https://www.wemos.cc/en/latest/d1_mini_shield/tft_2_4.html


Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash 

Firmware from  `GENERIC-ili9342`_.

.. _GENERIC-ili9342: https://github.com/russhughes/ili9342c_mpy/tree/main/firmware/GENERIC-ili9342

And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 115200 write_flash -z 0x1000 firmware.bin

result::

    esptool.py v4.3
    Serial port /dev/cu.SLAB_USBtoUART
    Connecting.......
    Chip is ESP32-D0WDQ6 (revision v1.0)
    Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
    Crystal is 40MHz
    MAC: a4:cf:12:44:d8:a4
    Uploading stub...
    Running stub...
    Stub running...
    Configuring flash size...
    Flash will be erased from 0x00001000 to 0x001a0fff...
    Compressed 1701552 bytes to 1053029...
    Wrote 1701552 bytes (1053029 compressed) at 0x00001000 in 92.9 seconds (effective 146.5 kbit/s)...
    Hash of data verified.
    Leaving...
    Hard resetting via RTS pin...

ESP32 LILYGO® TTGO T-Display
----------------------------
.. image:: /ESP32/ESP32-TTGO-T-Display.jpg
   :scale: 30%
   
.. image:: /ESP32/CgAGTF0Zc5SAG4UiAAJJ4Gb-zko935.jpg
   :scale: 30%
   
.. image:: /ESP32/H39c2130da52e43e7ac7ccee871075b46E.webp
   :scale: 60%
   
more Information over Hardware `Xinyuan-LilyGO`_.

.. _Xinyuan-LilyGO: https://github.com/Xinyuan-LilyGO/TTGO-T-Display

Firmware from  `Russ Hughes`_.

.. _Russ Hughes: https://github.com/russhughes/st7789_mpy/blob/master/firmware/T-DISPLAY-ESP32/firmware.bin


Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash 
    
result::

    esptool.py v4.3
    Serial port /dev/cu.SLAB_USBtoUART
    Connecting....
    Detecting chip type... Unsupported detection protocol, switching and trying again...
    Connecting....
    Detecting chip type... ESP32
    Chip is ESP32-D0WDQ6-V3 (revision v3.0)
    Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
    Crystal is 40MHz
    MAC: c4:4f:33:7f:f5:89
    Uploading stub...
    Running stub...
    Stub running...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 39.8s
    Hard resetting via RTS pin...

And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 115200 write_flash -z 0x1000 firmware.bin

result::

    esptool.py v4.3
    Serial port /dev/cu.SLAB_USBtoUART
    Connecting....
    Chip is ESP32-D0WDQ6-V3 (revision v3.0)
    Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
    Crystal is 40MHz
    MAC: c4:4f:33:7f:f5:89
    Uploading stub...
    Running stub...
    Stub running...
    Configuring flash size...
    Flash will be erased from 0x00001000 to 0x001b5fff...
    Compressed 1788416 bytes to 1096932...
    Wrote 1788416 bytes (1096932 compressed) at 0x00001000 in 96.9 seconds (effective 147.7 kbit/s)...
    Hash of data verified.

    Leaving...
    Hard resetting via RTS pin...

ESP32-S2
--------

.. image:: /ESP32-S2/s2_mini_v1.0.0_1_16x161.jpg
   :scale: 15%
.. image:: /ESP32-S2/s2-pico-pinout.jpeg
   :scale: 25%
.. image:: /ESP32-S2/s2_mini_v1.0.0_2_16x16.jpg
   :scale: 15%

   
for more Information go to `WEMOS`_.

.. _WEMOS: https://www.wemos.cc/en/latest/s2/s2_mini.html



Make S2 boards into Device Firmware Upgrade (DFU) mode.

Hold on Button 0
Press Button Reset
Release Button 0 When you hear the prompt tone on usb reconnection

now search serial port with:
ls /dev/tty.*

Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/ttyUSB0 erase_flash
    e.g. esptool.py --port /dev/tty.usbmodem01 erase_flash

result::

    esptool.py --port /dev/tty.usbmodem01 erase_flash
    esptool.py v4.3
    Serial port /dev/tty.usbmodem01
    Connecting...
    Detecting chip type... Unsupported detection protocol, switching and trying again...
    Detecting chip type... ESP32-S2
    Chip is ESP32-S2FNR2 (revision v0.0)
    Features: WiFi, Embedded Flash 4MB, Embedded PSRAM 2MB, ADC and temperature sensor calibration in BLK2 of efuse V1
    Crystal is 40MHz
    MAC: 84:f7:03:xx:xx:xx
    Uploading stub...
    Running stub...
    Stub running...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 16.9s
    WARNING: ESP32-S2FNR2 (revision v0.0) chip was placed into download mode using GPIO0.
    esptool.py can not exit the download mode over USB. To run the app, reset the chip manually.
    To suppress this note, set --after option to 'no_reset'.

    
And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
    e.g. esptool.py --chip esp32s2 --port /dev/tty.usbmodem01 --baud 1000000 write_flash -z 0x1000 firmware-LOLIN_S2_PICO-v1.19.1-602-g515088ffd.bin

result::

    esptool.py v4.3
    Serial port /dev/tty.usbmodem01
    Connecting...
    Chip is ESP32-S2FNR2 (revision v0.0)
    Features: WiFi, Embedded Flash 4MB, Embedded PSRAM 2MB, ADC and temperature sensor calibration in BLK2 of efuse V1
    Crystal is 40MHz
    MAC: 84:f7:03:xx:xx:xx
    Uploading stub...
    Running stub...
    Stub running...
    Changing baud rate to 1000000
    Changed.
    Configuring flash size...
    Flash will be erased from 0x00001000 to 0x0012ffff...
    Compressed 1238288 bytes to 818236...
    Wrote 1238288 bytes (818236 compressed) at 0x00001000 in 23.5 seconds (effective 422.4 kbit/s)...
    Hash of data verified.

    Leaving...
    WARNING: ESP32-S2FNR2 (revision v0.0) chip was placed into download mode using GPIO0.
    esptool.py can not exit the download mode over USB. To run the app, reset the chip manually.
    To suppress this note, set --after option to 'no_reset'.

run over tty::

    MicroPython v1.19.1-602-g515088ffd3 on 2022-10-13; LOLIN_S2_PICO with ESP32-S2FN4R2
    Type "help()" for more information.
    >>> import mip
    >>>

please check the deploy tool <mip>
import mip

when successfully the is right version.

LILYGO® TTGO T8 ESP32-S2 V1.1 ST7789 1.14 Inch LCD Display
----------------------------------------------------------

.. image:: /ESP32-S2/LILYGO-TTGO-T8-ESP32-S2-V1.1-ST7789.png
   :scale: 40%
   
.. image:: /ESP32-S2/H4a77f8684c144384a165d7a89476c602q.webp
   :scale: 60%
   
Switch to Program Mode::

    USB       

    On      
    o   o      
      o   o
    1 2 3 4

Using esptool.py you can erase the flash with the command::

    esptool.py --port <port> erase_flash
    e.g. esptool.py --port /dev/cu.usbserial-2120 erase_flash

result::

    esptool.py v4.3
    Serial port /dev/cu.usbserial-2120
    Connecting.........
    Detecting chip type... Unsupported detection protocol, switching and trying again...
    Detecting chip type... ESP32-S2
    Chip is ESP32-S2 (revision v0.0)
    Features: WiFi, No Embedded Flash, No Embedded PSRAM, ADC and temperature sensor calibration in BLK2 of efuse V1
    Crystal is 40MHz
    MAC: 7c:df:a1:32:f4:fa
    Uploading stub...
    Running stub...
    Stub running...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 13.2s
    Hard resetting via RTS pin...


   
Firmware from  `Russ Hughes`_.

.. _Russ Hughes: https://github.com/russhughes/st7789_mpy/blob/master/firmware/T-DISPLAY-ESP32/firmware.bin


Switch to Program Mode::

    USB        OTG

    On         On
    o   o        o   o
      o   o    o   o
    1 2 3 4    1 2 3 4

.. image:: /ESP32-S2/H4a77f8684c144384a165d7a89476c602q.webp
   :scale: 60%

And then deploy the new firmware using::

    esptool.py  --chip esp32s2 --port /dev/cu.usbserial-2120 --baud 115200 write_flash 0x000 firmware.bin
    esptool.py  --chip esp32s2 --port /dev/cu.usbserial-2120 --baud 115200 write_flash 0x000 adafruit-circuitpython-lilygo_ttgo_t8_s2_st7789-de_DE-7.3.3.bin

result::

    esptool.py v4.3
    Serial port /dev/cu.usbserial-2120
    Connecting.........
    Chip is ESP32-S2 (revision v0.0)
    Features: WiFi, No Embedded Flash, No Embedded PSRAM, ADC and temperature sensor calibration in BLK2 of efuse V1
    Crystal is 40MHz
    MAC: 7c:df:a1:32:f4:fa
    Uploading stub...
    Running stub...
    Stub running...
    Configuring flash size...
    Flash will be erased from 0x00000000 to 0x0015bfff...
    Compressed 1421616 bytes to 930326...
    Wrote 1421616 bytes (930326 compressed) at 0x00000000 in 90.5 seconds (effective 125.6 kbit/s)...
    Hash of data verified.

    Leaving...
    Hard resetting via RTS pin...

ESP32-S3
--------

.. image:: /ESP32-S3/s3_v1.0.0_1_16x161.jpg
   :scale: 20%
.. image:: /ESP32-S3/s3_v1.0.0_2_16x16.jpg
   :scale: 20%

S3 Firmware
    https://github.com/wemos/micropython/releases
    
First press IO0 and hold, then press RST

Using esptool.py you can erase the flash with the command::

    esptool.py --port PORT_NAME erase_flash
    esptool.py --port /dev/cu.usbserial-10 erase_flash

    
And then deploy the new firmware using::

    esptool.py --port PORT_NAME --baud 1000000 write_flash -z 0 FIRMWARE.bin
    esptool.py --port /dev/cu.usbserial-110 --baud 1000000 write_flash -z 0 firmware-LOLIN_S3-v1.19.1-669-gd4b9df176.bin
    esptool.py --port /dev/cu.usbserial-110 --baud 1000000 write_flash -z 0 firmware-LOLIN_S3_PRO-v1.19.1-669-gd4b9df176.bin

.. image:: /ESP32-S3/s3_v1.0.0_4_16x9.jpg
   :scale: 40%
   
   
ESP32-C3
--------

Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/ttyUSB0 erase_flash
    
And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin

Raspberry Pico
--------------

Using esptool.py you can erase the flash with the command::

    esptool.py --port /dev/ttyUSB0 erase_flash
    
And then deploy the new firmware using::

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin