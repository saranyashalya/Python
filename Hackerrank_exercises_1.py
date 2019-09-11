class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)

obj1 = Rocket("Rocket 1", "till stratosphere")
print(obj1.launch())

class MarsRover(Rocket):
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker
        
    def get_maker(self):
        return "%s is made by %s" % (self.name, self.maker)

obj2 = MarsRover("Mars rover","till mars","ISRO")
print(obj2.get_maker())

class MarsRoverComp():
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)
        self.maker = maker
    
    def get_maker(self):
        return ("%s launched by %s" %(self.rocket.name, self.maker))

obj3 = MarsRoverComp("Mars rover2","till Mars", "ISRO")
print(obj3.get_maker())



class employee:
    perc_raise = 1.15
    def __init__(self, first, last, sal):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.email = first + "." + last +"@company.com"
    
    def apply_incre(self):
        self.sal = self.sal * 1.15 

emp1 = employee('sara','g',6000)
emp1.email
emp2 = employee('shal','p',5000)
emp2.email

print(emp1.sal)
emp1.apply_incre()
print(emp1.sal)

emp1.__dict__


### errors and exceptions

try:
    print("Inside try block")
    print(10/0)
except:
    print("Inside except block")
finally:
    print("Inside finally block")


## read only positive input
    
while True:
    try:
        user_input = int(input())
        if user_input< 0:
            raise ValueError("Please give positive number")
        else:
            print("user entered %s " %user_input)
    except ValueError as e:
         print(e)
         

### Hackerrank exercise - set operations - pop, remove and discard

n = int(input())
if (n>0) & (n<20):
    s = set(map(int, input().strip().split()[:n]))
N = int(input())

if (N>0) & (N<20):
    for i in range(N):
        eval('s.{0}({1})'.format(*input().split()+['']))
    print(sum(s))


## set union
    
n= int(input())
e = set(map(int, input().strip().split()[:n]))
b = int(input())     
f = set(map(int, input().strip().split()[:b]))
len(e | f)
print(len(e.union(f)))

##set intersection
n= int(input())
e = set(map(int, input().strip().split()[:n]))
b = int(input())     
f = set(map(int, input().strip().split()[:b]))
len(e & f)
print(len(e.intersection(f)))

##set Difference
n= int(input())
e = set(map(int, input().strip().split()[:n]))
b = int(input())     
f = set(map(int, input().strip().split()[:b]))
len(e - f)
print(len(e.difference(f)))


##set Symmetric Difference
n= int(input())
e = set(map(int, input().strip().split()[:n]))
b = int(input())     
f = set(map(int, input().strip().split()[:b]))
print(e ^ f)
print(len(e.symmetric_difference(f)))

## set mutations
#We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

#we can use below operations for set mutations
# =============================================================================
# .update() or |= 
# .intersection_update() or &=
# .difference_update() or -=
# .symmetric_difference_update() or ^=
# =============================================================================

if __name__ == '__main__':
    n =int(input())
    s = set(map(int, input().strip().split()[:n]))
    B = int(input())
    for _ in range(B):
        command, c = input().split()
        new_s = set(map(int, input().strip().split()[:int(c)]))
        getattr(s, command)(new_s)

    print(sum(s))


### Counting set elements
from collections import Counter

K=int(input())
if (K>1) & (K<1000):
    s = list(map(int, input().strip().split()))
    ab = Counter(s)
    for i in set(s):
        if ab[i] == 1:
            print(i)

         
### Finding subsets 
    
for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
    
    
## Finding Supersets
    
### Finding subsets 
result = []
a=  set(input().split())
z = int(input())
for _ in range(z):
    result.append(a.issuperset(set(input().split())))

print('True' if all(result) else 'False')


### regular expression substitution
import re

n= int(input())
for _ in range(n):
    lines = input()
    

print(re.sub(r"\s&&\s", " and " , str(lines)))
print(re.sub(r"*\s||\s*", " or " , str(lines)))


##nested List comprehensions
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

if X+Y+Z != N:
    print([[i,j,k] for k in range(Z) for j in range(Y) for i in range(X) if i+j+k !=N])


##nested list comprehension
    
l =[[3,2,1],[5,6,7]]
print([float(xs) for x in l for xs in x])


## Finding runner up in list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = set(arr)
    print(sorted(arr)[-2])


## finding students with second lowest score

combination =[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = (input())
        score = (float(input()))
        combination.append([name,score])
        
combination.sort(key = lambda x : x[1])
values_set = list(set([values[1] for values in combination]))
values_set.sort()
final = [ v for v in combination if v[1]==values_set[1]]
final.sort(key=lambda x:x[0])
names = [f[0] for f in final]
print(*names, sep="\n")


### Finding average mark for the student who is interested in
from statistics import mean

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("%.2f" %round(mean(student_marks[query_name]),2))


##Multiple operations in list
    
l=[]
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        command = input().split()
        cmd = command[0]
        args = command[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) +")"
            eval("l." +cmd)
        else:
            print(l)


### Text wrap

import textwrap
            
python_desc = """Python is a general-purpose interpreted, interactive, object-oriented, 
                 and high-level programming language. It was created by Guido van Rossum 
                 during 1985- 1990. Like Perl, Python source code is also available under 
                 the GNU General Public License (GPL). This tutorial gives enough 
                 understanding on Python programming language."""
                 
my_wrap = textwrap.TextWrapper(width =40)
#wrap returns list
wrap_list = my_wrap.wrap(text = python_desc)

for line in wrap_list:
    print(line)

single_line = """Python is a general-purpose interpreted, interactive, object-oriented, 
                 and high-level programming language."""
# fill returns string and not list
print('\n\n' + my_wrap.fill(text = single_line))

# dedent function removes any common leading whitespaces

s ="""\
        hello
         world
        """

print(repr(s))
new_text = textwrap.dedent(s)
print(repr(new_text))

## shorten function truncates the input string to the width specified

sample_text = """This function wraps the input paragraph such that each line 
n the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

wrapper = textwrap.TextWrapper(width =50)

dedented_text = textwrap.dedent(text = sample_text)
original = wrapper.fill(text= dedented_text)

print("Orignial : \n")
print(original)

shortened = textwrap.shorten(text = original, width =100)
shortened_wrapper = wrapper.fill(text= shortened)

print("\n Shortened: \n")
print(shortened_wrapper)

## indent function used to add a given prefix to the beginning of the selected lines of the text.

s1 = textwrap.indent(text = s, prefix =" ")
print(s1)

s2 = textwrap.indent(text=s, prefix ="+", predicate = lambda line: True)
print(s2)




############################################################################################################################
## difference between str and repr
# str is used for creating output for end user -> informal string representation of object
# repr is sed for debugging and development -> official string representaiton of an object
print(str('hi saranya'))
print(repr('hi saranya'))

print(str(2/11))
print(repr(2/11))


import datetime
today = datetime.datetime.now()

print(str(today))

print(repr(today))


class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __repr__(self):
        return ("Rational(%s, %s)"% (self.real, self.img))
        
    def __str__(self):
        return ("%s +i%s" % (self.real, self.img))
    
t =complex(10,20)
repr(t)
str(t)


## assert

u=[]
assert len(u) != 0, "List is empty"
#o/p:
#AssertionError: List is empty

##zip and unzip
##using list comprehension
test_list =[('Sara',1),('welcome',2),('back',3)]
print([[i for i,j in test_list],[j for i,j in test_list]])

##using zip

print(list(zip(*test_list)))

zip_o = zip(*test_list)

[i for i in zip_o]

# unzipping
names, marks = zip(*test_list)

players =['a','b','c']
scores =[10,20,30]

#using just zip(players,scores) will empty zip variable after first use.
zipped_version = list(zip(players, scores))

print(zipped_version)

p,s = zip(*zipped_version)

pd.DataFrame(dict(list(zip(players,scores))), index = [0])
