from functools import reduce
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from.models import zhilian
from mongoengine import *
from django.db.models import Count
from .db import *

import json
import operator


# 划分为八大行业
# navbar={'互联网':0,'金融':1,'房地产/建筑/工业':2,
#         '贸易/销售/物流':3,'教育/传媒/广告 ':4,
#         '服务业':5,'市场/销售':6,'人事/财务/行政':7}

# 每个行业的关键字参数
# jobKey={
#     0:['软件','互联网','系统集成','计算机','IT','硬件'],
#     1:['金融','投资','银行','证券','财产','理财','审计'],
#     2:['房地产','建筑','土木','工业','化工'],
#     3:['贸易','销售','物流','零售','外贸','仓库','仓储','质量'],
#     4:['教育','传媒','广告','教师','编导','老师','策划','制片','美术','公关'],
#     5:['服务','客服','售后','旅游'],
#     6:['市场','销售','SEO','活动','营销','农/林'],
#     7:['人事','财务','行政','人力','主管','出纳','会计'],
# }

def index(request):
    data=index_data()
    # 地图数据
    map_data=data[0]
    # 右侧上部柱状图数据
    ringt_top_data=data[1]
    # print(ringt_top_data)
    # 右侧下部数据
    right_bottom_data=data[2]



    return render(request, 'myapp/index.html',context={
        'map_data':map_data,
        'ringt_top_data':ringt_top_data,
        'right_bottom_data':right_bottom_data,
    })

@cache_page(24*3600)
def detail(request,page):
    '''
    详情页视图函数
    :param request:
    :return:
    '''

    # 筛选地图数据
    mapData=get_map_data(page)

    # 各城市职位排名
    rightTop=top5level(page)

    # 各城市职位数所占比重
    rightBottom=to5LevelCityPie(page)

    # 词云
    wordCloudData=wordCloud(page)

    # Top5职位柱状图
    top5JobNum=getTop5JobNum(page)

    # 工作年限与薪资
    salary_exp=exp_salary(page)

    # 学历与薪资
    salary_level=level_salary(page)


    return render(request,'myapp/detail_page.html',{
        'map_data':mapData,
        'right_top':rightTop,
        'right_bottom':rightBottom,
        'word_cloud_data':wordCloudData,
        'top5JobNum':top5JobNum,
        'salary_exp':salary_exp,
        'salary_level':salary_level
    })

def test(request):
    keys=list()
    with open('./myapp/static/myapp/keywords.json','r',encoding='utf-8') as f:
        keys=json.loads(f.read())
    sum = 0
    for key in keys[0]['Job_keywords']:
        result = zhilian.objects(jobType__icontains=key).count()
        sum += result

    job_data_all = zhilian.objects.values_list('city')
    data=job_data_all.count()

    return render(request,'myapp/test.html')

