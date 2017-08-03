#导入爬虫基本模块urllib
import urllib2
file = urllib2.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readline()
print(data)
print(dataline)

#写入本地html
fhandle = open("文件url","wb")
fhandle.write(data)
fhandle.close()