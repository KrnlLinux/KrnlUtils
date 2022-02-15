true = True
false = False
nil = None
null = None

import os
import getpass
try:
    from gi.repository import Gtk
except ModuleNotFoundError:
    print("Fatal error installing gi.repository to use gtk")
    sys.exit()
from gi.repository import Gtk
try:
    import git
    from git import repo
except ModuleNotFoundError:
    os.system("pip3 install --user gitpython")
import git
from git import Repo

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

HOME = f"/home/{getpass.getuser()}"
KrnlInstalled =exists(f"{HOME}/KRNL")
RunInstalled = exists(f"{HOME}/KRNL/krnl")
TkgInstalled=exists(f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.2.r0.g68441b1d/bin/wine")
LinkInstalled=exists("/bin/krnl")
KrnlPath=f"{HOME}/KRNL"
RunPath=f"{KrnlPath}/krnl"
TkgPath=f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.2.r0.g68441b1d/bin/wine"
LinkPath=f"/bin/krnl"

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
    text = str(text)
    if not exists(f"{HOME}/.krnltmp"):
        mkdir(f"{HOME}/.krnltmp",False,True)
    if not exists(f"{HOME}/.krnltmp/.debuglogs"):
        mkfile(f"{HOME}/.krnltmp/.debuglogs","[DEBUG LOGS BEGIN]",True)
    bash(f"echo '{text}' >> {HOME}/.krnltmp/.debuglogs")
    if quiet == True:
        return "Quiet Mode"
    print(f"{Fore.GREEN} [DEBUG] {Fore.WHITE} " + text)
def Question(text):
    sus = input(f"{Fore.LIGHTMAGENTA_EX} [:] {Fore.WHITE} " + text)
    return sus


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
    DEBUG("Downloadf url."+link+" path."+path)
    open(path,'wb').write(r.content)
def mkfile(path,content,debugrunning=False):
    if exists(path) == False:
        bash(f"touch {path} > /dev/null")
    if debugrunning == False:
        DEBUG("Writef path."+path+" content."+content)
    with open(path, 'w') as f:
        f.write(content)
def mkdir(path,sudo=False,debugrunning=False):
    if sudo == None or sudo == "":
        sudo = False
    if debugrunning == False:
        DEBUG("Mkdirf path."+path+" sudo."+str(sudo))
    if sudo == True:
        return bash(f"sudo mkdir {path}",True,debugrunning)
    else:
        return bash(f"mkdir {path}",True,debugrunning)
def readfile(path):
    DEBUG("Readfilef path."+path)
    return bash(f"cat {path}")

def remove(path,sudo=False,isdir=False):
    if isdir == "":
        isdir = False
    if sudo == "":
        sudo = False
    DEBUG("Removef path."+path+" sudo."+str(sudo)+" isdir."+str(isdir))
    if sudo == False and isdir == False:
        return bash(f"rm {path}")
    if sudo and isdir == False:
        return bash(f"sudo rm {path}")
    if sudo == False and isdir:
        return bash(f"rm -R {path}")
    if sudo and isdir:
        return bash(f"sudo rm -R {path}")

def copy(path,path2,sudo= False,isdir= False):
    if isdir == "":
        isdir = False
    if sudo == "":
        sudo = False
    DEBUG("Copyf frompath."+path+" topath."+path2+" sudo."+str(sudo)+" isdir."+str(isdir))
    if sudo == False and isdir == False:
        return bash(f"cp {path} {path2}")
    if sudo and isdir == False:
        return bash(f"sudo cp {path} {path2}")
    if sudo == False and isdir:
        return bash(f"cp -R {path} {path2}")
    if sudo and isdir:
        return bash(f"sudo cp -R {path} {path2} ")

def bash(cmd,output= True,debugrunning):
    if output == false:
        cmd = cmd + " > /dev/null"
    if debugrunning == False:
        try:
            re.findall("\n",cmd)[4]
            DEBUG("Bashf cmd.TOO_MUCH_NEWLINE")
        except:
            if len(cmd) > 1100:
                DEBUG("Bashf cmd.LEN_MORE_THAN_1100")
            else:
                DEBUG("Bashf cmd." + cmd)
    pipe = subprocess.Popen(cmd,shell=true,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    res = pipe.communicate()
    if not pipe.returncode == 0:
        Error("An error ocurred")
        DEBUG(res)
        sys.exit()
    return pipe.stdout

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
# KRNL for linux
def Help():
    print(f"{Fore.WHITE}Main : ")
    print("    --help (-h) : Displays this list")
    print("    --quiet : Disables any DEBUG message\n")
    print(f"{Fore.MAGENTA}Grapejuice (Linux) : ")
    print("    --grapejuice-install (-gi) : Installs grapejuice using the wiki")
    print("    --install-tkg (-tkg) : Installs the patched mouse wine for grapejuice\n")
    print(f"{Fore.CYAN}Linux : ")
    print(f"    {Fore.LIGHTRED_EX}KRNL : ")
    print("        --linux-install-krnl (-lik) : Installs KRNL")
    print("        --linux-krnl-attach (-lka) : The name says it all")
    print("        --linux-krnl-execute [ARG] (-lke) : Executes a script using KRNL (WARNING : ONLY 1 ARGUMENT SO ITS RECOMMENDED USING LOADSTRING)")
    print("        --linux-delete-krnl (-ldk) : Removes KRNL")
    print("        --linux-download-autoexec (-lda) : Downloads the internal gui")
    print("        --linux-set-prefix [ARG] (-lsp) : Set the variable PREFIX everytime you use a console (People that installed KRNL will understand what this does)")
    print("        --linux-beta-gui-build-install (-lbgbi) : Instead of using the console uses a GUI (TODO)")
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
    # Its monke or monkey

KrnlApiDownload = curl("https://pastebin.com/raw/JKeXKjLf")
KrnlExecutorDownload = curl("https://pastebin.com/raw/gcH1DTED")
KrnlAttacherDownload = curl("https://pastebin.com/raw/bU36nsCE")
def GrapejuiceInstall():
    if distro == "debian":
        Process("Installing Debian Grapejuice")
        bash("sudo apt update",false)
        bash("sudo apt upgrade -y",false)
        bash("sudo apt install -y curl",false)
        bash("curl https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg | sudo tee /usr/share/keyrings/grapejuice-archive-keyring.gpg",false)
        bash("sudo tee /etc/apt/sources.list.d/grapejuice.list <<< 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main'",false)
        bash("sudo apt update",false)
        bash("sudo apt install -y grapejuice",false)
        Info("Done")
    elif distro == "arch":
        Process("Instaling Arch Grapejuice")
        DEBUG("Installing base-devel (pacman -S base-devel)")
        bash("sudo pacman -S base-devel",false)
        bash("cd $HOME && git clone https://aur.archlinux.org/grapejuice-git.git")
        bash("cd $HOME/grapejuice-git && makepkg -si")
        Info("Done")
    else:
        DEBUG("Gentoo/Unknown Distro Detected, printing source code message")
        print("We cant detect your current distro, to install grapejuice is recommended doing it from source")
        print("Grapejuice Source Code : https://gitlab.com/brinkervii/grapejuice")
# Now i need to rewrite all the fucking code
if __name__ == '__main__':
    for argument in sys.argv:
        def GetFlag(text):
            if argument == text:
                if windows:
                    print("Executing any flag with windows will give massive errors")
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
        elif GetFlag("--linux-krnl-attach") or GetFlag("-lka"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                sys.exit()
            bash("sh attach.sh")
        elif GetFlag("--linux-krnl-execute") or GetFlag("-lke"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                sys.exit()
            bash(f"sh execute.sh {sys.argv[2]}")
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
        elif GetFlag("--grapejuice-install") or GetFlag("-gi"):
            flagexecuted = True
            GrapejuiceInstall()
        elif GetFlag("--linux-delete-krnl") or GetFlag("-ldk"):
            flagexecuted = True
            if KrnlInstalled:
                remove(f"{KrnlPath}",False,True)
                os.system(f"""
                rm -R {KrnlPath}
                """)
                Info("Done")
            else:
                Error("Krnl is not installed")
        elif GetFlag("--install-tkg") or GetFlag("-tkg"):
            flagexecuted = True
            if not TkgInstalled:
                Info("Downloading TKG")
                wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                os.system("python3 /tmp/install.py > /dev/null")
                Info("Sucessfully downloaded TKG")
            else:
                TKGQuestion= Question("TKG Is already installed, do you want to delete it and continue? (Y/N) : ")
                if re.search("Y",TKGQuestion):
                    remove(f"{TkgPath}",False,True)
                    DEBUG("Function wget, Content https://pastebin.com/raw/5SeVb005, File /tmp/install.py")
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005","/tmp/install.py")
                    os.system("python3 /tmp/install.py > /dev/null")
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
                            remove("/tmp/autoexec",False,True)
                        copy(f"{HOME}/KRNL/autoexec", "/tmp",False,True)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            remove("/tmp/workspace",False,True)
                        copy(f"{HOME}/KRNL/workspace","/tmp",False,True)
                    remove(f"{HOME}/KRNL",False,True)
                elif re.search("N",DeleteQuestion) == True:
                    print("")
                else:
                    if exists(f"{HOME}/KRNL/autoexec"):
                        if exists("/tmp/autoexec"):
                            remove("/tmp/autoexec",False,True)
                        copy(f"{HOME}/KRNL/autoexec", "/tmp",False,True)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            remove("/tmp/workspace",False,True)
                        copy(f"{HOME}/KRNL/workspace","/tmp",False,True)
                    remove(f"{HOME}/KRNL",False,True)
            if TkgInstalled == False:
                TKGQuestion = Question("The wine mouse patch is not installed and this is necessary to run Krnl. Do u want to install this? (Y/N) : ")
                if re.search("Y",TKGQuestion) == True:
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                    bash("python3 /tmp/install.py",false)
                    Info("Sucessfully downloaded TKG")
                elif re.search("N",TKGQuestion) == True:
                    print("")
                else:
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                    bash("python3 /tmp/install.py",false)
                    Info("Sucessfully downloaded TKG")
            mkdir("$HOME/KRNL")
            mkdir("$HOME/KRNL/autoexec")
            mkdir("$HOME/KRNL/workspace")
            mkdir("$HOME/KRNL/bin")
            mkfile(f"{KrnlPath}/attach.sh","""
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            echo 'To make KRNL not ask this everytime you execute it, use --linux-set-prefix [PREFIXNAME]
            read PREFIX
            fi
            echo "WARNING : If you have any error/question just call SimplyDeveloper"
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Executing Attacher..." 
            $HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/attach     
            """)
            mkfile(f"{KrnlPath}/execute.sh","""
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            echo 'To make KRNL not ask this everytime you execute it, use --linux-set-prefix [PREFIXNAME]
            read PREFIX
            fi
            echo "WARNING : If you have any error/question just call SimplyDeveloper"
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Executing Script..." 
            $HOME/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.1.r2.gc437a01e/bin/wine $HOME/KRNL/execute $@     
            """)

            mkfile(f"{KrnlPath}/autoexec/InternalGui.txt","loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()")
            wget(KrnlApiDownload, "$HOME/KRNL/KrnlAPI.dll")
            wget(KrnlAttacherDownload, "$HOME/KRNL/attach")
            wget(KrnlExecutorDownload, "$HOME/KRNL/execute")
            Info("KRNL Sucessfully downloaded")
        elif GetFlag("--linux-download-autoexec") or GetFlag("-lda"):
            flagexecuted = True
            if exists(f"{HOME}/KRNL")():
                mkfile(f"{KrnlPath}/autoexec/InternalGui.txt","loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()")
                Info("Done")
                DEBUG("Writing Ended")
            else:
                DEBUG(f"exists({HOME}/KRNL) False")
                Error("Krnl not installed")
        else:
            if flagexecuted == False:
                try:
                    lol = sys.argv[1]
                except:
                    Help()
