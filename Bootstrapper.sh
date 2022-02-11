if [[ $(whoami) = 'root' ]]; 
then
echo 'Dont run this with root'
exit
fi

distro=""

# Distro Detection
if [[ -f "/bin/emerge" ]];
then
$distro="gentoo"
elif [[ -f "/bin/apt" ]];
then
$distro="debian"
elif [[ -f "/bin/pacman" ]];
then
$distro="arch"
else
$distro="idk"
fi

if [[ $1 == "--help" ]];
then
echo 'Help:'
echo '--download-krnl-dll : Downloads KRNL.DLL'
echo '--grapejuice-install : Install grapejuice'
echo '--krnl-download : Installs KRNL but not anything more'
echo '-f : This was going to be called --run-download, the thing that this flag does is execute download.sh at the end of the installation'
echo '--install-tkg : Installs WINE TKG Binary (mouse patch)'
exit
elif [[ $1 == "--download-krnl-dll" ]];
then
wget -q https://k-storage.com/bootstrapper/files/krnl.dll -O $HOME/krnl.dll
exit
elif [[ $1 == "--krnl-download" ]];
then
# KRNL Download flag
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget -q https://k-storage.com/bootstrapper/files/krnl.dll -O $HOME/krnl.dll
wget -q $DOWNLOAD -O $HOME/krnl.exe
exit
elif [[ $1 == "--install-tkg" ]];
then
# Install WINE-TKG
cd /tmp
wget https://pastebin.com/raw/5SeVb005 -O install.py
python3 install.py
exit
fi
elif [[ $1 == "--grapejuice-install" ]];
then

if [[ $distro == "debian" ]];
then
# uvuntu insteletion
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl
curl https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg | sudo tee /usr/share/keyrings/grapejuice-archive-keyring.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/grapejuice.list <<< 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main' > /dev/null
sudo apt update -y
sudo apt install -y grapejuice
elif [[ $distro == "arch" ]];
then
# I use arch btw, installation
cd $HOME
sudo pacman -S base-devel
git clone https://aur.archlinux.org/grapejuice-git.git
cd grapejuice-git
makepkg -si
else
# Gentoo Installation
cd $HOME
git clone https://gitlab.com/brinkervii/grapejuice.git
cd grapejuice
python3 ./install.py
fi

fi

if [[ -f "${HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine" ]]; 
then
echo ' '
else
echo 'Wine TKG Binary 7.1.r2 not founded'
echo 'Install the newest mouse patch please, to do this is recommended to use the flag --install-tkg'
exit
fi

if [[ -d "${HOME}/KRNL" ]]; 
then
echo 'Delete ${HOME}/KRNL To continue'
exit
fi

echo '[+] Creating directories...'
cd $HOME
mkdir KRNL
cd KRNL
mkdir autoexec
mkdir linuxBIN
mkdir VERSION
mkdir workspace
echo '[+] Creating files...'
touch update.sh
touch run.sh
touch download.sh
echo '[+] Creating Internal Gui AutoExec...'
cd autoexec
touch 1.txt
echo '[:] Exporting KRNLALIAS...'
krnlalias="alias krnl='bash $HOME/KRNL/run.sh'"
echo '[+] Writing files...'
echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > 1.txt
cd ..
echo '
DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
echo "[#] Updating KRNL.DLL"
wget -q https://k-storage.com/bootstrapper/files/krnl.dll -O $HOME/KRNL/krnl.dll
echo "[#] Updating KRNL Console"
wget -q $DOWNLOAD -O $HOME/KRNL/linuxBIN/CLI 
' > update.sh
touch $HOME/KRNL/VERSION/VERSION_DOWNLOADER
touch $HOME/KRNL/VERSION/VERSION_PASTEBIN
echo '
export KRNL_VERSION="3.0"
export KRNL_VERSION_PASTEBIN="$(curl https://pastebin.com/raw/AQer6XDt)"
echo "[#] Downloading KRNL Console..."
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget -q $DOWNLOAD -O $HOME/KRNL/linuxBIN/CLI
echo "[:] Writing Extra Files..."
echo "${KRNL_VERSION}" > $HOME/KRNL/VERSIONS/VERSION_DOWNLOADER
echo "${KRNL_VERSION_PASTEBIN}" > $HOME/KRNL/VERSIONS/VERSION_PASTEBIN
echo "[#] Running Updater"
bash ./update.sh 
echo "KRNL Downloaded, Use RUN.SH to run it or you can use the command krnl"' > download.sh
if [ -f "$HOME/.local/share/grapejuice/prefixes/player" ]; 
then
echo 'echo "WARNING : If you have any error/question just call SimplyDeveloper"

export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/player"
export WINEPREFIX=$WINEPREFIXPATH
export WINEARCH="win64"
export WINEDEBUG="-all" 
export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
echo "[#] Executing Console..." 
$HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI

' > run.sh
else
echo '
if [[ -z "${WINEPREFIX}" ]]; then
echo "What is your PLAYER wineprefix name?"
read PREFIX
fi
echo "WARNING : If you have any error/question just call SimplyDeveloper"
export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
export WINEPREFIX=$WINEPREFIXPATH 
export WINEARCH="win64" 
export WINEDEBUG="-all" 
export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
echo "[#] Executing Console..." 
$HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI
 ' > run.sh
fi
echo 'Writing Extra Files'
cd ..
echo 'Execute ${HOME}/KRNL/download.sh to download the other stuff then use ${HOME}/KRNL/run.sh to run it or execute "krnl"'
echo 'Have any problems? Go to https://github.com/SimpIyDeveIoper/KRNL_Linux and read README.md'
cd $HOME/KRNL
echo "alias krnl='bash $HOME/KRNL/run.sh'" >> $HOME/.bashrc
alias krnl='bash $HOME/KRNL/run.sh'
# Im making it just better, it already works
