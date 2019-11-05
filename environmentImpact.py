# even as the condition of our planet worsens, we are failing to react and protect our environment. current funding for environmental efforts is little to none, so its important that each person realizes their individual responsibilites in term of helping to combat climate change

print ("Answer the following questions with the corresponding number to determine your environmental fooprint.")

# input statements to take in user data to begin calculations
regularTransportation = int(input("\nEstimate the number of miles you travel a year. \n  1.8,000 or less \n  2.8,000 - 10,000 \n  3.10,000 - 12,000 \n  4.12,000 or more \nanswer: "))
energy = int(input("\nHow much energy does your household use per year? \n  1.700 or less kWh \n  2.700 - 900 kWh \n  3.900 - 11,000 kWh \n  4.11,000 or more kWh \nanswer: "))
waste = int(input("\nHow much waste do you produce in a week (compared to others who live nearby) \n  1.less \n  2.same \n  3.more \n  4.much more \nanswer: "))
water = int(input("\nHow much water does your household use per day? \n  1.100 gallons or less \n  2.100 - 200 gallons \n  3.200 - 300 gallons \n  4.300 gallons or more \nanswer: "))
diet = int(input("\nHow often do you eat meet? \n  1.never(vegan) \n  2.rarely(vegetarian) \n  3.sometimes(2-3 times a week) \n  4.often(4-5 times a week) \nanswer: "))
schoolTransportation = int(input("\nHow do you get to school? \n  1.walking/bike \n  2.bus \n  3.carpool \n  4.car \nanswer: "))
houseSize = int(input("\nEstimate the size of your house. \n  1.500 sq ft or less \n  2.500 - 1000 sq ft \n  3.1000 - 5000 sq ft \n  4.5000 sq ft or more \nanswer: "))

# this line of code allows the user to change their mind and just get facts about the environment rather than 
suggestionsOrNot = str(input("\nIf you still want your score, type 'YES', if you just want suggestions on how to better conserve, type 'NO', and if you want both your score and randomized facts, type 'YES2'\nanswer: "))

# converison variable to account for the importance of each factor and determine a score on a scale of 1-4
def scaleAndAverage():
  scaleFormula = (regularTransportation * 5) + (energy * 4) + (waste * 4) + (water * 4) + (diet * 3) + (regularTransportation * 2) + (houseSize * 2)
  average = float(scaleFormula / 24)
  print ("\nHere is your score on a scale of 1-4.")
  print (float(average))

# conditional statements to give users feedback based on their scores, offer suggestions, or both
if (suggestionsOrNot == "YES"):
  average = 0
  scaleAndAverage()
  if (average >= 1 or average < 2):
    print ("\nWow! Your score shows that your impact on the environment is minimal and well below average.")
  elif (average >= 2 or average < 3):
    print ("\nNice! Your score shows that your impact on the environment is roughly the average.")
  elif (average >= 3 or average <= 4):
    print ("\nYikes! Your score shows that your impact on the environment high and well above average.")
elif(suggestionsOrNot == "NO"):
  facts = str(input("\nWhat kind of fact would you like to view? (water, energy, transportation) \nanswer: "))
  if (facts == "water"):
    print ("\nThe average American household uses 90 gallons of water per day. Much of this comes from sprinkler systems and flushing the toilet. To combat this issue, people should sotp taking baths and switch to water-efficient toilets.")
  elif (facts == "energy"):
    print ("\nThe average American household uses 900 kwh per month. To combat the issue, people can minimize wasting energy by leaving the lights on and etc. To further convserve energy, people should switch to energy-effiecient appliances and get their energy from renewable resources.")
  elif (facts == "transportation"):
    print ("\nThe United States alone emits 5.1 billion metric tons of carbon dioxide, which is 16% of the world output. Since much of carbon dioxide emissions come from vehicle usage, the best way to combat this issue is to switch to electric and hybrid cars. Using electrical energy has no effect on the greenhouse effect and will not contribute to climate change and rising global temperatures. ")
elif (suggestionsOrNot == "YES2"):
  average = 0
  scaleAndAverage()
  if (average >= 1 or average < 2):
    print ("\nWow! Your score shows that your impact on the environment is minimal and well below average.")
  elif (average >= 2 or average < 3):
    print ("\nNice! Your score shows that your impact on the environment is roughly the average.")
  elif (average >= 3 or average <= 4):
      print ("\nYikes! Your score shows that your impact on the environment high and well above average.")
  facts = str(input("\nWhat kind of fact would you like to view? (water, energy, transportation) \nanswer: "))
  if (facts == "water"):
    print ("\nThe average American household uses 90 gallons of water per day. Much of this comes from sprinkler systems and flushing the toilet. To combat this issue, people should sotp taking baths and switch to water-efficient toilets.")
  elif (facts == "energy"):
    print ("\nThe average American household uses 900 kwh per month. To combat the issue, people can minimize wasting energy by leaving the lights on and etc. To further convserve energy, people should switch to energy-effiecient appliances and get their energy from renewable resources.")
  elif (facts == "transportation"):
    print ("\nThe United States alone emits 5.1 billion metric tons of carbon dioxide, which is 16% of the world output. Since much of carbon dioxide emissions come from vehicle usage, the best way to combat this issue is to switch to electric and hybrid cars. Using electrical energy has no effect on the greenhouse effect and will not contribute to climate change and rising global temperatures. ")