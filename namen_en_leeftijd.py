def klaar(standaard):
    if standaard == 'stop':
        quit()
    else:
        pass

def volledig():
    name = input("what is your name?: ")
    klaar(name)
    LastName = input("what is your last name?: ")
    klaar(LastName)
    old = input("How old are you?: ")
    klaar(old)
    print(name, LastName, int(old))
    volledig()

volledig()


# def volledig():
#     name = input("what is your name?: ")
#     LastName = input("what is your last name?: ")
#     old = input("How old are you?: ")
#     if name != 'stop' or LastName != 'stop' or old != 'stop':
#         pass
#     else:
#         quit()
#     print(name, LastName, int(old))
#     volledig()

# volledig()




