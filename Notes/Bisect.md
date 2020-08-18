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

### 2.1 赤裸裸说明要搜索指定元素的

这部分基本就差二分贴脸，稍有常识的人便可以看出，如果（下略，水表坏了请窒息）

- [LC704](https://leetcode-cn.com/problems/binary-search/) 原 题 贴 脸

- [LC034](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) 不用说了吧，左右边界模板各用一次。

- [LC035](https://leetcode-cn.com/problems/search-insert-position/) 左边界，对于恰好等于的情况改一下。

- [LC033](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) / [LC081](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/) 通用思路是两次二分，第一次找旋转点（可以偷懒，找到有序区间且包含 `target` 就进行下一步），第二次找 `target`. 有重复时相对棘手一些，（可能）需要线性去重，（如果线性去重）最坏时间复杂度是线性的。

- [LC153](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) / [LC154](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) 二分找旋转点（比较 `mid` 和 `hi`），注意在有重复时遇到相同值的处理（线性去重）。

- [LC050](https://leetcode-cn.com/problems/powx-n/) / [LC069](https://leetcode-cn.com/problems/sqrtx/) 利用二分思想进行算术运算。


- [LC1533](https://leetcode-cn.com/problems/find-the-index-of-the-large-integer/) 二分找异常值问题，follow up 比较有意思。

### 2.2 （在给定范围内）寻找满足要求的值/最值

二分算法能将**优化问题** (optimal solution, optimization form) 转化为**决策问题** (whether solution exists, decision form)。

- [LC004](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/) 此处找中位数相当于找两个给定中间位置（可能相等）的值，考虑两个子数组都有序，求第 `k` 个元素就可以对于两个数组**均取** `k // 2` 位，比较后较小值对应的部分一定是在前 `k` 个的，余下类推，即可在对数时间内完成。

- [LC378](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)  事实上该问题的子问题是 [LC240](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/), 对于任意一个 `target`, 我们都能实现线性时间内的查找。同样，根据数组的有序性，我们也可以确定该矩阵中大于/小于/等于 `target` 的元素数量。那么问题就可以变成，**确定 `target` 使其恰好为矩阵中第 `k` 个最小的元素**。这样就可以以矩阵取值范围为上下界套二分查找了。

- [LC719](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/) 和前面的类似，小于某个数的对数具有单调性，因此可以上下界套二分查找。对于单次查找，可以排序后双指针寻找。

- [LC410](https://leetcode-cn.com/problems/split-array-largest-sum/) / [LC1552](https://leetcode-cn.com/problems/magnetic-force-between-two-balls/) 数组分割求子数组和最小值的最大值，同样寻找子问题，亦即给定一个值能实现满足（最小值）要求的分割，这是一个线性时间的贪心问题。对于不同取值的子问题，结果也有**单调性质**（可行->不可行），因此可以套二分求解。

- [LC878](https://leetcode-cn.com/problems/nth-magical-number/) / [LC1201](https://leetcode-cn.com/problems/ugly-number-iii/) 求满足条件的第 `n` 个数，可以考虑小于某个数 `num` 的满足条件数个数，其一定递增，并且可以通过最小公倍数+容斥原理求出，因而可以二分。

- [LC793](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/) 首先需要知道快速计算阶乘函数结尾 `0` 的个数，其次该函数是递增的，因此可以先确定上下界，然后二分搜索左右边界。

- [LC483](https://leetcode-cn.com/problems/smallest-good-base/) 从进制位数入手，从高位数到低位数遍历（进制越小位数越低），同时确定特定位数的进制数取值上下界，然后二分寻找是否匹配。


### 2.3 子过程中需要用到二分查找的问题

- [LC300](https://leetcode-cn.com/problems/longest-increasing-subsequence/) 可以重新定义状态以对动态规划进行优化，定义 `tail[i]` 表示长度为 `i + 1` 的所有上升子序列的结尾的最小值。之后每次寻找更新位置使用二分查找。附[详细解释](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/)。

- [LC354](https://leetcode-cn.com/problems/russian-doll-envelopes/) LC300 的升级版，将宽或者高排序后即可套用前面的模板，这里注意为了不让某一边相同的情况出现，排序时需要将另一边按照**降序**排列。

## 参考文献

- Python source code: [bisect](https://github.com/python/cpython/blob/3.8/Lib/bisect.py)

- [二分查找算法详解](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/) -- labuladong