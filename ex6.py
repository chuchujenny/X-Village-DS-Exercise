#針對ptt0726八卦板爬蟲作推文總數由大道小排序
#助教提供參考資料:https://docs.python.org/3/howto/sorting.html#key-functions
import json
with open('ptt_0726_m.json','r', encoding = 'utf8') as f: #此檔案必須與要讀入的檔案路徑相同(如何在路徑不同下open?)
    ptt=json.load(f)

#推文總數={}時，使期增加一相"all":0，以便最後排序
for i in range(len(ptt)):
    if ptt[i]["h_推文總數"]=={}:
        b=ptt[i]["h_推文總數"]
        b["all"]=0
        ptt[i]["h_推文總數"]=b


#以下5行純粹想看我最後結果有無成功，因此把總數抽出來，逆向排序前十個
c=[]
for i in range(len(ptt)):
    c.append(ptt[i]["h_推文總數"]["all"])
cc=sorted(c,reverse=True)
print(cc[0:10]) #[1300, 1233, 1217, 1173, 1113, 1071, 1024, 1024, 940, 937]

#依條件排序
'''
參考資料: 
http://yehnan.blogspot.com/2015/06/pythonoperatoritemgetter.html
https://www.polarxiong.com/archives/Python-%E4%BD%BF%E7%94%A8lambda%E5%BA%94%E5%AF%B9%E5%90%84%E7%A7%8D%E5%A4%8D%E6%9D%82%E6%83%85%E5%86%B5%E7%9A%84%E6%8E%92%E5%BA%8F-%E5%8C%85%E6%8B%AClist%E5%B5%8C%E5%A5%97dict.html
'''
b=sorted(ptt,key=lambda x:x["h_推文總數"]["all"],reverse=True) #錯誤: b=sorted(ptt,key=lambda x:ptt[i]["h_推文總數"]["all"],reverse=True)







#reverse其他方式
'''
例如:
a=[3,6,4,5,2,6,1,2,9,6,3]
a.sort()
a=a[::-1]
'''

#append也能append不是數字的元素
'''
例如:
a=[1,2,3]
a.append({'q':2})
print(a) #[1, 2, 3, {'q': 2}]
'''

#del、remove、pop的用法及區别
#https://blog.csdn.net/deqiangxiaozi/article/details/75808863
