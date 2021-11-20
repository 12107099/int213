'''

Welcome to SWACH
Self Welbeing Analyzing Computerised hospital

CSE211 CA1
        Section- K20PB
Designed by SALIK H M_12107099
         ~RAM C KUMAR_12107321

'''
#important contacts
guinness_recod=('https://www.guinnessworldrecords.com/contact')
police=('Dail 100')
ambulance=('Dial 102')
air_Ambulance=('Dial 9540161344')



#list of edibles/data set 1

my_list_foodA=["Apple","Banana",'cheese','Eggs','Fish','Milk','Yoghurt','Mangao','Papaya','Apricots','Spinach','Carrot','Sweet patato','red pepper']
my_list_foodB=['whole grains', 'potatoes', 'bananas', 'lentils', 'chili peppers', 'beans', 'yeast','molasses']
my_list_foodC=['oranges','guava','red and green peppers','kiwi','grapefruits','strawberries','Brussels','sprouts','cantaloupe']
my_list_foodD=['Eggs','Fish','Mushrooms']
my_list_foodE=['Nuts','Sunflower','Seeds','tomatoes']
my_list_foodK=['Spinach','Brussels','Sprouts','Broccoli']
my_list_foodcalcium=['milk', 'cheese curly kale', 'okra but', 'not spinach (spinach does contain high levels of calcium but the body cannot digest it all)']
my_list_food=['oranges','guava','red and green peppers','kiwi','grapefruits','strawberries','Brussels','sprouts','cantaloupe']

#list of food to avoid
cancer=['processed meat','Red meat','Alcohol','Salted fish','Sugary drinks','non-diet soda','Samosa','Manchurian','Chole Bhature','Pav Bhaji','Pakora']
pregnancy=['peanuts','Fully cooked egg','Cucumber','Bean','Salads','fish','Pork','sausages',]
diabeties=['dark meat','chicken','fatty cuts of pork','lamb','whole milk','butter','cheese','sour cream','candy','cookies','Ice Cream','Desserts','Fruit Juices','Soda','Sweet Tea','Energy drinks']
asthama=['Eggs','Cow\'s milk','Peanuts','Tree nuts','Soy','Wheat','Fish','Salads','Tobacco','Smoking']


#name exceptions
invalid_names=[0,1,2,3,4,5,6,7,8,9,"`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+"]

print("welcome to Swach\nYou own Hospital")

#Module 1(gender declaration)
# Human or robot declaration

list_gender=["Male","Female","Third gender","Robot"]
print('''Identify yourself by choosing
the correct option for accurate analysis\n''')
print(list_gender[0]+"           : 1")
print(list_gender[1]+"         : 2")
print(list_gender[2]+"   : 3")
print(list_gender[3]+"          : 4")
gender=int(input('\nIdentify your gender from the above given category:  '))

#terminate program if Robot
if 1<gender>4:
    print('Invalid Input! Try again')
    exit()
if gender==4:
    print('''\nPhew! You are immortal!!!
    YOU NEED TO VISIT A WORKSHOP, THIS PROGRAM IS FOR HUMANS\n\n''')
    print("\n Remember your pledge to serve mankind\n")
    exit()
    

#if human, proceed with the following
if gender==1:
    print('Do what you can, with what you have, where you are')
elif gender==2:
    print('\nYou don’t have to play masculine to be a strong woman.')
elif gender==3:
    print('Never be bullied into silence. Never allow yourself to be made a victim. Accept no one\'s definition of your life; define yourself,\n We are proud to have you.')
print("welcome aboard, we are ready to run a diagnosis on you")

print('\nEnter your details below to know your health report')
name=input('Enter your name: ')


#Module 2 [ Name declaration]
   # print('Invalid Name')
   # exit()
if len(name)<2:
    print('Invalid Name')
    exit()
#module 3 [age declaration]
age=int(input('Enter your age in(in Years): '))
if age<2:
    print('Invalid Age,Age should be atleast 2 years for the diagnosis')
    exit()
#module 4 [height declaration]
height=int(input('Enter your height(in cms): '))
if 15<height<54.6:
    print('CONGRATULATIONS %s,You broke the world record, you are the world\'s shortest Person'%(name))
    print('Visit %s to claim your record'%(guinness_recod))
elif height<15:
    print('Invalid Height')
    exit()
elif height>251:
    print('CONGRATULATIONS %s,You broke the world record, you are the world\'s tallest Person'%(name))
    print('Visit %s to claim your record'%(guinness_recod))
elif height<15:
    print('Invalid Height')
    exit()
#module 5 [wieght declaration]
weight=int(input('Enter your weight(in Kilograms): '))
if weight<0:
    print('Invalid Weight')
    exit()
print('Name-',name)
print("Age:-",age)
print("Height:-",height)
print('weight:-',weight)

#Exception-specify if any diseases/medical state [data set 2].

list_state=['None','Pregnant','CANCER','DIABETES','LIVER PTATIENT','ASTHAMA','DIARRHEA','ANAEMIA','DENGUE','MALERIA','CHICKEN POX','VIRAL FEVER',]
print('''\nMention your current medical condition\n''')
print(list_state[0]+"                    : 1")
print(list_state[1]+"                : 2")
print(list_state[2]+"                  : 3")
print(list_state[3]+"                : 4")
print(list_state[4]+"          : 5")
print(list_state[5]+"                 : 6")
print(list_state[6]+"                : 7")
print(list_state[7]+"                 : 8")
print(list_state[8]+"                  : 9")
print(list_state[9]+"                 : 10")
print(list_state[10]+"              : 11")
print(list_state[11]+"             : 12")

state=int(input('\n Identify Medical condition from the above given category: '))


#bmi calculation 

#hyt=pow((height/100),2)    #converting height in metre 
#hh=pow(hyt,2)               #taking the square of height(in m^2)
bmi=(weight/pow((height/100),2))
print('\n %s Your BMI is:- %d'%(name,bmi))

if bmi<18.5:
    print('\nyou are Underweight')
    print('\nWe have several ways for you to become Fit!')
elif 18.5<bmi<24.9:
    print('\nCongratulations, You are healthy!')
elif 24.9<bmi<29.9:
    print("\nYou are overweight")
elif bmi>30:
    print('\n Opps! Yuo are Obese!')
    print("\nDont worry, we'va got you covered")
    print("You may contact the following")
if state==2:
    fd=(*my_list_foodA,*my_list_foodB)
if 18.5<bmi<24.9 and state==1:
    print("\nYou must continue with your current routine\n You may eat diet from the list given below to stay healthy for a longer time")
    print(*my_list_foodA,*my_list_foodB,*my_list_foodC,*my_list_foodD,*my_list_foodE,*my_list_foodK,*my_list_foodcalcium, sep=" , ")
elif 24.9<bmi<29.9 and state==2:
    print()