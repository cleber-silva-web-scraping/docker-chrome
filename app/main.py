from sys import platform
import time
import os



def open_browser(url):
    print('Starting browser....')
    print('Starting browser....')
    os.system("ps aux | grep -i chrome | awk '{print $2}' | xargs kill -9")

    if platform == "darwin":
        os.system(f"open -a Google\ Chrome \"{url}\"")
    else:
        os.system(f"google-chrome --no-sandbox  \"{url}\"")




open_browser('https://www.google.com.br')

time.sleep(500)


