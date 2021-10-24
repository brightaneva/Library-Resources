from Dictionary.urban_dictionary import urban_dic
from Dictionary.real_dictionary import free_dic
from helpers import store_data


#The urban dictionry
#is a dictionary of 
#profane meaning
#Not a real dictionary
urban = urban_dic("fuck")

#A real dictionary that returns defininitons and pronounciations of words
free_dic_api =  free_dic("example")


#call the store_data fuction to store the result as json
store_data(free_dic_api,"real_dictionary")