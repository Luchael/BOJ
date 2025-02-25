# 21184번: New Maths - <img src="https://static.solved.ac/tier_small/16.svg" style="height:20px" /> Platinum V

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/21184)


<p>"Drat!" cursed Charles. &nbsp;"This stupid carry bar is not working in my Engine! &nbsp;I just tried to calculate the square of a number, but it's wrong; all of the carries are lost."</p>

<p>"Hmm," mused Ada, "arithmetic without carries! &nbsp;I wonder if I can figure out what your original input was, based on the result I see on the Engine."</p>

<p><em>Carryless addition</em>, denoted by $\oplus$, is the same as normal addition, except any carries are ignored (in base $10$). Thus, $37 \oplus 48$ is $75$, not $85$.</p>

<p><em>Carryless multiplication</em>, denoted by $\otimes$, is performed using the schoolboy algorithm for multiplication, column by column, but the intermediate additions are calculated using <em>carryless addition</em>. More formally, Let $a_m a_{m-1} \ldots a_1 a_0$ be the digits of $a$, where $a_0$ is its least significant digit. Similarly define $b_n b_{n-1} \ldots b_1 b_0$ be the digits of $b$. The digits of $c = a \otimes b$ are given by the following equation: \[ c_k = \left( a_0 b_k \oplus a_1 b_{k-1} \oplus \cdots \oplus a_{k-1} b_1 \oplus a_k b_0 \right) \bmod{10}, \] where any $a_i$ or $b_j$ is considered zero if $i &gt; m$ or $j &gt; n$. For example, $9 \otimes 1\,234$ is $9\,876$, $90 \otimes 1\,234$ is $98\,760$, and $99 \otimes 1\,234$ is $97\,536$.</p>

<p>Given $N$, find the smallest positive integer $a$ such that $a \otimes a = N$.</p>



## 입력


<p>The input consists of a single line with a positive integer $N$, with at most $25$ digits and no leading zeros.</p>



## 출력


<p>Print, on a single line, the least positive number $a$ such that $a \otimes a = N$. If there is no such $a$, print '<code>-1</code>' instead.</p>



## 소스코드

[소스코드 보기](New%20Maths.py)