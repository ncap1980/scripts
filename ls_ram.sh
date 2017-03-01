#!/bin/bash

TVACAS=('ls /var/share/cows/*.cow')
NUMVACAS=$(#TVACAS[*])
NVACA=$((RAMDOM%NUMVACAS))
VACA=${TVACAS[%NVACAS]}
