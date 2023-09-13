from random import *
import random

lower_chr = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upper_chr = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialchr = ['!', '@', '#', '$', '%', '^', '&', '*']


passwd = int(input('Enter the length of the password: '))
lower = int(input('Enter the number of lowercase letters: '))
upper=int(input('Enter the number of uppercase letters: '))
dig=int(input('Enter the number of digits: '))
spec=int(input('Enter the number of special characters: '))

strong_pass = ''
alert=0
if lower+upper+dig+spec==passwd:
  while passwd>0:
      if upper>0:
          strong_pass=str(upper_chr[randint(0,len(upper_chr)-1)])+strong_pass
          upper-=1
          passwd-=1  
      else:
          break
        
  while passwd>0:
      if lower>0:
          strong_pass=str(lower_chr[randint(0,len(lower_chr)-1)])+strong_pass
          lower-=1
          passwd-=1  
      else:
          break

  while passwd>0:
    if spec>0:
        strong_pass=str(specialchr[randint(0,len(specialchr)-1)])+strong_pass
        spec-=1
        passwd-=1  
    else:
        break

  while passwd>0:
    if dig>0:
        strong_pass=str(digit[randint(0,len(digit)-1)])+strong_pass
        dig-=1
        passwd-=1  
    else:
        break
else:
  alert=1
  print("Length Not Match")
      
def shuffle_chr(pas):
    val=''
    chrList = list(pas)
    random.shuffle(chrList)
    for i in chrList:
        val+=i
    return val

if alert!=1:
  print("Strong Password: "+shuffle_chr(strong_pass))
