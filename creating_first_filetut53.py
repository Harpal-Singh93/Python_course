class student:   # this time we are leaving file empty first than add elements letter on
    pass

harpal=student()    # harpal and pardeep are two instance of class student
pardeep=student()
print(harpal,pardeep)   # this show that harpal and pardeep are two different objects at different locations
harpal.name='harpal'   # adding data to data members of harpal object
harpal.age=28
harpal.subject=['c','c++','python']
pardeep.age=27
print(harpal.subject)
print(harpal.age)
print(pardeep.age)
