# 17991번: Carryless Square Root - <img src="https://static.solved.ac/tier_small/16.svg" style="height:20px" /> Platinum V

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/17991)


<p><em>Carryless</em> addition is the same as normal addition, except any carries are ignored (in base 10). Thus, 37 + 48 is 75, not 85.</p>

<p><em>Carryless</em> multiplication is performed using the schoolbook algorithm for multiplication, column by column, but the intermediate sums are calculated using <em>carryless</em> addition. Thus:</p>

<p style="text-align: center;">9 ∙ 1234 = 9000 + (900 + 900) + (90 + 90 + 90) + (9 + 9 + 9 + 9) = 9000 + 800 + 70 + 6 = 9876</p>

<p style="text-align: center;">90 ∙ 1234 = 98760</p>

<p style="text-align: center;">99 ∙ 1234 = 98760 + 9876 = 97536</p>

<p>Formally, define <em>c<sub>k</sub></em>&nbsp;to be the <em>k</em><sup>th</sup>&nbsp;digit of the value <em>c</em>. If <em>c</em>&nbsp;= <em>a</em>&nbsp;· <em>b</em> then</p>

<p>\[c_k = \left[ \sum_{i+j=k}{a_i \cdot b_j} \right] \mod 10\]</p>

<p>Given an integer <em>n</em>, calculate the smallest positive integer <em>a</em> such that <em>a</em> ∙ <em>a</em> = <em>n</em>&nbsp;in carryless multiplication.</p>



## 입력


<p>The input consists of a single line with an integer <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>25</sup>).</p>



## 출력


<p>Output the smallest positive integer that is a <em>carryless</em> square root of the input number, or −1 if no such number exists.</p>



## 소스코드

[소스코드 보기](Carryless%20Square%20Root.py)