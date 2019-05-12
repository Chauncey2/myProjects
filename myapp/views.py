from django.shortcuts import render
from.models import zhilian
import json

navbar={'互联网IT':0,'金融':1,'房地产/建筑':2,'贸易/销售/物流':3,'教育/传媒/广告 ':4,'服务业':5,'市场/销售':6,'人事/财务/行政':7}


def detail(request):
    '''
    详情页视图函数
    :param request:
    :return:
    '''
    return render(request,'myapp/detail_page.html')


def index(request):
    '''
    首页视图函数
    :param request:
    :return:
    '''
    keys = list()
    with open('./myapp/static/myapp/keywords.json', 'r', encoding='utf-8') as f:
        keys = json.loads(f.read())

    jobType = list()
    for item in range(len(keys)):
        jobType.append(keys[item]['Industy_name'])

    sum = 0
    data_list=[]
    for i in range(len(keys)):
        for key in keys[0]['Job_keywords']:
            result = zhilian.objects(jobType__icontains=key).count()
            sum += result
        val={'value':sum,'name':jobType[i]}
        data_list.append(val)

    return render(request, 'myapp/index.html',context={
        'jobType':json.dumps(jobType),
        'val_list':json.dumps(data_list)
    })


def test(request):
    keys=list()
    with open('./myapp/static/myapp/keywords.json','r',encoding='utf-8') as f:
        keys=json.loads(f.read())
    sum = 0
    for key in keys[0]['Job_keywords']:
        result = zhilian.objects(jobType__icontains=key).count()
        sum += result
    print(sum)
    print(keys[0]['Job_keywords'])
    return render(request,'myapp/test.html')

