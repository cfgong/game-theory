# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:39:17 2018

@author: Crystal Gong

Exercise 12.3 in the Game Theory by Steven Tadelis. 
Armed Conﬂict: Consider the following strategic situation: Two rival armies plan to seize a disputed territory. Each army’s general can choose either to attack (A) or to not attack (N). In addition, each army is either strong (S) or weak (W) with equal probability, and the realizations for each army are independent. Furthermore the type of each army is known only to that army’s general. An army can capture the territory if either (i) it attacks and its rival does not or (ii) it and its rival attack, but it is strong and the rival is weak. If both attack and are of equal strength then neither captures the territory. As for payoffs, the territory is worth m if captured and each army has a cost of ﬁghting equal to s if it is strong and w if it is weak, where s<w. If an army attacks but its rival does not, no costs are borne by either side. Identify all the pure-strategy Bayesian Nash equilibria of this game for the following two cases, and brieﬂy describe the intuition for your results: 

The action spaces of the two armies are A1 = A2 ={A, N}. (A  = attack, N = not attack)
The type spaces of the two armies are T1 = T2 = {S, W}. (S = strong, W = weak). Since, each army is either strong (S) or weak (W) with equal probability, Pr(S) = Pr(W) = ½. 
The strategy sets are S1 = S2 = {AA, AN, NA, NN} (AA = always attack, AN = attack if strong, but not attack if weak, NA = attack if weak, but not if strong, NN = never attack)


This is a brute force method to solve for the payoff matrix. 
To calculate the payoffs without computing the formulas use if statements to check who would win, in each scenario. 
"""

####

M = 3
w = 4
s = 2

###

def f1(M,s,w):
    ans1 = M/4 - (s + w)/2
    ans2 = M/4 - (s + w)/2
    print("AA, AA, ({0},{1})".format(ans1, ans2))

def f2(M,s,w):
    ans1 = (M/4) - (s/2)
    ans2 = M/2 - (s + w)/4
    print("AN, AA, ({0},{1})".format(ans1, ans2))
    
def f3(M,s,w):
    ans1 = -w/2
    ans2 = 3*M/4 - (s + w)/4
    print("NA, AA, ({0},{1})".format(ans1, ans2))
    
def f4(M,s,w):
    ans1 = 0
    ans2 = M
    print("NN, AA, ({0},{1})".format(ans1, ans2))
    
def f5(M,s,w):
    ans1 = M/2 - (s+w)/4
    ans2 = (M/4) - (s/2)
    print("AA, AN, ({0},{1})".format(ans1, ans2))

def f6(M,s,w):
    ans1 = (M-s)/4
    ans2 = (M-s)/4
    print("AN, AN, ({0},{1})".format(ans1, ans2))
    
def f7(M,s,w):
    ans1 = (M-w)/4
    ans2 = M/2 - s/4
    print("NA, AN, ({0},{1})".format(ans1, ans2))

def f8(M,s,w):
    ans1 = 0
    ans2 = M/2
    print("NN, AN, ({0},{1})".format(ans1, ans2))
    
def f9(M,s,w):
    ans1 = 3*M/4 - (s+w)
    ans2 = -w/2
    print("AA, NA, ({0},{1})".format(ans1, ans2))
    
def f10(M,s,w):
    ans1 = M/2 - s/4
    ans2 = (M-w)/4
    print("AN, NA, ({0},{1})".format(ans1, ans2))
    
def f11(M,s,w):
    ans1 = (M-w)/4
    ans2 = (M-w)/4
    print("NA, NA, ({0},{1})".format(ans1, ans2))
    
def f12(M,s,w):
    ans1 = 0
    ans2 = M/2
    print("NN, NA, ({0},{1})".format(ans1, ans2))
    
def f13(M,s,w):
    ans1 = M
    ans2 = 0
    print("AA, NN, ({0},{1})".format(ans1, ans2))
    
def f14(M,s,w):
    ans1 = M/2
    ans2 = 0
    print("AN, NN, ({0},{1})".format(ans1, ans2))
    
def f15(M,s,w):
    ans1 = M/2
    ans2 = 0
    print("NA, NN, ({0},{1})".format(ans1, ans2))
    
def f16(M,s,w):
    ans1 = 0
    ans2 = 0
    print("NN, NN, ({0},{1})".format(ans1, ans2))
    
for i in range (1, 17):
    fun = "f" + str(i) + "(M,s,w)"
    eval(fun)
    
    
    
    
    
    
    
    