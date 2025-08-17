#!/bin/bash

echo ¿Que diretorio quieres ver?
read dir
if [ -d $dir ]
then 
	directorio=`ls $dir`
	for fichero in $directorio
	do
		if [ -d $dir/$fichero ]
		then
			echo $fichero
		fi
	done
else 
	echo Ese diretorio no es valido
fi

