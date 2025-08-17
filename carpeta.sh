#!/bin/bash -x

#source clasificar_trazas.sh
declare -A listado
pwd

folder=`ls -1d */ | egrep '20[0-9][0-9]_[0-9][0-9]_part'`

files=`ls $folder*.csv`

for i in $files:
do
        echo $i
        listado[dirname $i]='`basename $i`'
done
#mv 2022_02_01/ 2022_02_01_`date +%d%m%Y%H%M%S`#

for i in $listado:
do
        echo $listado[]
done
