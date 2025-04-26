import requests
from bs4 import BeautifulSoup
def search_wikipedia(query):
    try:
        url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        response = requests.get(search_url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        summary_paragraph = soup.find('html').get_text()
        return summary_paragraph
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

print("Welcome to the Information Text Bot")
while True:
    query = input("Please enter a topic to search for (or type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("Thank you for using Text Bot.Goodbye!")
        break
    result = search_wikipedia(query)
    print(result)
    print()
        