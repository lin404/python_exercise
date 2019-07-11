# Python exercise
> [Reference (GitHub)](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

Python 2 versun Python 3
* http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
* http://py3readiness.org/

Editor
* http://www.sublimetext.com/

Practice
* [Basic Practice](http://codingbat.com/python)
* [More Mathematical (and Harder) Practice](https://projecteuler.net/archives)
* [List of Practice Problems](http://www.codeabbey.com/index/task_list)
* [A SubReddit Devoted to Daily Practice Problems](https://www.reddit.com/r/dailyprogrammer)
* [A very tricky website with very few hints and touch problems (Not for beginners but still interesting)](http://www.pythonchallenge.com/)

Dynamic typed

Reverse Index
* -1 is the last one
* trick: "String"[::-1])

Slice [Start:Stop:Size]

### String
* Immutability
* letter*num
* upper(), lower(), split(), capitalize()
* join(list) -> '--'.join([1,2,3]) == '1--2--3'

.format()
* float: {value:width.precision f}

f-strings
* e.g. print(f'{name} is {age} years old')

Moreover
* https://pyformat.info/

### List
* list = list1 + list2
* list.append()
* list.pop(index) -> return element
* list.sort() -> return None
* list.reverse() -> return None
* list*num -> [1]*2 == [1,1]

### Dictionary
* may.keys()
* may.values()
* may.items()

### Tuples
* Immutability
* tuples.count(key)
* tuples.index(key)

### Set
* myset = set(list)
* myset.add()

### I/O
%%writefile filename.txt \
file context \
myfile = open(filename.txt)
* **mode='r'** is read only
* **mode='w'** is write only (overwrite file or create new)
* **mode='a'** is append only (add on to file) -> myfile.write('new context')
* **mode='r+'** is reading and writting
* **mode='w+'** is writting and reading (overwrite file or create new)

myfile.close()
* with open(filename.txt) as myfile: myfile.read() -> no need use close()

myfile.read() -> return String \
myfile.seek(0) -> to do myfile.read() again \
myfile.readlines() -> return List with '\n' in the end

**while ... else ...** \
**break**: break out of the current closest enclosing loop \
**continue**: go to the top of the closest enclosing loop \
**pass**: do nothing at all

### Operators
* list(range(start, stop, stepSize)) returns list
* enumerate(list) returns (index, item)
* zip(list1, list2, list3, ...) returns tuples
* item in list/dictionary/dictionary.values()/dictionary.keys() returns boolean
* min(list)
* max(list)
* from random import shuffle -> shuffle(list) not returns anything
* from random import randint -> randint(begin, stop) returns a random num in the range
* result = input('input: ') returns any input as String
* string.capitalize() / string.title()

### function
* e.g. def myfunc(value='default') -> set defualt value
* e.g. def myfunc(*arg) -> takes in an arbitrary number of argument as tuple
* e.g. def myfunc(**kwargs) -> accept arguments(as many as wanted) as dictionary

### map/filter/lambda expression
* map(myfunc, list) returns myfunc(x) for x in list
* filter(myfunc, list) only returns myfunc(x) for x in list if condition is true
* map(lambda x: x/2, list) returns x/2 for x in list

### LEGB rule
* L - local -> name assigned in any way within a function, and not declared global in that function
* E - Enclosing function locals -> names in the local scope of any and all enclosing functions, from inner to outer
* G - Global(module) -> names assigned at the top-level of a module file, or declared global in a def within the file
* B - Built-in(Python) -> names preassigned in the built-in names module: open, range, SyntaxError
```Python
# Globla
def function1():
    # Enclosing
    def function2 ():
        # Local
        # reassign global variable (better avoid using it)
        global x
```

### Special (Magic/Dunder) methods
* __init__
* __str__
* __len__
* __del__

### Module and Package
* __init__.py
* if __name__ ==  "__main__"

### Test tools
* pylint
* unittest

### Decorators
```Python
def decorator_func(original_func):
        def wrap_func():
                # some extra code
                original_func()
                # some extra code
        return wrap_func

new_func = decorator_func(some_func)
```

``` Python
@new_decorator
def some_func():
        pass
```

### Python Web page Framework
* [decorators](http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/)
* [Flask](http://flask.pocoo.org/)
* [Django](https://www.djangoproject.com/)

### Python Generator
* yield -> memory efficient
* iter()

### Advanced modules
* from collections import Counter
```
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
```

* from collections import defaultdict -> return default dictionary
* from collections import OrderedDict -> return ordered dictionary
* from collections import namedtuple -> create a new object/class type with some attribute fields

* [pdb](https://docs.python.org/3/library/pdb.html) -> debugger pdb.set_trace()
* [timeit](https://docs.python.org/3/library/timeit.html) -> timeit.timeit(func, number=step_num) / %timeit func

### Regular Expressions
* https://docs.python.org/3/library/re.html#regular-expression-syntax
* http://www.tutorialspoint.com/python/python_reg_expressions.htm

#### Escape Codes

You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more. For example:

<table border="1" class="docutils">
<colgroup>
<col width="14%" />
<col width="86%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Code</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\d</span></tt></td>
<td>a digit</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\D</span></tt></td>
<td>a non-digit</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\s</span></tt></td>
<td>whitespace (tab, space, newline, etc.)</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\S</span></tt></td>
<td>non-whitespace</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\w</span></tt></td>
<td>alphanumeric</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\W</span></tt></td>
<td>non-alphanumeric</td>
</tr>
</tbody>
</table>

### StringIO (set String as file object)
* https://docs.python.org/3/library/io.html

### Advanced Numver
* hex(num) -> hexadecimal
* bin(num) -> binary
* pow(x,y,z) -> x**y%z
* abs() -> absolut value
* round(x, y) -> round x keep y decimals

### Advanced String
* s.find(x)
* s.count(x)
* s.center(num, x)
* s.expandtabs()
* s.isalnum()
* s.isalpha()
* s.istitle()
* s.isspace()
* s.endswith(x)
* s.partition(x) -> only split the first x

### Advanced Set
* s.clear()
* s.copy()
* s1.difference(s2) -> return items in s1 but not in s2
* s1.difference_update(s2) -> update s1, only keep difference
* s.discard(x)
* s1.intersection(s2) -> return {} both in s1 and s2
* s1.inrersection(s2) -> update s1, only keep the same items
* s1.isdisjoint(s2) -> return true if they do NOT have the same items
* s1.issubset(s2) -> return true if s2 contains s1
* s2.issuperset(s1) -> return true if s2 contains s1
* s1.symmetric_difference(s2) -> return items in s1 but not in s2, and the items in s2 but not in s1
* s1.union(s2) -> return {} either in s1 or s2
* s1.update(s2) -> update s1, add all items in s2 to s1

### Advanced List
* l1.extend(l2) -> extend l1 with l2
* l.pop(num)
* l.remove(x) -> only remove the first matched item

### GUI frameworks (Graphical User Interface)
* GUI -> dashboards for data/business analysis situations
* https://wiki.python.org/moin/GUI%20Programming%20in%20Python
* https://wiki.python.org/moin/GuiProgramming

* [PyGame](https://www.pygame.org/hifi.html) -> graphical game

### Interview Info
> [reference](https://www.javatpoint.com/python-interview-questions)
* Django, Flask
* SciPy, NumPy
* Extensible, Object-oriented
* PEP8
* the difference between del and remove()
* zip(), swapcase(), strip(), lstrip(), join(), shuffle()
* interpreted, machine language, no need compilation
* memory management
* namespace
* iterators -> next()
* generator -> yield

### Tree
* lookup, insert, delete -> O(logn)
* Depth-First Search (DFS)
