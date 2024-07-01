#1
# s = eval(input('Enter the string:'))
# if s[0].isupper():
#     print('yes')
# else:
#     print('No')


# value = eval(input('Enter the value:'))
# if type(value)==str:
#     print(f'The given value "{value}" is of String DT.')
# else:
#     print(f'The given value {value} is not string it is {type(value)} dt')
    
    
# str=eval(input('Enter the string:'))
# if str[0] in 'aeiouAEIOU':
#     print('it is start with vowel')
# else:
#     print('it is not start with vowel')



# n=int(input('Enter the number:'))    
# if (n%3 and n%5)==0:
#     print(True)
# # print(False)
# else:
#     print(False)
# int(str(num)[0]) % 2 == 0:

# num=567
# n=str(num)
# if int(n[0])%2==0:
#     print('even')
# else:
#     print('odd')

# num=567
# n=str(num)
# if int(n[0])%2==0:
#     print('even')
# else:
#     print('odd')





# s='hello'
# res=''
# for i in s:
#     if ord('a')<=ord(i)<=ord('z'):
#         res=res+chr(ord(i)-32)
#     else:
#         res=i
# print(res)
   
   
   
# s='hello'
# res=''
# for i in s:
#     if chr(97)>=chr(i)>=chr(122):
#         res=res+chr(ord(i)-32)
#     else:
#         res=i
# print(res)



# s=678
# if int(str(s)[0])%2==0:
#     print('it is even')
# else:
#     print('it is odd')



    
    
# s = 'T'
# if ord('A') <= ord(s) <= ord('Z'):   # A <= t <= Z
#     print(chr(ord(s)+32))

# elif ord('a') <= ord(s) <= ord('z'):   # a <= t <= z = T
#     print(chr(ord(s)-32))

# else:
#     print('It is not a Alphabet')
    
    
# s='t'
# if ord('a')<=ord(s)<=ord('z'):
#     print(chr(ord(s)-32))
# elif ord('A')<=ord(s)<=ord('Z'):
#     print(chr(ord(s)+32))
# else:
#     print('it is not alphabet')


# string = 'PythOn@ClaSS1991'
# res=''
# for i in string:
#     if i.isupper():
#         res+=i.lower()
#     elif i.islower():
#         res+=i.upper()
#     else:
#         res+=i
# print(res)

# string = 'PythOn@ClaSS1991'
# res=''
# for i in string:
#     if ord('a')<=ord(i)<ord('z'):
#         res+=chr(ord(i)-32)
#     elif ord('A')<=ord(i)<=ord('Z'):
#         res+=chr(ord(i)+32)
#     else:
#         res+=i
# print(res)



# l = [1, 2, 3, 4, 8, 6, 7, 8, 9, 5, 13]
# if l[len(l)//2]%2==0:
#     print('even')
# else:
#     print('odd')
    

# n=int(input('ENter the number:'))
# if n%6==0:
#     print(n**3)
# else:
#     print(n<<3)


# a=[1,2,3,[4,5]]
# b=a.copy()
# # print(id(a),id(b))
# # print(id(-1),id(-1))

# n1=eval(input('Enter the number1:'))
# n2=eval(input('Enter the number2:'))

# if n1 is n2:
#     print('Memroy add of both number is same')
# else:
#     print('memory add of both number is diff')
#     print(type(n1),type(n2))



# collection = [2, 4, 6, 8, [1,3,5]]
# coll=eval(input('Enter the collection:'))
# char=eval(input('Enter the character:'))
# if char in coll:
#     print('char {char} is present in your {coll} collection')
# else:
#     print('char{char} is not present in collection {coll}')


# a=30
# b=40
# c=20
# # var = a if a>b and a>c else b if b>c else c         # max number is 
# var= a if a<b and a<c else b if b<c else c
# print('minimum number is :',var)

# a=30
# b=40
# c=30
# var=a if a>b and a>c else b if b>c else c
# print('maximum number is',var)


# n1=eval(input('Enter the number1:'))
# n2=eval(input('Enter the number2:'))
# n3=eval(input('Enter the number3:'))
''' 
if n1>n2 and n1>n3:
    if n2>n3:
        print(f'{n2 } is second largest number')
    else:
        print(f'{n3 } is second largest number')
        
        

elif n2>n1 and n2>n3:
    if n1>n3:
        print(f'{n1} is second largst number')
    else:
        print(f'{n3} is second largst number')
        
        
    
else:
    if n1>n2:
        print(f'{n1} is second largest number')
    else:
        print(f'{n2} is second largst number')
        
 '''


# a=eval(input('Enter the number1:'))
# b=eval(input('Enter the number2:'))
# c=eval(input('Enter the number3:'))
# num=[a,b,c]
# # second=max([i for i in num if i<max(num)])
# # print('secoond maximun number is: ',second)

# second=min([i for i in num if i>min(num)])
# print('second minimum number is:',second)

# num=[10,30,20,50,7,50,40,70]
# second=max([i for i in num if i<max(num)])
# print(second)


# str=eval(input('Enter the string:'))
# if str==str[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')


# i=1
# while i<=20:
#     print(i,end=' ')
#     i+=1

# for i in range(1,21):
#     print(i,end=' ')


# i=ord('A')
# while i<=ord('Z'):
#     print(chr(i),end=' ')
#     i+=1

# for i in range(ord('a'),ord('z')):
#     print(chr(i),end=' ')



# for i in range(ord('A'),ord('Z')):
    # print(chr(i),end=' ')

    

# for i in range(ord('A'),ord('Z')):
#     print(chr(i),end=' ')

# i=ord('A')
# while i<=ord('Z'):
#     print(chr(i),(chr(i+32)),end='',sep='')
#     i+=1


# for i in range(ord('a'),ord('z')-1):
#     print(chr(i),chr(i-32),sep='',end='')
#     break


# i=20
# while i>=0:
#     print(i,end=' ')
#     i-=1


# num = 10
# n = 2
# while n <= num:   #2 <= 10
#     i = 1
#     while i <= 10:
#         print(f'{n} * {i} = {n*i}',end='     ')
#         i += 1
#     print()
#     n += 1
# # while n <= num:    # 2 <= 10
#     i = 1
#     while i <= 10:
#         print(f'{n} * {i} = {n*i}',end='    ')   # 2 * 1 = 2
#         i += 1
#     print()
#     n += 1

# for i in range(2,8,1):
#     for j in range(1,11,1):
#         print(f'{i}*{j}={i*j}',end='   ')
#     print()


# s = 'Hello guys Good morning python is a programming language'
# char=input('Enter the charracter:')
# count=0
# for i in range(len(s)):
#     if char==s[i]:
#         count+=1
#     i+=1
# print(count)

# s = 'Hello guys Good morning python is a programming language'
# char=input('Enter the character:')
# i=0
# count=0
# while i<len(s):
#     if char==s[i]:
#         count+=1
#     i+=1
# print(count)
    
    
# s = 'Hello guys Good morning python is a programming language'
# char = input('Enter a char:')  #'o'
# i = 0
# count = 0    #6

# while i < len(s):    #56
#     if char == s[i]:    #
#         count += 1

#     i += 1
# print(f'Count of "{char}" is occured {count} times')
      
      
# s = 'Hello guys Good morning python is a programming language'
# char=input('Enter the charector:')
# count=0
# for i in range(len(s)):
#     if s[i]==char:
#         count+=1
# print(count)


# s = 'hello world'
# char=input('Enter the character:')
# for i in range(len(s)):
#     if s[i]==char:
#         print(i)
#         break
# else:
#         print(f'enter {char} is not string')

# s = 'malayalam'
# old=input('Enter the old char:')
# new_char=input('Enter the new char:')
# res=''
# for i in s:
#     if i==old:
#         res+=new_char
#     else:
#         res+=i
# print(res)
    

# s = 'malayalam'
# count=0
# res=''
# for i in s:
#     if i=='a':
#         count+=1
#         if count==4 or count==3:
#             res+='#'
#         else:
#             res+=i
#     else:
#         res+=i
# print(res)


# s='malayalam'
# var=s[7:]
# print(var)
# d=var.replace('a','#')
# print(d)
# print(s[:7]+d)


# s='hello jaya'
# res=[]
# for i in s:
#     res=[i]+res
# print(''.join(res).split())


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('palindrome')
# else:
#     print('not palindrome')


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n+1):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         print(cn,end=' ')


# l = ['hai', (2,3,4), 2+3j, 4.66, {'a':1, 'b':2},
#      ['hello','good', 'morning']]
# res=[]
# for i in l:
#     if isinstance(i,(int,complex,float,str)):
#         res+=[i]
#     elif isinstance(i,dict):
#         for j in i.items():
#             res+=j
#     else:
#         res+=i
# print(res)
        
        
# res1=[]
# for i in l:
#     if not isinstance(i,(list,tuple,set,dict)):
#         res1+=[i]
#     elif isinstance(i,(list,set,tuple)):
#         for j in i:
#             res1+=[j]
#     else:
#         for k in i.items():
#             res1+=i
# print(res1)


# s = 'Python@1991'
# res=''
# for i in s:
#     if ord('a')<=ord(i)<=ord('z'):
#         res+=chr(ord(i)-32)
#     else:
#         res+=i
# print(res)
    
# s = 'PYTHON@1991' 
# res=''
# for i in s:
#     if ord('a')<=ord(i)<=ord('z'):
#         res+=chr(ord(i)+32)
#     else:
#         res+=i
# print(res)

    
    
# s='Good morning'
# for i in s:
#     print(f'{i} : {ord(i)}',end=' , ')


# s = 'hello guys good morning welcome to python session'
# res=[]
# space=''
# for i in s:
#     if i!=' ':
#         space+=i
#     else:
#         res+=[space]
#         space=''
# if len(space)>0:
#     res+=[space]
# print(res)


# s = 'hello guys good morning welcome to python session'
# res=''
# var=[]
# for i in s:
#     if i!=' ':
#         res+=i
#     else:
#         var+=[res]
#         res=''
# if len(res)>0:
#     var+=[res]
# print(var)



# lst = ['hello','guys','good','morning','welcome','to', 'python','session']
# res=''
# join_para=eval(input('Enter the join elements:'))
# count=1
# for i in lst:
#     if count<len(lst):
#         res=res+i+join_para
#         count+=1
#     else:
#         res+=i
# print(res)
    


# lst = ['hello','guys','good','morning','welcome','to', 'python','session']
# res=''
# join_para=eval(input('Enter the join elements:'))
# count=1
# for i in lst:
#     if count<len(lst):
#         res+=i+join_para
#         count+=1
#     else:
#         res+=i
# print(res)



# s = 'programming'
# char='g'
# for i in range(len(s)):
#     if s[i]==char:
#         print(i)
#         break


# s = 'hello guys good morning welcome to python session'
# res=''
# for i in s:
#     if i!=' ':
#         res+=i
#     else:
#         print(res)
#         res=''
# print(res)


# s = 'GooD mOrnIng'
# count=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         count+=1
# print(count)


# names = ['microsoft', 'apple', 'oracle', 'google',
#          'instagram', 'facebook']

# res=[]
# for i in names:
#     res=res+[i[::-1]]
# print(res)


# str=input('Enter the string:')
# char=eval(input('Enter the char do you want to strip:'))
# c=0
# for i in str:
#     if i in char:
#         c+=1
#     else:
#         str=str[c:]             #solve again
#         break
# print(c)
    
''' 
c=0 
for i in str[::-1]:
    if i in char:
        c -= 1

    else:
        str = str[:c]
        break
print(str) 
'''


''' 
string=input('Enter the string:')
char=input('Enter the char:')
index=int(input('Enter the position of index for insertion elements:'))
res=''

for i in range(len(string)):
    if i<index:
        res+=string[i]
    elif i==index:
        res+=char
    else:
        res+=string[i-1]
if index>=len(string):
    res+=char
else:
    res+=string[-1]
print(res) 
'''


# string=input('Enter the string:')
# char=input('Enter the char:')
# index=int(input('Enter the string to insert the elements:'))
# res=''
# if len(string)>=index:
#     for i,j in enumerate(string):
#         if i!=index:
#             res+=j
#         else:
#             res+=char
# # else:
# #     res+=string
# #     res+=char
# print(res)



# lst = ['hai', 'hello', 'pyhton', 'world', 'jimgilala']
# for i in range(len(lst)):
#     del lst[0]
# print(lst)


# lst = ['hai', 'hello', 'pyhton', 'world', 'jimgilala']
# if len(lst)>0:
#     lst=[]
# # else:
# #     lst=lst
# print(lst)


# names = ['apple', 'google', 'yahoo', 'walmart']
# elements=eval(input('Enter the elements:'))
# names+=elements
# print(names)

# l=eval(input('enter the iterable:'))
# if isinstance(l,list):
#     res=l[::]
#     print(res)
# else:
#     print(f'we can not perform copy operation in {type(l)} datatype')
    

# l=eval(input('enter the iterable:'))
# if isinstance(l,list):
#     res=l[::-1]
#     print(res)
# else:
#     print(f'we can not reverse operation in {type(l)} datatype')


# l = [1,2,3,4,5,6,7,8,9]
# res=[]
# for i ,j in enumerate(l):
#     if i%2==0:
#         res.append(j)
#     else:
#         res.append(j)
#         print(res)
#         res=[]
# if len(l)%2==1:
    
#     print(res)


# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',     'lambda.png', 'map.py', 'python.pdf', 'oops.py']
# res=[]
# for i in l:
#     var=i.split('.')
#     if var[1] not in res:
#         res+=[var[1]]
# print(res)


# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',     'lambda.png', 'map.py', 'python.pdf', 'oops.py']
# res=[]
# for i in l:
#     var=i.split('.')
#     if var[1] not in res:
#         res+=[var[0]]
# print(res)



# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
    # 'lambda.png', 'map.py', 'python.pdf', 'oops.py']
# from collections import defaultdict
# res=defaultdict(list)
# for i in l:
#     var=i.split('.')
#     res[var[1]]+=[var[0]]
# print(res)


# from collections import defaultdict
# rs=defaultdict(list)

# for i in l:
#     var=i.split('.')
#     rs[var[1]]+=[var[0]]
# print(rs)


# names = ['apple', 'google', 'yahoo', 'walmart', 'amazon',
#          'flipkart', 'ola', 'redbus']
# d={}
# for i in names:
#     if i in d:
#         d[i]+=len(i)
#     else:
#         d[i]=len(i)
# print(d)


# names = ['apple', 'yahoo', 'google', 'flipkart', 'google',
        #  'yahoo', 'google', 'flipkart', 'apple', 'yahoo', 'apple']

# from collections import defaultdict
# res=defaultdict(int)

# for i in names:
#     res[i]+=1
# print(res)
        
# d={}
# for i in names:
    
#         d[i]=names.count(i)
# print(d)


# var={i:names.count(i) for i in names}
# print(var)


# d={}
# for i in names:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# string = 'hello good morning how are youu'
# str=string.split()
# d={}
# for i in str:
#     d[i]=len(i)
# print(d)


# s = 'AABBCCCDAACD'
# res=''
# c=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c+=1
#     else:
#         res=res+str(c)+s[i]
#         c=1
# res=res+str(c)+s[-1]
# print(res)
    
    
# s = 'AABBCCCDAACD'
# res=''
# c=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c+=1
#     else:
#         res=res+str(c)+s[i]
#         c=1
# res=res+str(c)+s[-1]
# print(res)



# l = [1, 3, 5, 7,2, 3, 5, 6, 1, 9, 4, 5, 9, 8,3, 2]
# from collections import defaultdict
# res=defaultdict(list)

# for i,j in enumerate(l):
#     res[j]+=[i]
# print(res)
    
    
# string = 'hai hello good morning python is programming ' \
#          'language and programming is fun'

# str=string.split()
# res=''
# for i in str:
#     if len(res)<len(i) and str.count(i)==1:
#         res=i
# print(res)



# l = ['hello', 78, 'python', True, [3, 2, 1], 67.8]
# res=[]
# for i in l:
#     if isinstance(i,str):
#         res.append(i)
#     elif isinstance(i,list):
#         res.append(i[::-1])

#     else:
#         res.append(str(i)[::-1])
# print(res)


# s = 'hi hello good morning'
# res=s[::-1]
# print(res)

# str=s.split()
# res=''
# for i in str:
#     res=i[::-1]+' '+res
# print(res)
''' 
num=342
n=num
sum=0
while n!=0:
    sum=sum+n%10
    n=n//10
print(sum)
if n%sum==0:
    print(f'{num} is harshad number')
else:
    print(f'{num} is not harshad number')

 '''



#harshad number is number that is divisible by sum of it's digit Ex=> 342: 3+4+2=6  means 342%6==0 then 'yes' o.v. 'no'
'''

num=342
n1=str(num)
sum=0
for i in n1:
    sum+=int(i)
print(sum)
if num%sum==0:
    print('harshad number')
else:
    print('not harshad number')

    
 '''

# l = [23, 67, 15, 30, 89, 65, 20]
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)


# l = [23, 67, 15, 30, 89, 65, 20]
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)


# l = [23, 67, 15, 30, 89, 65, 20]
# n=int(input('ENter the number:'))
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[-n])


# l = [23, 67, 15, 30, 89, 65, 20]
# n=int(input('Enter the number:'))
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[n-1])


# l = ['hello', 'hai', 'how', 'are', 'you']
# res=[]
# for i,j in enumerate(l):
#     # res.append((i,j))
#     res+=[i]
# print(res)


# s = 'Rona2ldo be4st th1e pl5ayer i3s'
# res=''
# for i in s:
#     if i.isalpha() or i.isspace():
#         res+=i
# res1=res.split()
# print(res1)

# # res2=res1.sort(key=len,reverse=False)
# res2=sorted(res1,key=len)
# print(' '.join(res2))



''' 
res = ''
for i in s:
    if i.isalpha() or i.isspace():
        res += i
res1 = res.split()
print(res1)
# lam = lambda
res2 = sorted(res1,key=len)
print(' '.join(res2)) 
'''


# s = "ronaldo is the best player"
# str=s.split()
# if 'ronaldo' in str and 'the' in str:
#     index_ronaldo=str.index('ronaldo')
#     index_the=str.index('the')
#     str[index_ronaldo],str[index_the]=str[index_the],str[index_ronaldo]
# # print(str)
# print(' '.join(str))   #the is ronaldo best player




# the Ronaldo is best player                          #ask_pending
# s = 'Rona2ldo be4st th1e pl5ayer i3s por56tu123g2l'
# res=''
# for i in s:
#     if i.isalpha() or i.isspace():
#         res+=i
# print(res)




''' 
s = 'Rona2ldo be4st th1e pl5ayer i3s por56tu123g2l'     #ask_pending
res=[]
temp=[]
for i in s.split():
    for j in i:
        if j.isdigit():
            temp.insert(0,j)
        else:
            temp.append(j)
            # print(''.join(temp))
    res.append(''.join(temp))
    temp=[]
    # res=[]
        
print(res)
for i in sorted(res):
    print(i[1:],end=' ')

'''


# words = 'hey guys good moring hello everyone glad to see each ' \
#     'of you are becoming python masters best of luck'

# from collections import defaultdict
# res=defaultdict(list)
# for i in words.split():
#     res[i[0]]+=[i]
# print(res)
     
     
     
# lst = ["see", "into", "my", "eyes", "dont", "see", "into", "her", "eyes", "see",
#        "into", "my", "eyes", "not", "her", "eyes", "eyes", "are", "eyes", "to",
#        "see", "into", "my", "eyes", "not", "her", "eyes"]

# # from collections import defaultdict
# # res=defaultdict(int)
# # for i in lst:
# #     res[i]+=1
# # print(res)


# print({i:lst.count(i) for i in lst})

# d={}
# for i in lst:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# string = 'hEy Guys gOod MornIng Happy sAturdAy'
# res=''
# for i in string:
#     if i in 'aeiouAEIOU':
#        if ord('a')<=ord(i)<=ord('z'):
#            res+=chr(ord(i)-32)
#        elif ord('A')<=ord(i)<=ord('Z'):
#            res+=chr(ord(i)+32)
#     else:
#         res+=i
# print(res)

# words = 'Good Morning @mic testing 123 123 Party president #420'
# # print(len(words))
# alpha=0
# digit=0
# space=0
# specil_char=0

# for i in words:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace():
#         space+=1
#     else:
#         specil_char+=1
# print(alpha)
# print(digit)
# print(space)
# print(specil_char)

# s = 'ABCEGILMNPRTUWYZ'

# total='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# var=set(total)
# miss_alphabet=var.difference(s)
# print(miss_alphabet)
# sort_miss=sorted(miss_alphabet)
# print(' '.join(sort_miss))



# s = 'ABCEGILMNPRTUWYZ'
# res = ''
# for i in range(26):
#     if ord('A') <= ord(s[0]) <= ord('Z') and chr(ord('A')+i) not in s:
#         res += chr(ord('A')+ i)
# print(res)

# s = 'ABCEGILMNPRTUWYZ'
# res=''
# for i in range(26):
#     if ord('A')<=ord(s[0])<=ord('Z') and chr(ord('A')+i) not in s:
#         res+=chr(ord('A')+i)
# print(res)



# char = 'a'
# for i in range(0,26,2):
    # print(chr(ord(char)+i),end=' ')

''' 
n=int(input('Enter the number:'))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('it is prime number')
else:
    print('it is not prime number')

 '''
 
'''  
n=int(input('Enter the number:'))
count=0
for i in range(1,n+1):
    cn=i
    count=0
    for j in range(1,cn+1):
        if cn%j==0:
            count+=1
    if count==2:
        print(cn,end=' ')
 '''

''' 

sentence = "sdfh45gjh54 the45ght5 ronal0do"
l=[]
for i in sentence.split():
    d=''
    ch=''
    for j in i:
        if j.isdigit():            #pending_ask
            d+=j
        else:
            ch+=j
l.append((int(d),ch))
for i,j in sorted(l):
    print(j,end=' ')
  '''           


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n+1):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         print(cn,end=' ')
        



l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal',
     'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']

# d={}
# for i in l:
#     var=i.split()
#     if var[1] in d:
#         d[var[1]]+=[var[0]]
#     else:
#         d[var[1]]=[var[0]]
# print(d)

# from collections import defaultdict
# res=defaultdict(list)

# for i in l:
#     var=i.split()
#     res[var[1]]+=[var[0]]
# print(res)



# a=ord('A')
# b=ord('a')
# for i in range(0,26):
#     print(chr(a+i),chr(b+i),sep='',end=' ')

''' 
l1 = [2, 3, 5, 7, 5, 2]
l2 = [5, 4, 2, 7, 8, 4, 5]

res=[]
for i in l1+l2:
    if (l1+l2).count(i)==1:
        res+=[i]
print(res)


'''

''' l1 = [2, 3, 5, 7, 5, 2]
l2 = [5, 4, 2, 7, 8, 4, 5]

for i in zip(l1,l2):
    print(i,end=' ') '''




# l1 = [2, 3, 5, 7, 5, 2]
# l2 = [5, 4, 2, 7, 8, 4, 5]
# from collections import defaultdict
# res=defaultdict(int)

# for i in l1+l2:
#     res[i]+=1
# print(res)



# # l1 = [2, 3, 5, 7, 5, 2]
# # l2 = [5, 4, 2, 7, 8, 4, 5]

# print([j for j in res if res[j]==1])
# var=filter(lambda i:res[i]==1,res)
# print(list(var))


''' 
s = 'hello guys good morning welcome to programming class'
from collections import defaultdict
res=defaultdict(str)

for i in s:
    if i in 'aeiouAEIOU':
        res['vowel']+=i+''
    else:
        res['consonent']+=i+''
print(res)
    
 ''' 
 
# l1 = ['a', 'b','c', 'd', 'e', 'f']   
# l2 = ['apple', 'basket', 'camera', 'donut', 'egg', 'fish']

# d={}
# for i,j in zip(l1,l2):
#     d[i]=j
# print(d)



# file = ['python', 'oops', 'whileloop', 'abstraction', 'functions']
# ext = ['txt', 'py', 'pdf', 'pptx']
# d={}
# from itertools import zip_longest
# for i,j in zip_longest(file,ext,fillvalue='No Extension'):
#     d[i]=j
# print(d)


# res=[i+'.'+j for i,j in zip(file,ext)]
# print(res)
    
    
'''     
n=int(input('Enter the number:'))
temp=n
rev=0

while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print('palindrom enumber')
else:
    print('not palindrome number')
''' 

# n=int(input('Enter the number:'))
# temp=n
# rev=0

# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if temp==rev:
#     print('it is palindrom number')
# else:
#     print('not palindrome number')

''' 
def check_palin(num):
    return str(num)==str(num)[::-1]

def number_range_btwn(start,end):
    palindrome=[]
    for i in range(start,end+1):
        if check_palin(i):
            palindrome.append(i)
    return palindrome
start=int(input('Enter the frst number:'))
end=int(input('Enter the lst number:'))

var=number_range_btwn(start,end)
print(f'palindrome between {start} and {end} is :',var)
 '''

 
# def palindrome(num):
#     return str(num)==str(num)[::-1]
# start=100
# end=200
# var=[i for i in range(start,end+1) if palindrome(i)]
# print(f'palindrome number between {start} and {end} is :',var)

''' 
def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num,end=' ')
    # else:
    #     print('not prime')
start=10
end=50
var=[i for i in range(start,end+1) if is_prime(i)]
# print(f'prime number between {start} and {end} is:',,end='')
   '''      


# n = 12345
# sum=0
# while n!=0:
    
#     sum+=n%10
#     n=n//10
# print(sum)


# n=int(input('Enter the number:'))
# sum=0
# for i in range(n):
#     sum+=n%10
#     n=n//10
# print(sum)


# n=int(input('Enter the number:'))
# sum=0
# while n!=0:
#     n=n//10
#     sum+=1
# print(sum)


# ====>LCM
# a=int(input('Enter the number1:'))
# b=int(input('Enter the number2:'))
# if a>b:
#     min=a
# else:
#     min=b
# while (1):
#     if (min%a==0 and min%b==0):
#         print('LCM is :',min)
#         break
#     min+=1


#GCD ?/HCF
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# ans=gcd(a=int(input('1st===>')),b=int(input('2nd===>')))
# print('GCD is :',ans)

''' 
n=int(input('Enter the number:'))
temp=n
rev=0
for i in range(1,n+1):
    a=n%10
    rev=rev+a*a*a
    n=n//10
if temp==rev:
    print('it is armstromng number')
else:
    print('it is not armstrong number') 
'''

''' 
start=int(input('Enter the 1st number:'))
end=int(input('Enter the 2nd number:'))


for num in range(start,end+1):
    n=str(num)
    l=len(n)
    rev=0
    for i in n:
        rev+=int(i)**l
    if rev==num:
        print(num,end=' ')
 '''


# n=int(input('Enter the number:'))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if n==sum:
#     print('perfact number')
# else:
#     print('not perfact number')


# n=int(input('Enter the number:'))
# a=0
# b=1
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ')


# n=int(input('Enter the number:'))
# sum=0
# for i in range(n):
#     sum+=n%10
#     n=n//10
# print(sum)  
    
'''     
n=int(input('Enter the number:'))
temp=n
sum=0
for i in range(n):
    sum+=n%10
    n=n//10
if temp%sum==0:
    print('it is harshad number')
else:
    print('it is not harshad number')

#342=>3+4+2==6 that is 342%6==0 means harshad else 'not harshad'

 '''
 
 
# WAP to check given number is Automorphic or not
#square end with the integer
#1,5,6,25,76,376,625,9376


# n=int(input('Enter the number:'))
# l=len(str(n))
# res=n**2
# if str(n)==str(res)[-l:]:
#     print(f'{n} is automorphic number')
# else:
#     print(f'{n} is not automorphic number')



# names = ['apple', 'google', 'yahoo', 'walmart']
# n=[]
# for i in names:
#     n.append(i[::-1])
# print(n)

# print(list(reversed(n)))


# s = 'hello guys good morning'
# rev=''
# for i in s.split():
#     rev=rev+i[::-1]+' '
# # print(rev)
# rev1=' '.join(rev)
# # print(rev1)
# rev2=rev1.split()[::-1]
# print(' '.join(rev2))
# print(s[::-1])



# s = 'hello python'
# len=0
# for i in s:
#     len+=1
# print(len)


# s = 'hello world'
# re_wrd='universe'
# res=''
# for i in s.split():
#     if i=='world':
#         res+=re_wrd
#     else:
#         res+=i+' '
# print(res)


# s = 'hello world'
# l=[]
# for i in s:
#     l+=[i]
# print(''.join(l).split())

# s = 'hello world'
# l=s.split()
# r=''
# for j in l:
#     r+=j+' '
# print(r)



# s = 'hello python'
# for i in range(0,len(s),2):
#     print(s[i],end=' ')
    
    
# l1 = [1,3,5,7]


# l2 = [2,4,6,8]
# l22=set(l1)
# var=l22.update(str(l1))
# print(var)

# s = 'hellohai'
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,'-')
# print(s)




# l = [34, 'hello', 'apple', 56.7, 4546, 67.8,
#      'google', '45']

# def rev(lst,res=[]):
#     for i in lst:
#         if isinstance(i,str):
#             res.append(i)
#         elif isinstance(i,float):
#             res+=[float(str(i)[::-1])]
#         elif isinstance(i,int):
#             res+=[int(str(i)[::-1])]
#         else:
#             None
#     return res
# print(rev(l))

''' 
def reverse(*a):
    for i in a:
        if isinstance(i,(str,list,tuple)):
            return i[::-1]
        return a

print(reverse('hello'))
print(reverse([1,2,34,4]))
print(reverse((1,2,3,4,5,6)))

'''


# s = 'Sony12India567pvt21ltd'
# res=''
# sum=0
# for i in s:
#     if i.isdigit():
#         res+=i
#     else:
#         if res:
#             sum+=int(res)
#             res=''
# print(sum)


# s = 'India got Indepndence on Aug 15 1947'
# res=0
# for i in s:
#     if i.isdigit():
#         res+=int(i)
# print(res)


# l = ['hello', '123', 'hai', 'python', '345']
# l1=[]
# for i in l:
#     if i.isdigit():
#         l1.append(int(i))
# print(l1)


# a = ['hello','hai','world']
# b = ['hello', 'hai', 'world', 'python']

# for i in b:
#     if i not in a:
#         print(i)
    
    
# l = [1, 3, 5, 7]
# var=lambda i:i**2
# print(list(map(var,l)))


# l = [[1,2,3], [4,5,6], [7,8,9]]
# var=[sum(i) for i in l]
# print(sum(var))


# l = ['hello', 'hai', 'python']
# res=[]
# for i in l:
#     res=[i]+res
# print(res)


d = {'a':100, 'b':{'m':'man', 'n':'nose', 'o':'ox'},
     'c':'camera'}
# d['b']['n']='net'
# print(d)

# def replace(dict_,old,new):
#     for i,j in d.items():
#         if isinstance(j,dict):
#             for k,v in j.items():
#                 if v==old:
#                     j[k]=new
#     return dict_

# print(replace(d,'nose','place'))


# def replace(dict_,old,new):
#     for i,j in d.items():
#         if isinstance(j,dict):
#             for k,v in j.items():
#                 if v==old:
#                     j[k]=new
#     return dict_
# print(replace(d,'ox','jaya'))


# names = ['listen', 'hello', 'eat', 'desserts', 'silent',
#          'peek', 'ate', 'keep', 'stressed', 'tea']

# from collections import defaultdict
# d=defaultdict(list)

# for i in names:
#     nms=''.join(sorted(i))
#     d[nms]+=[i]




''' 
names = ['listen', 'hello', 'eat', 'desserts', 'silent',
         'peek', 'ate', 'keep', 'stressed', 'tea']


anagram={}
for i in names:
    nms=''.join(sorted(i))
    if nms in anagram:
        anagram[nms]+=[i]
    else:
        anagram[nms]=[i]
print(anagram) 
'''


names = ['apple', 'google', 'yahoo', 'gmail', 'apple',
         'yahoo', 'google']

# dupli=[]
# for i in names:
#     if i not  in dupli:
#         dupli.append(i)
# print(dupli)


# dupli=[]
# for i in names:
#     if names.count(i)>1:
#         if i not in dupli:
#             dupli.append(i)
# print(dupli)


# var=[i for i in names if names.count(i)>1]
# print(set(var))

# names = ['apple', 'google', 'yahoo', 'gmail', 'apple',
#          'yahoo', 'google']


# from collections import defaultdict
# res=defaultdict(int)
# for i in names:
#     res[i]+=1
# print(res)
    
    
# numbers = [10, 30, 50, 80, 15, 20, 70,25]
# # print(max(numbers))

# n=0
# for i in numbers:
#     if i>n:
#         n=i
# print(n)
        
        
        
# words=['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','the',
#        'eyes','not','around','the','eyes','dont','look',
#        'around','the','eyes','look','into','my',
#        'eyes',"youre",'under']
# word={i:words.count(i) for i in words }
# print(word)
# var=list(word.items())
# print(var[0])


# def tail(args,n):
#     return list(args[-n::])

# print(tail('hello world',3))
# print(tail([1,2,3,4,5],3))



# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],
#      True, (1,3,7), 6+3j]
# res=[]
# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         res.append(i)
# print(res)


# s = 'hai hello how are you good to see you'
# c=0
# for i in s:
#     if i==' ':
#         c+=1
# print(c)


# year=int(input("ENter the year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('year is leap year')
# else:
#     print('year is not leap year')


# s = 'Hi How are you Welcome to Python & its Fun'
# U_c=0
# for i in s:
#     if i.isupper():
#         U_c+=1
# print(U_c)



# s = 'hello123world24welcome2python@1991'
# c=''
# for i in s:
#     if i.isdigit()!=True:
#         c+=i
# print(c)
        
        
        
# inp = [1,2,['a','b',['ses', 10]]]

# res=[]
# for i in inp:
#     if isinstance(i,list):
#         res.extend(i)
#     else:
#         res.append(i)
# print(res)


# inp = [1,2,['a','b',['ses', 10]]]
# def unpacking(lst):
#     res=[]
#     for i in lst:
#         if isinstance(i,list):
#             res.extend(unpacking(i))
#         else:
#             res.append(i)
#     return res
# print(unpacking(inp))



# tup=([1,2,3], (4,5), ['apple', 'yahoo'],
#                  'gmail', {'a':1,'b':2})

# def total_len(args):
#     length=0
#     for i in args:
#         length+=len(i)
#     return length

# print(total_len(tup))

# tup=([1,2,3], (4,5), ['apple', 'yahoo'],
#                  'gmail', {'a':1,'b':2})

# length=0
# for i in  tup:
#     length+=len(i)
# print(length)



# s = 'hello world welcome to python'

# for i in s:
#     if i==' ':
#         res=s.replace(i,'\n')
# print(res)


# s = 'hello world welcome to python'
# for i in s:
#     if i==' ':
#         res=s.replace(i,'\n')
# print(res)



# s = 'hello world welcome to python'
# res=''
# for i in  s:
#     if i in 'aeiouAEIOU':
#         res+='*'
#     else:
#         res+=i
# print(res)


# l = [1, 2, 3, 4, 6, 10]
# res=[]
# for i in range(1,11):
#     if i  not in l:
#         res.append(i)
# print(res)
    
    
# import math
# def is_perfact(num):
#     res=math.sqrt(num)
#     if res==int(res):
#         return True
#     else:
#         return False
# print(is_perfact(25))
# print(is_perfact(36))
# print(is_perfact(35))

''' 
all_products = ['iphone', 'mac', 'gmail', 'google maps', 'windows',
                'ios', 'google drive', 'one drive']


apple=['iphone','mac','ios']
google=['gmail','google maps','google drive']
window=['windows','one drive']
from collections import defaultdict
res=defaultdict(list)

for i in all_products:
    if i in apple:
        res['apple_product']+=[i]
    elif i in google:
        res['google_product']+=[i]
    elif i in window:
        res['window_product']+=[i]
print(res)
    
'''       


# names = ['apple', 'google', 'yahoo', 'gmail', 'amazon',
#          'yahoo', 'golang', 'flipkart']

# def rotate(lst,n):
#     return lst[-n:]+lst[:-n]
# print(rotate(names,2))


# names = ['apple', 'google', 'yahoo', 'gmail', 'amazon',
#          'yahoo', 'golang', 'flipkart']

# from collections import deque
# d=deque()

# d.append(10)
# d.append(15)

# d.append(20)
# d.append(30)
# d.append(40)
# # print(d.rotate())
# d.rotate(3)
# print(d)



# s='Darshan'
# def rotate(str,n=2):
#     return str[n:]+str[:n]
# print(rotate(s))

# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(sorted(even))
# print(sorted(odd))


# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
# odd_filter=filter(lambda i:i%2==1,l)
# even_filter=filter(lambda i:i%2==0,l)
# print(list(odd_filter))
# print(list(even_filter))


# l = [3, 4, 1, 7, 2, 12, 8, 9, 11, 16, 13]
# odd_filter=filter(lambda i:i%2==1,l) 
# even_filter=filter(lambda i:i%2==0,l)
# res=sorted(odd_filter,reverse=True)+sorted(even_filter,reverse=True)
# print(res)



# s = '0-0,4-8,20-20,43-45'
# s1=s.split(',')
# res=[]
# for i in s1:
#     var=i.split('-')
#     for j in range(int(var[0]),int(var[1])+1):
#         res.append(j)
# print(res)
        
        
# s = '0-0,4-8,20-20,43-45'
# s1=s.split(',')
# res=[]
# for i in s1:
#     var=i.split('-')
#     for j in range(int(var[0]),int(var[1])+1):
#         res.append(j)
# print(res)



# s = 'java is a programming and java is fun to learn java is ' \
#     'java'

# res=''
# s1=s.split()
# for i in s1:
#     if i=='java':
#         res=res+'python'+' '
#     else:
#         res=res+i+' '
# print(res)


# numbers = [18,15,20,25, 30,35, 40, 5,10,15]
# sort=sorted(numbers)
# print(sort)
# min_sum=sum(sort[:3])
# # print(sort[:3])
# # print(min_sum)
# max_sum=sum(sort[-3:])
# print(max_sum)


# s = 'python@#$%pool'
# res=[]
# for i in s:
#     if i.isalpha():
#         res+=[i]
# print(''.join(res))
# print(''.join(res))




# s = 'python@#$%pool'
# s = 'python@#$%pool'
# res=[]
# temp=''
# for i in s:
#     if i.isalpha():
#         temp+=i
#     else:
#         if i in '!@#$%^&*()_+<>{}[]':
#             if temp:
#                 res.append(temp)
#             temp=''
# if temp:
#     res.append(temp)
# print(res)



# s = 'python@#$%pool'
# res=[]
# temp=''
# for i in s:
#     if i.isalpha():
#         temp+=i
#     else:
#         if temp:
#             if i in '!@#$%^&*()_+{}<>?[]':
#                 res.append(temp)
#             temp=''
# if temp:
#     res.append(temp)
# print(res)



# names = ['apple', 'google', 'yahoo', 'apple', 'yahoo', 'google',
#          'gmail', 'apple', 'yahoo', 'gmail']
# from collections import defaultdict
# res=defaultdict(list)

# for i,j in enumerate(names):
#     res[j]+=[i]
# print(res)
    
    

# s = 'hello world hi hello universe how are you python ' \
#     'happy birthday'

# res=[]
# for i in s.split():
#     if i.startswith('h'):
#         res.append(i)
# print(' '.join(res).split())
    
    
    
# s = 'hello 123 world 456 welcome to python498675634'
# odd_num=[i for i in s if i%2==1 and i.isdigit()]
# print(odd_num)


# odd=''
# even=''
# for i in s:
#     if i.isdigit() and int(i)%2==0:
#         even+=i+' '
#     else:
#         if i.isdigit():
#             odd+=i+' '
# print(odd)
# print(even)


# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
#         print(l)
#     else:
#         print(l)
#         # del i
# print(l)



# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
#         print(l)
#     else:
#         print(l)
        

# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# #exp o/p :[1,2,3,4,5]
# for i in l:
#     if l.count(i)>1:
#         print(l)
#         break
#         # l.remove(i)
#         # print(l)
#     # else:
#         # print(l)


# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]

# for i in range(len(l)):
#     value = l[i]
#     for j in range(i + 1, len(l)):
#         if l[j] == value:
#             l.pop(j)
#             break

# print(l)  # This will print [1, 2, 3, 4, 5]


# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# var=[j for i,j in enumerate(l) if j not in l[:i]]
# print(var)

# l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]
# print([j for i,j in enumerate(l) if j not in l[:i]])



# l = [3, 5, 4, 8, 11, 1, -1, 6]
# for i in l:
#     for j in l:
#         if i-j==10 or i+j==10 and i!=j:
#             print(i,j)


# l = [3, 5, 4, 8, 11, 1, -1, 6]
# for i,j in enumerate(l):
#     for k,v in enumerate(l):
#         if j-v==10 or j+v==10 and j!=v:
#             print((i,k),(j,v))


# l = [3, 5, 4, 8, 11, 1, -1, 6]
# res=[]
# for i in range(0,len(l)-1):
#     if i%2==0:
#         res.append(l[i]+l[i+1])
# print(res)


# def outer(func):
#     def inner(*a,**b):
#         res=func(*a,**b)
#         return f'+91 {res}'
#     return inner
# @outer
# def number(num):
#     return num
# print(number(9118762851))
# # print(op)


# def outer(func):
#     def inner(*a,**b):
#         res=func(*a,**b)
#         return f'+91 {a[0]}'
#     return inner
# @outer
# def number(num):
#     pass
# number(9118762851)



# ========================= PATTERN ===========================
# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(j,end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('*',end=' ')
#         else:
#             print(j,end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1  or i==j or i==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==1 or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ') 
#     for j in range(2*i+1):
#         print('*',end=' ')
#     print()
        
        
        
# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for j in range(2*i+1):
#         print('*',end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(n-i):
#         print('',end=' ')
#     for j in range(i+1):
#         print('* ',end='')
#     print()


# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()



# n=int(input('Enter the number:'))
# for i in range(n-1):
#     for j in range(n-i):
#         print('',end=' ')
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print('',end=' ')
#     for j in range(n-i):
#         print('* ',end='')
#     print()



# n=5
# s=n*2-3
# r=1

# for i  in range(1,n*2):
#     for j in range(1,r+1):
#         print('*',end=' ')
#     for k in range(1,s+1):
#         print(' ',end=' ')
#     for k in range(1,r+1):
#         if k!=n:
#             print('*',end=' ')
#     if i<n:
#         s-=2
#         r+=1
#     else:
#         s+=2
#         r-=1
#     print() 


# n=int(input('ENter the number:'))
# s=n*2
# r=1
# for i in range(1,n*2):
#     for j in range(1,r+1):
#         print(' ',end=' ')
#     for j in range(1,s):
#         print('*',end=' ')
#     for j in range(1,r+1):
#         if j!=n:
#             print(' ',end=' ')

#     if i<n:
#         s-=2
#         r+=1
#     else:
#         s+=2
#         r-=1
#     print()


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=' ')
#     print()


# n = int(input('Enter the range:'))
# pat = ''
# for i in range(1,n):
#     pat += str(i)+ ' '
#     print(pat)


# n = 8
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if i == j or i+j == n+1:
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(n-1):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()



# n=int(input('Enter the number:'))
# for i in range(n-1):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()



# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1  or i==n//2+1  or j==1 or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
    
    

# for i in range(7):
#     for j in range(5):
#         if (j==0 or j==4) or (i==0 or i==3):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==1 or i==1 or i==n or (i>n//2 and j==n) or (i==n//2+1) and j>n//2):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')

#     print()



# for i in range(7):
#     for j in range(5):
#         if j==0 or i==0 or i==6 or (i==3 and j >2) or (i==4 and j==4) or (i==5 and j ==4) :
#             print('*', end= ' ')
#         else:
#             print(' ', end= ' ')
#     print()


# for i in range(7):
#     for j in range(5):
#         if j==0 or i==0 or i==6 or (i==3 and j>2) or (j==4 and i==4) or (i==5 and j==4):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# for i in range(7):
#     for j in range(5):
#         if j==0 or (i==j+2 and j>1) or (j+i==4):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')

#     print()




# ? date
# from datetime import date
# print(date.today())
# print(today.year())


# from datetime import date
# Mydate=date(2023,8,23)
# print(Mydate)




# today=date.today()
# print(today)
# print(today.year,today.month,today.day)

#!time
# from datetime import time
# mytime=time(22,56,45,2345)
# print(mytime)



# time=time(22,56,45,2345)
# print(time.hour,time.minute,time.second,time.microse

# ! datetime

# from datetime import datetime
# c_date_time=datetime(2023,11,9,8,50,50,5050)
# print(c_date_time)

# from  datetime import datetime
# date = datetime(2023,7,2,7,39,25)
# modify_date=date.strftime('%d/%m/%Y')
# print(modify_date)

# from datetime import datetime
# date = datetime(2023,7,2,8,15,30)


# formated_date=date.strftime('%d[%A]-%B-%Y')
# print(formated_date)


# from datetime import datetime
# c_date=datetime.now()
# print(c_date)
# c_date=datetime.now().time()
# print(c_date)


# from datetime import date,time, datetime,timedelta,timezone
# tz=timezone(timedelta(minutes=45))
# datetime=datetime(2013,9,23,22,45,0,tzinfo=tz)
# print(datetime)


# c_time=datetime.today().time()
# print(c_time)


# delta=timedelta(hours=23,minutes=20)
# print(delta)

''' 

class Bank:
    bnk_name = 'ICICI'
    ifsc = 'ICICI00123'
    brch = 'BTR'
    mgr = 'Johnny Depp'
    addr = 'Bull-temple Road'
    pin_code = 560040

    def __init__(self,cname,acc_no, mob, address, bal):
        self.cname = cname
        self.acc_no = acc_no
        self.mob = mob
        self.caddr = address
        self.bal = bal
        self.stmt = [[1,    '-  ',  '-  ',  self.bal]]

    def details(self):
        print(f'{"*"*10}BANKDETAILS{"*"*10}\n'
              f'Bank name : {self.bnk_name}\n'
              f'Branch name : {self.brch}\n'
              f'IFSC : {self.ifsc}\n'
              f'Bank Manger : Mr/Ms.{self.mgr}\n'
              f'Bank Address: {self.addr},{self.pin_code}')
        print(f'{"="*10}CUSTOMER DETAILS{"*"*10}\n'
              f'Customer Name : {self.cname}\n'
              f'Acc number : {self.acc_no}\n'
              f'Total Balance : Rs.{self.bal}/-\n'
              f'Customer Addres : {self.caddr}\n')

    def deposit(self,amt):
        print(f'Available balance : Rs.{self.bal}/-\n'
              f'Deposited Amount : Rs.{amt}/-')
        self.bal += amt
        print(f'Availbale Balance : Rs.{self.bal}/-\n'
              f'{"*"*30}')
        sl_no = self.stmt[0][0] + 1
        temp = [sl_no,  amt,    '-  ',  self.bal]
        self.stmt.append(temp)


    def withdrawl(self,amt):
        print(f'Available balance : Rs.{self.bal}/-')
        if amt <= self.bal:
            self.bal -= amt
            print(f'Withdrawl Amt : Rs.{amt}/-\n'
                  f'Available balance : Rs.{self.bal}/-')

            sl_no = self.stmt[0][0] + 1
            temp = [sl_no,  '-  ',    amt,  self.bal]
            self.stmt.append(temp)

        else:
            raise Exception ('Insufficent Balance')


    def transfer(self,cust,amt):
        print(f'Available balance : Rs.{self.bal}/-')
        if amt <= self.bal:
            self.bal -= amt
            cust.bal += amt
            print(f'Transferred Amt : Rs.{amt}/-\n'
                  f'Available balance : Rs.{self.bal}/-\n'
                  f'{"*"*30}')

            sl_no = self.stmt[0][0] + sl_no
            temp = [sl_no, '-  ', amt, self.bal]
            self.stmt.append(temp)

            cust.stmt = [[1, '-  ', '-  ', cust.bal]]
            sl_no = self.stmt[0][0] + 1
            temp = [sl_no,    amt,    '-   ',    cust.bal]
            cust.stmt.append(temp)

        else:
            raise Exception ('Insufficent Balance')

    def mini_stmt(self):
        print(f'SL_No   Dp  Wd  bal')
        for i in self.stmt:
            print(f'{i[0]}    {i[1]}    {i[2]}    {i[3]}')




b=Bank('Jaya',1234567,9118762851,'Patel Nager',30000)
print(b.mini_stmt())
print(b.bnk_name)
print(b.acc_no,b.brch,b.deposit(5000)) 
'''


# ===========================================>>>
# s = 'hello python'
# res=0
# for i in s:
#     res+=1
# print(res)



# s = 'hello pyhton'
# res=''
# for i in s:
#     res=i+res
# print(res)

# s = 'Hello World'
# u='universe'
# r=''
# for i in s.split():
#     if i=='World':
#         r+=u
#     else:
#         r=i+' '
# print(r)



# s = 'Hello World'
# if 'World' in s:
#     s1=s.replace('World','universe')
# print(s1)


# s = 'hello world'
# res=[]
# for i in s:
#     res+=[i]
# print(res)



# s='hello world'.split()
# res=''
# for i in s:
#     res+=i+' '
# print(res)



# s = 'hello python'
# # print(s[::2])

# for i in range(0,len(s),2):
#     print(s[i],end=' ')



# s = 'hello python'
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)


# def swap_case(string):
#     res=''
#     for i in string:
#         if ord('a')<=ord(i)<=ord('z'):
#             res+=chr(ord(i)-32)
#         else:
#             res+=chr(ord(i)+32)
#     return res
# print(swap_case('hegHSHlksuns'))
# print(swap_case('jaAY'))
        
        
        
# string='jaYA'
# rs=''
# for i in string:
#     if ord('a')<=ord(i)<=ord('z'):
#         rs+=chr(ord(i)-32)
#     else:
#         rs+=chr(ord(i)+32)
# print(rs)


# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# l3 = [3,6,9,12]
# l4 = []

# print(sum([l1,l2,l3,l4],[]))
# print([*l1,*l2,*l3])



# for i in zip(l1,l2):
#     # print(i,end=' ')
#     l4.append(i)
# print(l4)


# s = 'malayalam'
# if s==s[::-1]:
#     print('it is palindrome ')
# else:
#     print('it is not palindrome')


# s = 'hello world'
# ch='w'
# for i,j in enumerate(s):
#     if j=='w':
#         print(f'the charecter {ch} is present in the index {i}')



# sentence = 'hello world welcome to python programming hi there'
# d={}
# for i in sentence.split():
#     if i[0] in d:
#         d[i[0]]+=[i]
#     else:
#         d[i[0]]=[i]
# print(d)


# from collections import defaultdict
# d=defaultdict(list)

# for i in sentence.split():
#     d[i[0]]+=[i]
# print(d)



# s = 'hellohai'
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,'-')
# print(s)



# def outer(func):
#     def inner(*a,**b):
#         print('only positive integer')
#         res=func(*a,**b)
#         return abs(res)
#     return inner

# @outer
# def number(a,b):
#     return a-b
# print(number(-10,5))


# l = [34, 'hello', 'apple', 56.7, 4546, 67.8,'google', 45]
# def check(lst):
#     res=[]
#     for i in l:
#         if isinstance(i,str):
#             res.append(i)
#         elif isinstance(i,int):
#             res+=[int(str(i)[::-1])]
#         elif isinstance(i,float):
#             res+=[float(str(i)[::-1])]
#     return res
# print(check(l))


# class simple:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self,dx,dy):
#         return self.a+dx,self.b+dy
    
#     def sub(self,dx,dy):
#         return self.a-dx,self.b+dy
    
# s=simple(10,20)
# print(s.sub(3,5))



# class Acces_dict:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __getitem__(self,key):
#         return self.__dict__[key]
    
# s=Acces_dict('jaya',21)
# print(s['name'])
# print(s.name)


# s = 'Hi How are you'
# s1=s.split()
# print(s1[::-1])


# res=''
# for i in s.split():
#     res+=i[::-1]+' '
# print(res)


# s = 'Hi How are you'
# res=''
# for i in s:
#     res=i+res
# print(res)


# l = [1,2,3,4]
# l1 = [2,4,6,8]

# print([l,l1])
# print([l, l1])
# print((l,l1))
# print((l, l1))



# l = [1,3,5,7,2,4,6,7,3,1]
# lst=[]
# for i in l:
#     if i not in lst:
#         lst.append(i)
# print(lst)


# l = [1,3,5,7,2,4,6,7,3,1]
# dupli=[]
# non_dupli=[]
# for i in l:
#     if i not in non_dupli:
#        non_dupli.append(i) 
#     else:
#         dupli.append(i)
# print(dupli)
# print(non_dupli)


# s = 'Life is full of surprises and miracles'
# long_word=''
# for i in s.split():
#     if len(long_word)<len(i):
#         long_word=i
# print(long_word)


# d = {'a': 'apple', 'one': 1, 'b': 'ball', 'three': 3,
# 'four':4, 'n': 45.7}
# l={}
# for i,j in d.items():
#     if isinstance(j,str):
#         l[i]=j[::-1]
#     else:
#         l[i]=j
# print(l)
    
    
    
# t = ('1', '2', '3', '4')
# # print(''.join(t))
# res=''
# for i in t:
#     res+=i
# print(res)


# a = ['hello', 'hai', 'world']
# b = ['hello', 'hai', 'world', 'python']

# for i in b:
#     if i not in a:
#         print(i,end=' ')



# d={1:1,2:2,'1':2,'2':3}
# d['1']=2
# # print(d[d[d[str(d[1])]]])
# print(d[1])
# # print(str(d[1]))
# # print(d[str(d[1])])
# print(d[d[str(d[1])]])
# print(d[d[d[str(d[1])]]])
# print(d[2])


# class demo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __getitem__(self,kay):
#         return self.__dict__[kay]

# d=demo('jaya',21)
# print(d.name)
# print(d['name'])
        


# l = [1,3,5,7,2,4,6,7,3,1]
# dupli=[]
# non_dupl=[]
# for i in l:
#     if i not in  non_dupl:
#         non_dupl.append(i)

        
#     else:
#         dupli.append(i)
        
# print(dupli)
# print(non_dupl)


# s = 'Life is full of surprises and miracles'
# l_word=''
# for i in s.split():
#     if len(l_word)<len(i):
#         l_word=i
# print(l_word)



# d = {'a': 'apple', 'one': 1, 'b': 'ball', 'three': 3,
# 'four':4, 'n': 45.7}
# dd={}
# for i,j in d.items():
#     if isinstance(j,str):
#         dd[i]=j[::-1]
#     else:
#         dd[i]=j
# print(dd)



# t = ('1', '2', '3', '4')
# res=''
# for i in t:
#     res+=i
# print(res)


# a = ['hello', 'hai', 'world']
# b = ['hello', 'hai', 'world', 'python']

# for i in b:
#     if i not in a:
#         print(i,end=' ')


# def check(*a,**b):
#     if len(a)>5:
#         print(f'the arguments length is {len(a)} i.e more than five')
# check(1,3,5,7,8,9)



# def revee(s):
#     res=[]
#     for i in s:
#         if i in res:
#             res=i+res
#             print(res)
# print(revee([1,2,3,4]))


# def fun(*a):
#     for i in a:
#         if isinstance(i,(list,tuple,str)):
#             return i[::-1]
#     return a
# print(fun('hello'))
# print(fun([1,2,3,4]))



# def fun(s):
#     res=[]
#     for i in s:
#         if i in res:
#             res.append(i[::-1])
#             print(res)
# print(fun('hello'))


# def fun(str,i):
#     if i%2==0:
#         print(str[1::2])
#     else:
#         print(str[0::2])
# fun('TRACXN', 0)
# fun('TRACXN', 1)



# s = 'Sony12India567pvt21ltd'
# sum=0

# for i in s:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)

# import re
# s = 'Sony12India567pvt21ltd'
# from re import findall
# r=findall('[0-9]',s)
# var=[int(i) for i in r]
# print(sum(var))



# l = ['hello', '123', 'hai', 'python', '345']
# num=[]
# for i in l:
#     if i.isdigit():
#         num.append(i)
# print(num)


# l = ['hello', '123', 'hai', 'python', '345']
# n=''.join(l)
# import re
# from re import findall
# s=findall('[0-9]+',n)
# var=[int(i) for i in s]
# print(var)


# s = 'hiihellowordhellowar'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# s = 'hiihellowordhellowar'
# from collections import defaultdict
# dd=defaultdict(int)
# for i in s:
#     dd[i]+=1
# print(dd)


# from collections import defaultdict
# dd = defaultdict(int)
# for i in s:
#     dd[i] +=1
# print(dd)



# s = 'helloworld'
# d={}
# for i in s:
#     if s.count(i)>1:
#         d[i]=s.count(i)
# print(d)



# s = 'helloworld'
# for i in s[1::2]:
#     print(i,end=' ')



# l = [1,3,5,7]
# var=lambda i:i**2
# print(list(map(var,l)))
     
     
     
# def check(str1,str2):
#     if sorted(str1)==sorted(str2):
#         print(f'{str1} & {str2} is anagram')
#     else:

#         print(f'{str1} & {str2} is not anagram')

# check('cola','coal')


# names = ['apple', 'google', 'yahoo', 'gmail',
# 'flipkart', 'amazon']
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=len(i)
# print(d)
    
    
    
# l = [[1,2,3], [4,5,6], [7,8,9]]
# var=[sum(i) for i in l]
# print(var)
# print(sum(var))


# s = ['hello', 'hai', 'python']
# rs=[]
# for i in s:
#     rs=[i[::-1]]+rs
# print(rs)

# old=eval(input('Enter the old string:'))
# new=eval(input('Enter the new string:'))
# d = {'a': 100, 'b':{'m':'man', 'n':'nose', 'o':'ox'}}
# for i,j in d.items():
#     if isinstance(j,dict):
#         for k,v in j.items():
#             if v==old:
#                 j[k]=new
# print(d)

# d = {'a': 100, 'b':{'m':'man', 'n':'nose', 'o':'ox'}}
# def  replace(str,old,new):
#     for i,j in d.items():
#         if isinstance(j,dict):
#             for k,v in j.items():
#                 if v==old:
#                     j[k]=new
#     return d
# print(replace(d,'man','jaya'))
# print(replace(d,'100','jaya'))
    
# d = {'a': 100, 'b':{'m':'man', 'n':'nose', 'o':'ox'}}
# print(d.items())


# names = ['listen', 'hello', 'eat', 'desserts',
# 'silent', 'peek', 'ate',
# 'keep', 'tea', 'stressed']
# d={}
# for i in names:
#     nms=''.join(sorted(i))
#     if nms not in d:
#         d[nms]=[i]
#     else:
#         d[nms]+=[i]
# print(d)

# names = ['listen', 'hello', 'eat', 'desserts',
# 'silent', 'peek', 'ate',
# 'keep', 'tea', 'stressed']
# d={}
# for i in names:
#     nms=''.join(sorted(i))
#     if nms not in d:
#         d[nms]=[i]
#     else:
#         d[nms]+=[i]
# print(d)



# print([i for i in range(2,50,2)])



# s = 'This is a programming language and programming is fun'
# res=''
# for i in s.split():
#     if len(i)>len(res) and s.count(i)==1:
#         res=i
# print(res)



# names = ['apple', 'google', 'gmail', 'apple',
# 'yahoo', 'google']
# l=[]
# var=[i for i in names if names.count(i)==1]
# print(var)
    
    
    
# names = ['apple', 'google', 'yahoo', 'google',
# 'apple', 'yahoo',
# 'apple', 'yahoo', 'gamil']


# var={i:names.count(i) for i in names}
# print(var)

# n=int(input('ENter the number:'))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('it is prime number')
# else:
#     print('it is not prime number')



# l=[]
# for i in range(10):
#     l.append(i)
# print(tuple(l))


# numbers = [10,30, 50, 40, 60, 20]
# num=0
# for i in numbers:
#     if num<i:

#         num=i

# print(num)


# num=int(input('Enter the numer:'))
# var=str(num)
# print(var[-1])



# words=['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','the','eyes','not',
#        'around','the','eyes','dont','look','around','the','eyes','look'
# ,'into','my','eyes',"youre",'under']

# var={i:words.count(i) for i in words }
# print(var)
# print()
# s=list(var.items())
# print(s[0])


# def tail(args,n):
#     return list(args[-n:])

# print(tail('hello',3))


# import math
# def perfact(num):
#     res=num//2
#     for i in range(res):
#         if i*i==num:
#             return True,'it is perfact squre'
#         else:
#             return False,'it is not perfact squre'
# # print(perfact(11))
# print(perfact(169))


# def is_perfectsqu(num):
# res = num//2
# for i in range(res):
# if i * i == num:
# return True
# #return f'{num}--> is a perfect square'
# return False
# # return f'{num}--> is not a perfect square'
#
# print(is_perfectsqu(11))
# print(is_perfectsqu(169))
# print(is_perfectsqu(256))


# def perfact(num):
#     res=num//2
#     for i in range(res):
#         if i*i==num:
#             return True
#         else:
#             return False
        
# print(perfact(121))
# print(perfact(11))


# import math
# def perfact(num):
#     res=math.sqrt(num)
#     if res==int(res):
#         return True
#     else:
#         return False
# print(perfact(121))


# def perfact(num):
#     res=num//2
#     for i in range(res):
#         if i*i==num:
#             return True
#         return False
# print(perfact(121))


# import math
# def perfact(num):
#     res=math.sqrt(num)
#     if res==int(res):
#         return True
#     return False
# print(perfact(121))



# names = ['apple', 'google', 'yahoo', 'google',
# 'apple', 'yahoo',
# 'apple', 'yahoo', 'gamil']
# var={i:names.count(i) for i in names if names.count(i)>1}
# print(var)



# l = ['apple', 123,45.6, 'google', [1,2,3], '4+6',
# 3+3j]
# res=[]
# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         res.append(i)
# print(res)


# print([i for i in l if isinstance(i,(int,float,complex))])


# all_products = ['iphone', 'mac', 'gmail', 'google maps', 'iwatch', 'windows',
#  'ios','google drive', 'one drive']
# from collections import defaultdict
# apple_product=[]
# google_product=[]
# windows_product=[]
# products=defaultdict(list)

# for i in all_products:
#     if i in apple_product:
#         products['apple_product']+=[i]
#     elif i in google_product:
#         products['google_product']+=[i]
#     elif i in windows_product:
#         products['windows_product']+=[i]
# print(products)
    

all_products = ['iphone', 'mac', 'gmail', 'google maps', 'iwatch', 'windows',
 'ios','google drive', 'one drive']

from collections import defaultdict
# pro=defaultdict(list)


# apple=[]
# google=[]
# window=[]

# for i in all_products:
#     if i in apple:
#         pro['apple']+=[i]
#     elif i in google:
#         pro['google']+=[i]
#     elif i in window:
#         pro['window']+=[i]
# print(pro)

# apple_products=[]
# google_product=[]
# windows_product=[]
# products = defaultdict(list)                 #try again
# for product in all_products:
#     if product in apple_products:
#         products['apple_products'] += [product]
#     elif product in google_product:
#         products['google_product']+=[product]
#     elif product in windows_product:
#         products['windows_product']+=[product]
# print(products)



# names = ['apple', 'google', 'yahoo', 'gamil',
# 'facebook', 'flipkart', 'amazon']

# def rotate(l,n):
#     return l[n:]+l[:n]
# print(rotate(names,3))


# l = [1,2,3,4,5]
# shift=2
# for i in range(0,shift):
#     temp=l[0]
#     for j in range(0,len(l)-1):
#         l[j]=l[j+1]
#         l[len(l)-1]=temp
    
# for i in range(0,len(l)):
#     print(l[i],end=' ')
    
    
# s = 'darshan'
# def rotate(l,n):
#     return l[-n:]+l[:-n]
# print(rotate(s,2))



# s = 'hai hello how are you'
# from re import findall
# space=findall('[a-z]+' ,s)
# print(len(space))


# s = 'hai hello how are you'
# res=''
# for i in s:
#     if s.count(i)==1:
#         res+=i+' '
# print(res)


# s = 'hello world'
# consonent=''
# for i in s:
#     if i not in 'aeiouAEIOU':
#         consonent+=i
# print(consonent)


# year=int(input('Enter the year:'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print('it is leap year') 
# else:
#     print('it is not leap year')


# s = 'Hi How are You Welcome to Python And its Fun'
# c=0
# for i in s:
#     if i.isupper():
#         c+=1
# print(c)


# l = [1,2,3,4,5,6,7,8,9]
# res=[]
# for i,j in enumerate(l):
#     if i%2==0:
#         res.append(j)
#     else:
#         res.append(j)
#         print(res)
#         res=[]
# print(res)


# def check_series(l1,l2):
#     if len(l2)<len(l1):
#         return False
#     for i in range(len(l1)-1):
#         if l2[i+i]!=l1[i]+1:
#             return False
#     return True
# l1=[1,2,3,4]
# l2=[5,6,7,8,9]
# if check_series(l1,l2):
#     print('it is countinue series')
# else:
#     print('it is not continue series')


# def check(l1,l2):
#     if len(l2)<2:
#         return False
#     diff=l1[1]-l1[0]
#     for i in range(1,len(l2)):
#         if l2[i]-l2[i-1]!=diff:
#             return False
#     return True
# l1=[1,3,5,7,9]
# l2=[11,13,15,17,19]
# if check(l1,l2):
#     print('continue seires')
# else:
#     print('it is not continue series')
        
        
# def check(l1,l2):
#     if len(l2)<2:
#         return False
#     diff=l1[1]-l1[0]
#     for i in range(1,len(l2)):
#         if l2[i]-l2[i-1]!=diff:
#             return False
#     return True
# l1=[1,2,3,4]
# l2=[5,6,7,8,9]
# if check(l1,l2):
#     print('it is continue series')
# else:
#     print('it is not continue seires')


# s = 'hi hello world how are you hello how are you'
# import re
# from re import finditer
# res=finditer('you',s)
# res1=list(res)
# print(res1[-1])


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         print(cn,end=' ')


# l = [3,4,1,7,2,12,8,6,9,11]
# odd=[]
# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)
# print(sorted(odd)+sorted(even))
# print(sorted(odd)+sorted(even,reverse=True))


# l=[1,2,3,4,5]
# for i in l:
#     l.remove(i)
# print(l)


# s = 'hello@world!welcome!!!python hi how are you & where are you'
# c=0
# for i in s:
#     if i.isalpha():
#         c+=1
# print(c)


# items = ['lotus-flower', 'lilly-flower', 'catanimal', 'dog-animal', 'sunflower-flower']
# d={}
# for i in items:
#     temp=i.split('-')
#     if temp[-1] in d:
#         d[temp[-1]]+=[temp[0]]
#     else:
#         d[temp[-1]]=[temp[0]]
# print(d)
    
    
# files = ['apple.txt', 'yahoo.pdf', 'google.pdf',
# 'gmail.txt', 'amazon.pdf','flipkart.txt']
# d={}
# for i in files:
#     temp=i.split('.')
#     if temp[-1] in d:
#         d[temp[-1]]+=[temp[0]]
#     else:
#         d[temp[-1]]=[temp[0]]
# print(d)
        
        
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_even={}
# for i in numbers:
#     if i%2==0:
#         if 'even' not in odd_even:
#             odd_even['even']=[i]
#         else:
#             odd_even['even']+=[i]
#     else:
#         if 'odd' not in odd_even:
#             odd_even['odd']=[i]
#         else:
#             odd_even['odd']+=[i]
# print(odd_even)


# numbers = [1,2,3,0,4,3,2,4,2,2,0,4]
# sort=sorted(numbers)
# max=[i for i in sort if i>=sort[-1]]
# print(max)

# numbers = [1,2,3,0,4,3,2,4,2,2,0,4]
# sort=sorted(numbers)
# max=[]
# for i in sort:
#     if i>=sort[-1]:
#         max.append(i)
# print(max)
        
        
# s = 'hello world hi apple you yahoo to you'
# s1=s.split()
# max_len=[]
# for i in s1:
#     if len(i)<len(max_len):
#         max_len=i
#         max_len.append(i)
# print(max_len)


# s = '0-0,4-8,20-20,43-45'
# s1=s.split(',')
# res=[]
# for i in s1:
#     var=i.split('-')
#     for j in range(int(var[0]),int(var[1])+1):
#         res.append(j)

# print(res)
        
        
# total_length = ([1, 2, 3], (4,5), ['apple', 'google',
# 'yahoo', 'gmail'],
# (1,2,3), {'a':1, 'b': 2})
# def total(a):
#     length=0
#     for i in total_length:
#         length+=len(i)
#     return length
# print(total(total_length))


# s = 'hello world welcome to python'
# for i in s:
#     if i==' ':
#         var=s.replace(' ','\n')
# print(var)



# numbers = [18, 15, 20, 25, 30, 35, 40, 15, 5]
# sort=sorted(numbers)
# maix_sum=sum(sort[:3])
# mxx_sum=sum(sort[-3:])
# print(sort)
# print(maix_sum,mxx_sum)


# s = 'python@#$%pool'
# from re import findall

# res=findall('[a-z]+',s)
# print(res)

# var=findall(r'p\w+',s)
# print(var)


# num = ['1', '12', '13', '12345', '125', '905', '55',
# '5', '95655', '55555']
# l=[]
# for i in num:
#     if i.endswith('5'):
#         l.append(i)
# print(l)


# names = ['apple', 'google', 'yahoo', 'apple',
# 'yahoo', 'google', 'gmail',
# 'apple', 'gmail', 'yahoo']
# d={}
# for i,j in enumerate(names):
#     if j not in d:
#         d[j]=[i]
#     else:
#         d[j]+=[i]
# print(d)
        
        
        
# s = 'hello world hi hello universe how are you happy birthday'
# from re import findall
# var=findall(r'\bh[a-z]+\b',s)
# print(' '.join(var))



# s = 'hello 123 world 567 wlcome to 9724 python'
# sum=0
# for i in s:
#     if i.isdigit() and int(i)%2==0 :
#         sum+=int(i)
# print(sum) 

# s=input("Enter the string:")
# str=''
# for i in s:
#     if i.isalpha():
#         str+=i
#         pre=i
#     else:
#         str=str+pre*(int(i)-1)
# print(str)
          
          
# s=input("Enter the str:")
# str=''
# for i in s:
#     if i.isalpha():
#         str+=i
#         pre=i
#     else:
#         str=str+chr(ord(pre)+int(i))
# print(str)



    
# def great():
#     name='jaya'
#     return 'hi '+name
# mess=great()
# print(mess)


# n=8
# num=float(input('Enter the number:'))

# res=num**0.5
# print(num,res)


# import cmath
# a=2
# b=6
# c=4

# d=(b**2)-4*a*c

# s1=(-b-cmath.sqrt(d))/(2*a)
# s2=(-b+cmath.sqrt(d))/(2*a)
# print(s1)
# print(s2)

# n=16
# num=int(input('Enter the number:'))
# sum=0
# while(num>0):
#     sum+=num
#     num-=1
# print(sum)


# n=16
# print(n*(n+1)/2)


# n=320
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# import calendar
# print(calendar.calendar(2023))



# X = [[12,7,3],
    # [4 ,5,6],
    # [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# res=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
    
# ]


# for i in range(len(X)):
#     for j in range(len(X[0])):
#         res[i][j]=X[i][j]+Y[i][j]

# for r in res:
#     print(r)


# Program to sort alphabetically the words form a string provided by the user

# str = "Hello this Is an Example With cased letters"

# # print(var)
# var=[i.lower() for i in str.split()]
    
# var.sort()
# for i in var:
#     print(i)



#  ! Basic Python Programs
# base=float(input('Enter the base length of triangle:'))
# height=float(input('Enter the height of the triangle:'))
# area=0.5*base * height
# print('the area of triangle is :', area)


# a=int(input('1st number is :'))
# b=int(input('2nd number is :'))

# temp=a
# a=b
# b=temp

# print(f'After swapping value: a={a}, b={b}')



# import random
# print(random.randint(1,100))

# km=float(input('Enterthe distance in km:'))
# con_factor=0.621
# miles=km*con_factor
# print(f'{km} kilometers is qual to {miles}')


# cel=float(input('Enter the temperature in celcius: '))
# fahrenheit=(cel*1.8)+32
# print(f'{cel} degrees celcius is qual to {fahrenheit} degrees fahrenheit')


# n=int(input('Enter the number:'))
# sum=0
# for i in range(n):
#     sum+=i
# print(sum)


# def find_pairs_with_sum(arr, target_sum):
#     result_pairs = []
#     seen_numbers = set()

#     for num in arr:
#         complement = target_sum - num

#         if complement in seen_numbers:
#             result_pairs.append((num, complement))

#         seen_numbers.add(num)

#     return result_pairs

# # Example usage:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_sum = 10
# pairs = find_pairs_with_sum(arr, target_sum)

# if pairs:
#     print("Pairs with sum", target_sum, "are:", pairs)
# else:
#     print("No pairs found with the given sum.")

# ! ProALLPY1.py
# s=101010
# print(str(s)[::-1])




