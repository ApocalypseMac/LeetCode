#lc weekly contest 202

12/18

1:04:02

最后一题在比赛结束后几分钟做完了

想T3T4花了好久，明明套路都是之前做过的，甚至有一个套路是昨天学会的

------

- 5185 easy
    模拟，为了避免重复计算可以用三个变量循环使用。

- 5488 middle
    数学题，等差数列求和，分奇偶讨论，验证一下小的数字对不对即可。

- 5489 middle
    咋一看可以贪心，但是贪心的要求是：判断对于一个**给定**的数字是否满足条件，看一下数据范围，平方算法就别想了，正好可以求出上下界，二分即可。

- 5490 hard
    之前看数据规模想找规律失败了，最后老老实实dp table超时了。其实这里并不需要计算所有小于 n 的值。
    
    这里有三个操作，减一，被2整除就除2，被3整除就除3，第一个操作可以和后两个操作合并，亦即减去余数然后整除。那么选择枝就很清晰了，我们可以通过记忆化搜索来向下递归寻找答案。

    主方程为： $T(n) = T(n//2) + T(n//3) + O(1)$

    最后的复杂度约为 $O(n^0.787885)$

------

没啥想说的，做过还是要总结，不然还是会傻逼
