from bs4 import BeautifulSoup
import requests
file = open('total.txt','a')
main_page=1
while True:
	print main_page
	file.write(str(main_page)+'\n')
	website="https://archive.org/details/image?&sort=-downloads&page=%d"%main_page
	website=BeautifulSoup(requests.get(website).content)
	channeldiv=website.findAll("div",{"class":"collection-title C C2"})
	if type(channeldiv) is list:
		break
	else:
		for per_div in channeldiv:
			channel_page=1
			print per_div.find('a').find('div').string
			file.write(str(per_div.find('a').find('div').string)+'\n')
			while True:
				print channel_page
				file.write(str(channel_page)+'\n')
				channel_link= "https://archive.org"+per_div.find('a').get('href')+"?&sort=-downloads&page=%d"%channel_page
				channel_content= BeautifulSoup(requests.get(channel_link).content)
				channel_img=channel_content.findAll("img",{"class":"item-img"})
				if type(channel_img) is list:
					break
				else:
					for img in channel_img:
						img= img.get('source')
						m= "https://archive.org/services/img/"+img[14:]
						print m
						file.write(str(m)+'\n')
						
				channel_page+=1				
	main_page+=1
