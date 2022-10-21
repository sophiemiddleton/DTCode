# Notes on how to use this code:

## Getting data:

The only mode we can use remotely is Multi-Channel Analysis (MCA) mode. Before lowering the REM500 into the pit, put it in MCA mode before. This is the optional multichannel analyzer mode and is used to dump the contents of the memory to an external computer for analysis (see manual for details). An RS232 seriel connection can be used to send this information to a computer for analysis.

On the device the MCA display shows the time and counts on the top line. The bottom line shows the
operations:

* TIM will go to the time setting display. See below for a detailed description.
* NXT will return to the last menu level before the MCA display.
* RST will reset the time, counts and the MCA memory. If the MCA is running it will stop it. If time is
set to zero, it will reset to zero. If it is set to a number, it will reset to that number.
* RUN will start the time, counts, and MCA.
* STP will stop the time, counts and MCA.
* CK will turn on the optional internal source. To turn off the internal source press RST. If the
detector contains the option source, this choice will be shown only when the MCA is running. If
the source is not installed, this choice will not be shown.

Serial port can be read using the python library "serial": https://pyserial.readthedocs.io/en/latest/pyserial.html .

When in the MCA mode to communicate with the device:

* S Stops Counting
* G Go, Starts counting
* C Clears MCA memory
* D Downloads the MCA memory

The MCA data is downloaded in hex format, 2 bytes per channel. Channel 1 is first,
followed by channel 2, channel 3, etc until all 256 channels have been downloaded.
There is a space between each channel. e.g. 0A32 counts is 2610 counts.
