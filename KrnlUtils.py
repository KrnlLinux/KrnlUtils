import os
import getpass
import sys
import re
import urllib.request
try:
    import requests
except ModuleNotFoundError:
    os.system("pip3 install --user requests")
import requests
import subprocess
from os.path import exists
gentoo = exists("/usr/bin/emerge")
debian = exists("/usr/bin/apt")
arch = exists("/usr/bin/pacman")
windows = exists("C:/Windows")
flagexecuted = False
forloopc = 0
def curl(link):
    return urllib.request.urlopen(link).read()
def wget(link,path):
    r = requests.get(link, allow_redirects=True)
    open(path,'wb').write(r.content)
def remove(path,sudo,isdir):
    if isdir == "":
        isdir = False
    if sudo == "":
        sudo = False
    if sudo == False and isdir == False:
        return os.popen(f"rm {path}").read()
    if sudo and isdir == False:
        return os.popen(f"sudo rm {path}").read()
    if sudo == False and isdir:
        return os.popen(f"rm -R {path}").read()
    if sudo and isdir:
        return os.popen(f"sudo rm -R {path}").read()
def copy(path,path2,sudo,isdir):
    if isdir == "":
        isdir = False
    if sudo == "":
        sudo = False
    if sudo == False and isdir == False:
        return os.popen(f"cp {path} {path2}").read()
    if sudo and isdir == False:
        return os.popen(f"sudo cp {path} {path2}").read()
    if sudo == False and isdir:
        return os.popen(f"cp -R {path} {path2}").read()
    if sudo and isdir:
        return os.popen(f"sudo cp -R {path} {path2}").read()


def GetDistro():
    if gentoo == True:
        return "gentoo"
    if debian == True:
        return "debian"
    if arch == True:
        return "arch"
    if windows == True:
        return "windows"
    if arch == False and gentoo == False and debian == False:
        return "idk"
distro = GetDistro()
try:
    import colorama
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    os.system("pip3 install --user colorama")
import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)
if getpass.getuser() == "root":
    print("Do not run this with root")

    sys.exit()

quiet = False
def Error(text):
    print(f"{Fore.RED} [!] {Fore.WHITE}Error : " + text)
def Info(text):
    print(f"{Fore.BLUE} [¡] {Fore.WHITE} " + text)
def Warning(text):
    print(f"{Fore.YELLOW} [;] {Fore.WHITE}Warning : " + text)
def Process(text):
    print(f"{Fore.MAGENTA} [#] {Fore.WHITE} " + text)
def DEBUG(text):
    if quiet == True:
        return "Quiet Mode"
    print(f"{Fore.GREEN} [DEBUG] {Fore.WHITE} " + text)
def Question(text):
    sus = input(f"{Fore.LIGHTMAGENTA_EX} [:] {Fore.WHITE} " + text)
    return sus
def Help():
    print(f"{Fore.WHITE}Main : ")
    print("    --help (-h) : Displays this list")
    print("    --quiet : Disables any DEBUG message\n")
    print(f"{Fore.MAGENTA}Grapejuice (Linux) : ")
    print("    --grapejuice-install (-gi) : Installs grapejuice using the wiki")
    print("    --install-tkg (-tkg) : Installs the patched mouse wine for grapejuice\n")
    print(f"{Fore.CYAN}Linux KRNL : ")
    print("    --linux-install-krnl (-lik) : Installs KRNL")
    print("    --linux-delete-krnl (-ldk) : Removes KRNL")
    print("    --linux-download-autoexec (-lda) : Downloads the internal gui")
    print("    --linux-add-krnl-path (-lakp) : Adds KRNL to path so that you can execute it using the command krnl")
    print("    --linux-set-prefix [ARG] (-lsp) : Set the variable PREFIX everytime you use a console (People that installed KRNL will understand what this does)")
    print("    --linux-delete-krnl-path (-ldkp) : Unlinks /bin/krnl if it exists")
    print("    --linux-beta-gui-build-install (-lbgbi) : Instead of using the console uses a GUI (TODO)")
    print("    --linux-update-krnl (-luk) : Updates KRNL\n")
    print(f"{Fore.CYAN}MacOS KRNL : ")
    print("    Soon\n")
    print(f"{Fore.CYAN}Windows : ")
    print("    Soon\n")
    print(f"{Fore.CYAN}About Messages :")
    print(f"    {Fore.RED}[!]{Fore.WHITE} : Error")
    print(f"    {Fore.BLUE}[¡]{Fore.WHITE} : Info")
    print(f"    {Fore.YELLOW}[;]{Fore.WHITE} : Warning")
    print(f"    {Fore.MAGENTA}[#]{Fore.WHITE} : Process/Downloading/Loading")
    print(f"    {Fore.LIGHTMAGENTA_EX}[:]{Fore.WHITE} : Question")
    print(f"    {Fore.GREEN}[DEBUG]{Fore.WHITE} : Debug Messages (Disable with --quiet)")

def GrapejuiceInstall():
    if distro == "debian":
        DEBUG("/usr/bin/apt Exists running debian installation for grapejuice")
        Process("Installing Debian Grapejuice")
        DEBUG("Updating & Upgrading (apt update, apt upgrade)")
        os.system("""
            sudo apt update > /dev/null
            sudo apt upgrade -y > /dev/null""")
        DEBUG("Installing Curl (apt install curl)")
        os.system(""""
            sudo apt install -y curl > /dev/null""")
        DEBUG("Downloading the keyrings (curl CONTENT_TOO_LONG | tee CONTENT_TOO_LONG)")
        os.system("""
            curl https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg | sudo tee /usr/share/keyrings/grapejuice-archive-keyring.gpg > /dev/null
            sudo tee /etc/apt/sources.list.d/grapejuice.list <<< 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main' > /dev/null
            """)
        DEBUG("Updating and installing grapejuice (apt update, apt install grapejuice)")
        os.system("""
            sudo apt update > /dev/null
            sudo apt install -y grapejuice > /dev/null
        """)
        Info("Done")
    elif distro == "arch":
        DEBUG("/usr/bin/pacman Exists running arch installation for grapejuice")
        Process("Instaling Arch Grapejuice")
        DEBUG("Installing base-devel (pacman -S base-devel)")
        os.system("""
        sudo pacman -S base-devel""")
        DEBUG("Cloning grapejuice repository (git clone https://aur.archlinux.org/grapejuice-git.git)")
        os.system("""
        cd $HOME
        git clone https://aur.archlinux.org/grapejuice-git.git
        cd grapejuice-git""")
        DEBUG("Installing AUR Package (makepkg -si)")
        os.system("""
        makepkg -si
        """)
        Info("Done")
    else:
        DEBUG("Gentoo/Unknown Distro Detected, printing source code message")
        print("We cant detect your current distro, to install grapejuice is recommended doing it from source")
        print("Grapejuice Source Code : https://gitlab.com/brinkervii/grapejuice")

HOME = f"/home/{getpass.getuser()}"
KrnlInstalled =exists(f"{HOME}/KRNL")
RunInstalled = exists(f"{HOME}/KRNL/krnl")
TkgInstalled=exists(f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine")
LinkInstalled=exists("/bin/krnl")
KrnlPath=f"{HOME}/KRNL"
RunPath=f"{KrnlPath}/krnl"
TkgPath=f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine"
LinkPath=f"/bin/krnl"
if __name__ == '__main__':
    for argument in sys.argv:
        def GetFlag(text):
            if argument == text:
                if windows:
                    print("Dont try to do that again, it will probably give massive errors because your using windows")
                    sys.exit()
                flagexecuted = True
                return True
            else:
                return False
        if GetFlag("--quiet"):
            quiet = True
        
        if GetFlag("--help") or GetFlag("-h"):
            flagexecuted = True
            Help()
            sys.exit()
        elif GetFlag("--linux-set-prefix") or GetFlag("-lsp"):
            if RunInstalled:
                try:
                    lol = sys.argv[2]
                    os.system(f"""
                    echo 'export PREFIX="{sys.argv[2]}"' > $HOME/.bashrc
                    """)
                    DEBUG(f"Added to .bashrc export PREFIX='{sys.argv[2]}'")
                    Info("Done")
                except:
                    Error("No argument given")
            else:
                Error("KRNL Is not installed")
        elif GetFlag("--linux-add-krnl-path") or GetFlag("-lakp"):
            if RunInstalled:
                if not LinkInstalled:
                    os.system(f"""
                    cd /bin
                    sudo ln -s {RunPath} krnl
                    """)
                    DEBUG(f"Linked {HOME}/KRNL/krnl to /bin/krnl (ln -s {HOME}/KRNL/krnl /bin/krnl)")
                    Info("Done")
                else:
                    Error("Krnl already linked")
            else:
                Error("Krnl is not installed")
        elif GetFlag("--linux-delete-krnl-path") or GetFlag("-ldkp"):
            if LinkInstalled:
                os.system(f"sudo unlink {LinkPath}")
                DEBUG("Unlinked /bin/krnl (unlink /bin/krnl)")
                Info("Done")
            else:
                Error("Krnl is not linked")
                DEBUG("exists(/bin/krnl) False")
        elif GetFlag("--grapejuice-install") or GetFlag("-gi"):
            flagexecuted = True
            GrapejuiceInstall()
        elif GetFlag("--linux-delete-krnl") or GetFlag("-ldk"):
            flagexecuted = True
            if KrnlInstalled:
                os.system(f"""
                rm -R {KrnlPath}
                """)
                Info("Done")
            else:
                Error("Krnl is not installed")
        elif GetFlag("--install-tkg") or GetFlag("-tkg"):
            flagexecuted = True
            if not TkgInstalled:
                DEBUG("Function wget, Content https://pastebin.com/raw/5SeVb005, File /tmp/install.py")
                Info("Downloading TKG")
                wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                os.system("python3 /tmp/install.py > /dev/null")
                Info("Sucessfully downloaded TKG")
            else:
                TKGQuestion= Question("TKG Is already installed, do you want to delete it and continue? (Y/N) : ")
                if re.search("Y",TKGQuestion):
                    os.system(f"rm -R {TkgPath}")
                    DEBUG("Downloading & running install.py (wget https://pastebin.com/raw/5SeVb005 -O install.py, python3 install.py > /dev/null)")
                    Info("Downloading TKG")
                    os.system("""
                    cd /tmp
                    wget https://pastebin.com/raw/5SeVb005 -O install.py > /dev/null
                    python3 install.py > /dev/null
                    """)
                    Info("Sucessfully downloaded TKG")
                else:
                    Info("Okay, TKG Will not be deleted or installed")
        elif GetFlag("--linux-install-krnl") or GetFlag("-lik"):
            flagexecuted = True
            if exists(f"{HOME}/KRNL"):
                Warning("This will delete every file inside of krnl but autoexec and workspace will be copied into TMP if they exist")
                DeleteQuestion = Question("Krnl is already installed, do u want to delete it? (Y/N) : ")
                if re.search("Y",DeleteQuestion) == True:
                    if exists(f"{HOME}/KRNL/autoexec"):
                        if exists("/tmp/autoexec"):
                            os.system("""
                            rm -R /tmp/autoexec
                            """)
                        os.system("""
                        cp -R $HOME/KRNL/autoexec /tmp
                        """)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            os.system("""
                            rm -R /tmp/workspace
                            """)
                        os.system("""
                        cp -R $HOME/KRNL/workspace /tmp
                        """)
                    os.system("""
                    rm -R $HOME/KRNL
                    """)
                elif re.search("N",DeleteQuestion) == True:
                    print("")
                else:
                    if exists(f"{HOME}/KRNL/autoexec"):
                        if exists("/tmp/autoexec"):
                            os.system("""
                            rm -R /tmp/autoexec
                            """)
                        os.system("""
                        cp -R $HOME/KRNL/autoexec /tmp
                        """)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            os.system("""
                            rm -R /tmp/workspace
                            """)
                        os.system("""
                        cp -R $HOME/KRNL/workspace /tmp
                        """)
                    os.system("""
                    rm -R $HOME/KRNL
                    """)
            if TkgInstalled == False:
                TKGQuestion = Question("The wine mouse patch is not installed and this is necessary to run Krnl. Do u want to install this? (Y/N) : ")
                if re.search("Y",TKGQuestion) == True:
                    Info("Installing TKG")
                    DEBUG("Downloading install.py and executing it (wget CONTENT_TOO_LONG, python3 install.py > /dev/null)")
                    os.system("""
                        cd /tmp
                        wget https://pastebin.com/raw/5SeVb005 -O install.py > /dev/null
                        python3 install.py > /dev/null
                    """)
                elif re.search("N",TKGQuestion) == True:
                    print("")
                else:
                    Info("Installing TKG")
                    DEBUG("Downloading install.py and executing it (wget CONTENT_TOO_LONG, python3 install.py > /dev/null)")
                    os.system("""
                        cd /tmp
                        wget https://pastebin.com/raw/5SeVb005 -O install.py > /dev/null
                        python3 install.py > /dev/null
                    """)
            DEBUG("Making KRNL Directory (mkdir KRNL)")
            Info("Making Files")
            os.system("""
            cd $HOME
            mkdir KRNL
            cd KRNL""")
            DEBUG("Making autoexec,workspace,bin Directories (mkdir autoexec, mkdir workspace, mkdir bin)")
            os.system("""""
            cd $HOME/KRNL
            mkdir autoexec
            mkdir workspace
            mkdir bin""")
            DEBUG("Making run.sh (krnl) (touch krnl, chmod +x krnl, echo CONTENT_TOO_LONG > krnl)")
            os.system("""
            cd $HOME/KRNL
            touch krnl
            chmod +x krnl
            echo '
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            echo 'To make KRNL not ask this everytime you execute it, add to your bashrc export PREFIX="WINEPREFIX_NAME"'
            read PREFIX
            fi
            echo "WARNING : If you have any error/question just call SimplyDeveloper"
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Executing Console..." 
            $HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/bin/CLI
            ' > krnl""")
            DEBUG(f"Downloading InternalGui & krnl.dll & CLI (touch autoexec/InternalGui.txt, wget CONTENT_TOO_LONG KRNL/krnl.dll, wget CONTENT_TOO_LONG KRNL/bin/CLI")
            Info("Downloading Dependencies")
            os.system("""
            cd $HOME/KRNL
            cd autoexec
            touch InternalGui.txt
            echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > InternalGui.txt
            cd $HOME/KRNL
            DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
            wget https://k-storage.com/bootstrapper/files/krnl.dll -O $HOME/KRNL/krnl.dll > /dev/null
            wget $DOWNLOAD -O $HOME/KRNL/bin/CLI > /dev/null
            """)
            Info("KRNL Sucessfully downloaded")
        elif GetFlag("--linux-download-autoexec") or GetFlag("-lda"):
            flagexecuted = True
            if exists(f"{HOME}/KRNL")():
                if exists(f"/home/{getpass.getuser()}/KRNL/autoexec/1.txt")():
                    DEBUG(f"Downloading InternalGui (echo CONTENT_TOO_LONG > InternalGui.txt)")
                    os.system("""
                    cd $HOME/KRNL
                    cd autoexec
                    echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > InternalGui.txt
                    cd $HOME/KRNL
                    """)
                else:
                    DEBUG(f"Downloading InternalGui (touch InternalGui.txt, echo CONTENT_TOO_LONG > InternalGui.txt)")
                    os.system("""
                    cd $HOME/KRNL
                    cd autoexec
                    touch InternalGui.txt
                    echo "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()" > InternalGui.txt
                    cd $HOME/KRNL
                    """)
                Info("Done")
                DEBUG("Writing Ended")
            else:
                DEBUG(f"exists({HOME}/KRNL) False")
                Error("Krnl not installed")
        elif GetFlag("--linux-update-krnl") or GetFlag("-luk"):
            flagexecuted = True
            print(f"{Fore.GREEN} [+] {Fore.WHITE}Downloading Dependencies")
            if exists(f"{HOME}/KRNL/") == True:
                os.system("""
                DOWNLOAD="$(curl https://pastebin.com/raw/gcH1DTED)"
                wget -q https://k-storage.com/bootstrapper/files/krnl.dll -O $HOME/KRNL/krnl.dll > /dev/null
                wget -q $DOWNLOAD -O $HOME/KRNL/bin/CLI > /dev/null
                """)
                Info("Sucesfully updated krnl")
            else:
                DEBUG(f"exists({HOME}/KRNL) False")
                Error("Krnl is not downloaded")
        else:
            if flagexecuted == False:
                try:
                    lol = sys.argv[1]
                except:
                    Help()
