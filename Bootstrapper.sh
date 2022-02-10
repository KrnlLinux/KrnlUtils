if [[ -f "${HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine" ]]; 
then
echo ' '
else
echo 'Wine TKG Binary 7.1.r2 not founded'
echo 'Install the newest mouse patch please'
exit
fi

if [[ -d "${HOME}/KRNL" ]]; 
then
echo 'Delete ${HOME}/KRNL To continue'
exit
fi

if [[ $(whoami) = 'root' ]]; 
then
echo 'Dont run this with root'
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
wget https://k-storage.com/bootstrapper/files/krnl.dll -O krnl.dll > ./linuxBIN/updaterLogs
echo "[#] Updating KRNL Console"
wget $DOWNLOAD -O $HOME/KRNL/linuxBIN/CLI > $HOME/KRNL/linuxBIN/krnlDownload.log 
' > update.sh
echo '
export KRNL_VERSION="3.0"
export KRNL_VERSION_PASTEBIN="$(curl https://pastebin.com/raw/AQer6XDt)"
echo "[#] Downloading KRNL Console..."
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget  $DOWNLOAD -O ./linuxBIN/CLI > $HOME/KRNL/linuxBIN/krnlDownload.log 
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
cd VERSION
touch VERSION_DOWNLOADER
touch VERSION_PASTEBIN
cd ..
echo 'Execute ${HOME}/KRNL/download.sh to download the other stuff then use ${HOME}/KRNL/run.sh to run it or execute "krnl"'
echo 'Have any problems? Go to https://github.com/SimpIyDeveIoper/KRNL_Linux and read README.md'
cd $HOME/KRNL
echo "alias krnl='bash $HOME/KRNL/run.sh'" >> $HOME/.bashrc
alias krnl='bash $HOME/KRNL/run.sh'
