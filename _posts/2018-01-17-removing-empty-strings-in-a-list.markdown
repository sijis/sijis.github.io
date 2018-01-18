---
layout: post
title: Removing empty strings in a list
date: 2018-01-17 22:05:11
categories: python code
---

I've needed on occassion to remove empty strings or entries from a list in python. These are the ways I could think of removing those empty strings.

I would highly recommend the first two solutions. All the other ones are unusual and experimental.

```
action_heros = [
    'Iron Man',
    '',
    'Superman',
    'Spider-Man',
    '',
    'Hulk',
    '',
    'Captain America',
]
```

Solution 1
----------

Using `filter()`.

```
In [1]: filter(None, action_heros)
Out[1]: <filter at 0x7f56268964a8>

In [2]: list(filter(None, action_heros))
Out[2]: ['Iron Man', 'Superman', 'Spider-Man', 'Hulk', 'Captain America']
```


Solution 2
----------

A `for` loop.

```
In [1]: heros = []

In [2]: for hero in action_heros:
    ...:     if hero:
    ...:         heros.append(hero)
    ...:

In [3]: heros
Out[3]: ['Iron Man', 'Superman', 'Spider-Man', 'Hulk', 'Captain America']
```

Solution 3
----------

Using `collections.Counter`.

```
In [1]: from collections import Counter

In [2]: c = Counter(action_heros)

In [3]: c
Out[3]:
Counter({'': 3,
         'Captain America': 1,
         'Hulk': 1,
         'Iron Man': 1,
         'Spider-Man': 1,
         'Superman': 1})

In [4]: c.pop('')
Out[4]: 3

In [5]: c.keys()
Out[5]: dict_keys(['Iron Man', 'Superman', 'Spider-Man', 'Hulk', 'Captain America'])

In [6]: list(c.keys())
Out[6]: ['Iron Man', 'Superman', 'Spider-Man', 'Hulk', 'Captain America']
```

Solution 4
----------

Using `collections.UserList`.

```
In [1]: from collections import UserList

In [2]: n = UserList(action_heros)

In [3]: n
Out[3]: ['Iron Man', '', 'Superman', 'Spider-Man', '', 'Hulk', '', 'Captain America']

In [4]: for i in range(0, n.count('')):
    ...:     n.remove('')
    ...:

In [5]: n
Out[5]: ['Iron Man', 'Superman', 'Spider-Man', 'Hulk', 'Captain America']
```
