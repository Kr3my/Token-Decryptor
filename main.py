import base64, os, colorama
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

def decrypt(raw_token: str, key: str) -> str:
    try:
        return AES.new(CryptUnprotectData(key, None, None, None, 0)[1], AES.MODE_GCM, raw_token[3:15]).decrypt(raw_token[15:])[:-16].decode()
    
    except Exception as err:
        print(colorama.Fore.RED + "[!]" + colorama.Fore.LIGHTRED_EX + " {0}".format(err) + colorama.Fore.RESET)
        return "Error"
 
def main() -> None:
    os.system("cls")
    
    print(colorama.Fore.LIGHTCYAN_EX + """
  _____     _                ____                             _             
 |_   _|__ | | _____ _ __   |  _ \  ___  ___ _ __ _   _ _ __ | |_ ___  _ __ 
   | |/ _ \| |/ / _ \ '_ \  | | | |/ _ \/ __| '__| | | | '_ \| __/ _ \| '__|
   | | (_) |   <  __/ | | | | |_| |  __/ (__| |  | |_| | |_) | || (_) | |   
   |_|\___/|_|\_\___|_| |_| |____/ \___|\___|_|   \__, | .__/ \__\___/|_|   
                                                  |___/|_|                  
          """ + colorama.Fore.RESET)
    
    try:
        token = input(colorama.Fore.MAGENTA + ">" + colorama.Fore.LIGHTMAGENTA_EX + " Token: " + colorama.Fore.MAGENTA)
        key = input(colorama.Fore.MAGENTA + ">" + colorama.Fore.LIGHTMAGENTA_EX + " Key: " + colorama.Fore.MAGENTA)
        
        plain_text = decrypt(base64.b64decode(token.split("dQw4w9WgXcQ:")[1]), base64.b64decode(key)[5:])
        
        print(colorama.Fore.YELLOW + "\n[*]" + colorama.Fore.LIGHTYELLOW_EX + " Token: {0}".format(plain_text) + colorama.Fore.RESET)
    
    except Exception as err:
        print(colorama.Fore.RED + "[!]" + colorama.Fore.LIGHTRED_EX + " {0}".format(err) + colorama.Fore.RESET)

if __name__ == "__main__":
    main()
