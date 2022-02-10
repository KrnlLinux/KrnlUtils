cd $HOME
mkdir KRNL
cd KRNL
mkdir autoexec
mkdir linuxBIN
mkdir VERSION
mkdir workspace
touch update.sh
touch run.sh
touch download.sh
cd autoexec
touch 1.txt
echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > 1.txt
cd ..
echo "echo 'UPDATE.SH > Downloading KRNL.DLL' && wget https://k-storage.com/bootstrapper/files/krnl.dll -O krnl.dll" > update.sh
echo "echo 'If you have a problem that u cant execute KRNL, you probably need to start linuxBin/CLI via grapejuice's taskmgr' && echo 'If you dont know how to update it just run update.sh' && echo 'If it attaches but it doesnt make anything make sure the internal gui in AUTOEXEC works and u have it, too the internal gui is opened with Insert'" > troubleshooting.sh
echo '
echo "Exporting KRNL_VERSION..."
export KRNL_VERSION="2.0"
echo "Exporting KRNL_VERSION_PASTEBIN..."
export KRNL_VERSION_PASTEBIN="$(curl https://pastebin.com/raw/AQer6XDt)"
echo "Downloading Console (KRNL)..."
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget  $DOWNLOAD -O ./linuxBIN/CLI > ./linuxBIN/wgetlogs.log 
echo "Logging Versions..."
echo "${KRNL_VERSION}" > $HOME/KRNL/VERSIONS/VERSION_DOWNLOADER
echo "${KRNL_VERSION_PASTEBIN}" > $HOME/KRNL/VERSIONS/VERSION_PASTEBIN
echo "Running UPDATE.SH"
bash ./update.sh 
echo "KRNL Downloaded, Use RUN.SH to run it"' > download.sh
echo 'echo "What is your PLAYER wineprefix name? (To make it dont question everytime you execute it delete the first two lines and put your wineprefix name in WINEPREFIXPATH)"
echo "WARNING : If you have any error/question just call SimplyDeveloper"
read PREFIX

export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
echo "Exporting WINEPREFIX..." && export WINEPREFIX=$WINEPREFIXPATH && echo "Exporting WINEARCH..." && export WINEARCH="win64" && echo "Exporting WINEDEBUG" && export WINEDEBUG="-all" && echo "Exporting WINEDLLOVERRIDES" && export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" && echo "Resolving WINE-TKG Binary path..." && echo "Executing Console..." && $HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI
 ' > run.sh
 cd VERSION
 touch VERSION_DOWNLOADER
 touch VERSION_PASTEBIN
 cd ..
echo 'Execute $HOME/KRNL/DOWNLOAD.SH to download the other parts, then use $HOME/KRNL/RUN.SH to run it'
echo 'If there is an update just run update.sh it will install automatically KRNL.DLL'
echo 'Too to delete it execute "rm -R $HOME/KRNL"'
echo 'Have any problems? Execute troubleshooting.sh'
cd $HOME/KRNL

