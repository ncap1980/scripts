#!/bin/bash

folder_certs=`sudo grep -ir '"domains" : "ghost.ncapsyn.com"' /usr/syno/etc/certificate/_archive/`
echo $folder_certs
#folder_ghost=`dirname -z $folder_certs | cut -d / -f 7`
#echo ${folder_certs:0:42}
folder_ghost=${folder_certs:0:42}
echo $folder_ghost
 
scp -i copy_vu_plus $folder_ghost/fullchain.pem root@192.168.2.6:/etc/enigma2/ghost/cert.pem
scp -i copy_vu_plus $folder_ghost/privkey.pem root@192.168.2.6:/etc/enigma2/ghost/privkey.pem
