import re

string1 = "abb29ABCLK%1CnrDBCabbbb"

#A
print(re.findall(r"abb29ABCLK%1CnrDBC(.+)",string1))
# We could use the re.findall to search specific string. as we want to get the abbbb behind ...DBC,
# so we could use ...DBC(.+) to return the left string after it

#B
print(re.search("[A-Z][a-z]+",string1))
#re.search return the first match result in target string;
# [A-Z][a-z]+ means begain with one uppercase letter and following by unlimited number of lowercase letters