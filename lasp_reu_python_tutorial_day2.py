
# coding: utf-8

# # LASP REU Python Tutorial Day 2
# 
# ## Imports
# 
# Remember the huge stack of science libraries (or the list of built-in libraries)?
# 
# So, how to get those?
# 
# With imports:

# In[ ]:

from math import pi
tau = 2*pi
print("The real circular constant is", tau)
# read tauday.com if you don't believe me. ;)


# How to import other libraries, their functions or their values is very flexible.
# 
# One can distinguish mainly 2 kinds:
# * One imports a function directly into the current `namespace`:
# ```python
# from math import sin
# ```
# * import the top module and access via the dot `.`:
# ```python
# import math
# print(math.sin(0.5))
# ```
# 
# In both cases one can rename the object being imported.
# 
# This is a very powerful feature of Python: You can do what you want in terms of how to call things up.

# In[ ]:

from math import sin as stupid_sine
print(stupid_sine(0.5))


# In[ ]:

import math as i_hate_math
print(i_hate_math.cos(-1))


# ## Function returns, packing and unpacking
# 
# Functions can return values.
# 
# (you saw this in the last exercise already):

# In[ ]:

from math import log10

def mylog(value):
    if value < 0:
        return "Logarithm not defined."
    else:
        return log10(value)


# In[ ]:

result = mylog(-1)
result


# In[ ]:

import math
math.log10(-1)


# Maybe you want to return more than one value?
# 
# Python will automatically pack things up:

# In[ ]:

from math import log10

def mylog(value):
    if value < 0:
        return "Logarithm not defined."
    else:
        return value, log10(value)


# In[ ]:

result = mylog(3)
result


# In[ ]:

print(type(result))
len(result)


# Tuples are the immutable version of lists:

# In[ ]:

result[0] = 4


# In[ ]:

mylist = list(result)
mylist


# In[ ]:

mylist[0] = 5
mylist


# and "iterable" as well (meaning I can loop over them):

# In[ ]:

for item in result:
    print(item)


# In[ ]:

waves = [5000, 6000]


# In[ ]:

for wave in waves:
    print(wave)


# In[ ]:

d = {'a':5, 'b':6}
d


# In[ ]:

for key,val in d.items():
    print(key, val)


# Python will always automatically pack for you (as it did above with result), but will never
# automatically unpack for you:

# In[ ]:

val, res = mylog(3)
print(val)
res


# Because of the automatic packing, you can always have less than required variables, but never more:

# In[ ]:

a, b, c = mylog(17)


# In[ ]:

out = mylog(17)


# In[ ]:

type(out)


# In[ ]:

out[0]


# In[ ]:

out[1]


# ### Interlude: strings
# 
# They are also iterables:

# In[ ]:

for char in "Han":  # Remember that I decide on the name of my temporary variable
    print(char)


# Strings have a lot of useful support functions (lingo: `methods`) inside them:

# In[ ]:

s = "Han shot first!"


# In[ ]:

get_ipython().magic('pinfo s.center')


# In[ ]:

s.split()   # by default, spaces are assumed to be the separator


# In[ ]:

s.split('s')  #  note that the separator can be anything, but it will be removed!


# Why are the methods already available when I did not store a string into a variable?

# In[ ]:

'{1}, I am your {0}.'.format('father', 'Luke')


# Note, I am using the `format` method even so I haven't stored that string anywhere.
# 
# Now, even an empty string or a string with only a space has those methods, and one very useful is the 'join' method:

# In[ ]:

' '.join(["It's", 'a','trap!'])


# ### Back to functions: Default values
# Functions can have optional arguments that hold a default value:

# In[ ]:

def sub_reverser(alist, index=0):
    reversed_list = list(reversed(alist))
    return ''.join(reversed_list[index:])


# In[ ]:

''.join(list(reversed('astring')))


# In[ ]:

sub_reverser('astring')


# In[ ]:

sub_reverser('astring', 3)


# This is a very powerful design feature of Python as well: I only need to write one function, but can use it in very different ways, depending on my default arguments (also known as `keyword argument`).

# Ok, let's go to some more meaty science libraries.
# 
# ## matplotlib gallery
# 
# * Can't go into depth of matplotlib library here, very rich and powerful
# * Best way to learn: Go to their gallery page http://matplotlib.org/gallery.html

# In[ ]:

from IPython.display import IFrame
IFrame("http://matplotlib.org/gallery.html", width=800, height=350)


# ## numpy
# 
# For any serious array/vector/matrix based math, you should use the numpy library.
# 
# It is faster, because in contrast to lists, it insists on keeping every item the same data-type. This enables under the hood to create C-objects and pass them to the C or Fortran math libraries.
# 
# These libraries are decade old standards with very well researched behaviour!
# 
# Contrary to the above mentioned freedom for importing, there are some standards that you should just adapt if you don't want to confuse yourself, when searching for tutorials, blogs etc. to help you out.
# 
# This standard imports are:

# In[ ]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Okay, let's do some math:

# In[ ]:

mylist = list(range(10))
mylist


# In[ ]:

arr = np.array(mylist)
arr


# Most import feature of numpy arrays is to support vector math, which lists can't do:

# In[ ]:

mylist / 3


# In[ ]:

arr / 3


# Lingo: `Lists` are Python lists, `arrays` are numpy arrays.
# 
# Basic indexing works the same:

# In[ ]:

mylist[2:4]


# In[ ]:

arr[2:4]


# numpy has it's own range function: `arange()` (standing for array-range):

# In[ ]:

np.arange(10)


# In[ ]:

get_ipython().magic('pinfo np.arange')


# In[ ]:

arr = np.arange(1, 11, 2, dtype='float')  # works the same as range, but also type-able


# In[ ]:

arr.dtype


# Handy array creators:

# In[ ]:

np.ones(3)


# In[ ]:

np.zeros(5)


# Multi-dimensional:

# In[ ]:

np.ones((2,3))  # rows first, then columns


# Note that the `ones` function wants the dimensions as a tuple if more than 1, to not confuse things with other arguments.
# 
# Here's 3D:

# In[ ]:

np.zeros((2,4,3))  # the depth dimension (how many 2D arrays) first!


# Lot's of methods inside the numpy array object:

# In[ ]:

arr.


# Most useful:

# In[ ]:

arr.mean()


# In[ ]:

arr.std()


# In[ ]:

arr.dot(arr)


# In[ ]:

np.ones((3,3)).diagonal()


# In[ ]:

arr.max()


# In[ ]:

arr.argmax()  # WHERE is the max?


# Lazy indexing one of most important functionality:

# In[ ]:

arr


# In[ ]:

arr < 3


# In[ ]:

arr[arr<3]


# 2D numpy (= matrices) have a lot of matrix features:

# In[ ]:

arr2d = np.random.randn(2,3)  # randn provides Gaussian-distributed random values.
arr2d


# In[ ]:

get_ipython().magic('matplotlib inline')

plt.hist(np.random.randn(1000), bins=100, color='green');


# In[ ]:

arr2d


# In[ ]:

arr2d.transpose()


# Absolutely impossible to cover `numpy` even half here, but it's one of the most important tools in Python.
# 
# ## pandas
# 
# Most important high-level data analysis library (in my POV).
# 
# It uses `numpy` under the hood.
# 
# So, my recommendation: 
# 1. Learn the numpy basics, don't try to get it all in, hardly possible.
#  * For example the scipy quickstart tutorial
# 2. Learn Pandas first, and whenever they refer to an unknown numpy feature, look that up.
# 
# Pandas has a nice 10 minutes intro here: http://pandas.pydata.org/pandas-docs/stable/10min.html
# 
# Most important objects in `pandas` are Series and DataFrames

# In[ ]:

import pandas as pd

s = pd.Series(np.arange(10)*24.1)
s


# Important concept in `pandas` are the indexes. `pandas` always keeps the relationship between indices and data intact!
# 
# series filtering works the same as for numpy arrays, as it's build on it:

# In[ ]:

s[s<100]


# DataFrames are the 2D version of Series, complete with column names.
# 
# Another very enticing feature of `pandas` are its datetime abilities:

# In[ ]:

dates = pd.date_range('20130101', periods=10)

print(dates)
df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list('ABCD'))
df


# In[ ]:

df.loc['2013-01-01','A':'C']


# Coolest part is the automatic datetime and multi-graph plotting of DataFrames:

# In[ ]:

df.plot()


# It is using `matplotlib` under the hood, so you could do this yourself, but with much more code.

# In[ ]:

df.head()


# In[ ]:

df.tail(3)


# In[ ]:

df.loc['2013-01-4':'2013-01-09', 'B':'C']


# Above, using the `.loc` attribute of dataframes, this is the fully official way to select data in a dataframe in all possible ways. The first part will always filter the rows you want, the second part always on the columns.
# 
# But if you only want to filter/select on your current index, one can put these conditions directly like an indexing choice into brackets `[]`:

# In[ ]:

df['2013-01-4':'2013-01-09']


# In[ ]:

df[df > 0]


# In[ ]:

df.describe()


# In real-life interactive data analysis, one often calculates new sets of values based on measured stuff.
# 
# It's a breeze with pd.DataFrames:

# In[ ]:

df['E'] = df.A + df.B


# In[ ]:

df['my new column'] = df.C + df.D


# In[ ]:

df['my new column']


# In[ ]:

df.head()


# ### groupby
# 
# Let's have a look at one last powerful feature: Grouping and per-group stats.
# 
# First, we need to create something to group by:

# In[ ]:

import random


# In[ ]:

group = [random.choice('abc') for _ in range(df.shape[0])]
group


# In[ ]:

df['group'] = group
df


# In[ ]:

g = df.groupby('group')
g.size()


# In[ ]:

g.mean()


# Can you imagine how much code you would have to write to do this from scratch?
# 
# Ok, exercise time!
