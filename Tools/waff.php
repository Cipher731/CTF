<?php
/**
 * Created by Cipher731
 */
error_reporting(0);
date_default_timezone_set('Asia/Shanghai');

define('LOG_FILE_PREFIX', '/tmp/Cipher_Log/');
if (!file_exists('/tmp/Cipher_Log')) {
    mkdir('/tmp/Cipher_Log');
}

if (!function_exists('getallheaders')) {
    function getallheaders()
    {
        $headers = array();
        foreach ($_SERVER as $name => $value) {
            if (substr($name, 0, 5) == 'HTTP_')
                $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
        }
        return $headers;
    }
}

function logData($data)
{
    $filename = date('H_');
    $filename .= floor(time() % 3600 / 300) * 5;
    $filepath = LOG_FILE_PREFIX . "$filename" . '.log';

    if (!file_exists($filepath)) {
        $fp = fopen($filepath, 'w');
        fwrite($fp, '[');
    } else {
        $fp = fopen($filepath, 'r+');
        $stat = fstat($fp);
        fseek($fp, -1, SEEK_END);
    }
    fwrite($fp, json_encode($data) . ",]");
    fclose($fp);
}

function filter(&$data)
{
    $patterns = "select|insert|update|delete|and|or|\'|\/\*|\*|\.\.\/|\.\/|union|[^c]into|load_file|outfile|dumpfile|sub|hex";
    $patterns .= "|file_put_contents|fwrite|curl|system|eval|assert";
    $patterns .= "|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
    $patterns .= "|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
    $patterns = explode("|", $patterns);
    foreach ($data as $d_value) {
        foreach ($d_value as $key => $value) {
            foreach ($patterns as $pattern) {
                if (stristr($value, $pattern) !== false) {
                    $data['detected'] = true;
                    $data['detected_pattern'] = $pattern;
                    $data['detected_string'] = $value;
                    return;
                }
            }
        }
    }
}

$data = array(
    'time' => date('H:i:s'),
    'from' => $_SERVER['REMOTE_ADDR'],
    'filename' => $_SERVER['SCRIPT_FILENAME'],
    'method' => $_SERVER['REQUEST_METHOD'],
    'url' => "$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]",
    'header' => getallheaders(),
    'cookie' => $_COOKIE,
    'get' => $_GET,
    'post' => $_POST,
    'entity_body' => file_get_contents('php://input'),
    'files' => $_FILES,
    'detected' => false
);

filter($data);
logData($data);

$kill = False;
if ($kill && $data['detected']) {
    die('Oh, no');
}

?>