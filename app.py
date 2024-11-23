from bs4 import BeautifulSoup
import requests
import os

def luricPars(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    lyrics = soup.find('div', class_='Lyrics__Root-sc-1ynbvzw-0')
    
    if lyrics:
        lyrics_text = lyrics.get_text(strip=True, separator='\n')
        print(lyrics_text)
        
        filename = url.split('/')[-1].lower() + '.txt'
        filename = filename.replace(' ', '_').replace('?', '').replace('&', 'and')
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(lyrics_text)
        
        print(f"Text saved to: {filename}")
    else:
        print("Text not found.")

luricPars("https://genius.com/Saluki-of-lights-lyrics")
