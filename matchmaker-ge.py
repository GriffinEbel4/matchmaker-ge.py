Intro = '''
              Griffin's Match Maker!
        00000000000___________000000000000
      00000000_____00000___000000_____0000000
    0000000_____________000______________00000
   0000000_______________0_________________0000
  000000 _~Are you compatable with me?~_____0000
  00000___This little program will help______0000
 00000____answer this through a series _____00000
 00000_____of 5 questions that reveal______000000
  000000_____how compatable we are!______0000000
   0000000__________~Have fun!~_________0000000
     000000____________________________000000
       000000________________________000000
          00000_____________________0000
             0000_________________0000
               0000_____________000
                 000_________000
                    000_____00
                      00__00
                        00
AKA: The "Are You Capatable With Griffin?" Experience

instructions: 
For each statement, enter the corresponding number for how strongly you agree or disagree with what was said
5-Highly agree
4-Kinda agree
3-Ehhhhh....
2-Kinda disagree
1-I despise what is being stated
'''
Statement1='''
  *💖💖💖💖*
 Statement 1
*💖💖💖💖*
'''
Statement2='''
  *💖💖💖💖*
 Statement 2
*💖💖💖💖*
'''
Statement3='''
  *💖💖💖💖*
 Statement 3
*💖💖💖💖*
'''
Statement4='''
  *💖💖💖💖*
 Statement 4
*💖💖💖💖*
'''
Statement5='''
  *💖💖💖💖*
 Statement 5
*💖💖💖💖*
'''

print(Intro)
v= "Cats are the superior pet."
w= "Go pack Go!"
x= "The muppets are underappreciated"
y= "Brownies are an amazing dessert"
z= "Double decker couches are a revolutionary innovation"

dr1=3
dr2=1
dr3=5
dr4=2
dr5=4

unweightedMaximumCompatability=5
weightedMaximumCompatability=15

import io, os, sys, time
import functools
from typing import Counter

compatability= []
#1
while True:
    try:
      print(Statement1)
      userResponse1 = int(input(v))
      desiredResponse1 = dr1
      #weight of 1
      gme1= 5 - abs(userResponse1-desiredResponse1)
      combatability1 =  gme1
      compatability.append(combatability1)
      if userResponse1 == 1:
        print("")
        print ("My rating: " + str(desiredResponse1))
        print("")
        print ("Compatability: " + str(combatability1))
        weightedCompatability1= (combatability1 * 1)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability1))
        print("")
        print("A liitle mean dont you think?")
        print("")
        break;
      elif userResponse1 == 2:
          print("")
          print ("My rating: " + str(desiredResponse1))
          print("")
          print ("Compatability: " + str(combatability1))
          weightedCompatability1= (combatability1 * 0.5)
          print("")
          print ("Weighted Compatability: " + str(weightedCompatability1))
          print("")
          print("Come on, cats are adorable.")
          print("")
          break;
      elif userResponse1 == 3:
          print("")
          print ("My rating: " + str(desiredResponse1))
          print("")
          print ("Compatability: " + str(combatability1))
          weightedCompatability1= (combatability1 * 0.75)
          print("")
          print ("Weighted Compatability: " + str(weightedCompatability1))
          print("")
          print("Cats and dogs are on the same level")
          print("")
          break;
      elif userResponse1 == 4:
          print("")
          print ("My rating: " + str(desiredResponse1))
          print("")
          print ("Compatability: " + str(combatability1))
          weightedCompatability1= (combatability1 * 0.9)
          print("")
          print ("Weighted Compatability: " + str(weightedCompatability1))
          print("")
          print("Are they really better than dogs?")
          print("")
          break;
      elif userResponse1 == 5:
          print("")
          print ("My rating: " + str(desiredResponse1))
          print("")
          print ("Compatability: " + str(combatability1))
          weightedCompatability1= (combatability1 * 0.8)
          print("")
          print ("Weighted Compatability: " + str(weightedCompatability1))
          print("")
          print("Crazy cat lady I presume?")
          print("")
          break;
      else:
          print("")
          print("Do you know how to read directions? 1-5 only!")
          print("")
          continue
    except ValueError:
      print("")
      print("A word? Really? 1-5 only!")
      print("")
    continue   
#2
while True:
    try:
      print(Statement2)
      userResponse2 = int(input(w))
      desiredResponse2 = dr2
      #weight of 1
      gme2= 5 - abs(userResponse2-desiredResponse2)
      combatability2 =  gme2
      compatability.append(combatability2)
      if userResponse2 == 1:
        print("")
        print ("My rating: " + str(desiredResponse2))
        print("")
        print ("Compatability: " + str(combatability2))
        weightedCompatability2= (combatability2 * 3)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability2))
        print("")
        print("Bear down.")
        print("")
        break;
      elif userResponse2 == 2:
        print("")
        print ("My rating: " + str(desiredResponse2))
        print("")
        print ("Compatability: " + str(combatability2))
        weightedCompatability2= (combatability2 * 2.5)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability2))
        print("")
        print("Liking them slightly is just too much.")
        print("")
        break;
      elif userResponse2 == 3:
        print("")
        print ("My rating: " + str(desiredResponse2))
        print("")
        print ("Compatability: " + str(combatability2))
        weightedCompatability2= (combatability2 * 2.25)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability2))
        print("")
        print("Shame on you.")
        print("")
        break;
      elif userResponse2 == 4:
        print("")
        print ("My rating: " + str(desiredResponse2))
        print("")
        print ("Compatability: " + str(combatability2))
        weightedCompatability2= (combatability2 * 2)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability2))
        print("")
        print("Disgraceful.")
        print("")
        break;
      elif userResponse2 == 5:
        print("")
        print ("My rating: " + str(desiredResponse2))
        print("")
        print ("Compatability: " + str(combatability2))
        weightedCompatability2= (combatability2 * 2)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability2))
        print("")
        print("Despicable me? No. Despicable you.")
        print("")
        break;
      else:
        print("")
        print("Do you know how to read directions? 1-5 only!")
        print("")
        continue
    except ValueError:
      print("")
      print("A word? Really? 1-5 only!")
      print("")
    continue
#3
while True:
    try:
      print(Statement3)
      userResponse3 = int(input(x))
      desiredResponse3 = dr3
      #weight of 1
      gme3= 5 - abs(userResponse3-desiredResponse3)
      combatability3 =  gme3
      compatability.append(combatability3)
      if userResponse3 == 1:
        print("")
        print ("My rating: " + str(desiredResponse3))
        print("")
        print ("Compatability: " + str(combatability3))
        weightedCompatability3= (combatability3 * 2.25)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability3))
        print("")
        print("No childhood detected.")
        print("")
        break;
      elif userResponse3 == 2:
        print("")
        print ("My rating: " + str(desiredResponse3))
        print("")
        print ("Compatability: " + str(combatability3))
        weightedCompatability3= (combatability3 * 2.5)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability3))
        print("")
        print("What a shame.")
        print("")
        break;
      elif userResponse3 == 3:
        print("")
        print ("My rating: " + str(desiredResponse3))
        print("")
        print ("Compatability: " + str(combatability3))
        weightedCompatability3= (combatability3 * 2.75)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability3))
        print("")
        print("This isn't an isse to be indifferent upon.")
        print("")
        break;
      elif userResponse3 == 4:
        print("")
        print ("My rating: " + str(desiredResponse3))
        print("")
        print ("Compatability: " + str(combatability3))
        weightedCompatability3= (combatability3 * 2.8)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability3))
        print("")
        print("Respectable viewpoint.")
        print("")
        break;
      elif userResponse3 == 5:
        print("")
        print ("My rating: " + str(desiredResponse3))
        print("")
        print ("Compatability: " + str(combatability3))
        weightedCompatability3= (combatability3 * 3)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability3))
        print("")
        print("A man of respect and dignity I see.")
        print("")
        break;
      else:
        print("")
        print("Do you know how to read directions? 1-5 only!")
        print("")
        continue
    except ValueError:
      print("")
      print("A word? Really? 1-5 only!")
      print("")
    continue
#4
while True:
    try:
      print(Statement4)
      userResponse4 = int(input(y))
      desiredResponse4 = dr4
      #weight of 1
      gme4= 5 - abs(userResponse4-desiredResponse4)
      combatability4 =  gme4
      compatability.append(combatability4)
      if userResponse4 == 1:
        print("")
        print ("My rating: " + str(desiredResponse4))
        print("")
        print ("Compatability: " + str(combatability4))
        weightedCompatability4= (combatability4 * 1.8)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability4))
        print("")
        print("It's impressive you dislike them more than me.")
        print("")
        break;
      elif userResponse4 == 2:
        print("")
        print ("My rating: " + str(desiredResponse4))
        print("")
        print ("Compatability: " + str(combatability4))
        weightedCompatability4= (combatability4 * 2)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability4))
        print("")
        print("Exactly, the most overrated dessert option of all time.")
        print("")
        break;
      elif userResponse4 == 3:
        print("")
        print ("My rating: " + str(desiredResponse4))
        print("")
        print ("Compatability: " + str(combatability4))
        weightedCompatability4= (combatability4 * 1.75)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability4))
        print("")
        print("Cavity Conuisuier.")
        print("")
        break;
      elif userResponse4 == 4:
        print("")
        print ("My rating: " + str(desiredResponse4))
        print("")
        print ("Compatability: " + str(combatability4))
        weightedCompatability4= (combatability4 * 1.6)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability4))
        print("")
        print("I'll be picking the resturaunt.")
        print("")
        break;
      elif userResponse4 == 5:
        print("")
        print ("My rating: " + str(desiredResponse4))
        print("")
        print ("Compatability: " + str(combatability4))
        weightedCompatability4= (combatability4 * 1.5)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability4))
        print("")
        print("Get better taste buds.")
        print("")
        break;
      else:
        print("")
        print("Do you know how to read directions? 1-5 only!")
        print("")
        continue
    except ValueError:
      print("")
      print("A word? Really? 1-5 only!")
      print("")
    continue
#5
while True:
    try:
      print(Statement5)
      userResponse5 = int(input(z))
      desiredResponse5 = dr5
      #weight of 1
      gme5= 5 - abs(userResponse5-desiredResponse5)
      combatability5 =  gme5
      compatability.append(combatability5)
      if userResponse5 == 1:
        print("")
        print ("My rating: " + str(desiredResponse5))
        print("")
        print ("Compatability: " + str(combatability5))
        weightedCompatability5= (combatability5 * .50)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability5))
        print("")
        print("You are afraid of the future.")
        print("")
        break;
      elif userResponse5 == 2:
        print("")
        print ("My rating: " + str(desiredResponse5))
        print("")
        print ("Compatability: " + str(combatability5))
        weightedCompatability5= (combatability5 * .60)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability5))
        print("")
        print("You are made foolish by your lack of vision.")
        print("")
        break;
      elif userResponse5 == 3:
        print("")
        print ("My rating: " + str(desiredResponse5))
        print("")
        print ("Compatability: " + str(combatability5))
        weightedCompatability5= (combatability5 * .75)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability5))
        print("")
        print("The world is changing, you have to be ready.")
        print("")
        break;
      elif userResponse5 == 4:
        print("")
        print ("My rating: " + str(desiredResponse5))
        print("")
        print ("Compatability: " + str(combatability5))
        weightedCompatability5= (combatability5 * 1)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability5))
        print("")
        print("A true visionary.")
        print("")
        break;
      elif userResponse5 == 5:
        print("")
        print ("My rating: " + str(desiredResponse5))
        print("")
        print ("Compatability: " + str(combatability5))
        weightedCompatability5= (combatability5 * .9)
        print("")
        print ("Weighted Compatability: " + str(weightedCompatability5))
        print("")
        print("Dare I say it, your vision might've become too big for its own briches.")
        print('')
        break;
      else:
        print("")
        print("Do you know how to read directions? 1-5 only!")
        print("")
        continue
    except ValueError:
      print("")
      print("A word? Really? 1-5 only!")
      print("")
    continue

time.sleep(1)

totalUnweightedCompatibility = 0
for c in compatability:
	totalUnweightedCompatibility += c

totalUnweightedCompatibility *= 20 / unweightedMaximumCompatability

weightedTotalCompatibility= (weightedCompatability1+ weightedCompatability2+ weightedCompatability3+ weightedCompatability4+weightedCompatability5)

weightedTotalCompatibility *= 30/ weightedMaximumCompatability

print("Calculating compatibility score.")
def countdown (t):
  while t > 0:
    print(t)
    t -= 1
    time.sleep(1)
    print("Calculating...")

seconds= 3
countdown(seconds)
print("")
print("calculated!")
print("")

print("Total Unweighted Score: %d\n" % (totalUnweightedCompatibility))
("%")
print("Total Weighted Compatibility: %d\n" % (weightedTotalCompatibility))
("%")
if weightedTotalCompatibility == 100:
  print("It was meant to be")
  print("")
elif weightedTotalCompatibility>=80 and weightedTotalCompatibility<100:
  print("Looks promising")
  print("")
elif weightedTotalCompatibility<80 and weightedTotalCompatibility>=60:
  print("Maybe we can talk things out.") 
  print("or maybe just be friend?")
  print("")
elif weightedTotalCompatibility<60 and weightedTotalCompatibility>=50:
  print("Doesnt look too promising for us")
  print("")
elif weightedTotalCompatibility <50:
  print("We weren't meant to be")
  print("")
print("Thank you for matchmaking!")