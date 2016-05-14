from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


# these are the variables to make up the URL and the unique ID

core1 = "http://paper.people.com.cn/rmrb/html/"
core2 = "/nw.D110000renmrb_"
core3 = "-01.htm"
#start all of these one below where you want to start because step 1 is +=1
#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year = 2013
month = 4
day = 5
story = 2

#initiates the dictionary to hold the output

holder = []

#this function takes the current website and adds the headlines to the holder dict

def headliner(url, uid):
	#opens the url for read access
	this_url = urllib.urlopen(url).read()
	#creates a new BS holder based on the URL
	soup = BeautifulSoup(this_url, 'lxml')
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])

	#body1 is all of the body text
	body1 = soup.find_all('p')
	
	#gets all the headline encoding right	
	
	head1_fixed = str(head1)
	soup1 = BeautifulSoup(head1_fixed, 'lxml')
	gold_head = soup1.text.decode("unicode-escape").encode("utf-8")

	#gets all of the body encoding right
	body1_fixed = str(body1)
	soup2 = BeautifulSoup(body1_fixed, 'lxml')
	gold_body = soup2.text.decode("unicode-escape").encode("utf-8")
	
	#creates the list and adds it to holder
	mini_holder = [uid, gold_head, gold_body]
	holder.append(mini_holder)

	
	

#walks through all of the days/months/years/stories

for i in range(0,2):
	year += 1
	year_fixed = str(year)
	
	for i in range(0,2):
		month += 1
		month_fixed = str(month).zfill(2)

		for i in range(0,2):
			
			day += 1
			#turns day into a string
			day_fixed = str(day).zfill(2)
			
			for i in range(0,2):
		
				story += 1
				story_fixed = str(story)

				unique_ID = year_fixed+"-"+month_fixed+"-"+day_fixed+"-"+story_fixed

				#this is the url 
				url_name = core1+year_fixed+"-"+month_fixed+"/"+day_fixed+core2+year_fixed+month_fixed+day_fixed+"_"+story_fixed+core3				
				#just so you can see it doing something
				print url_name
				print unique_ID
				print ""
				print ""
				#calls the headliner function
				headliner(url_name, unique_ID)
			
			story = 2

		day = 2

	#this resets the month to the starting point so it stays in the right 		range	
	month = 4

#writes a csv file called 'rrs_csv_gobble.csv'
with open('rrs_gobble_csv.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(holder)
