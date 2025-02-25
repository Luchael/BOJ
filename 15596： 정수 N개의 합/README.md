# 15552번: 빠른 A+B - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/15596)

<p>정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.</p>

<p>작성해야 하는 함수는 다음과 같다.</p>

<ul>
<li>C, C11, C (Clang), C11 (Clang): <code>long long sum(int *a, int n);</code>

<ul>
<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
<li><code>n</code>: 합을 구해야 하는 정수의 개수</li>
<li>리턴값:&nbsp;a에 포함되어 있는 정수 <code>n</code>개의 합</li>
</ul>
</li>
<li>C++, C++11, C++14, C++17, C++ (Clang), C++11 (Clang), C++14 (Clang), C++17 (Clang): <code>long long sum(std::vector&lt;int&gt; &amp;a);</code>
<ul>
<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
<li>리턴값:&nbsp;<code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
</ul>
</li>
<li>Python 2, Python 3, PyPy, PyPy3: <code>def solve(a: list) -&gt; int</code>
<ul>
<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
<li>리턴값:&nbsp;<code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합 (정수)</li>
</ul>
</li>
<li>Java: <code>long sum(int[] a);</code> (클래스 이름: Test)
<ul>
<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
<li>리턴값:&nbsp;<code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
</ul>
</li>
<li>Go:&nbsp;<code>sum(a []int) int</code>
<ul>
<li><code>a</code>: 합을 구해야 하는 정수 <code>n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
<li>리턴값:&nbsp;<code>a</code>에 포함되어 있는 정수 <code>n</code>개의 합</li>
</ul>
</li>
</ul>

## 소스코드

[소스코드 보기](정수%20N개의%20합.c)
