# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:45:37 2016

@author: Rahul
"""


Rel = {'Pranav' : 'Rhea' ,  'Ataur' : 'Aastha'}

import random
class SocialNetworking:
    
    """
    profile_name : string
    city : string
    no_of_friends : integer
    in_a_relationship : Yes / No 
    """
    
    
    def __init__ (self,profile_name,city,no_of_friends):
        self.name = profile_name
        self.city = city
        self.friends = no_of_friends
        self.in_a_relationship = 'No'
        
    def GoOnDate(self):
        if self.name in Rel :
             self.in_a_relationship = 'Yes'
             
        else:
            self.in_a_relationship = 'No'
        
        
    def RelationshipStatus(self):
        if self.in_a_relationship == 'No' :
            print 'Single'
            
        else:
            print 'In A Relationship'
            
    def NameOfYourLove(self) :
        if self.in_a_relationship == 'Yes' :
                if self.name in Rel:
                   print Rel[self.name],"and You are made for each other"
        else:
            print "Sadddd! You're single!"
                
    def LoveCalculator(self):
        if self.in_a_relationship == 'Yes' :
            love_percent = random.randint(69,98)
            print "your love percent is",love_percent
        else:
            print "You're fucking single mannnn!"