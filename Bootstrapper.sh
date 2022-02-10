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
echo "echo 'UPDATE.SH > Downloading KRNL.DLL' && sleep 2 && wget https://k-storage.com/bootstrapper/files/krnl.dll -O krnl.dll" > update.sh
echo "echo 'If you have a problem that u cant execute KRNL, you probably need to start linuxBin/CLI via grapejuice's taskmgr' && echo 'If you dont know how to update it just run update.sh' && echo 'If it attaches but it doesnt make anything make sure the internal gui in AUTOEXEC works and u have it, too the internal gui is opened with Insert'" > troubleshooting.sh
echo '
echo "Exporting KRNL_VERSION..."
sleep 1
export KRNL_VERSION="1.0"
echo "Exporting KRNL_VERSION_PASTEBIN..."
sleep 1
export KRNL_VERSION_PASTEBIN="$(curl https://pastebin.com/raw/AQer6XDt)"
echo "Downloading Console (KRNL)..."
sleep 1
export DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
wget  $DOWNLOAD -O ./linuxBIN/CLI > ./linuxBIN/wgetlogs.log 
echo "Logging Versions..."
sleep 1
cat ./VERSION/VERSION_DOWNLOADER > $KRNL_VERSION
cat ./VERSION/VERSION_PASTEBIN > $KRNL_VERSION_PASTEBIN 
echo "Running UPDATE.SH"
bash ./update.sh 
echo "KRNL Downloaded, Use RUN.SH to run it"' > download.sh
echo 'echo "What is your PLAYER wineprefix name? (To make it dont question everytime you execute it delete the first two lines and put your wineprefix name in WINEPREFIXPATH)"
echo "WARNING : If you have any error/question just call SimplyDeveloper"
read PREFIX

export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
echo "Exporting WINEPREFIX..." && sleep 1 && export WINEPREFIX=$WINEPREFIXPATH && echo "Exporting WINEARCH..." && sleep 1 && export WINEARCH="win64" && echo "Exporting WINEDEBUG" && sleep
 1 && export WINEDEBUG="-all" && echo "Exporting WINEDLLOVERRIDES" && sleep 1 && export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" && echo "Resolving WINE-TKG Binary path..." && sleep 1 && echo "Executing Console..." && $HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/linuxBIN/CLI
 ' > run.sh
 cd VERSION
 touch VERSION_DOWNLOADER
 touch VERSION_PASTEBIN
 cd ..
echo 'Execute DOWNLOAD.SH to download the other parts, then use RUN.SH to run it'
echo 'If there is an update just run update.sh it will install automatically KRNL.DLL'
echo 'Too to delete it execute "rm -R $HOME/KRNL"'
echo 'Have any problems? Execute troubleshooting.sh'
