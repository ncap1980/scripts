#!/bin/bash
#Script de Administración de Linux.
zenity
#Comprobamos que el usuario es root.
if [ $(whoami) != "root" ]; then
    echo "Debes ser root para correr este script."
sleep 5
    echo "Para entrar como root, escribe \"sudo su\" sin las comillas."
    exit 1
fi

#Presentación.
echo
echo "Script de Administración de Linux Ubuntu v. 0.1"
echo "------ -- -------------- -- ----- ------ -- ---"
echo

#Menu de Administración
while [ "$opcion" != "0" ]
do
    #Mostramos el menú
    echo
    echo "Menú"
    echo "----"
    echo "    1. Crear un usuario."
    echo "    2. Cambiarle la contraseña a un usuario."
    echo "    3. Crear grupo."
    echo "    4. Añadir un usuario a un grupo."
    echo "    5. Ver datos de un usuario."
    echo "    6. Borrar un usuario."
    echo "    7. Borrar un grupo."
    echo "    0. Salir."
    echo
    echo -n "     Elige una opción: "
    read opcion

    case $opcion in
        1 )
            echo
            echo -n "    Dame el nombre del usuario a crear: "
            read nombre
            echo
            adduser $nombre
            echo
            ;;
        2 )
            echo
            echo -n "    Dame el nombre del usuario a cuya contraseña quieres cambiar: "
            read nombre
            echo
            passwd $nombre
            echo
            ;;
        3 )
            echo
            echo -n "    Dame el nombre del grupo: "
            read grupo
            echo
            addgroup $grupo
            echo
            ;;
        4 )
            echo
            echo -n "    Dame el nombre del usuario: "
            read nombre
            echo -n "    Dame el nombre del grupo: "
            read grupo
            echo
            addgroup $nombre $grupo
            echo
            ;;
        5 )
            echo
            echo -n "    Dame el nombre del usuario: "
            read nombre
            echo
            id $nombre
            echo
            ;;
        6 )
            echo
            echo -n "    Dame el nombre del usuario: "
            read nombre
            echo
            deluser $nombre
            echo
            ;;
        7 )
            echo -n "    Dame el nombre del grupo: "
            read grupo
            echo
            delgroup $grupo
            echo
            ;;
    esac
done

echo
echo "    Hasta Pronto!"
echo "    ----- -------"
echo
exit 0

