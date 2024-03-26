import time
import os
import requests
import concurrent.futures

if __name__ == '__main__':
    freeze_support()

    TARGET_PATH = "./"

    urls = ["https://www.opticon.com/support/OPN-2001/OPN-2001.zip","https://www.opticon.com/support/Appload/Appload%20Setup.exe","https://www.opticon.com/support/Drivers/USB%20Drivers%20Installer.exe","https://www.opticon.com/support/OPN-2001%20PC%20Application/OPN200x%20Setup.exe"]

    def download_files(url):
        r = requests.get(url)

        filename = url.split("/")[-1].split(".")[0].replace("%","")

        if r.ok:
            with open(os.path.join(TARGET_PATH,filename+".exe"),"wb") as file:
                file.write(r.content)
                print(f"{filename}'s download finished.")
        else:
            print(f"Ressource at {url} couldn't be retrieved, try again.")

    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(download_files,urls)
    end = time.perf_counter()
    print(f"Download finished in {round(end-start,2)} seconds.")

    input("Press enter to exit...")
