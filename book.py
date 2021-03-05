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
        self.list_order.append([self.id, quantity, price, "BUY"])
        return quantity, price
    
    
    def insert_sell(self, quantity, price):
        self.id_order += 1
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
            i = i - 1
        if i < len(self.list_order):
            self.list_order.insert(i+1,[self.id, quantity, price, "SELL"])
        elif quantity>0 and price>=self.list_order[i][2]:
                self.list_order.insert(i+1,[self.id, quantity, price, "SELL"])
        self.list_order.append([self.id, quantity, price, "SELL"])
        return quantity, price


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
