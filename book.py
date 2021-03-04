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
        
        a = -1
        
        self.id_order += 1
        
        for i in range(len(self.list_order)):
            temp = self.list_order[i]
            if price <= temp[2] and temp[3] == "BUY":
                a = i
            elif temp[3] == "SELL":
                break
        if a < 0 :
            self.list_order.append([self.id, quantity, price, "SELL"])
        elif a > 0 :
            
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
