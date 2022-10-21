# Notes on how to use this code:

## Overview:

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

## Using this code for data extraction:

The file labeled "read_rem.py" will read the output of the REM and store it in a .txt file. The first stage is to RESET ('R') and GO ('G') i.e. start the run. The run goes then for a given amount of seconds before STOPPING ('S'), CLEARING ('C') and DUMPING ('D').

Two output text files are produced:

* raw_data.txt - the raw data in HEX (for all channels)
* channel_file.txt - provides 256 numbers, each is a count per that channel

Each file is produced for a given run_time.

The MCA has 256 channels, the dump over RS232 gives a number of counts for each channel.This is stored in the "channel_file".

## Using this code for data analysis:

The "data_analysis.py" file can be used to analyze the output of the extraction phase.

The manual describes how to find the mu rem/hr and mu rad / hr  using an equation. The QF for the channels is derived from a smoothing of the ICRP values and ranges from 1 to 24.8. K is the Calibration Factor. It is used to get the rad/hr calculation. The channel-by-channel quality factors are given on page 39.

This script provides some plots:

* Time .v. Counts from the raw data
* Counts .v. Channel number from the channel data file
