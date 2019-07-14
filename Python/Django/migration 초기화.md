# 초기화

  1. 먼저 초기화를 하기 위해서 해당 데이터를 db에서 먼저 table을 지워준다.
  2. migration 기록을 제거한다.
  2-1. migration 기록 보기 (python manage.py showmigrations)
  2-2. migration 기록 지운 거처럼 보이게하기 (python manage.py migrate --fake app이름 zero
  2-3. 실제 directory에서 해당 기록들 삭제하기 migration 폴더 안에 cache랑 해당 기록들 삭제
  2-4. python manage.py makemigration 실행
  2-5. 한 번도 migration안했던 것처럼 속여서 실행. (python manage.py migrate --fake-initial)
  3. 끝.
