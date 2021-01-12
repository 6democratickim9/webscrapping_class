import requests


response = requests.get("https://blog.naver.com/vega2k")
print("응답코드 : ",res.status_code)

if res.status_code ==requests.codes.ok:
    print("정상")
else:
    print("문제- 에러코드 ",res.status_code)

res.