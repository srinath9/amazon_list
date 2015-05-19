from bs4 import BeautifulSoup
import requests


fopen = open('Amaz.html','r')
soup = BeautifulSoup(fopen.read())

def get_request(z):
	r = requests.get(z)

def get_class_feature(z,class_name,fopen):
	print "printing the data into files"
	soup = BeautifulSoup(z.text)
	fopen.write("giving the "+class_name)
	for link in soup.findAll('div',{'class' : class_name}):
		print "data classs into the file"
		print link.find('a')['href']
		fopen.write(link.find('a')['href']+'\n')

def get_span(z,class_name,fopen):
	print "printing the data into files"
	soup = BeautifulSoup(z.text)
	fopen.write("giving the "+class_name)
	for link in soup.findAll('span',{'class' : class_name}):
		print "data classs into the file"
		fopen.write(link.get('src')+'\n')

list_name = open("names.txt",'w')

for link in soup.findAll('a',{'class':'nav_a'}):
	filename =str(link.text)
	filename = filename.replace('.','_').replace(" ","") + '.html'
	print link.text
	fopen = open(filename,'w')
	href = link.get('href')
	print  link.get('href')

	try:		
		next_page = requests.get(href)
		fopen.write(str(BeautifulSoup(next_page.text))
   
	except :
		print "some problem"
		
	         
