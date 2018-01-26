# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:17:57 2018

@author: Crystal Gong

Find all of the pure strategy Bayesian Nash equilibria of the voting game. 

2 jurors, p>q, q> 1/2
Strategy {(C,A)x(C,A)} (guilty, innocent)
"""
p= 5/6
q = 4/6

def f1(p, q):
    ans = q
    print(ans)

def f2(p, q):
    ans = 1-p
    print(ans)
    
def f3(p, q):
    ans = p
    print(ans)
    
def f4(p, q):
    ans = 1-q
    print(ans)
    print('____')
    
def f5(p, q):
    ans = 1-p
    print(ans)

def f6(p, q):
    ans = (1-p)*(1-p)*q +(1-p*p)*(1-q)
    print(ans)
    
def f7(p, q):
    ans = p*(1-p)*q +(1-p*(1-p))*(1-q)
    print(ans)
    
def f8(p, q):
    ans = 1-q
    print(ans)
    print('____')
    
def f9(p, q):
    ans = p
    print(ans)

def f10(p, q):
    ans = p*(1-p)*q +(1-p*(1-p))*(1-q)
    print(ans)
    
def f11(p, q):
    ans = p*p*q +(1-(1-p)*(1-p))*(1-q)
    print(ans)
    
def f12(p, q):
    ans = 1-q
    print(ans)
    print('____')
    
def f13(p, q):
    ans = 1-q
    print(ans)

def f14(p, q):
    ans = 1-q
    print(ans)
    
def f15(p, q):
    ans = 1-q
    print(ans)
    
def f16(p, q):
    ans = 1-q
    print(ans)
    print('____')
    
for i in range (1, 17):
    fun = "f" + str(i) + "(p,q)"
    eval(fun)