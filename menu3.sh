

Executing:


$ ./menu.sh

R U N M E N U

1. Regression Tests
2. Smoke Tests
3. Quit

Your choice? :


________
Way2:
________

The other way of making a continuous menu is to have a variable set to "no", and exit the menu when the value is "yes" (set the value to "yes" for the quit option in the menu like below):


#!/bin/sh

quit="no"

f_Reg () {
echo "Regression function"
echo "All your logic in this function"
}

f_Smoke () {
echo "Smoke function"
echo "All your logic in this function"
}

while [ $quit != "yes" ]
do
echo "1. Regression Tests"
echo "2. Smoke Tests"
echo "3. Quit"
echo -n "Your choice? : "
read choice

case $choice in
1) f_Reg ;;
2) f_Smoke ;;
3) quit="yes" ;;
*) echo "\"$choice\" is not valid"
sleep 2 ;;
esac
done
