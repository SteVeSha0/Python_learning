spam = ['apples', 'bananas', 'tofu', 'cats']

def set_list(userlist):  
    mumber = '' 
    for item in userlist[0:-1]:
        mumber += item + ', '
    result = mumber + 'and ' + userlist[-1]
    return(result)
      
a = set_list(spam)

print(a)
