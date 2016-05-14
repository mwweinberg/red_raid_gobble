from bs4 import BeautifulSoup
import urllib


#sets the URLs
h1 = "test_eng.htm"
h2 = "test2_eng.htm"


# need to either figure out how to skip "None" results or turn search_all into a string



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

	print gold
	print ""
	print gold_body
	
	#print gold[0].get_text()
	
	#print head1[1].get_text()
	#print head2[2].get_text()
	
	
	#print head2
	
	#print head3
	
	print ""

headliner(h1)
headliner(h2)
	
