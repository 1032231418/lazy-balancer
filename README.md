# Lazy-Balancer


项目起源于好哥们（Win平台）需要一个 7 层负载均衡器，无奈商业负载均衡器成本高昂，操作复杂。又没有特别喜欢（好看，好用）的开源产品，作为一名大 Ops 怎么能没有办法？正好最近在看 Django 框架，尝试自己给 Nginx 画皮，项目诞生！非专业开发，代码凑合看吧。
> 项目基于 [Django](https://www.djangoproject.com/) + [AdminLTE](https://www.almsaeedstudio.com/) 构建，在 Ubuntu 14.04 上测试通过；因为增加了 iptables 自动控制，所以暂时不支持 docker 方式部署

## 运行
* 克隆代码
```
mkdir -p /app  
git clone https://github.com/v55448330/lazy-balancer.git /app/nginx_balancer  
```
* 安装 nginx
```
apt-get install nginx  
update-rc.d nginx disable  
service nginx stop  
echo "daemon off;" >> /etc/nginx/nginx.conf  
```
* 安装 supervisor
```
apt-get install supervisor  
update-rc.d supervisor enable  
```
* 配置 supervisor
```
cp -rf service/* /etc/supervisor/
```
* 安装依赖
```
pip install -r requirements.txt  
```
* 初始化数据库
```
python manage.py makemigrations  
python manage.py migrate  
```
* 启动服务
```
service supervisor start  
```
* 登录系统（默认管理员：admin/1234.com）
```
http://[IP]:8000/  
```

## 功能
* Nginx 可视化配置
* Nginx 负载均衡（反向代理）配置
* Nginx 证书支持
* 系统状态监测
* 自动维护防火墙规则（白名单）

## 演示
![image](readme_img/1.jpg)
![image](readme_img/2.jpg)
![image](readme_img/3.jpg)
![image](readme_img/4.jpg)
![image](readme_img/5.jpg)
![image](readme_img/6.jpg)
