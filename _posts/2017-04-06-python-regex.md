---
layout: post
title: Python Regular Expression
tags: programming
---

<!-- excerpt -->

<style>
    strong, em {
        color: black;
    }
</style>

```python
# `re` module
import re
# compile regular expression into reusable **regex object**
pattern = re.compile('foo')
```

Once you have a **regex object**, you can use several methods it has.

`regex.match(string[, pos[, endpos]])`
: - Return a corresponding [**match object**](https://docs.python.org/3/library/re.html#match-objects), if the regex matches *at the beginning of* the `string`  
  - Return `None` if the string does not match the pattern

`regex.search(string[, pos[, endpos]])`
: - Return a corresponding **match object**, scanning through `string` looking for the first location where this regex produces a match  
  - Return `None` if there is no match.

Now we can query the **match object** for information about the matching string. It also has several methods and attributes.

`match.group([num1, ...])`
: Return one or more subgroups of the match.

---

<https://docs.python.org/3/library/re.html>
