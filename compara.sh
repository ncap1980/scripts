result=`diff -sq a.txt crl/a.txt`

cadena='Los ficheros a.txt y crl/a.txt son idénticos'

if [[ "$result" == "$cadena" ]];
then
        echo 'Los archivos son identicos, no se hara nada'
else
        echo 'Los archivos son diferentes, se copiara el archivo'
        cp a.txt crl/a.txt
fi