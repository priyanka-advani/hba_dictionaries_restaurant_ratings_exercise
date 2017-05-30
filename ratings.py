
# import sys


# new_restaurant = raw_input("What was the last restaurant you went to? ")
# new_restaurant_rating = raw_input("Rate that restaurant on a scale of 1 to 5\n\
#         1 is terrible, 5 is excellent: ")


# def list_restaurant_ratings(text_file):
#     """Restaurant rating lister."""

#     # text_file is .txt file that contains list of restaurants and their ratings
#     text_file = open(text_file)

#     restaurant_ratings = {}

#     # add user's restaurant and rating to restaurant_ratings dict
#     restaurant_ratings[new_restaurant] = new_restaurant_rating

#     # for loop iterates over lines in text_file
#     # text in text_file to the left of each colon will be key in dict
#     # text to the right of each colon will be value in dict
#     for line in text_file:
#         line = line.rstrip()
#         restaurant, rating = line.split(":")
#         restaurant_ratings[restaurant] = rating

#     # used sorted() function to return rest list in alphabetical order
#     for restaurant, rating in sorted(restaurant_ratings.items()):
#         print "{} is rated at {}".format(restaurant, rating)

#     return restaurant_ratings

# list_restaurant_ratings("scores.txt")


def print_restaurant_ratings(rest_dict):

    for restaurant, rating in sorted(rest_dict.items()):
        print "{} is rated at {}".format(restaurant, rating)

def get_user_rest_rating(rest_dict):

    new_restaurant = raw_input("What was the last restaurant you went to? ")

    while True:
    
        new_restaurant_rating = int(raw_input("Enter a rating on a scale of 1 to 5\n\
            1 is terrible, 5 is excellent: "))

        if new_restaurant_rating in range(1, 6):
            rest_dict[new_restaurant] = new_restaurant_rating
            break

        else:
            print "That's not a valid rating"


def import_rest_ratings(text_file, rest_dict):

    text_file = open(text_file)

    for line in text_file:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        rest_dict[restaurant] = rating
