#coding = utf-8

import pymongo

#查询所有用户
def queryAll():
	db = pymongo.MongoClient().game	
	users = []
	l = list(db.user.find())
	for user in l:
		u = {}
		u['name'] = user['name']
		u['age'] = user['age']
		print(u)
		users.append(u)
	return users