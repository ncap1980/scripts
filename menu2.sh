#!/bin/sh

f_Reg () {
echo "Regression function"
echo "All your logic in this function"
}

f_Smoke () {
echo "Smoke function"
echo "All your logic in this function"
}

while : # Loop forever
do
cat << !

R U N M E N U

1. Regression Tests
2. Smoke Tests
3. Quit

!

echo -n " Your choice? : "
read choice

case $choice in
1) f_Reg ;;
2) f_Smoke ;;
3) exit ;;
*) echo "\"$choice\" is not valid "; sleep 2 ;;
esac
done

