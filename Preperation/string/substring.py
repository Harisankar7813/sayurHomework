'''def substring():
    string="this is a data"
    substring="data"
    return string.index(substring)   
result=substring()
print("Substring index is:",result)'''

def substring():
    string="this is a data"
    substring="data"
    return string.find(substring)
result=substring()
print("Substring index is:",result)