from collections import Counter

a = "aaaaaaaabbbbbbccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))
# for elem in my_counter.elements():
#     print(elem)
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['d'] = 4
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

from collections import defaultdict
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
# d.pop()
# d.popleft()
# d.clear()
# d.extend([4, 5, 6])
d.extendleft(reversed([5,6,7]))
print(d)
# d.rotate(1)
d.rotate(-1)
print(d)