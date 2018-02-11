#! /usr/bin/python
"""
Sophie Hannah
CSC 217 470

Implement a class Address. The address has a house number, a street, an optional apartment number, a city, state and postal code. 

define constructor so object can be created in 2 ways; with apartment number, or without. supply print method that prints address on one line
and city, state, postal code on the next.

supply def comesBefore(self, other) that tests whether this address comes before other by comparing postal codes.
"""
import errno
import os

class Address() :
    def __init__(self, house, city, state, postal_code, apt = ' '):
        """initialize the variables for the class, remember, apartment is an optional parameter. """
        self.house = house
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.apt = apt

    def create_address(self) :
        if self.apt :
            preprogrammed_houses = self.house + ", " + self.apt + "\n" + self.city + ", " + self.state + ", " + str(self.postal_code) 
            print preprogrammed_houses         
            return preprogrammed_houses 

        else :
            preprogrammed_house = self.house + "\n" + self.city + ", " + self.state + ", " + str(self.postal_code)

            print preprogramed_house 
            return preprogrammed_house

    def comes_before(self, other) :
        """  this will ask a user where they live and compare the zip codes of two locations."""
        ray_gun = raw_input("What is your address? " )
        anti_tank_gun = raw_input("What city are you in? ")
        drone = raw_input("What state? " )
        captive = int(raw_input("What zip code do you inhabit? "))
        if captive > self.postal_code :
            print "Your postal address falls behind the previous address. "
        else :
            print "Your postal address should be listed ahead. "

        nuclear_missile = raw_input("Do you live in an apartment? enter y if so, or q to continue.")
        try :
            if nuclear_missile == 'y' :
                num = raw_input("Enter the number: ")
                my_address = ray_gun + ", " + num + "\n" + anti_tank_gun + ", " + drone + ", "+ str(captive)

                print my_address
                return my_address

            elif nuclear_missile == 'q' :
                my_address = ray_gun + "\n" + anti_tank_gun + ", " + drone + ", " + str(captive)

                print my_address
                return my_address

        except IOError as e :
            print "Not valid input try again."
def main() :
    your_address = Address('2 15th St. NW', 'Washington', 'DC', int('20024'))
    your_address.create_address()
    """ the ' ' will allow the user to input their information. """
    your_address.comes_before(' ')

main()

