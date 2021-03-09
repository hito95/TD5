#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:10:48 2021

@author: marwanmenaa
"""


class Book:
    
    def __init__(self, name):
        self.name = name
        self.id_order = 0
        self.list_order = []
        
    def insert_buy(self, quantity, price):
        self.id_order += 1
        print("--- Insert BUY " + str(quantity) + "@" + str(price) + " id=" + str(self.id_order) + " on " + self.name + '\n')
        i = 0
        while i<=len(self.list_order)-1 and price>self.list_order[i][2] and quantity>0:
            if self.list_order[i][3] == "SELL":
                counter = 0
                while self.list_order[i][1] - counter > 0 and quantity - counter > 0:
                    counter = counter + 1
                if self.list_order[i][1] - counter == 0:
                    self.list_order.pop(i)
                    i = i - 1
                elif self.list_order[i][1] - counter > 0:
                    self.list_order[i][1] -= counter
                print("Execute " + str(counter) + " at " + str(price) + " on " + str(self.name) + '\n')
            i = i + 1
        if i > len(self.list_order) - 1:
            self.list_order.insert(i+1,[self.id_order, quantity, price, "BUY"])
        elif quantity>0 and price<=self.list_order[i][2]:
                self.list_order.insert(i+1,[self.id_order, quantity, price, "BUY"])
        print("Book on " + str(self.name) + '\n')
        for obj in self.list_order:
            print(obj[3],obj[1],"@",obj[2], " id=",obj[0])
        print("----------------------------" + '\n')
    
    
    def insert_sell(self, quantity, price):
        self.id_order += 1
        print("--- Insert SELL " + str(quantity) + "@" + str(price) + " id=" + str(self.id_order) + " on " + str(self.name) + '\n')
        i = -1
        while i>=-len(self.list_order) and price<self.list_order[i][2] and quantity>0:
            if self.list_order[i][3] == "BUY":
                counter = 0
                while self.list_order[i][1] - counter > 0 and quantity - counter > 0:
                    counter = counter + 1
                if self.list_order[i][1] - counter == 0:
                    self.list_order.pop(i)
                    i = i + 1
                elif self.list_order[i][1] - counter > 0:
                    self.list_order[i][1] -= counter
                print("Execute " + str(counter) + " at " + str(price) + " on " + str(self.name) + '\n')
            i = i - 1
        if i < -len(self.list_order):
            self.list_order.insert(i+1,[self.id_order, quantity, price, "SELL"])
        elif quantity>0 and price>=self.list_order[i][2]:
                self.list_order.insert(i+1,[self.id_order, quantity, price, "SELL"])
        print("Book on " + str(self.name) + '\n')
        for obj in self.list_order:
            print(obj[3],obj[1],"@",obj[2], " id=",obj[0])
        print("----------------------------" + '\n')

def main():
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)
    
if __name__ == "__main__":
    main() 
