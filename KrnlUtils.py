from colorama import Fore, Back, Style
import colorama
from os.path import exists
import subprocess
import requests
import urllib.request
import re
import sys
from git import Repo
import git
from discord import Webhook, RequestsWebhookAdapter
import getpass
import os
true = True
false = False
nil = None
null = None

try:
    from discord import Webhook, RequestsWebhookAdapter
except ModuleNotFoundError:
    print("Collecting Discord API...")
    os.system("pip3 install --user discord.py > /dev/null")
"""
try:
    from gi.repository import Gtk
except ModuleNotFoundError:
    print("Fatal error installing gi.repository to use gtk")
    sys.exit()
from gi.repository import Gtk"""
try:
    import git
    from git import repo
except ModuleNotFoundError:
    print("Collecting Git...")
    os.system("pip3 install --user gitpython > /dev/null")

try:
    import requests
except ModuleNotFoundError:
    print("Collecting requests...")
    os.system("pip3 install --user requests > /dev/null")

try:
    import colorama
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print("Collecting colorama...")
    os.system("pip3 install --user colorama > /dev/null")

colorama.init(autoreset=True)
if getpass.getuser() == "root":
    print("Do not run this with root")

    sys.exit()

HOME = f"/home/{getpass.getuser()}"
KrnlInstalled = exists(f"{HOME}/KRNL")
RunInstalled = exists(f"{HOME}/KRNL/krnl")
TkgInstalled = exists(
    f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.2.r0.g68441b1d/bin/wine")
LinkInstalled = exists("/bin/krnl")
KrnlPath = f"{HOME}/KRNL"
RunPath = f"{KrnlPath}/krnl"
TkgPath = f"{HOME}/.local/share/grapejuice/user/wine-download/wine-tkg-staging-fsync-git-7.2.r0.g68441b1d/bin/wine"
LinkPath = f"/bin/krnl"

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
    try:
        if not windows:
            if not exists(f"{HOME}/.krnltmp"):
                mkdir(f"{HOME}/.krnltmp", False, True)
            if not exists(f"{HOME}/.krnltmp/.debuglogs"):
                mkfile(f"{HOME}/.krnltmp/.debuglogs", "[DEBUG LOGS BEGIN]", True)
    except KeyboardInterrupt:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Keyboard interruption detected, exiting")
        sys.exit()
    except Exception as e:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Fatal Code Error : Exception catched at line 74")
        print(e)
        sys.exit()
    bash(f"echo '{text}' >> {HOME}/.krnltmp/.debuglogs", False, True)
    if quiet == True:
        return "Quiet Mode"
    print(f"{Fore.GREEN} [DEBUG] {Fore.WHITE} " + text)


def DEBUG_ERROR(text):
    text = str(text)
    try:
        if not windows:
            if not exists(f"{HOME}/.krnltmp"):
                mkdir(f"{HOME}/.krnltmp", False, True)
            if not exists(f"{HOME}/.krnltmp/.debuglogs"):
                mkfile(f"{HOME}/.krnltmp/.debuglogs", "[DEBUG LOGS BEGIN]", True)
    except KeyboardInterrupt:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Keyboard interruption detected, exiting")
        sys.exit()
    except Exception as e:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Fatal Code Error : Exception catched at line 84, sending data to the developer")
        print(e)
    bash(f"echo 'ERROR : {text}' >> {HOME}/.krnltmp/.debuglogs", True, True)
    if quiet == True:
        return "Quiet Mode"
    print(f"{Fore.RED} [!DEBUG] Error : {Fore.WHITE} " + text)


def Question(text):
    Input = input(f"{Fore.LIGHTMAGENTA_EX} [:] {Fore.WHITE} " + text)
    return Input


gentoo = exists("/usr/bin/emerge")
debian = exists("/usr/bin/apt")
arch = exists("/usr/bin/pacman")
windows = exists("C:/Windows")
flagexecuted = False
forloopc = 0


def curl(link):
    try:
        return urllib.request.urlopen(link).read()
    except Exception as e:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Fatal Code Error : Exception catched at line 116, sending data to the developer")
        print(e)
        sys.exit()


def wget(link, path):
    try:
        r = requests.get(link, allow_redirects=True)
    except Exception as e:
        print(
            f"{Fore.RED}[!DEBUG]{Fore.WHITE} Fatal Code Error : Exception catched at line 118, sending data to the developer")
        print(e)
    DEBUG("Downloadf url."+str(link)+" path."+str(path))
    if exists(path) == False:
        bash(f"touch {path}")
    open(path, 'wb').write(r.content)


def mkfile(path, content, debugrunning=False):

    if debugrunning == False:
        try:
            re.findall("\n", content)[4]
            DEBUG(f"Writefile path.{path}")
        except:
            if len(content) > 1100:
                DEBUG(f"Writefile path.{path}")
            else:
                DEBUG(f"Writefile content.{content} path.{path}")
    with open(path, 'w') as f:
        f.write(content)
        f.close()
    if exists(path) == False:
        Error("An error ocurred")
        DEBUG_ERROR(f"Weird, error in function mkfile")
        print(f"How did u get here bud?")
        sys.exit()


def mkdir(path, sudo=False, debugrunning=False):
    
    if sudo == None or sudo == "":
        sudo = False
    if debugrunning == False:
        DEBUG("Mkdirf path."+path+" sudo."+str(sudo))
    if sudo == True:
        return bash(f"sudo mkdir {path}", True, debugrunning)
    else:
        return bash(f"mkdir {path}", True, debugrunning)


def readfile(path):
    DEBUG("Readfilef path."+path)
    return bash(f"cat {path}")


def remove(path, sudo=False, isdir=False):
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


def copy(path, path2, sudo=False, isdir=False):
    if isdir == "":
        isdir = False
    if sudo == "":
        sudo = False
    DEBUG("Copyf frompath."+path+" topath."+path2 +
          " sudo."+str(sudo)+" isdir."+str(isdir))
    if sudo == False and isdir == False:
        return bash(f"cp {path} {path2}")
    if sudo and isdir == False:
        return bash(f"sudo cp {path} {path2}")
    if sudo == False and isdir:
        return bash(f"cp -R {path} {path2}")
    if sudo and isdir:
        return bash(f"sudo cp -R {path} {path2} ")


def bash(cmd, output=True, debugrunning=False):
    if output == false and not windows:
        cmd = cmd + " > /dev/null"
    if debugrunning == False:
        try:
            re.findall("\n", cmd)[4]
            DEBUG("Bashf cmd.TOO_MUCH_NEWLINE")
        except:
            if len(cmd) > 1100:
                DEBUG("Bashf cmd.LEN_MORE_THAN_1100")
            else:
                DEBUG("Bashf cmd." + cmd)
    if not windows:
        pipe = subprocess.Popen(
            cmd, shell=true, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = pipe.communicate()
        if not pipe.returncode == 0:
            Error(f"An error ocurred, error code : {str(pipe.returncode)}")
            DEBUG_ERROR(res)
            sys.exit()
        return pipe.stdout
    else:
        pipe = subprocess.Popen(
            "C:\Windows\System32\powershell.exe "+cmd, shell=true, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = pipe.communicate()
        if not pipe.returncode == 0:
            Error(f"An error ocurred, error code : {str(pipe.returncode)}")
            DEBUG_ERROR(res)
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
        print("Oogabooga is STILL the best...")
        return "idk"


distro = GetDistro()
# KRNL for linux


def Help():
    print(f"{Fore.WHITE}Main : ")
    print("    --help (-h) : Displays this list")
    print("    --quiet : Disables any DEBUG message\n")
    print(f"{Fore.MAGENTA}Grapejuice (Linux) : ")
    print("    install grapejuice : Installs grapejuice using the wiki")
    print("    install tkg : Installs the patched mouse wine for grapejuice\n")
    print(f"{Fore.CYAN}Linux : ")
    print(f"    {Fore.LIGHTRED_EX}KRNL : ")
    print("        install krnl : Installs KRNL")
    print("        install vcredist : Installs KRNL's Requirements using winetricks")
    print("        krnl launch : The name says it all")
    print("        krnl execute [ARG] (TODO) : Executes a script using KRNL (WARNING : ONLY 1 ARGUMENT SO ITS RECOMMENDED USING LOADSTRING)")
    print("        remove krnl : Removes KRNL")
    print("        install internalgui : Downloads the internal gui")
    print("        krnl set wineprefix [ARG] : Set the variable PREFIX everytime you use a console (People that installed KRNL will understand what this does)")
    print("        install guibeta (TODO) : Instead of using the console uses a GUI (TODO)")
    print(f"{Fore.CYAN}MacOS KRNL : ")
    print("    Soon\n")
    print(f"{Fore.CYAN}Windows : ")
    print(f"    {Fore.LIGHTRED_EX}Troubleshooting : ")
    print(f"        fix unexpectedclient : Fixes 'Kicked due to an unexpected client behaviour'")
    print(f"        fix dllmissing : Fixes 'krnl.dll Missing' NOTE : Requieres putting the full KRNL path")
    print(f"        fix dependenciesnotinstalled : Downloads every KRNL dll NOTE : Requieres putting the full KRNL path")
    print(f"        fix outdated : Fixes 'KRNL Outdated' NOTE : Requires putting the full KRNL path")
    print(f"        fix unknownerror : Fixes KRNL crashing because of an unknown error")
    print(f"        fix downloadblock : Fixes google chrome blocking KRNL")
    print(f"        fix krnldelete : Fixes KRNL Deleting")
    print(f"        fix bootstrapper : Fixes ANY ERROR with the bootstrapper")
    print(f"        fix infiniteinjection : Fixes KRNL getting stuck in a loop with injecting")
    print(f"        fix injectionstuck : Fixes KRNL being stuck in Correct Key/Checking Key/Loading Dependencies")
    print(f"        fix robloxnotfound : Fixes KRNL not finding ROBLOX")
    print(f"        fix krnlcrash : Fixes KRNL Crashing")
    print(f"        fix invalidkey : Fixes Invalid Key KRNL Error")
    print(f"        fix errortxt : Fixes ERROR.txt")
    print(f"{Fore.CYAN}About Messages :")
    print(f"    {Fore.RED}[!]{Fore.WHITE} : Error")
    print(f"    {Fore.BLUE}[¡]{Fore.WHITE} : Info")
    print(f"    {Fore.YELLOW}[;]{Fore.WHITE} : Warning")
    print(f"    {Fore.MAGENTA}[#]{Fore.WHITE} : Process/Downloading/Loading")
    print(f"    {Fore.LIGHTMAGENTA_EX}[:]{Fore.WHITE} : Question")
    print(
        f"    {Fore.GREEN}[DEBUG]{Fore.WHITE} : Debug Messages (Disable with --quiet)")
    print(f"    {Fore.RED}[!DEBUG]{Fore.WHITE} : More detailed error")

KrnlLauncherDownload = curl("https://pastebin.com/raw/wgeLyD2y")
#KrnlApiDownload = curl("https://pastebin.com/raw/JKeXKjLf")
#KrnlExecutorDownload = curl("https://pastebin.com/raw/gcH1DTED")
#KrnlAttacherDownload = curl("https://pastebin.com/raw/bU36nsCE")


def GrapejuiceInstall():
    if distro == "debian":
        Process("Installing Debian Grapejuice")
        bash("sudo apt update", false)
        bash("sudo apt upgrade -y", false)
        bash("sudo apt install -y curl", false)
        bash("curl https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg | sudo tee /usr/share/keyrings/grapejuice-archive-keyring.gpg", false)
        bash(
            "sudo tee /etc/apt/sources.list.d/grapejuice.list <<< 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main'", false)
        bash("sudo apt update", false)
        bash("sudo apt install -y grapejuice", false)
        Info("Done")
    elif distro == "arch":
        Process("Instaling Arch Grapejuice")
        DEBUG("Installing base-devel (pacman -S base-devel)")
        bash("sudo pacman -S base-devel", false)
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
        def GetFlag(text,iswin=false,isboth=false):
            if argument == text:
                if windows:
                    if iswin == False:
                        if not isboth:
                            print("Dont do that")
                            sys.exit()
                if iswin:
                    if gentoo or arch or debian:
                        if not isboth:
                            print("Dont do that")
                            sys.exit()
                flagexecuted = True
                return True
            else:
                return False
        if GetFlag("--quiet",true, true):
            quiet = True

        if GetFlag("--help",true, true) or GetFlag("-h",true):
            flagexecuted = True
            Help()
            sys.exit()
        # Im just making something to fix other errors, not krnl being outdated
        elif GetFlag("fix errortxt",True,False):
            if not sys.argv[2]:
                DEBUG_ERROR("sys.argv[2] Missing, please insert KRNL's full path")
                Error("Please insert KRNL's full path")
                sys.exit()
            wget("https://aka.ms/vs/16/release/vc_redist.x64.exe",f"C:/Users/{getpass.getuser()}/Downloads/vc_redist.x64.exe")
            wget("https://go.microsoft.com/fwlink/?LinkId=2085155",f"C:/Users/{getpass.getuser()}/Downloads/dotnet472.exe")
            bash(f"C:/Users/{getpass.getuser()}/Downloads/vc_redist.x64.exe")
            bash(f"C:/Users/{getpass.getuser()}/Downloads/dotnet472.exe")
        #elif GetFlag("fix dependenciesnotinstalled",True,False):
        #    if not sys.argv[2]:
        #       DEBUG_ERROR("sys.argv[2] Missing, please insert KRNL's full path")
        #        Error("Please insert KRNL's full path")
        #         sys.exit()
        #    Info("Downloading Dependencies")
        #    wget("",sys.argv[2])
        #    #wget("https://k-storage.com/bootstrapper/files/krnl.dll",sys.argv[2])
        #   Info("Done")
        elif GetFlag("fix dllmissing",True,False):
            if not sys.argv[2]:
                DEBUG_ERROR("sys.argv[2] Missing, please insert KRNL's full path")
                Error("Please insert KRNL's full path")
                sys.exit()
            Info("Downloading KRNL's DLL")
            wget("https://k-storage.com/bootstrapper/files/krnl.dll",sys.argv[2] + "/krnl.dll")
            Info("Done")
        elif GetFlag("fix outdated",True,False):
            if not sys.argv[2]:
                DEBUG_ERROR("sys.argv[2] Missing, please insert KRNL's full path")
                Error("Please insert KRNL's full path")
                sys.exit()
            Info("Downloading KRNL's DLL")
            wget("https://k-storage.com/bootstrapper/files/krnl.dll",sys.argv[2])
            Info("Done")
        elif GetFlag("fix unexpectedclient",True,False):
            Info("Deleting Roblox's Configuration Files")
            if exists(f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/GlobalBasicSettings_13.xml"):
                bash(f"rm C:/Users/{getpass.getuser()}/AppData/Local/Roblox/GlobalBasicSettings_13.xml")
            else:
                Warning(f"Configuration File 0 Not Found. Skipping")
            if exists(f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/GlobalSettings_13.xml"):
                bash(f"rm C:/Users/{getpass.getuser()}/AppData/Local/Roblox/GlobalSettings_13.xml")
            else:
                Warning(f"Configuration File 1 Not Found. Skipping")
            if exists(f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/frm.cfg"):
                bash(f"rm C:/Users/{getpass.getuser()}/AppData/Local/Roblox/frm.cfg")
            else:
                Warning(f"Configuration File 2 Not Found. Skipping")
            if exists(f"C:/Users/{getpass.getuser()}/AppData/Local/Roblox/AnalysticsSettings"):
                bash(f"rm C:/Users/{getpass.getuser()}/AppData/Local/Roblox/AnalysticsSettings")
            else:
                Warning(f"Configuration File 3 Not Found. Skipping")
            wget("https://setup.rbxcdn.com/version-a10a6fc51c06421b-Roblox.exe",f"C:/Users/{getpass.getuser()}/Downloads/RobloxPlayerLauncher.exe")
            bash(f"C:/Users/{getpass.getuser()}/Downloads/RobloxPlayerLauncher.exe")
        elif GetFlag("krnl launch"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                DEBUG_ERROR(
                    f"{KrnlPath} Does not exist, to install use install krnl argument")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                DEBUG_ERROR(
                    f"{TkgPath} Does not exist, to install use install tkg argument")
                sys.exit()
            bash("sh $HOME/KRNL/launch")
        elif GetFlag("install vcredist"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                DEBUG_ERROR(
                    f"{KrnlPath} Does not exist, to install use install krnl argument")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                DEBUG_ERROR(
                    f"{TkgPath} Does not exist, to install use install tkg argument")
                sys.exit()
            mkfile("/tmp/vcredist","""
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            read PREFIX
            fi
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Downloading VCRedist"
            winetricks --force vcrun2019
            """)
            bash("bash /tmp/vcredist")
        elif GetFlag("install dotnet"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                DEBUG_ERROR(
                    f"{KrnlPath} Does not exist, to install use install krnl")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                DEBUG_ERROR(
                    f"{TkgPath} Does not exist, to install use install tkg")
                sys.exit()
            mkfile("/tmp/dotnet","""
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            read PREFIX
            fi
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Downloading VCRedist"
            winetricks --force dotnet472
            """)
            bash("bash /tmp/dotnet")
        elif GetFlag("install dependencies"):
            if exists(KrnlPath) == False:
                Error("KRNL Not installed")
                DEBUG_ERROR(
                    f"{KrnlPath} Does not exist, to install use install krnl argument")
                sys.exit()
            if exists(TkgPath) == False:
                Error("TKG-Binary mouse patch not installed")
                DEBUG_ERROR(
                    f"{TkgPath} Does not exist, to install use install tkg argument")
                sys.exit()
            mkfile("/tmp/dependencies","""
            if [[ -z "${PREFIX}" ]]; then
            echo "What is your PLAYER wineprefix name?"
            read PREFIX
            fi
            export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
            export WINEPREFIX=$WINEPREFIXPATH 
            export WINEARCH="win64" 
            export WINEDEBUG="-all" 
            export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
            echo "[#] Downloading VCRedist"
            winetricks --force vcrun2019 dotnet472
            """)
            bash("bash /tmp/dependencies")
        #elif GetFlag("--linux-krnl-execute") or GetFlag("-lke"):
        #    if exists(KrnlPath) == False:
        #        Error("KRNL Not installed")
        #        DEBUG_ERROR(
        #            f"{KrnlPath} Does not exist, to install use -lik argument")
        #        sys.exit()
        #    if exists(TkgPath) == False:
        #        Error("TKG-Binary mouse patch not installed")
        #        DEBUG_ERROR(
        #            f"{TkgPath} Does not exist, to install use --install-tkg argument")
        #        sys.exit()
        #    bash(f"sh $HOME/KRNL/execute.sh {sys.argv[2]}")
        
        elif GetFlag("krnl set wineprefix"):
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
        elif GetFlag("install grapejuice"):
            flagexecuted = True
            GrapejuiceInstall()
        elif GetFlag("remove krnl"):
            flagexecuted = True
            if KrnlInstalled:
                remove(f"{KrnlPath}", False, True)
                Info("Done")
            else:
                Error("Krnl is not installed")
        elif GetFlag("install tkg"):
            flagexecuted = True
            if not TkgInstalled:
                Info("Downloading TKG")
                wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                bash("python3 /tmp/install.py", False)
                Info("Sucessfully downloaded TKG")
            else:
                TKGQuestion = Question(
                    "TKG Is already installed, do you want to delete it and continue? (Y/N) : ")
                if re.search("Y", TKGQuestion):
                    remove(f"{TkgPath}", False, True)
                    DEBUG(
                        "Function wget, Content https://pastebin.com/raw/5SeVb005, File /tmp/install.py")
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                    bash("python3 /tmp/install.py", false)
                    Info("Sucessfully downloaded TKG")
                else:
                    Info("Okay, TKG Will not be deleted or installed")
        elif GetFlag("install krnl"):
            flagexecuted = True
            if exists(f"{HOME}/KRNL"):
                Warning(
                    "This will delete every file inside of krnl but autoexec and workspace will be copied into TMP if they exist")
                DeleteQuestion = Question(
                    "Krnl is already installed, do u want to delete it? (Y/N) : ")
                if re.search("Y", DeleteQuestion) == True:
                    if exists(f"{HOME}/KRNL/autoexec"):
                        if exists("/tmp/autoexec"):
                            remove("/tmp/autoexec", False, True)
                        copy(f"{HOME}/KRNL/autoexec", "/tmp", False, True)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            remove("/tmp/workspace", False, True)
                        copy(f"{HOME}/KRNL/workspace", "/tmp", False, True)
                    remove(f"{HOME}/KRNL", False, True)
                elif re.search("N", DeleteQuestion) == True:
                    print("")
                else:
                    if exists(f"{HOME}/KRNL/autoexec"):
                        if exists("/tmp/autoexec"):
                            remove("/tmp/autoexec", False, True)
                        copy(f"{HOME}/KRNL/autoexec", "/tmp", False, True)
                    if exists(f"{HOME}/KRNL/workspace"):
                        if exists("/tmp/workspace"):
                            remove("/tmp/workspace", False, True)
                        copy(f"{HOME}/KRNL/workspace", "/tmp", False, True)
                    remove(f"{HOME}/KRNL", False, True)
            if TkgInstalled == False:
                TKGQuestion = Question(
                    "The wine mouse patch is not installed and this is necessary to run Krnl. Do u want to install this? (Y/N) : ")
                if re.search("Y", TKGQuestion) == True:
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                    bash("python3 /tmp/install.py", false)
                    Info("Sucessfully downloaded TKG")
                elif re.search("N", TKGQuestion) == True:
                    print("")
                else:
                    Info("Downloading TKG")
                    wget("https://pastebin.com/raw/5SeVb005", "/tmp/install.py")
                    bash("python3 /tmp/install.py", false)
                    Info("Sucessfully downloaded TKG")
            mkdir("$HOME/KRNL")
            mkdir("$HOME/KRNL/autoexec")
            mkdir("$HOME/KRNL/workspace")
            mkdir("$HOME/KRNL/bin")
            mkfile(f"{KrnlPath}/launch", """
if [[ -z "${PREFIX}" ]]; then
echo "What is your PLAYER wineprefix name?"
echo 'To make KRNL dont ask this everytime you execute it, use krnl set wineprefix [PREFIXNAME]'
read PREFIX
fi
echo "WARNING : If you have any error/question just call SimplyDeveloper"
export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
export WINEPREFIX=$WINEPREFIXPATH 
export WINEARCH="win64" 
export WINEDEBUG="-all" 
export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
echo "[#] Executing Attacher..." 
"""+TkgPath+""" $HOME/KRNL/.launcher.exe""")
            #mkfile(f"{KrnlPath}/execute.sh", """
#if [[ -z "${PREFIX}" ]]; then
#echo "What is your PLAYER wineprefix name?"
#echo 'To make KRNL not ask this everytime you execute it, use --linux-set-prefix [PREFIXNAME]'
#read PREFIX
#fi
#echo "WARNING : If you have any error/question just call SimplyDeveloper"
#export WINEPREFIXPATH="$HOME/.local/share/grapejuice/prefixes/${PREFIX}"
#export WINEPREFIX=$WINEPREFIXPATH 
#export WINEARCH="win64" 
#export WINEDEBUG="-all" 
#export WINEDLLOVERRIDES="dxdiagn=;winemenubuilder.exe=" 
#echo "[#] Executing Script..." 
#""" + TkgPath + """ $HOME/KRNL/execute $@""")

            mkfile(f"{KrnlPath}/autoexec/InternalGui.txt",
                   """
if not writefile then
    warn("You can't execute this script.")
    
else
    local s,e = pcall(function()
        loadstring(game:HttpGet("https://raw.githubusercontent.com/Seflengfist/Scripts/main/Internal", true))()
    end)

    if s then
        print("1.1")
    else
       print("Error: ", e)
    end
end
                   """)
            wget(KrnlLauncherDownload, f"{KrnlPath}/.launcher.exe")
            Info("KRNL Sucessfully downloaded")
            Warning("The InternalGui is being rewritten so you wont be able to use it, tho you can add your own internal gui to the autoexec")
        elif GetFlag("install internalgui"):
            flagexecuted = True
            if exists(f"{HOME}/KRNL")():
                mkfile(f"{KrnlPath}/autoexec/InternalGui.txt",
                       "loadstring(game:HttpGet('https://raw.githubusercontent.com/Seflengfist/Scripts/main/Gui', true))()")
                Info("Done")
                DEBUG("Writing Ended")
                Warning("The InternalGui is being rewritten so you wont be able to use it, tho you can add your own internal gui to the autoexec")
            else:
                DEBUG(f"exists({HOME}/KRNL) False")
                Error("Krnl not installed")
        else:
            if flagexecuted == False:
                try:
                    lol = sys.argv[1]
                except:
                    Help()
