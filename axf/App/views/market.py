from django.shortcuts import render,HttpResponse
from App.models import FoodTypes,Goods

# 闪送超市的样式
# categoryid是商品表里的类别id  在foodtypes表里叫typeid
# childcid商品表中 子类别的id
# orderby 按照某个值进行排序
def market(req,categoryid=104749,childcid=0,orderby=0):
    footTypeData = FoodTypes.objects.all()
    # 查询右侧商品数据
    # 判断是否查询当前类别的所有商品还是查询当前类别子类的商品
    goodsData = Goods.objects.filter(categoryid=categoryid)
    if int(childcid):
        goodsData = goodsData.filter(childcid=childcid)

    # 对商品根据传递进来的orderby参数值进行排序
    orderby = int(orderby)
    # 销量
    if orderby == 1:
        goodsData = goodsData.order_by('-productnum')
    #  价格最低
    elif orderby == 2:
        goodsData = goodsData.order_by('price')
    #     价格最高
    elif orderby == 3:
        goodsData = goodsData.order_by('-price')

    # 通过左侧类别的查询 查询出当前类别的子类 在goods表中叫childcid也就是foodtype表中的childtypenames的数据
    childCidData = footTypeData.filter(typeid=categoryid).first().childtypenames
    # print(childCidData)
    # 迭代获取 其中的名字和id的二维列表
    # 按照# 号进行拆分每一对类别名称和id
    childCidDataList = childCidData.split('#')
    childCidList = []
    # 拿到每一对的类别名称和id
    for typeStr in childCidDataList:
        # 将每一对类别名称和id再次进行拆分成列表
        childCidList.append(typeStr.split(':'))
    # print(childCidList)
    return render(req,'market/market.html',{'footTypeData':footTypeData,'goodsData':goodsData,'childCidList':childCidList,'categoryid':categoryid,'childcid':childcid})

