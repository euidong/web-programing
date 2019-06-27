# mysql과 django 준비하기


# 연동하기 위한 mysqlclient, sqlparse install
1) anaconda 환경을 사용하는 경우
```
conda install mysqlclient
conda install sqlparse
```
2) virtual environment
```
pip install mysqlclient
pip install sqlparse
```

# settings.py 설정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'khu_ce_notice', # DB명
        'USER': 'root', # 데이터베이스 계정
        'PASSWORD': '3213210a', # 계정 비밀번호
        'HOST': 'localhost', # 데이테베이스 주소(IP)
        'PORT': '3306', # 데이터베이스 포트(보통은 3306)
    }
}
```
