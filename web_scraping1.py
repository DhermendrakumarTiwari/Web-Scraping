#pip install bs4
#import requests # requests inbuilt package , to accept request of selected url
#from bs4 import BeautifulSoup

#page=requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
#page user defined  object to hold all details of selected page of given website



import requests
from bs4 import BeautifulSoup


page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
 #Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')#<a>
# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

