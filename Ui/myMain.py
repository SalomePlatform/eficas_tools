# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMain.ui'
#
# Created: Thu Jun 19 11:40:51 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x38\x8d\xed\xd5\xc1\x09\xc0" \
    "\x20\x0c\x05\xd0\x6f\xe9\x36\x81\x2c\x10\xb2\xff" \
    "\xdd\x85\xd2\x53\x85\xb6\xa9\x91\x48\x0f\x05\x3f" \
    "\x08\x1a\xf0\x29\x12\x10\xf8\x28\xc5\xa9\xd9\xc4" \
    "\xde\x96\xcd\x2b\x9a\xd9\xeb\x00\x00\x66\x0e\x2f" \
    "\xe0\xc2\x51\x98\x39\xc4\xf7\x0c\x4c\x44\x6d\x5e" \
    "\x6b\x35\x38\xcf\x92\x82\x45\xe4\xb2\xf6\xf0\x14" \
    "\xac\xaa\x8f\xda\x1d\x4f\xc1\xa5\x74\x1b\x22\x07" \
    "\x9f\x9d\x11\x1d\x96\xea\x8a\x91\x2c\x78\xc1\x0b" \
    "\xee\x64\xe6\x07\x19\xf5\x7e\x92\x03\xad\x45\x2a" \
    "\x04\xcc\x4e\x50\x20\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x99\x49\x44\x41\x54\x38\x8d\xed\x94\x41\x0e\x85" \
    "\x20\x0c\x44\x5f\x89\xc7\x36\x7f\x61\xbc\x77\x5d" \
    "\x28\x48\xa4\x28\x60\xff\xce\xd9\x54\x8b\xbe\x8e" \
    "\x13\x04\x3e\x1d\x92\x81\x77\xf4\x81\xa1\x23\xdc" \
    "\x2b\x34\xf6\xf4\x7a\x3d\xe2\xb8\x65\xa8\x84\x3f" \
    "\x40\x01\x98\x2a\x0b\x3d\x5f\x62\xc5\x83\x00\xaa" \
    "\x1a\xd7\x05\x50\x44\x9a\xb9\xd5\x07\xa7\x73\xa8" \
    "\xa4\xba\x4f\x92\xa2\xdf\x33\x3c\x64\xc6\x3b\xeb" \
    "\xbd\x82\xe5\xb8\xad\xde\xcb\xcc\x78\x20\xeb\x42" \
    "\x66\xc6\x39\x74\x5d\xfa\x80\xf3\x6f\xaf\x66\xc6" \
    "\x6f\xa1\x9c\x3f\x88\x2f\xb4\x70\xec\x05\xcd\xc0" \
    "\xbe\xd0\x78\x93\xf6\x8e\x17\x14\x92\x63\x5f\x68" \
    "\x6c\x3e\xef\xf6\xba\x3c\x8f\xdd\x36\x6d\xc4\xc0" \
    "\x45\x2c\x87\x81\xf8\x08\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image2_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xa0\x49\x44\x41\x54\x38\x8d\xd5\x95\x4d\x0a\x80" \
    "\x20\x10\x85\x9f\xd1\x46\x68\xe1\x8d\xe6\x62\xd2" \
    "\x22\xbc\x98\x37\x6a\x21\xb4\xac\x45\x19\x92\xc6" \
    "\x64\x69\xe0\xb7\xf1\x87\xf1\xf1\x1c\x47\x05\x2a" \
    "\x21\x8e\x76\x2d\xad\xdb\xfb\x9e\x99\xf6\x56\x8f" \
    "\x80\xb5\x36\x4b\x85\x88\xce\x35\x44\x04\x00\xe8" \
    "\x0a\x39\x8c\xe8\xf9\x90\x34\xd2\x29\x2c\xc3\x7c" \
    "\x8e\xbd\x53\x0f\xeb\x58\x3a\x05\xe9\x54\x34\x1f" \
    "\x8a\x02\x7b\x2a\x7d\x3a\x1f\x09\xbf\x85\x4d\xc5" \
    "\xd5\xd9\x53\xaa\x39\x6e\x4f\x38\xca\xb1\x99\xe2" \
    "\xd2\xe1\x08\xab\xe1\x56\xf8\x2e\x30\x97\x7f\xcb" \
    "\x4d\x8f\xf9\x42\xd7\x5d\xbe\xbe\xd2\xe1\x43\x95" \
    "\x3a\x93\xf6\xca\xad\x3d\x61\x11\xf4\x4b\x7d\x4f" \
    "\x82\x0f\xf9\xc0\x06\x9b\xb5\x1e\xcd\xed\x31\x8c" \
    "\x5c\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
image3_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x73\x49\x44\x41\x54\x38\x8d\xed\x92\xc1\x0e\x80" \
    "\x20\x08\x40\xb1\xef\x66\x1d\x1c\xff\x4d\x87\x6a" \
    "\xa8\x88\xa1\x76\x69\xf9\x36\x0f\x28\x3e\xd8\x00" \
    "\x60\xf1\x59\x42\x5f\x3a\x71\xf5\x36\x02\xe0\x8e" \
    "\x99\x2b\x09\x88\x01\xd0\x28\x54\x17\x6a\xe4\x7f" \
    "\x21\xce\x1f\xb5\xb0\x5d\x38\xed\xdc\x90\x60\xd0" \
    "\xf1\x13\x79\x63\x5b\x3b\xc9\x2b\xd5\x18\xe2\x39" \
    "\xa9\x43\xec\x1d\x5a\xb7\x78\x5c\xee\x10\x7b\xe4" \
    "\xb2\x15\xaf\x40\x91\xf8\x94\xde\x47\x18\x1e\xce" \
    "\xa5\x9e\xde\x9e\xc5\x9f\x38\x00\x62\xac\x28\xb1" \
    "\xe3\xd7\x01\xd9\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"
image4_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x38\x8d\xed\x92\xc1\x0a\xc0" \
    "\x20\x08\x40\x6d\xdf\x2d\x3b\x84\xff\xed\x0e\xa3" \
    "\x58\x6a\x26\xd1\x65\xe0\x83\x0e\xa5\x3e\x85\x04" \
    "\x48\x7e\x4b\x91\x0f\x54\x89\xf1\x9e\xa5\xa3\xca" \
    "\x0f\x8a\x89\x63\x65\xb3\x06\xc4\x2d\xd6\x13\xc6" \
    "\x49\xbd\xc2\x59\x83\x16\x13\x62\x19\xf0\xf9\x36" \
    "\xc0\xa2\xef\x00\xd7\x5a\x62\x61\x4d\x3a\xb2\x29" \
    "\x96\xf2\xa3\x62\xff\xa3\x37\xc5\xeb\xed\xe9\x62" \
    "\xaa\xd1\xa2\xe8\x4a\xaa\xa2\xf7\x50\xdd\x12\x74" \
    "\x8c\x0f\xd0\xab\x93\x24\x67\x78\x00\x59\x6e\x28" \
    "\xb1\x74\x3f\x46\x86\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image5_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x82\x49\x44\x41\x54\x38\x8d\xcd\xd3\x41\x12\x80" \
    "\x20\x08\x05\x50\xe8\xe0\x2e\xbc\x38\xad\x32\x73" \
    "\x50\x3e\x48\x53\x7f\xe3\xe4\x8c\x4f\x24\x25\xfa" \
    "\x28\xe2\x9c\x6f\x39\x92\x0b\xf9\x27\x6c\xb6\x01" \
    "\x85\x35\x88\x77\x61\x13\x88\xc2\x57\x64\x18\xcd" \
    "\xa0\x15\xf5\x20\xb4\xe6\xb5\x5b\xe1\x09\xdc\x06" \
    "\x22\xb8\xe2\x2a\xcf\x31\x05\x6e\x18\xdf\xdf\xf8" \
    "\x06\x06\xaa\x55\x1c\xc6\x35\x64\xc4\xdc\xf8\x0c" \
    "\xd0\x20\x1d\x57\x7a\x5c\x85\xa8\x84\x5f\xdc\x02" \
    "\x5e\xa5\x30\x7a\xfc\xcd\x07\xe2\x3a\x1d\xf2\x83" \
    "\xec\x2b\x37\xd9\xad\x5f\xb4\xdf\xef\xd4\x9c\xfb" \
    "\xf7\x2f\xac\x98\xc8\xcc\x89\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
image6_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xbf\x49\x44\x41\x54\x38\x8d\xd5\x93\x41\x0a\x83" \
    "\x30\x10\x45\xdf\x48\x8e\xe5\x1d\xbc\x8c\x3b\xa9" \
    "\x8b\xf4\x6a\x9e\xab\xd3\x85\x35\x0d\x26\x63\x62" \
    "\x44\x4a\x3f\x0c\x42\x66\xfc\xf3\xf8\x24\xf0\x6f" \
    "\x12\x40\x2b\x66\xda\x8c\x55\xf3\xde\x22\x12\xcf" \
    "\x9d\x92\xcb\x98\xc0\xba\x2d\x7c\x45\x44\xcf\x9a" \
    "\x07\x63\x8b\xba\xd5\x3c\x44\x91\x23\x5e\xcf\x7c" \
    "\xc1\x62\x36\x97\xa9\x25\x40\xc1\x1f\xf4\xfd\xa7" \
    "\x52\x75\x01\x5d\x24\xa9\x38\x9e\x7d\x6f\x53\xdf" \
    "\x4f\xe4\xcc\xab\x32\x3e\xea\x0f\x03\xc0\xc4\xb2" \
    "\xa0\x71\x2c\xe6\xad\xd8\x9b\x59\xb7\x66\x1c\x3b" \
    "\xe0\x95\x98\x5f\x26\x16\x79\xee\x4e\xbc\xc2\x2c" \
    "\x97\x88\x55\x1f\xe6\xa2\xcb\xc4\x96\x9a\x89\x4b" \
    "\xcb\x6f\x23\xee\x36\x1a\xab\x62\xe2\x52\xc5\x72" \
    "\x94\xdf\xbf\xb6\x10\xbb\xf2\xc8\x97\xb8\xa4\x6c" \
    "\xc6\x67\x7e\xaa\x51\x95\x71\xfa\x08\x7e\xa8\x37" \
    "\x62\xda\x9a\xba\xcb\x20\x23\x5f\x00\x00\x00\x00" \
    "\x49\x45\x4e\x44\xae\x42\x60\x82"
image7_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xd5\x49\x44\x41\x54\x38\x8d\xc5\x95\x5d\x0a\x84" \
    "\x30\x0c\x84\x27\xe2\xa9\x0a\x9e\x6c\x8b\x0f\x4b" \
    "\x3d\xd9\x82\xd7\xca\x3e\x58\xd7\xfe\x4c\xd0\xba" \
    "\x5d\x76\x40\x02\x4d\xf2\x65\xda\x0a\x05\x7e\x24" \
    "\x39\xc9\xeb\x8d\x9e\xaa\x88\x41\xa0\xc9\xaa\xd8" \
    "\xc8\x2a\xb3\x2f\x9c\x42\x5b\xe1\xe3\x0e\x0d\xcf" \
    "\x00\xc0\x03\x08\xf0\xb3\xa7\xa0\x74\x10\xa9\xd7" \
    "\x14\x2e\x00\xb4\x2c\x5a\x5f\xab\x69\x6b\x97\x9b" \
    "\x1c\x83\x7f\xc0\xc3\x16\xb6\xe4\x16\x5b\x64\xf7" \
    "\x8d\x71\x63\x59\x91\x9b\xdc\x45\x70\xde\x47\xc0" \
    "\x47\x32\xdd\x5e\x5b\xcc\x35\xf0\xc9\x77\x62\xae" \
    "\x78\x79\x36\xdc\xcf\x75\x13\x57\x7e\x79\xf4\x8c" \
    "\x4b\x27\xaa\x0f\x13\x27\xb2\x40\xf5\x11\x7f\xcb" \
    "\xe3\x48\xaa\x33\xb6\xe0\x22\x4b\x05\x4d\x07\x46" \
    "\xb8\x02\x5e\x2e\x3b\x3e\x73\xcd\xe0\xdd\x1c\x97" \
    "\xf0\x2e\x8e\xd9\xd0\xaf\x1d\xb3\x81\x22\x4b\xdf" \
    "\x33\xee\xe6\x98\xa9\x34\xa0\xf6\x17\xb4\x55\x40" \
    "\xd0\x0b\xcf\x4c\xa0\x8f\xc0\xdf\xf4\x06\xe3\x25" \
    "\xc1\x98\x1b\xc4\x18\x76\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image8_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x5d\x49\x44\x41\x54\x38\x8d\xd5\x93\xa1\x72\xdb" \
    "\x40\x10\x86\x3f\x67\x0a\x56\xec\xc4\x22\x78\xd0" \
    "\x65\x36\x93\xa0\xc2\x1c\x68\xd6\xc2\xe6\x0d\xf2" \
    "\x1a\x81\x81\x11\x34\x94\x99\xc2\x54\xa8\x32\x9b" \
    "\x55\xf0\xe0\x89\xdd\xb1\x5b\xa6\x02\xb7\x9d\x66" \
    "\x92\xd6\x99\xb6\xd3\x99\xfe\xe8\x6e\x67\xe7\xdb" \
    "\x7f\x77\xef\xe0\x7f\xd3\xe2\xc7\x4b\xd7\x75\xb3" \
    "\x73\x0e\xef\x3d\x51\x15\x00\x23\x82\xb5\x16\x6b" \
    "\x2d\x57\x57\x57\x8b\x17\x29\xbf\x02\xb7\x6d\x3b" \
    "\x0f\x87\x03\xb9\x2d\x58\xae\xd7\x60\x04\x00\xef" \
    "\x1c\xe3\xc7\x03\x06\xa8\xaa\x8a\xeb\xeb\xeb\x57" \
    "\xc1\x17\xdf\xa0\x6d\xdb\x52\x5d\xd7\x54\xef\xb6" \
    "\x00\xa8\x2a\x49\x13\x8a\x12\x35\x32\xec\x3a\xc4" \
    "\x2b\x9b\xcd\xe6\x55\xce\x2f\xfa\xbe\x9f\x87\xc3" \
    "\x40\xfd\xe1\x3d\xcb\x4d\x8d\xaa\xa2\x4e\x48\xee" \
    "\x12\xc6\x82\x38\x08\xc1\x07\x96\x9b\x1a\x8a\x9c" \
    "\xe3\xf1\xf8\xaa\x51\x5c\x38\xe7\xc8\xad\xa5\xaa" \
    "\x6b\x00\xc4\x5f\x12\x9c\x67\xd2\x23\x93\x8c\x88" \
    "\xe6\xc8\x60\xd1\x18\xb1\xd5\x92\xd1\x39\xba\xae" \
    "\x9b\xcf\x83\xa7\x89\x65\xb5\x46\x51\x34\x80\x1b" \
    "\x1d\x2e\x1f\x49\x45\xc0\xe3\x50\x09\x64\x08\xea" \
    "\x15\x44\x90\xc2\xe0\xbd\x3f\xef\x58\x53\xc2\xe4" \
    "\x86\xa0\x01\x9f\x4d\x84\xf5\x84\x18\x41\x83\x62" \
    "\xb0\x40\x8e\x8b\x23\xc9\x24\x50\x10\x93\x31\x4d" \
    "\xd3\x59\xf0\x1b\x80\x98\x14\x11\x20\x25\x14\x40" \
    "\x15\xf1\x96\x4c\x0b\xbc\x1b\x48\x4b\x07\xe4\x68" \
    "\x88\x80\xc0\x29\xeb\xd7\x8e\x41\x41\xf5\xb4\x34" \
    "\xfd\x76\x86\x4c\x05\x3f\x1e\x08\x4b\x0f\x85\x80" \
    "\x26\x54\x40\x63\x40\x44\xce\x83\x8b\xbc\xc0\x39" \
    "\x87\xa6\x13\x50\xa3\xa2\x28\x5e\x1d\x5a\x44\x14" \
    "\xd0\x70\x8a\xa5\x98\x08\x21\x62\xad\x3d\x0f\xb6" \
    "\xd6\xe2\x87\xcf\xa4\x98\x50\x8d\x27\x40\x50\x44" \
    "\x73\x70\x42\x8c\x91\xaf\x8d\x10\xfd\x44\x81\x60" \
    "\x8c\x39\x0b\x5e\x00\xdc\xdd\xdd\xcd\x8e\x80\xa9" \
    "\xde\x42\x02\x48\xe8\x04\x84\x08\x56\xf0\x3e\x02" \
    "\x90\x7d\x72\x94\x65\xc9\xba\x5a\xe3\x46\x87\x31" \
    "\xe6\xa7\x9f\xe5\x02\x60\xb5\x5a\x61\x02\xc4\xee" \
    "\x40\xa6\x89\x4c\x33\xf2\xcb\x0c\xb1\x06\x51\x28" \
    "\x14\xf8\xf8\x99\xb2\x2c\xb9\xb9\xb9\x59\xb8\xd1" \
    "\xf1\xf8\xf8\x48\xd3\x34\xb4\x6d\xfb\xe2\x9b\xfe" \
    "\x5e\xad\xef\xfb\xf9\x78\x3c\x32\x3a\x87\x18\x81" \
    "\xec\xb4\x20\x0d\x11\x51\xa8\xeb\x9a\xed\x76\xbb" \
    "\x00\x18\x86\x61\xee\xba\x8e\xfd\x7e\x8f\x31\x86" \
    "\xed\x76\xcb\x6a\xb5\x7a\xe2\xfe\x59\x1b\x5d\xd7" \
    "\xcd\xde\x7b\x62\x8c\x88\x08\x79\x9e\x63\xad\xa5" \
    "\xaa\xaa\x67\xb9\xbb\xdd\x6e\x6e\x9a\x06\xef\x3d" \
    "\x75\x5d\x3f\x29\xfe\xc7\xea\xfb\x7e\xbe\xbd\xbd" \
    "\x9d\xad\xb5\x73\x59\x96\xf3\xfd\xfd\xfd\xfc\xa2" \
    "\xe3\xdf\xd5\xc3\xc3\xc3\xdc\x34\x0d\xd3\x34\xb1" \
    "\xd9\x6c\xfe\x1e\x18\x4e\x63\xdc\xef\xf7\xa4\x94" \
    "\xfe\x26\xf6\x1f\xe9\x0b\xbc\x4c\x5e\x59\xd6\x14" \
    "\xca\xf4\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"

class Eficas(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        self.image2 = QPixmap()
        self.image2.loadFromData(image2_data,"PNG")
        self.image3 = QPixmap()
        self.image3.loadFromData(image3_data,"PNG")
        self.image4 = QPixmap()
        self.image4.loadFromData(image4_data,"PNG")
        self.image5 = QPixmap()
        self.image5.loadFromData(image5_data,"PNG")
        self.image6 = QPixmap()
        self.image6.loadFromData(image6_data,"PNG")
        self.image7 = QPixmap()
        self.image7.loadFromData(image7_data,"PNG")
        self.image8 = QPixmap()
        self.image8.loadFromData(image8_data,"PNG")
        if not name:
            self.setName("Eficas")

        self.setEnabled(1)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.sizePolicy().hasHeightForWidth()))
        self.setMinimumSize(QSize(21,336))
        self.setBackgroundOrigin(QMainWindow.WidgetOrigin)
        f = QFont(self.font())
        self.setFont(f)

        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.line1 = QFrame(self.centralWidget(),"line1")
        self.line1.setGeometry(QRect(-30,-10,930,20))
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.HLine)

        self.fileNewAction = QAction(self,"fileNewAction")
        self.fileNewAction.setIconSet(QIconSet(self.image0))
        self.fileOpenAction = QAction(self,"fileOpenAction")
        self.fileOpenAction.setIconSet(QIconSet(self.image1))
        self.fileSaveAction = QAction(self,"fileSaveAction")
        self.fileSaveAction.setIconSet(QIconSet(self.image2))
        self.fileSaveAsAction = QAction(self,"fileSaveAsAction")
        self.fileExitAction = QAction(self,"fileExitAction")
        self.editUndoAction = QAction(self,"editUndoAction")
        self.editUndoAction.setEnabled(0)
        self.editUndoAction.setIconSet(QIconSet(self.image3))
        self.editRedoAction = QAction(self,"editRedoAction")
        self.editRedoAction.setEnabled(0)
        self.editRedoAction.setIconSet(QIconSet(self.image4))
        self.editCutAction = QAction(self,"editCutAction")
        self.editCutAction.setIconSet(QIconSet(self.image5))
        self.editCopyAction = QAction(self,"editCopyAction")
        self.editCopyAction.setIconSet(QIconSet(self.image6))
        self.editPasteAction = QAction(self,"editPasteAction")
        self.editPasteAction.setIconSet(QIconSet(self.image7))
        self.jdcFichierResultatAction = QAction(self,"jdcFichierResultatAction")
        self.jdcFichierResultatAction.setEnabled(1)
        self.jdcFichierResultatAction.setIconSet(QIconSet(self.image8))
        self.helpContentsAction = QAction(self,"helpContentsAction")
        self.helpIndexAction = QAction(self,"helpIndexAction")
        self.helpAboutAction = QAction(self,"helpAboutAction")
        self.helpAboutAction.setOn(0)
        self.fileSaveCloseAction = QAction(self,"fileSaveCloseAction")
        self.fileCloseAction = QAction(self,"fileCloseAction")
        self.fileNewViewAction = QAction(self,"fileNewViewAction")
        self.fileNewViewAction.setEnabled(0)
        self.fileCloseAllAction = QAction(self,"fileCloseAllAction")
        self.jdcRapportDeValidationAction = QAction(self,"jdcRapportDeValidationAction")
        self.jdcFichierSourceAction = QAction(self,"jdcFichierSourceAction")
        self.traduitV7V8Action = QAction(self,"traduitV7V8Action")
        self.aidenew_itemAction = QAction(self,"aidenew_itemAction")
        self.fileNewInclude = QAction(self,"fileNewInclude")
        self.optionEditeurAction = QAction(self,"optionEditeurAction")
        self.optionPdfAction = QAction(self,"optionPdfAction")


        self.toolBar = QToolBar(QString(""),self,Qt.DockTop)

        self.toolBar.setFrameShape(QToolBar.MenuBarPanel)
        self.toolBar.setHorizontallyStretchable(0)
        self.fileNewAction.addTo(self.toolBar)
        self.fileSaveAction.addTo(self.toolBar)
        self.fileOpenAction.addTo(self.toolBar)
        self.fileSaveAsAction.addTo(self.toolBar)
        self.editCutAction.addTo(self.toolBar)
        self.editPasteAction.addTo(self.toolBar)
        self.jdcFichierResultatAction.addTo(self.toolBar)
        self.fileExitAction.addTo(self.toolBar)
        self.toolBar.addSeparator()


        self.MenuBar = QMenuBar(self,"MenuBar")

        self.MenuBar.setMargin(2)

        self.Fichier = QPopupMenu(self)
        self.fileNewAction.addTo(self.Fichier)
        self.fileNewInclude.addTo(self.Fichier)
        self.fileOpenAction.addTo(self.Fichier)
        self.fileSaveAction.addTo(self.Fichier)
        self.fileSaveAsAction.addTo(self.Fichier)
        self.fileCloseAction.addTo(self.Fichier)
        self.fileCloseAllAction.addTo(self.Fichier)
        self.Fichier.insertSeparator()
        self.Fichier.insertSeparator()
        self.fileExitAction.addTo(self.Fichier)
        self.MenuBar.insertItem(QString(""),self.Fichier,2)

        self.Edition = QPopupMenu(self)
        self.Edition.insertSeparator()
        self.editCutAction.addTo(self.Edition)
        self.editCopyAction.addTo(self.Edition)
        self.editPasteAction.addTo(self.Edition)
        self.MenuBar.insertItem(QString(""),self.Edition,3)

        self.JdC = QPopupMenu(self)
        self.jdcRapportDeValidationAction.addTo(self.JdC)
        self.jdcFichierSourceAction.addTo(self.JdC)
        self.jdcFichierResultatAction.addTo(self.JdC)
        self.MenuBar.insertItem(QString(""),self.JdC,4)

        self.Aide = QPopupMenu(self)
        self.aidenew_itemAction.addTo(self.Aide)
        self.MenuBar.insertItem(QString(""),self.Aide,5)

        self.Options = QPopupMenu(self)
        self.optionEditeurAction.addTo(self.Options)
        self.optionPdfAction.addTo(self.Options)
        self.MenuBar.insertItem(QString(""),self.Options,6)

        self.Traduction = QPopupMenu(self)
        self.traduitV7V8Action.addTo(self.Traduction)
        self.MenuBar.insertItem(QString(""),self.Traduction,7)

        self.Patrons = QPopupMenu(self)
        self.MenuBar.insertItem(QString(""),self.Patrons,8)


        self.languageChange()

        self.resize(QSize(902,594).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.fileNewAction,SIGNAL("activated()"),self.fileNew)
        self.connect(self.fileOpenAction,SIGNAL("activated()"),self.fileOpen)
        self.connect(self.fileSaveAction,SIGNAL("activated()"),self.fileSave)
        self.connect(self.fileSaveAsAction,SIGNAL("activated()"),self.fileSaveAs)
        self.connect(self.fileExitAction,SIGNAL("activated()"),self.fileExit)
        self.connect(self.editUndoAction,SIGNAL("activated()"),self.editUndo)
        self.connect(self.editRedoAction,SIGNAL("activated()"),self.editRedo)
        self.connect(self.editCutAction,SIGNAL("activated()"),self.editCut)
        self.connect(self.editPasteAction,SIGNAL("activated()"),self.editPaste)
        self.connect(self.jdcFichierResultatAction,SIGNAL("activated()"),self.visuJdcPy)
        self.connect(self.helpIndexAction,SIGNAL("activated()"),self.helpIndex)
        self.connect(self.helpContentsAction,SIGNAL("activated()"),self.helpContents)
        self.connect(self.helpAboutAction,SIGNAL("activated()"),self.helpAbout)
        self.connect(self.fileCloseAction,SIGNAL("activated()"),self.fileClose)
        self.connect(self.fileNewViewAction,SIGNAL("activated()"),self.fileNewView)
        self.connect(self.fileCloseAllAction,SIGNAL("activated()"),self.fileCloseAll)
        self.connect(self.editCopyAction,SIGNAL("activated()"),self.editCopy)
        self.connect(self.jdcRapportDeValidationAction,SIGNAL("activated()"),self.jdcRapport)
        self.connect(self.jdcFichierSourceAction,SIGNAL("activated()"),self.jdcFichierSource)
        self.connect(self.traduitV7V8Action,SIGNAL("activated()"),self.traductionV7V8)
        self.connect(self.aidenew_itemAction,SIGNAL("activated()"),self.helpAbout)
        self.connect(self.fileNewInclude,SIGNAL("activated()"),self.NewInclude)
        self.connect(self.optionEditeurAction,SIGNAL("activated()"),self.optionEditeur)
        self.connect(self.optionPdfAction,SIGNAL("activated()"),self.optionPdf)


    def languageChange(self):
        self.setCaption(self.__tr("Eficas "))
        self.fileNewAction.setText(self.__tr("Nouveau"))
        self.fileNewAction.setMenuText(self.__tr("&Nouveau"))
        self.fileNewAction.setAccel(self.__tr("Ctrl+N"))
        self.fileOpenAction.setText(self.__tr("Ouvrir"))
        self.fileOpenAction.setMenuText(self.__tr("&Ouvrir"))
        self.fileOpenAction.setAccel(self.__tr("Ctrl+O"))
        self.fileSaveAction.setText(self.__tr("Enregistrer"))
        self.fileSaveAction.setMenuText(self.__tr("&Enregistrer"))
        self.fileSaveAction.setAccel(self.__tr("Ctrl+E"))
        self.fileSaveAsAction.setText(self.__tr("Enregistrer Sous"))
        self.fileSaveAsAction.setMenuText(self.__tr("Enregistrer Sous"))
        self.fileSaveAsAction.setAccel(QString.null)
        self.fileExitAction.setText(self.__tr("Quitter"))
        self.fileExitAction.setMenuText(self.__tr("Q&uitter"))
        self.fileExitAction.setAccel(QString.null)
        self.editUndoAction.setText(self.__tr("Undo"))
        self.editUndoAction.setMenuText(self.__tr("&Undo"))
        self.editUndoAction.setAccel(self.__tr("Ctrl+Z"))
        self.editRedoAction.setText(self.__tr("Redo"))
        self.editRedoAction.setMenuText(self.__tr("&Redo"))
        self.editRedoAction.setAccel(self.__tr("Ctrl+Y"))
        self.editCutAction.setText(self.__tr("Couper"))
        self.editCutAction.setMenuText(self.__tr("C&ouper"))
        self.editCutAction.setAccel(self.__tr("Ctrl+X"))
        self.editCopyAction.setText(self.__tr("Copier"))
        self.editCopyAction.setMenuText(self.__tr("&Copier"))
        self.editCopyAction.setAccel(self.__tr("Ctrl+C"))
        self.editPasteAction.setText(self.__tr("Coller"))
        self.editPasteAction.setMenuText(self.__tr("&Coller"))
        self.editPasteAction.setAccel(self.__tr("Ctrl+V"))
        self.jdcFichierResultatAction.setText(self.__tr("Fichier Resultat"))
        self.jdcFichierResultatAction.setMenuText(self.__tr("Fichier Resultat"))
        self.jdcFichierResultatAction.setAccel(self.__tr("Ctrl+F"))
        self.helpContentsAction.setText(self.__tr("Contents"))
        self.helpContentsAction.setMenuText(self.__tr("&Contents..."))
        self.helpContentsAction.setAccel(QString.null)
        self.helpIndexAction.setText(self.__tr("Index"))
        self.helpIndexAction.setMenuText(self.__tr("&Index..."))
        self.helpIndexAction.setAccel(QString.null)
        self.helpAboutAction.setText(self.__tr("About"))
        self.helpAboutAction.setMenuText(self.__tr("&About"))
        self.helpAboutAction.setAccel(QString.null)
        self.fileSaveCloseAction.setText(self.__tr("Fermer"))
        self.fileSaveCloseAction.setMenuText(self.__tr("Fermer"))
        self.fileCloseAction.setText(self.__tr("Fermer"))
        self.fileCloseAction.setMenuText(self.__tr("Fermer"))
        self.fileCloseAction.setAccel(self.__tr("Ctrl+W"))
        self.fileNewViewAction.setText(self.__tr("New view"))
        self.fileCloseAllAction.setText(self.__tr("Tout Fermer"))
        self.fileCloseAllAction.setMenuText(self.__tr("Tout Fermer"))
        self.jdcRapportDeValidationAction.setText(self.__tr("Rapport de validation"))
        self.jdcRapportDeValidationAction.setMenuText(self.__tr("Rapport de validation"))
        self.jdcRapportDeValidationAction.setAccel(self.__tr("Ctrl+R"))
        self.jdcFichierSourceAction.setText(self.__tr("Fichier source"))
        self.jdcFichierSourceAction.setMenuText(self.__tr("Fichier source"))
        self.jdcFichierSourceAction.setAccel(self.__tr("Ctrl+B"))
        self.traduitV7V8Action.setText(self.__tr("traduitV7V8"))
        self.traduitV7V8Action.setMenuText(self.__tr("traduitV7V8"))
        self.aidenew_itemAction.setText(self.__tr("Eficas"))
        self.fileNewInclude.setText(self.__tr("Nouvel Include"))
        self.fileNewInclude.setMenuText(self.__tr("Nouvel Include"))
        self.optionEditeurAction.setText(self.__tr("Parametres Eficas"))
        self.optionEditeurAction.setMenuText(self.__tr("Parametres Eficas"))
        self.optionPdfAction.setText(self.__tr("Lecteur Pdf"))
        self.optionPdfAction.setMenuText(self.__tr("Lecteur Pdf"))
        self.toolBar.setLabel(self.__tr("Tools"))
        if self.MenuBar.findItem(2):
            self.MenuBar.findItem(2).setText(self.__tr("&Fichier"))
        if self.MenuBar.findItem(3):
            self.MenuBar.findItem(3).setText(self.__tr("&Edition"))
        if self.MenuBar.findItem(4):
            self.MenuBar.findItem(4).setText(self.__tr("JdC"))
        if self.MenuBar.findItem(5):
            self.MenuBar.findItem(5).setText(self.__tr("&Aide"))
        if self.MenuBar.findItem(6):
            self.MenuBar.findItem(6).setText(self.__tr("Options"))
        if self.MenuBar.findItem(7):
            self.MenuBar.findItem(7).setText(self.__tr("Traduction"))
        if self.MenuBar.findItem(8):
            self.MenuBar.findItem(8).setText(self.__tr("Patrons"))


    def fileNew(self):
        print "Eficas.fileNew(): Not implemented yet"

    def fileOpen(self):
        print "Eficas.fileOpen(): Not implemented yet"

    def fileSave(self):
        print "Eficas.fileSave(): Not implemented yet"

    def fileSaveAs(self):
        print "Eficas.fileSaveAs(): Not implemented yet"

    def filePrint(self):
        print "Eficas.filePrint(): Not implemented yet"

    def fileExit(self):
        print "Eficas.fileExit(): Not implemented yet"

    def editUndo(self):
        print "Eficas.editUndo(): Not implemented yet"

    def editRedo(self):
        print "Eficas.editRedo(): Not implemented yet"

    def jdcFichierSource(self):
        print "Eficas.jdcFichierSource(): Not implemented yet"

    def fileNewView(self):
        print "Eficas.fileNewView(): Not implemented yet"

    def editPaste(self):
        print "Eficas.editPaste(): Not implemented yet"

    def visuJdcPy(self):
        print "Eficas.visuJdcPy(): Not implemented yet"

    def helpIndex(self):
        print "Eficas.helpIndex(): Not implemented yet"

    def helpContents(self):
        print "Eficas.helpContents(): Not implemented yet"

    def helpAbout(self):
        print "Eficas.helpAbout(): Not implemented yet"

    def fileClose(self):
        print "Eficas.fileClose(): Not implemented yet"

    def fileCloseAll(self):
        print "Eficas.fileCloseAll(): Not implemented yet"

    def jdcRapport(self):
        print "Eficas.jdcRapport(): Not implemented yet"

    def editCut(self):
        print "Eficas.editCut(): Not implemented yet"

    def editCopy(self):
        print "Eficas.editCopy(): Not implemented yet"

    def traductionV7V8(self):
        print "Eficas.traductionV7V8(): Not implemented yet"

    def NewInclude(self):
        print "Eficas.NewInclude(): Not implemented yet"

    def optionEditeur(self):
        print "Eficas.optionEditeur(): Not implemented yet"

    def optionPdf(self):
        print "Eficas.optionPdf(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Eficas",s,c)
