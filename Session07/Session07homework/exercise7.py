def remove_dollar_sign(oldstr):
    newstr = oldstr.replace("$","")
    return newstr
a = remove_dollar_sign("Quang has $50")
print(a)