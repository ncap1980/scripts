#!/bin/bash
clear
d=~/Descargas

if [ -d ~/Descargas ] && [ -e ~/Descargas/*.avi ]
	then
		echo "Copiando Capitulos"
		find $d -iname "*.avi" -size "-700M"
		find $d -iname "*.avi" -size "-700M" | xargs -i ls {} | xargs -i cp {} /media/series/
		echo "Borrando Series descargadas"
		find $d -iname "*.avi" -size "-700M" | xargs -i rm {} 
	else
		echo "No hay Series descargadas"
	
fi
sleep 5
if [ -d ~/Descargas ] && [ -e ~/Descargas/*.avi ]
	then
		echo "Copiando Peliculas"
		find $d -iname "*.avi" -size "+701M"
		find $d -iname "*.avi" -size "+701M" | xargs -i ls {} | xargs -i cp {} /media/peliculas/Ver
		echo "Borrando Peliculas descargadas"
		find $d -iname "*.avi" -size "+701M" | xargs -i rm {} 
	else
		echo "No hay Peliculas descargadas"
fi
sleep 5
if [ -d ~/Descargas ] && [ -e ~/Descargas/*.iso ]
	then
		echo "Copiando Isos"
		find $d -iname "*.iso" 
		find $d -iname "*.iso"  | xargs -i ls {} | xargs -i cp {} /media/soft/
		echo "Borrando Isos"
		find $d -iname "*.iso" | xargs -i rm {} 
	else
		echo "No hay Isos descargadas"
	
fi
sleep 5
