# bluetooth-trace
Bluetooth trace data from Purdue user study. Subject of our CPSIoTSec'20 paper. We conducted a measurement study and collected traces of Bluetooth advertisements from 49 users over a period of two weeks in Feb-Mar, 2019. The participating users were asked to install an Android app written by the authors which periodically collected and uploaded traces of Bluetooth advertisements and device locations.

If you use this trace, please cite our paper:

Heng Zhang, Amiya K. Maji, and Saurabh Bagchi. 2020. Privacy in the Mobile World: An Analysis of Bluetooth Scan Traces. In 2020 Joint Workshop on CPS&IoT Security and Privacy (CPSIOTSEC’20), November 9, 2020, Virtual Event, USA. ACM, New York, NY, USA, 5 pages.

The paper is available [here](https://engineering.purdue.edu/dcsl/publications/papers/2020/CPSIOTSEC_2020_camera_ready.pdf).

# Sample script
We have a sample_usage.py file for an easy hands-on check of the data.

# Data Format
1. The trace is a json file once you unzip it (trace.zip). In the unzipped json file, each user has a uniqued hashed id, e.g. 9e0356c01899ce49f002c995c08c306f6f75335aa8087448adb5eccc2333bdbd
2. The data for each user is sorted list of timestamp points. At each time point, it also records the location of the user (latitude, longitude) and the neighbor Bluetooth signals (rssi, mac address, advertisement name). The mac address and the advertisement name are both hashed to protect user privacy.
