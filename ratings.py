"""Restaurant rating lister."""
#open file
import sys

filename = sys.argv[1]

#read and code into variables
def read_ratings(filename):

    ratingsfile = open(filename)
    rating_dict = {}

    for line in ratingsfile:
        line = line.rstrip()
        rating_list = line.split(":")

        #store information in dictionary
        rating_dict[rating_list[0]] = rating_list[1]

    print_dictionary(rating_dict)

    return rating_dict



def print_dictionary(rating_dict):
    sorted_tuples = sorted(rating_dict.items())
    for restaurant, rating in sorted_tuples:
        print("{} is rated at {}".format(restaurant, rating))

    #sorted_list = sorted(rating_dict)
    #for item in sorted_list:
    #    print("{} is rated at {}".format(item, rating_dict[item]))

def add_ratings(rating_dict):

    new_rest_name = input("Hello! Enter restaurant name. ")
    new_rest_rating = input("Enter restaunt rating. ")

    rating_dict[new_rest_name] = new_rest_rating

    print_dictionary(rating_dict)

add_ratings(read_ratings(filename))