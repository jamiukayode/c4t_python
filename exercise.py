# def Greet():
#     YourName = input('What is your Name?:')
#     print("Welcome " + YourName)

#     # Another example for function


# def Drive():
#     age = input("how old are you?")

#     if int(age) >= 18:
#         print('You are safe to drive ')
#     else:
#         print('wait till you are 18')

    
#  # Class Function
# class CV:

#  def __init__(self, a, b):
#     self.name = a
#     self.email = b

# p1 = CV("Olawale", "wale@gmail.com")
# p2 = CV("Tola", "tola@gmail.com")

# print( p1.name, p1.email )
# print (p2.name, p2.email)


# #lambda, list & filter
# data = ["finland", "iceland", "turkey"]
# result = filter(lambda country: country.endswith("land"), data)
# print(list(result))


# # Error handling
# try: 
#     name = input("enter your name: ")
#     if name == "Samlarry":
#         raise NameError("You are Restricted on our website")
    
# except BaseException as a:
#     print(a)   


# #function & conditional
# def checkuser():
#     email = input("Enter your email address")
#     paasword = input("Enter your password ")

#     check = filter(lambda user: user["email"] == email and user["password"] == paasword )

#     if len (list(check)) == 0:
#         print("Invalid cresidential")
#     else:
#         print('Success')
#         checkuser()


# #  python exercise.py ----- run this code in your terminal
# name = input("Enter your name: ")
# print(f"Hello, {name}!")


#Example of class
# class Animal:
#     def __init__(self, name, feed):
#         self.name = name
#         self.feed = feed

#     def checkIfCanivorus(self):
#         if self.feed == "flesh":
#             print(self.name + " is canivorus")   
#         else:
#             print(self.name +"is herbivorus")   

# a1 = Animal("Tiger ", "flesh")
# a1.checkIfCanivorus() 




#Another exercise
# class center4tech:
#     def __init__(self, name, dpt, amount) :
#         self.name = name
#         self.dpt = dpt
#         self.amount = amount
       
#     def ifUserIsValid(self):
#         if self.dpt == "fronted" and self.amount >= 100000:
#             print("Registration successful")

#         elif self.dpt == "fullstack" and self.amount >= 150000:
#             print("Registration successful")

#         elif self.dpt == "DataAnalysis" and self.amount >= 120000:
#             print("Registration successful. Welcome to our school")    

#         else:
#             print("The Price is too low to take this course") 

# student1 = center4tech("Abdul lateef", "fronted", 100000)              
# student2 = center4tech("Habeeb", "fullstack", 100000)              
   
# student1.ifUserIsValid()
# student2.ifUserIsValid()
    



#Another exercise
# class StudyInSaudi:
#     def __init__(self, name, religion, age, programme, passport, toefl_grade, eligible_country, medical_report):
#         self.name = name
#         self.religion = religion
#         self.age = age
#         self.programme = programme
#         self.passport = passport
#         self.toefl_grade = toefl_grade
#         self.eligible_country = eligible_country
#         self.medical_report  = medical_report


#     def ifApplicantProvideRequirement(self):
#         if self.religion == "islam" and self.age >= 18 and self.age <= 25 and self.programme == "Bachelor"  and self.passport == "standard" and self.toefl_grade >= 90 and self.eligible_country != "Saudi" and self.medical_report == "Fitness" :
#             print("You are eligible for Bsc Scholarship, congratulation in advance")

#         elif self.religion == "islam" and self.age  >= 25 and self.age <= 35 and self.programme == "Master" and self.passport == "standard" and self.toefl_grade == 95 and self.eligible_country != "Saudi" and self.medical_report == "Fitness":
#             print ('You have granted initial acceptance, do check your email for final acceptance letter and  visa')

#         elif self.religion == " " and self.age  == " " and self.programme == " " and self.passport == " " and self.toefl_grade <= 89 and self.eligible_country == " " and self.medical_report == " ":
#             print ('You must fill the form complete before you  submmit')  

#         else:
#             print("You must meet all the requirements before you can apply for this scholarship")

# Applicant1 = StudyInSaudi("Abdullahi", "islam", 23, "Bachelor", "standard", 90, "Nigeria", "Fitness")            
# Applicant2 = StudyInSaudi("Zainu", "islam", 34, "Master", " ", 97, "Canada", " ")            
# Applicant3 = StudyInSaudi("Abdul", "islam", 14, "Bachelor", "Standard", 90, "Saudi", "Fitne")


# Applicant1.ifApplicantProvideRequirement()
# Applicant2.ifApplicantProvideRequirement()
# Applicant3.ifApplicantProvideRequirement()