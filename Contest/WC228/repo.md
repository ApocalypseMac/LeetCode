# lc weekly contest 228

17/17

0:19:44 + 2 errors = 0:29:44

T3 二分下界搞成 0 结果用作分母错了一发， T4 没加常数优化 T 了一发（

------

- 5676 easy

    统计两种修改方式的花费取最小即可，或者一次遍历奇偶的 0 和 1 数目。

- 5677 medium

    对于每段长度为 `k` 的相同字符子串，贡献 `k * (k + 1) // 2` 个同构子串。遍历统计即可。

- 5678 medium

    求最小化的最大值，可以考虑二分答案。对于给定的开销 `k`, 大小为 `n` 的袋子所需要的分割次数为 `(n - 1) // k`. 二分下界可取为 1, 上界可取为数组最大值。最终二分求符合要求的左边界即可。

- 5679 hard

    采用邻接矩阵存边，并记录每个点的度数。三重循环遍历即可。可以进行剪枝等操作以进行常数优化。

------