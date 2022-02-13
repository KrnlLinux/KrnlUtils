if [[ "$(whoami)" = 'root' ]];
then
cd /bin 
wget https://raw.githubusercontent.com/SimpIyDeveIoper/KrnlUtils/main/KrnlUtils.py -O krnlutils > /dev/null 
echo '#!$(which python3)' >> krnlutils
else
echo 'This script must be runned with root'
fi
