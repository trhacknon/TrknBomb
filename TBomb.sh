#!/bin/bash
clear
echo -e "\e[4;31m trhacknon Productions !!! \e[0m"
echo -e "\e[1;34m Presents \e[0m"
echo -e "\e[1;32m TBomb \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.speedx ]];then
echo "All Requirements Found...."
else
apt update
apt upgrade
apt install figlet toilet python -y
pip install urllib3
echo This Script Was Made By trhacknon >update.trhacknon
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
clear
echo -e "\e[1;31m"
figlet TBomb
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border trhacknon
echo -e "\e[4;34m This Bomber Was Modded By trhacknon \e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: jeremydilliotti@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.do/ \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/ \e[0m"
echo " "
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
echo " "
echo "Press 1 to Start Bombing "
echo "Press 2 For Instructions "
echo "Press 3 to Update (Works On Linux) "
echo "Press 4 to Exit "
read ch
if [ $ch -eq 1 ];then
clear
python bomber.py
echo -e "\e[1;32m"
figlet TBomb
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border trhacknon
echo  " "
echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"
echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"
echo -e "\e[1;32m Make Sure To Update it If It Does not Work.\e[0m"
echo  " "
echo -e "\e[4;31m That's All !!!\e[0m"
echo -e "\e[4;34m This Bomber Was Created By trhacknon\e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: jeremydilliotti@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.do/ \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/ \e[0m"
exit 0
elif [ $ch -eq 2 ];then
clear
echo -e "\e[1;33m"
figlet TBomb
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border trhacknon
echo  " "
echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"
echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"
echo -e "\e[1;32m Make Sure To Update it If It Does not Work.\e[0m"
echo  " "
echo -e "\e[4;31m That's All !!!\e[0m"
echo -e "\e[4;34m This Bomber Was Created By trhacknon\e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: jeremydilliotti@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.do/ \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/ \e[0m"
echo "Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 3 ];then
clear
apt install git -y
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/trhacknon/TrknBomb
if [[ -s TrknBomb/TBomb.sh ]];then
cd TrknBomb
cp -r -f * .. > temp
cd ..
rm -rf  TrknBomb >> temp
rm update.trhacknon >> temp
rm temp
chmod +x TBomb.sh
fi
echo -e "\e[1;32m TBomb Will Restart Now..."
echo -e "\e[1;32m All The Required Packages Will Be Installed..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
./TBomb.sh
exit
elif [ $ch -eq 4 ];then

clear
echo -e "\e[1;31m"
figlet TBomb
echo -e "\e[1;34m Created By \e[0m"
toilet -f mono12 -F border trhacknon
echo -e "\e[4;34m This Bomber Was Created By trhacknon \e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: jeremydilliotti@gmail.com \e[0m"
echo -e "\e[1;32m       Whatsapp: https://bit.do/ \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/ \e[0m"
echo " "

exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
