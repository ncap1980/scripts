#!/bin/bash
clear
echo "introduce un directorio"
read opcion

until [ -d $opcion ];do
if [ -d $opcion ];then
	DIR=$(ls -d */)
	ls -d */
else


	FICH=$(ls -lh | grep -v "^d") 
fi done 
echo "$directorios"

