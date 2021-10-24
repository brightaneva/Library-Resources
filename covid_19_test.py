#Import the Covid_19 module
#call a fuction in the module
#and call the store_data moduel 
#to store the result as json data

from Stats_on_Covid.covid_stats import Covid_19 as cvd
from helpers import store_data

#return all countries affected with covid
all_affected_coun = cvd.coun_affected()

#return the stats on covid in a country in a particular date
his_on_date = cvd.history_coun("canada","2020-12-01")

#returns all countries statictics on covid-19
all_countries = cvd.all_coun_stats()

#returns current stats on covid in a particular country
one_country = cvd.stats_on_coun("ghana")

#call the store_data fuc in the module and store your results
store_data(all_affected_coun,"all_affected_coun")



