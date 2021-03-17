#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:10:48 2021

@author: marwanmenaa et gael tu mas oublié
"""
import pandas as pd

class Book:
    
    def __init__(self, name):
        self.name = name
        self.id_order = 0
        self.list_order = []
        self.df = pd.DataFrame(self.list_order,columns=['id', 'Quantity', 'Price','Type'])
        
    def insert_buy(self, quantity, price):
        self.id_order += 1
        print("--- Insert BUY " + str(quantity) + "@" + str(price) + " id=" + str(self.id_order) + " on " + self.name)
        i = -1
        while i>=-len(self.list_order) and price>=self.list_order[i][2] and quantity>0:
            if self.list_order[i][3] == "SELL":
                counter = 0
                while self.list_order[i][1] - counter > 0 and quantity - counter > 0:
                    counter = counter + 1
                print("Execute " + str(counter) + " at " + str(self.list_order[i][2]) + " on " + str(self.name))
                if self.list_order[i][1] - counter == 0:
                    self.list_order.pop(i)
                    quantity -= counter
                    i = i + 1
                elif self.list_order[i][1] - counter > 0:
                    self.list_order[i][1] -= counter
                    quantity -= counter
            elif price==self.list_order[i][2]:
                break
            i = i - 1
        if i < -len(self.list_order) and quantity>0:
            self.list_order.insert(i,[self.id_order, quantity, price, "BUY"])
        elif quantity>0 and price<=self.list_order[i][2]:
            if self.list_order[i][2] == price:
                if i+1<0:
                    self.list_order.insert(i+1,[self.id_order, quantity, price, "BUY"])
                else:
                    self.list_order.insert(len(self.list_order),[self.id_order, quantity, price, "BUY"])
            else:
                if i+1<0:
                    self.list_order.insert(i+1,[self.id_order, quantity, price, "BUY"])
                else:
                    self.list_order.insert(len(self.list_order),[self.id_order, quantity, price, "BUY"])
        
        print("Book on " + str(self.name))
        for obj in self.list_order:
            print("       ",obj[3],obj[1],"@",obj[2], "id=",obj[0])
        
        print('\n')
        print("—— Pandas visualization ——")
        self.df = self.df.iloc[0:0]
        for i in range(len(self.list_order)):
            self.df.at[i,'id'] = self.list_order[i][0]
            self.df.at[i,'Quantity'] = self.list_order[i][1]
            self.df.at[i,'Price'] = self.list_order[i][2]
            self.df.at[i,'Type'] = self.list_order[i][3]
        print(self.df)
        print("----------------------------")
        
        return self.list_order
    
    
    def insert_sell(self, quantity, price):
        self.id_order += 1
        print("--- Insert SELL " + str(quantity) + "@" + str(price) + " id=" + str(self.id_order) + " on " + str(self.name))
        i = 0
        while i<=len(self.list_order) - 1 and price<=self.list_order[i][2] and quantity>0:
            if self.list_order[i][3] == "BUY":
                counter = 0
                while self.list_order[i][1] - counter > 0 and quantity - counter > 0:
                    counter = counter + 1
                print("Execute " + str(counter) + " at " + str(self.list_order[i][2]) + " on " + str(self.name))
                if self.list_order[i][1] - counter == 0:
                    self.list_order.pop(i)
                    quantity -= counter
                    i = i - 1
                elif self.list_order[i][1] - counter > 0:
                    self.list_order[i][1] -= counter
                    quantity -= counter
            elif price==self.list_order[i][2]:
                break
            i = i + 1
        if i > len(self.list_order) - 1 and quantity>0:
            self.list_order.insert(i,[self.id_order, quantity, price, "SELL"])
        elif quantity>0 and price>=self.list_order[i][2]:
            if self.list_order[i][2] == price:
                self.list_order.insert(i,[self.id_order, quantity, price, "SELL"])
            else:
                self.list_order.insert(i,[self.id_order, quantity, price, "SELL"])
       
        print("Book on " + str(self.name))
        for obj in self.list_order:
            print("       ",obj[3],obj[1],"@",obj[2],"id=",obj[0])
                
        print('\n')
        print("—— Pandas visualization ——")
        self.df = self.df.iloc[0:0]
        for i in range(len(self.list_order)):
            self.df.at[i,'id'] = self.list_order[i][0]
            self.df.at[i,'Quantity'] = self.list_order[i][1]
            self.df.at[i,'Price'] = self.list_order[i][2]
            self.df.at[i,'Type'] = self.list_order[i][3]
        print(self.df)
        print("----------------------------")
        
        return self.list_order
    