from bs4 import BeautifulSoup

def read_html():
    with open('./indeed.html') as file: 
        return file.read() 
    
def scraper(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.find_all("a")
    title_text = [text.get('title') for text in title]

    print(title_text)

def test_scraper():
    scrapeData = scraper(read_html())
    print(scrapeData)

test_scraper()