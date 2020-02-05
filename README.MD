1需求分析
    查看用户对话历史记录
    登录
    退出
    对话 点对点
    发文件
    加好友
    显示所有好友信息
2.概要 使用udp套接字 使用pyqt5建view界面，，，，
发文件tcp 和 聊天udp 协议确定
3建表 表user id name pwd  addr             #name也设置为索引
    create table user(id int auto_increment primary key,
                      name varchar(20) not null,
                      pwd varchar(30) not null,
                      addr varchar(40) default null ,
                      port varchar(20) default null ,
                      index(name));
    用户对话记录表 chat_his id sender rever record times    rever是接受信息的人
    create table chat_his(id int primary key auto_increment,sender varchar(20) not null,rever varchar(20) not null,record text,moment datetime default now());
    friend id name frie
    create table friend(id int primary key auto_increment,name varchar(20),frie varchar(20));
insert into friend (name,frie) values ("uu","ll"),("uu","tt"),("uu","ss");
4技术点
通信协议 文件 F 文件 或者F
        聊天 C name other msg
        登录 L name pwd
        注册 R name pwd
历史记录存储  发的时候要存，收的也要存
5功能分析
界面
实现2个界面   注册和登录的用户信息发送给服务端    服务端把信息发给数据检验
服务端
登录  检查用户是否是否收到消息，
聊天  用户是否在线,如在线发送 接受反馈 成功存到本地  并存入对方的历史记录
                    不在线 发送信息保存在数据库
发送文件   把文件拖过来,直接显示其路径点击发送,直接发送过去