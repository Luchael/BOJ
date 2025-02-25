# 27736번: 찬반투표 - <img src="https://static.solved.ac/tier_small/3.svg" style="height:20px" /> Bronze III

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/27736)


<p>중앙대학교에서 재학생을 대상으로 하는 어떤 찬반투표가 치러졌다. 모든 재학생은 각자 찬성이나 반대, 혹은 기권 중 하나로 투표에 응답하였다.</p>

<p>해당 투표에서 찬성이 반대보다 많으면 투표가 통과된다. 반대가 찬성보다 많거나, 반대와 찬성의 수가 동일하다면 투표는 통과되지 않는다. 단, 기권한 사람이 재학생의 절반 이상이라면 찬성과 반대의 수와 관계없이 항상 투표는 무효 처리된다.</p>

<p>재학생들의 투표 내역을 입력받아 찬반투표의 결과를 출력하는 프로그램을 구현하시오.</p>



## 입력


<p>첫 번째 줄에 중앙대학교 재학생의 수 $N$이 주어진다.</p>

<p>두 번째 줄에 $N$개의 투표 내역이 공백으로 구분되어 주어진다. 각각 찬성은 <span style="color:#e74c3c;"><code>1</code></span>, 반대는 <span style="color:#e74c3c;"><code>-1</code></span>, 기권은 <span style="color:#e74c3c;"><code>0</code></span>으로 주어진다.</p>



## 출력


<p>투표가 통과되었으면 <span style="color:#e74c3c;"><code>APPROVED</code></span>, 통과되지 않았으면 <span style="color:#e74c3c;"><code>REJECTED</code></span>, 무효 처리되었으면 <span style="color:#e74c3c;"><code>INVALID</code></span>를 출력한다.</p>



## 소스코드

[소스코드 보기](찬반투표.py)