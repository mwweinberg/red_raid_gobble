from bs4 import BeautifulSoup
import urllib
import csv


#sets the URLs
h1 = "test_eng.htm"
h2 = "test2_eng.htm"


holder = []



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

	#print gold
	#print ""
	#print gold_body

	#this updates the list by first creating a list of the results
	# and then adding them to the existing list
	
	mini_holder = ['uid', gold, gold_body]
	holder.append(mini_holder)
	
	

headliner(h1)
headliner(h2)



with open('names.csv', 'w') as csvfile:
	fieldnames = ['key', 'headline', 'body']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    	writer.writeheader()
    	writer.writerow({'key': holder[0][0] , 'headline': holder[0][1], 'body': holder[0][2]})
	writer.writerow({'key': holder[1][0] , 'headline': holder[1][1], 'body': holder[1][2]})


	
