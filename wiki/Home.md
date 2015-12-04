# 哈尔滨工业大学移动平台身份认证SDK(Python)

## 概述

本项目根据原有Java版SDK反编译代码编写。

由于平台签名函数使用Java编写致使个别字符串为Java风格。为保证接口统一性，全部沿用原变量、接口名称。

## 代码说明

本项目对外提供一个用户类和一个认证函数。

其中用户类`CloudUser`接收从平台获取的用户json，自动将其转换为Python对象，CloudUser拥有以下属性：

- `idsNo` : 用户统一身份账号
- `nickName` : 用户昵称
- `realName` : 用户真实姓名
- `avatar` : 用户头像
- `gender` : 用户性别
- `enterYear` : 入学年份
- `birthday` : 生日
- `region` :
- `dept` : 系
- `major` : 专业
- `qq` : QQ
- `sign` : 数字签名（用于验证）

在`CloudUtils`中提供用户验证函数check：

此函数接收两个参数返回用户是否通过验证的bool值。第一个参数为一个CloudUser的实例，第二个参数为学校的appSecret密钥。

具体的测试用例见`test.py`
