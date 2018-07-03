"""Restaurant rating lister."""
#open file
import sys

filename = sys.argv[1]


#read and code into variables

#Step1: retrieve each line
#Step2: remove whitestrip
#Step3: Split on :
def read_ratings(filename):

    ratingsfile = open(filename)
    rating_dict = {}

    for line in ratingsfile:
        line = line.rstrip()
        rating_list = line.split(":")

    #store information in dictionary

        rating_dict[rating_list[0]] = rating_list[1]

    print_dictionary(rating_dict)
    # sorted_tuples = sorted(rating_dict.items())
    # for restaurant, rating in sorted_tuples:
    #     print("{} is rated at {}".format(restaurant, rating))

    #sort the dictionary
    #sorted_list = sorted(rating_dict)
    #for item in sorted_list:
    #    print("{} is rated at {}".format(item, rating_dict[item]))

    return rating_dict
    #for each key, find the matching value and return that value


def print_dictionary(rating_dict):
    sorted_tuples = sorted(rating_dict.items())
    for restaurant, rating in sorted_tuples:
        print("{} is rated at {}".format(restaurant, rating))

def add_ratings(rating_dict):

    new_rest_name = input("Hello! Enter restaurant name. ")
    new_rest_rating = input("Enter restaunt rating. ")

    rating_dict[new_rest_name] = new_rest_rating

    print_dictionary(rating_dict)

    # sorted_tuples = sorted(rating_dict.items())
    # for restaurant, rating in sorted_tuples:
    #     print("{} is rated at {}".format(restaurant, rating))

    # sorted_list = sorted(rating_dict)
    # for item in sorted_list:
    #     print("{} is rated at {}".format(item, rating_dict[item]))


add_ratings(read_ratings(filename))