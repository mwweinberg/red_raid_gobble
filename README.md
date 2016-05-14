# red_raid_gobble

All you  need is rrs_gobble.py.  All of the rest of the files were for figuring things out and are described below.

This scraper pulls the full text of headlines and articles from the People's Daily.  The iteration process has been rationalized so that it works from smallest time to biggest time.  It goes through all of the days in a month, and then all of the months in a year, and then all of the years in that order.  Previous Red Raids did not have this rational flow which made it hard to troubleshoot when the script stopped in the middle.

rrs_logical_iterate.py - rrs.py but with the iteration tree fixed so that it works through in a logical way - all of the stories on the first day, then the next day, then the next month, then the next year.  

rrs_cleaner.py - used to verify that the search for headlines and search for body terms work to actually identify the headline and body. Require a local copy of a page.

rrs_saver.py - takes the uniqueID, headline, and body and tries to store them in a dictionary/list ({id: [headline, body]})

rrs_saver_csv.py - takes the dictionary created in rrs_saver.py and writes it to a csv file

rrs_dict_to_csv.py - a static dictionary that can be used to help test various ways to write dictionaries to csv files.

rrs_saver_list.py - creates the uid, head, and body and saves it in a list

rrs_saver_list_csv.py - takes the list from rrs_saver_list and outputs it to csv

rrs_saver_list_csv_iterate.py - takes rrs_saver_list_csv and adds to the list with a loop instead of hard coding the variable locations 
