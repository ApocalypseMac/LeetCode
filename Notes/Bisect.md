# 二分查找算法

## 1. 模板

二分查找一般而言都可以化为三种形式：

- 无重复形式 （寻找该值，例如严格单调连续函数求零点）

- 有重复形式

    - 寻找左边界

    - 寻找右边界

实际上，对于上述任意一种形式，在比较时的选择都有三种：

- `f(mid) > target`

- `f(mid) == target`

- `f(mid) < target`

而三种形式，实质上就是在这三个选择时进行不同的收缩边界的操作。

对于第一种而言，我们假设找到则返回下标，否则返回 `-1` ，具体实现如下（这里为了显示三种选择做了一定改写，下同）：

```python
def bisect(a: List[int], target: int):
    lo, hi = 0, len(a) - 1 # closed interval
    while lo <= hi: # exit loop if lo > hi (not found)
        mid = lo + (hi - lo) // 2 # avoid exceed
        if a[mid] == target: # found
            return mid
        elif a[mid] < target:
            lo = mid + 1 # mid not match, thus increase lo
        elif a[mid] > target:
            hi = mid - 1 # mid not match, thus decrease hi
    return -1 # not found
```

对于第二种，事实上在 Python 里有内置的库函数（注意输出值，详见源代码）`bisect.bisect_left()` 和 `bisect.bisect_right()` 可以参考，这里我们对其稍作改动，使其输出的内容为 `target` 的左边界和右边界（不存在的情况参见注释, 段落注释为库代码内注释）。详细实现如下（还是一样对于三种选择分开写）：

```python
def bisect_left(a: List[int], target: int):
    '''
    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  

    So if x already appears in the list, a.insert(x) will insert just 
    before the leftmost x already there.
    '''
    lo, hi = 0, len(a) # right-open interval
    while lo < hi: # exit loop if lo = hi
        mid = lo + (hi - lo) // 2
        if a[mid] == target: # found, decrease hi
            hi = mid
        elif a[mid] < target:
            lo = mid + 1
        elif a[mid] > target:
            hi = mid
    return lo

def bisect_right(a: List[int], target: int):
    '''
    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  

    So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    '''
    lo, hi = 0, len(a) # right-open interval
    while lo < hi: # exit loop if lo = hi
        mid = lo + (hi - lo) // 2
        if a[mid] == target: # found, increase lo
            lo = mid + 1
        elif a[mid] < target:
            lo = mid + 1
        elif a[mid] > target:
            hi = mid
    return lo # SEE REMARK ABOVE
    # return lo - 1 ##NOTE: if return right bound, then MINUS 1.
```

注：需要强调的是，对于上述 `bisect.bisect_right()` 未注释的返回值，返回的是使得 `all e in a[:i] have e <= x`, 这里的 `i` 是**取不到**的，因此如果需要寻找右边界，需要在返回值做 `-1` 处理。

注2：事实上，上述 `bisect.bisect_right(a, target)` 和 `bisect.bisect_left(a, target + 1)` 是**等价**的，具体证明从略。换言之，其实左右边界的模板本质是相同的。

## 2. 题目