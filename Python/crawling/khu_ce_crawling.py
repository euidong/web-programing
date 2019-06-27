import urllib.request
from bs4 import BeautifulSoup
from time import sleep

while (True) :
    f = open("test.txt", mode ="rt", encoding="utf-8")
    RECENT_POST_NUMBER = f.read()
    f.close()

    RESULT_POST_NUMBER = RECENT_POST_NUMBER
    with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
        soup = BeautifulSoup(r, "html.parser")

        count = -1
        for post in soup.body.table.find_all("tr") :
            
            if count != -1:
                if post.contents[1].get_text() >= RECENT_POST_NUMBER :
                    if count == 0 : RESULT_POST_NUMBER = post.contents[1].get_text()
                    print(post.contents[1].get_text()) #번호
                    print(post.contents[3].get_text()) #게시물이름
                    print(post.contents[9].get_text()) #게시일
                    print("http://ce.khu.ac.kr/index.php", post.find("a")["href"]) #링크
            count+= 1

    f = open("test.txt", mode ="wt", encoding ="utf-8")
    f.write(RESULT_POST_NUMBER)
    f.close()
    sleep(10)
