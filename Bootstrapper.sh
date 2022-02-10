if [ -f "${HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine" ]; then
echo 'Wine TKG Binary 7.1.r2 not founded'
echo 'Install the newest mouse patch please'
exit
fi
if [ -f "${HOME}/KRNL" ]; then
echo 'Delete ${HOME}/KRNL To continue'
exit
fi
if [ $(whoami) = 'root' ] then
echo 'Dont run this with root'
exit
fi
echo 'Creating directories...'
cd $HOME
mkdir KRNL
cd KRNL
mkdir autoexec
mkdir linuxBIN
mkdir VERSION
mkdir workspace
echo 'Creating files...'
touch update.sh
touch run.sh
touch download.sh
echo 'Creating AUTOEXEC files...'
cd autoexec
touch 1.txt
echo 'Exporting KRNLALIAS...'
krnlalias="alias krnl='bash $HOME/KRNL/run.sh'"
echo 'Writing files...'
echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > 1.txt
cd ..
echo "echo 'UPDATE.SH > Downloading KRNL.DLL' && wget https://k-storage.com/bootstrapper/files/krnl.dll -O krnl.dll > ./linuxBIN/updaterLogs" > update.sh
echo "echo 'If you have a problem that u cant execute KRNL, you probably need to start linuxBin/CLI via grapejuice taskmgr'
echo 'If you dont know how to update it just run update.sh'
echo 'If it attaches but it doesnt make anything make sure the internal gui in AUTOEXEC works and u have it, too the internal gui is opened with Insert'" > troubleshooting.sh
echo '
echo "Exporting KRNL_VERSION..."
export KRNL_VERSION="3.0"
echo "Exporting KRNL_VERSION_PASTEBIN..."
export KRNL_VERSION_PASTEBIN="$(curl https://pastebin.com/raw/AQer6XDt)"
echo "Downloading Console (KRNL)..."
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget  $DOWNLOAD -O ./linuxBIN/CLI > ./linuxBIN/krnlDownload.log 
echo "Writing VERSION..."
echo "${KRNL_VERSION}" > $HOME/KRNL/VERSIONS/VERSION_DOWNLOADER
echo "${KRNL_VERSION_PASTEBIN}" > $HOME/KRNL/VERSIONS/VERSION_PASTEBIN
echo "Running UPDATE.SH"
bash ./update.sh 
echo "${krnlalias}" >> $HOME/.bashrc
alias krnl="bash $HOME/KRNL/run.sh"
echo "KRNL Downloaded, Use RUN.SH to run it or you can use the command krnl"' > download.sh
if [ -f "$HOME/.local/share/grapejuice/prefixes/player" ]; 
then
echo 'echo "WARNING : If you have any error/question just call SimplyDeveloper"

export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/player"
echo "Exporting WINEPREFIX..."
export WINEPREFIX=$WINEPREFIXPATH
echo "Exporting WINEARCH..."
export WINEARCH="win64"
echo "Exporting WINEDEBUG" 
export WINEDEBUG="-all" 
echo "Exporting WINEDLLOVERRIDES" 
export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
echo "Resolving WINE-TKG Binary path..." 
echo "Executing Console..." 
$HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI

 ' > run.sh
else
 echo '
 if [[ -z "${WINEPREFIX}" ]]; then
 echo "What is your PLAYER wineprefix name?"
read WINEPREFIX
fi
echo "export WINEPREFIX=${WINEPREFIX}" >> $HOME/.bashrc
echo "WARNING : If you have any error/question just call SimplyDeveloper"
export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
echo "Exporting WINEPREFIX..."
export WINEPREFIX=$WINEPREFIXPATH 
echo "Exporting WINEARCH..." 
export WINEARCH="win64" 
echo "Exporting WINEDEBUG" 
export WINEDEBUG="-all" 
echo "Exporting WINEDLLOVERRIDES" 
export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
echo "Resolving WINE-TKG Binary path..." 
echo "Executing Console..." 
$HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI
 ' > run.sh
fi
echo 'Writing VERSION...'
cd VERSION
touch VERSION_DOWNLOADER
touch VERSION_PASTEBIN
cd ..
echo 'Execute ${$HOME}/KRNL/download.sh to download the other parts, then use ${$HOME}/KRNL/run.sh to run it or execute "krnl"'
echo 'If there is an update just run update.sh it will install automatically KRNL.DLL'
echo 'To delete KRNL execute "rm -R $HOME/KRNL"'
echo 'Have any problems? Execute troubleshooting.sh'
cd $HOME/KRNL
