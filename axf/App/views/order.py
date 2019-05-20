from django.shortcuts import render,HttpResponse,redirect,reverse
from App.models import Order,Car,Address,OrderDetail


# 展示订单详情页
def order(req):
    # 查询默认选中的地址数据
    address = Address.objects.filter(state=True).first()
    # print(address)
    # 查询购物车选中的商品
    carObj = Car.objects.filter(isChoose=True)
    # 计算总价
    money = 0
    for car in carObj:
        money += car.num * eval(car.goods.price)
    return render(req,'order/order.html',{'address':address,'carObj':carObj,'money':'%.2f'%money})

import time
# 处理的操作
def doOrder(req):
    addressId = int(req.POST.get('addressId'))
    money = req.POST.get('money')
    message = req.POST.get('message')
    # 将订单数据存储到表单中
    addressObj = Address.objects.get(pk=addressId)
    orderObj = Order()
    orderObj.user = req.user
    orderObj.address = addressObj
    orderObj.money = money
    orderObj.message = message
    orderObj.orderId = time.strftime('%y%m%d')
    orderObj.save()
    # 先获取到购物车选中的商品
    carObj = Car.objects.filter(isChoose = True)
    # 迭代获取到每一个对象
    for car in carObj:
        # 生成订单详情
        OrderDetail(order=orderObj,goodsImg=car.goods.productimg,goodsName=car.goods.productname,price=car.goods.price,num=car.num,total=car.num*eval(car.goods.price)).save()
    return redirect(reverse('App:car'))