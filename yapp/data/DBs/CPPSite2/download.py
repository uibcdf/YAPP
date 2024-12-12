from pathlib import Path
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import pickle

def web_scrapping(url):
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code!=200:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all('table')[1]
        rows = table.find_all('tr')
        data = {}
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                data[key] = value
        return data
    except:
        return None

def main():

    db_file = Path('CPPSite2.pkl')
    
    if db_file.exists():
        with open(db_file, 'rb') as fff:
            db = pickle.load(fff)
    else:
        db = {}

    with_problems = [f"{i:04d}" for i in range(0,4000)]

    while len(with_problems):

        aux_with_problems = []

        for string_id in tqdm(with_problems):
            if string_id not in db:
                url = f'https://webs.iiitd.edu.in/raghava/cppsite/display.php?details={string_id}'
                data = web_scrapping(url)
                if data is None:
                    aux_with_problems.append(string_id)
                elif len(data):
                    db[string_id]=data

        with_problems=aux_with_problems

    with open(db_file, 'wb') as fff:
        pickle.dump(db,fff)


if __name__ == "__main__":
    main()

