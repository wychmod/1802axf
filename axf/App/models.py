from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#创建用户模型
class User(AbstractUser):
    icon = models.CharField(max_length=70,default='default.jpg')
    class Meta:
        db_table = 'user'

# 公共的抽象类 子类继承
class Common(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True

# 轮播图模型
class Wheel(Common):
    class Meta:
        db_table = 'axf_wheel'


# 导航的模型
class Nav(Common):
    class Meta:
        db_table = 'axf_nav'


# 必买
class MustBuy(Common):
    class Meta:
        db_table = 'axf_mustbuy'


# 首页便利店
class Shop(Common):
    class Meta:
        db_table = 'axf_shop'


# 主要卖品
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=10)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=100)
    productid1 = models.CharField(max_length=100)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    marketprice1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=100)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    marketprice2 = models.CharField(max_length=100)
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=100)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    marketprice3 = models.CharField(max_length=100)
    class Meta:
        db_table = 'axf_mainshow'

# 创建商品类别表
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=100)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=120)
    typesort = models.CharField(max_length=100)
    class Meta:
        db_table = 'axf_foodtypes'


# 创建商品表
class Goods(models.Model):
    productid = models.CharField(max_length=100)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=100)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    marketprice = models.CharField(max_length=100)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=100)
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = 'axf_goods'


# 创建购物车
class Car(models.Model):
    goods = models.ForeignKey(Goods) # 创建一对多 获取该商品在商品表里的所有数据
    user = models.ForeignKey(User) #创建一对多 通过唯一的userid 查询出当前用户的所有购物车中的商品
    num = models.IntegerField(default=1) # 购物车中该商品的数量
    isChoose = models.BooleanField(default=True) # 该商品在购物车中是否被用户选中
    class Meta:
        db_table = 'axf_car'


# 创建地址表
class Address(models.Model):
    user = models.ForeignKey(User) # 创建地址和用户模型一对多关系 当下订单时 查询该用户下有哪些地址
    address = models.CharField(max_length=100) # 存储地址数据的字段
    phone = models.CharField(max_length=11) # 存储地址联系人的手机号码
    name = models.CharField(max_length=10) # 收货人名称
    state = models.BooleanField(default=False) # 当前地址是否为默认选中地址
    class Meta:
        db_table = 'axf_address'


# 订单表
class Order(models.Model):
    user = models.ForeignKey(User) # 在查看订单的时候 查询该用户下用哪些订单
    address = models.ForeignKey(Address) # 在订单中 还有收货人的信息
    money = models.DecimalField(max_digits=8,decimal_places=2) # 下订单时 该商品的价格
    message = models.CharField(max_length=100) # 买家给卖家的留言
    createTime = models.DateTimeField(auto_now_add=True) # 订单创建时间
    orderId = models.CharField(max_length=20) # 订单生成的字符串id
    status = models.IntegerField(default=0) # 订单状态 0 下单未付款 1 未发货 2 以收货
    class Meta:
        db_table = 'axf_order'
# 订单详情表
class OrderDetail(models.Model):
    order = models.ForeignKey(Order) # 通过订单 查询出该订单下有哪些商品
    goodsImg = models.CharField(max_length=100) # 商品图片
    goodsName = models.CharField(max_length=100) # 商品名称
    price = models.DecimalField(max_digits=8,decimal_places=2) # 商品单价
    num = models.IntegerField(default=1) # 商品数量
    total = models.DecimalField(max_digits=8,decimal_places=2) # 商品总价
    class Meta:
        db_table = 'axf_orderdetail'