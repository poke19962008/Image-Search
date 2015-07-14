import requests
from bs4 import BeautifulSoup as b
main_page=1
file=open("archive.txt","a")
while True:
	web="https://archive.org/details/image?&sort=-downloads&page=%d"%main_page
	soup=b(requests.get(web).content)
	soup=soup.findAll("div",{"class":"collection-title C C2"})
	main_page+=1
	for category in soup:
		category_link=category.find('a').get('href')
		category_name=category.find('a').find('div').text
		file.write(str(category_name)+'\n')
		file.write(str( "https://archive.org"+category_link)+'\n')
		print category_name
		category_page=1
		while True:
			cat="https://archive.org"+category_link+"?&sort=-downloads&page=%d"%category_page
			cat_soup=b(requests.get(cat).content)
			cat_soup=cat_soup.findAll('div',{"class":"ttl C C2"})
			category_page+=1
			cat_soup=cat_soup[1:]
			if len(cat_soup)==0:
				break
			for img in cat_soup:
				link=img.find('a').get('href')
				desc=(img.find('a').text).encode('utf-8')
				file.write(str(desc)+'\n')
				file.write(str( "https://archive.org"+link)+'\n')
			print category_page-1
		
	print main_page-1
	
	
