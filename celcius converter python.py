#practicing list comprehension
#Cel means celsius
#Far means fahrenheit
Cel = [18.7, 36.3, 43.1, 9.7, 37.4] # this part here can be subbed with any celsius temperature(s).
Far = [ ((float)(9)/5)*x + 32 for x in Cel] # this eqaution here, go to next line,
print (Far) # expresses the C x (9/5) + 32 = F. Must remeber to add in that float because computers are dumb.


