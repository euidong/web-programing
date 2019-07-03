# BeautifulSoup 설치
```
pip install requests beautifulsoup
```

# URL로 WEB SITE 가져오기
urllib를 이용한다.

```python
import urllib.request

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
  
```

# BeautifulSoup으로 web site 추출하기

### 1. soup안으로 html 문서 끌고 오기

```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
  soup = BeautifulSoup(r, "html.parser")
```

### 2. 특정 부분으로 한정하기

특정 태그 내용만 불러오고 싶다면, 태그 이름을 명시하여 사용할 수 있다.<br>
But, 중복된 종류가 있다면, 맨 첫번째로 나오는 대상만 가져온다.

```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
  soup = BeautifulSoup(r, "html.parser")
  print(soup.head.title)
  print(soup.body.table)
  print(soup.body.p)
```

### 3. find, find_all 사용하기

#### find
대체로 2번에서 쓰는 방법과 동일하다.<br>
위에서는 태그를통해서만 찾았다면, 여기서는 속성을 통해서도 찾을 수 있다.

사용법 : [find(name, attrs, recursive, string, **kwargs)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find)
```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
  soup = BeautifulSoup(r, "html.parser")
  print(soup.find(string = "664"))
  print(soup.find("td", class_="text_center"))
  print(soup.find(id="layor")
```
*find(string =" ") 할 때, 한국어는 사용할 수 없는 거 같음.

#### find_all
HTML 문서의 모든 일치하는 대상을 배열 형태로 저장합니다.<br>
find에 limit가 추가된 형태로 대상의 수를 제한할 수 있습니다.

사용법 : [find_all(name, attrs, recursive, string, limit, **kwargs)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all)

```python
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
  soup = BeautifulSoup(r, "html.parser")
  print(soup.find_all(string = "664"))
  print(soup.find_all("td", class_="text_center"))
  print(soup.find_all(id="layor")
```

### 4. 문서 내용 string으로 가져오기

#### text 내용 가져오기
get_text()를 통해 해당 문자를 string형태로 불러올 수 있다.
```python
soup.find("a").get_text()
soup.find("a").get_text(strip=True)            # 공백 제거
soup.find("a").get_text().replace("$","")      # 특수문자 제거
```

#### 속성값 가져오기
```python
soup.find("img")["src"]    # 이미지의 소스
soup.find("a")["href"]     # 링크의 url
```
