from django.shortcuts import render
from App.models import Car,Goods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse # 导入响应json的方法

# 购物车
@login_required(login_url='/login/')
def car(req):
    # 查询当前用户下的购物车的所有数据
    carData = req.user.car_set.all()
    # 计算购物车中商品的总价格
    money = 0
    if carData.exists():
        for obj in carData:
            if obj.isChoose:
                money += obj.num*eval(obj.goods.price)
    return render(req,'car/car.html',{'carData':carData,'money':'%.2f'%money})


# 处理购物车数量的+ -
# goodsId 为商品自增Id
# state 为当前状态
# 0 商品数量减1
# 1 商品数量加1
def doCar(req):
    # 判断当前这个用户是否为登录状态
    if not req.user.is_authenticated:
        return JsonResponse({'code':500})
    goodsId = req.GET.get('goodsId')
    state = int(req.GET.get('state'))
    # 获取当前用户对象
    user = req.user
    # 查询出该商品的对象
    goodsObj = Goods.objects.filter(id=goodsId).first()
    # 获取出当前用户在购物车中的商品
    carObj = user.car_set.filter(goods=goodsObj).first()
    # print(carObj)
    # 显示商品数量的变量
    totalNum = 0
    # 对购物中选中与未选中的一个值的初始化
    Bool = True
    # 购物车商品总钱数
    money = 0
    # 商品 数量-1
    # 如果购物车中没有该商品 则不做任何处理 如果商品存在 在原有基础减1
    if state == 0:
        # 判断该商品是否存在于购物车中 存在则-1 否则不做任何处理
        if carObj:
            totalNum = carObj.num - 1
            if totalNum > 0:
                carObj.num = totalNum
                carObj.save()
            else:
                # 如果该商品数量=0 则将该商品删除
                user.car_set.filter(goods=goodsObj).delete()


    # 购物车商品数量+1
    """
    商品如果不在购物车中 则将该商品添加到购物车中
    如果该商品在购物车中 则将该商品的数量+1 并且与库存量进行判断
    """
    if state == 1:
        # 判断购物车是否有该商品
        if carObj:
            # 获取该商品的库存量
            storenums = int(goodsObj.storenums)
            # 将原有购物车中该商品的数量+1
            totalNum = carObj.num+1
            # 和该商品的库存量进行对比 购物车中的商品 不能超出库存量
            if totalNum >= storenums:
                totalNum = storenums
            carObj.num = totalNum
            carObj.save()
        else:
            # 将该商品添加到购物车中
            Car(goods=goodsObj,user=user).save()
            totalNum = 1

    #
    mycarObj = user.car_set.filter(goods=goodsObj)
    if mycarObj.exists():
        Bool = mycarObj.first().isChoose
    # 如果state为2 则为选中与取消选中的操作
    if state == 2:
        Bool = carObj.isChoose
        carObj.isChoose = not Bool
        carObj.save()
        Bool = not Bool
        totalNum = carObj.num


    # 通过 选中与取消选中 商品数量+1与-1 都对当前购物车中商品的总价格产生变化
    # 获取当前购物车下全部选中的商品
    carChoose = user.car_set.filter(isChoose=True)
    # 先判断是否有选中商品 如果没有 就没有必要在进行商品价格计算的处理
    if carChoose.exists():
        for obj in carChoose:
            money += obj.num*eval(obj.goods.price)
    return JsonResponse({'code':200,'totalNum':totalNum,'money':'%.2f'%money,'Bool':Bool})


# 判断是否存在选中商品进行下单
def findChoose(req):
    # 查询当前下单时 是否有选中的商品
    isChoose = req.user.car_set.filter(isChoose=True).exists()
    return JsonResponse({'isChoose':isChoose})