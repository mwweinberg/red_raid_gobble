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


with open("names.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(holder)



#with open('names.csv', 'w') as csvfile:
#	fieldnames = ['key', 'headline', 'body']
#    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 #   	writer.writeheader()
#	length = len(holder)
#	for i in range(0-length):
		
 #   		writer.writerow({'key': holder[i][0] , 'headline': holder[i][1], 'body': holder[i][2]})
	


	
