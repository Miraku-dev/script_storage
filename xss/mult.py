import requests
from bs4 import BeautifulSoup

# Read the list of websites from site.txt
with open('site.txt', 'r') as file:
    websites = file.read().splitlines()

# Function to extract all pages of a website
def extract_pages(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=False)  # Установите allow_redirects в False
        soup = BeautifulSoup(response.content, 'html.parser')
        pages = [link.get('href') for link in soup.find_all('a', href=True)]
        return pages
    except requests.Timeout:
        print(f"Произошла ошибка таймаута при попытке доступа к {url}")
        return []
    except requests.ConnectionError:
        print(f"Произошла ошибка подключения при попытке доступа к {url}")
        return []



# Open multiple.txt for writing
with open('multiple.txt', 'w') as file:
    for website in websites:
        pages = extract_pages(website)
        file.write(f'Pages for {website}:\n')
        for page in pages:
            file.write(f'{page}\n')
        file.write('\n')

print('Pages extracted and saved to multiple.txt')
