#�����������ģ��urllib
import urllib2
file = urllib2.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readline()
print(data)
print(dataline)

#д�뱾��html
fhandle = open("�ļ�url","wb")
fhandle.write(data)
fhandle.close()