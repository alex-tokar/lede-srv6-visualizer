# lede-srv6-visualizer
Visualizer tool used for the Netconf/Sysrepo SRv6 route installation in LEDE.

Requires Python 3 with PyQT5, paramiko and ncclient

The application assumes an IP address of 192.168.56.101 for rtrA and 192.168.56.102 for rtrB. This can be changed by creating a configuration file called config.ini with the following contents:
```
[rtrA]
hostname = 1.1.1.1
[rtrB]
hostname = 2.2.2.2
```
You can find pre-built x86 LEDE images with everything pre-configured in the images directory, complete with VirtualBox configuration. Alternatively, you can build the images yourself from this repository: https://github.com/alex-tokar/lede-srv6
