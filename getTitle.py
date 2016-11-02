#!/user/sbin/python
# -*- coding: UTF-8 -*-

import urllib2
import cookielib
import MySQLdb
from bs4 import BeautifulSoup


conn = MySQLdb.connect(host='172.16.203.129',user='root',passwd='root',port=3306,db='zlh')
cur =  conn.cursor()


class GetTitles():
	"""docstring for ClassName"""

	def __init__(self,arg):
		self.arg = arg
		print  'hello: %s' % self.arg
	
	# 获取一个页面的title	
	def getTitle(self,id):
		#url='https://www.v2ex.com/t/'+id
		url="https://www.v2ex.com/t/314469"
	 	opener=urllib2.build_opener()
		opener.addheaders.append(('Cookie','V2EX_TAB="2|1:0|10:1476279637|8:V2EX_TAB|8:dGVjaA==|dabc53b73e7dfc5e0eeba218dcdf6c382c3ae282982212680c9a398ddc48b4eb"; PB3_SESSION="2|1:0|10:1476869198|11:PB3_SESSION|36:djJleDoxNC4xNy4yMi40ODo0Mzk0ODcwOQ==|6be4cd922068b59e70d548a1451e769640ff25199606c637ea16836c771ec44b"; V2EX_REFERRER="2|1:0|10:1477122167|13:V2EX_REFERRER|8:emhhb3Ni|015a836cdcd8e07c8556e6ab9f5a415d52aa6c5db4d13ad570c48a38b6c0c710"; V2EX_LANG=zhcn; _ga=GA1.2.396097307.1465800688'))
		html=opener.open(url).read()
		soup=BeautifulSoup(html,"html.parser")
		title=soup.title.string
		print 'title=    '+title
		#print 'html=  '+html
		return [url,id,title]

	#  创建数据库表
	#
	#def createTable(self,cur):
	#	cur.execute('create table title_info(url varchar(50) ,title_id VARCHAR(30) prmary key,title VARCHAR(80))')


'''
#将title插入数据库
# insertTitle( a = 1, b = 2, c =3)
# kwargs => {'a' :1 , 'b': 2, 'c' : 3}
def  insertTitle(**kwargs):

	url = kwargs.get('url', None)
	title_id = kwargs.get('title_id', None)
	title = kwargs.get('title', None)

	sql = "insert into title_info(`url`, " \
		  "`title_id`, `title`) values('%s', '%s', '%s')" % (url, title_id, title)
	cur.execute('insert into title_info values(%s,%s,%s)',title_para)
'''


def  insertTitle(url, title_id, title):


	#TODO CHECK URL, TITLE_ID, TITLE

	sql = "insert into title_info(`url`, " \
		  "`title_id`, `title`) values('%s', '%s', '%s')" % (url, title_id, title)
	cur.execute(sql)
	conn.commit() #insert 需要commit , select 不需要


if __name__ == '__main__':
	get_title=GetTitles('ahaha')
	title_para=get_title.getTitle('314225')

	#title_req_test.py.createTable(cur)
	insertTitle(title_para)



	