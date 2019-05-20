from django.shortcuts import render,HttpResponse
from App.models import  Wheel,Nav,MustBuy,Shop,MainShow
# Create your views here.
# 爱鲜蜂首页
def index(req):
    # 查询轮播的数据
    wheelList = Wheel.objects.all()
    # print(wheelList)
    # nav 导航数据
    navList = Nav.objects.all()
    # mustBuy 必买数据
    mustBuyList = MustBuy.objects.all()
    # 获取便利店的数据
    shopList = Shop.objects.all()
    # 取出第一个商品的数据
    shop1 = shopList[0]
    # 取出第二行的数据
    shop2 = shopList[1:3]
    # 取出第三行数据
    shop3 = shopList[3:7]
    # 最后俩行的数据
    shop4 = shopList[7:]
    # 主要卖品的数据
    mainList = MainShow.objects.all()
    return render(req,'home/home.html',{'wheelList':wheelList,'navList':navList,'mustBuyList':mustBuyList,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainList':mainList})
