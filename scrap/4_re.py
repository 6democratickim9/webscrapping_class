import re
p = re.compile("ca.e") 
#. : 하나의 문자를 뜻한다.>>ca?e--care,cafe
# ^: 문자열의 시작--> ^de: desk,destination
# $: 문자열의 끝 --> se$: case,base


m= p.match("case")
print(m.group())