# EC2

하나의 컴퓨터를 제공하는 서비스이다.

CPU, RAM과 같은 장치를 직접 커스터마이징 할 수도 있고 추천대로 사용할 수 있다.

대게는 운영체제까지 직접 적용해주며 이를 이용해서 프로그래밍을 할 수 있다.


### 시작하기

EC2 장치는 SSH를 통해 원격으로 제어한다. 

요금이 나가는 것을 방지하기 위하여 프리티어를 이용한다.

이를 위해 보안그룹에 SSH를 위한 PORT를 OPEN한다.

여기서 이용하고자하는 방식에 따라 PORT를 선택하고 OPEN한다.(WEB이라면 HTTP, HTTPS 등)

이후 bash를 이용하던 putty를 이용하던 다양한 방식으로 원격으로 연결한다.
