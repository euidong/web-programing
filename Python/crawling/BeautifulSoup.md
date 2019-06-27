# BeautifulSoup 설치
```
pip install requests beautifulsoup
```

# URL로 WEB SITE 가져오기
urllib를 이용한다.

```python
import urllib.request

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as html :
  
```

# BeautifulSoup으로 web site 추출하기

### 1. soup안으로 html 문서 끌고 오기

```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as html :
  soup = BeautifulSoup(r, "html.parser")
```

### 2. 특정 부분으로 한정하기

특정 태그 내용만 불러오고 싶다면, 태그 이름을 명시하여 사용할 수 있다.<br>
But, 중복된 종류가 있다면, 맨 첫번째로 나오는 대상만 가져온다.

```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as html :
  soup = BeautifulSoup(r, "html.parser")
  print(soup.head.title)
  print(soup.body.table)
  print(soup.body.p)
```

### 3. find, find_all 사용하기

#### find
대체로 2번에서 쓰는 방법과 동일하다.<br>
위에서는 태그를통해서만 찾았다면, 여기서는 속성을 통해서도 찾을 수 있다.
```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as html :
  soup = BeautifulSoup(r, "html.parser")
  print(soup.find("title", string = "경희대학교")
```
