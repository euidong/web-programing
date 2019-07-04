import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import pymysql.cursors

# 게시물 업데이트 되는지 계속 polling
while (True) :
    # file에서 최근 값을 불러오기(db에서 불러오는 걸로 바꿔도 될 듯)
    f = open("khu_ce_file.txt", mode ="rt", encoding="utf-8")
    RECENT_POST_NUMBER = f.read()
    f.close()

    RESULT_POST_NUMBER = RECENT_POST_NUMBER
    
    # url로 html 문서 받아오기 
    with urllib.request.urlopen("http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2") as r :
        soup = BeautifulSoup(r, "html.parser")

        # <tr> 안에 게시물 데이터가 담기므로 그 안에서 데이터 추출
        count = -1
        for post in soup.body.table.find_all("tr") :
            if count != -1: # 첫번째 index 열 거르기
                if post.contents[1].get_text() > RECENT_POST_NUMBER :
                    # db(mysql)와 연결
                    connection = pymysql.connect(host = 'localhost', port = 3306, user='user1', passwd='1234', db = 'notice', charset='utf8')
                    
                    # 파일에 쓸 가장 최근 업로드된 데이터를 저장 
                    if count == 0 : 
                        RESULT_POST_NUMBER = post.contents[1].get_text()
                    # 데이터 미리보기
                    print(post.contents[1].get_text()) #번호
                    print(post.contents[3].get_text()) #게시물이름
                    print(post.contents[9].get_text()) #게시일
                    print("http://ce.khu.ac.kr/index.php", post.find("a")["href"]) #링크
                    # db에 데이터 저장
                    try :
                        with connection.cursor() as cursor :
                            # 게시물 삽입
                            sql = "INSERT INTO `khu_alarm_notice` (`id`, `name`, `date`, `url`) VALUES (%s,%s,%s,%s)"
                            cursor.execute(sql,(post.contents[1].get_text(), post.contents[3].get_text(), post.contents[9].get_text(), 'http://ce.khu.ac.kr/index.php' + post.find('a')['href']))
                            connection.commit()
                            
                            # 게시물 100개 이상이면 삭제
                            sql = "DELETE FROM `khu_alarm_notice` WHERE `id` = %s"
                            cursor.execute(sql, str(int(RESULT_POST_NUMBER) - 100))
                            connection.commit()
                    finally:
                        connection.close()
                
            count+= 1

    # 변경점이 없을 경우
    if RESULT_POST_NUMBER == RECENT_POST_NUMBER :
        print("NOT Chaged")
    
    
    f = open("khu_ce_file.txt", mode ="wt", encoding ="utf-8")
    f.write(RESULT_POST_NUMBER)
    f.close()


    # 10초마다 반복
    sleep(10)
