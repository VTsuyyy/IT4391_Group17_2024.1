import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os
import time

columns = ["url", "content"]

run_time = "{:%d%m%Y}".format(datetime.now())

def extract_load(link, find_con, url_header, classification):
    t = requests.get(link).content
    soup = BeautifulSoup(t, "html.parser")
    links = soup.find_all('a')
    data = []

    for i in links:
        if str(i).find(find_con) != -1:
            url = url_header + i["href"]
            retries = 3
            content = None
            for attempt in range(retries):
                try:
                    content = requests.get(url, timeout=5).content
                    break
                except requests.exceptions.Timeout:
                    if attempt < retries - 1:
                        time.sleep(2)  # Wait before retrying
                    else:
                        print(f"Skipping {url} due to repeated timeouts.")
                        content = None
            
            if content:
                tmp = (url, content.decode("utf-8", errors="ignore"))
                data.append(tmp)
    
    if not os.path.exists(classification):
        os.makedirs(classification)

    df = pd.DataFrame(data, columns=columns)
    df.to_parquet(f"{classification}/{run_time}.csv", index=False)
    print(f"Data saved to {classification}/{run_time}.csv")

if __name__ == "__main__":
    # extract_load("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page=", "/apps/details", "https://www.topcv.vn", "top_CV")
    extract_load("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&company_field=0&sort=up_top&page=", "/apps/details", "https://www.topcv.vn", "Data")
    # extract_load("https://play.google.com/store/games?device=tablet", "/apps/details", "https://play.google.com", "google_play_tablet")
