from django.conf.urls import url
from App.views import *
urlpatterns = [
    # 首页路由地址
    url(r'^$',home.index),
    url(r'^home/$',home.index,name='home'),
    # 闪送超时的样式
    # 无参
    url(r'^market/$',market.market,name='market'),
    # 构造带参数的
    url(r'^market/(\d+)/(\d+)/(\d+)/$',market.market,name='market2'),
    # 购物车
    url(r'^car/$',car.car,name='car'),
    # 购物数量+ - 的操作
    url(r'^doCar/$',car.doCar,name='doCar'),
    # 当选中下单 进行查看是否有选中商品时的操作
    url(r'^findChoose/$',car.findChoose,name='findChoose'),
    # 我的路由地址
    url(r'^mine/$',mine.mine,name='mine'),
    # 注册
    url(r'^register/$',mine.Register,name='register'),
    # 登录
    url(r'^login/$',mine.Login,name='login'),
    # 退出登录
    url(r'^logout/$',mine.Logout,name='logout'),
    # 订单显示页面
    url(r'^order/$',order.order,name='order'),
    # 处理下订单
    url(r'^doOrder/$',order.doOrder,name='doOrder'),
]
