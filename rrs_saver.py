from bs4 import BeautifulSoup
import urllib


#sets the URLs
h1 = "test_eng.htm"
h2 = "test2_eng.htm"


holder = {}



def headliner(url):
	soup = BeautifulSoup((open(url)), "lxml")
	head1 = soup.find_all(['h1','h2','h3'])
	body = soup.find_all('p')
	
	

	head1_fixed = str(head1)
	soup1 = BeautifulSoup(head1_fixed, 'lxml')
	gold = soup1.text.decode("unicode-escape").encode("utf-8")

	body_fixed = str(body)
	soup_gold = BeautifulSoup(body_fixed, 'lxml')
	gold_body = soup_gold.text.decode("unicode-escape").encode("utf-8")

	#this prints the headline and body to confirm that we got it

	print gold
	print ""
	print gold_body

	#this updates the dictionary
	
	
	holder['key'] = [gold, gold_body]
	
	print ""

headliner(h1)


# this prints the dictionary
print "**********"
print "**********"
print holder
print "**********"
print "**********"
	
