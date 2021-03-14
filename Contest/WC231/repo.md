# lc weekly contest 231

20/20

1:23:53 + 3 errors = 1:38:53

T4 一开始写了个假的贪心 wa 了两发，然后想了半天才发现 dp 可以优化转移。。。

------

- 5697 easy

    顺序统计连续 1 的段数即可。

- 5698 medium

    计算数组和与目标的差的绝对值，然后计算最少数目即可。

- 5699 medium

    首先用 dijkstra 预处理终点到所有点的距离。然后就变成了 DAG 上的 dp 问题。

- 5700 hard

    首先可以证明最终数组的循环节一定为 `k`, 因此只需要考虑单个循环节的变化方式，并将数组按照模 `k` 的余数分组并统计各组的数字频率。然后发现数组元素上界为 `2^10`, 因此可以定义 `dp[i][j]` 为前 `i` 个数异或值为 `j` 所需要保留（改变类似）的数字个数。

    如果暴力转移，复杂度会达到 $O(maxn^2*n)$, 显然超时，因此需要优化。对于每一种情况，转移有两种方式。一种是将对应的数全部改为另一个数，这样就是 `max(dp[i-1])`; 另一种是考虑利用本组已经出现的数字，亦即 `dp[i-1][j^key] + val`. 组合即可。最终的时间复杂度是 $O(maxn*n)$.

------