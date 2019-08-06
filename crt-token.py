import hmac,base64,struct,hashlib,time,re

####方法1
#def Token(token):
#	totp = pyotp.TOTP("token")
#	a = totp.now()
#	return a

####方法2
def Token(secretKey):
    input = int(time.time())//30
    key = base64.b32decode(secretKey)
    msg = struct.pack(">Q", input)
    googleCode = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(googleCode[19]) & 15
    googleCode = str((struct.unpack(">I", googleCode[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(googleCode) == 5:             # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
        googleCode = '0' + googleCode
    return googleCode

#####方法3
#def get_hotp_token(secret, intervals_no):
#	key = base64.b32decode(secret, True)
#	msg = struct.pack(">Q", intervals_no)
#	h = hmac.new(key, msg, hashlib.sha1).digest()
#	o = ord(h[19]) & 15
#	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
#	return h
#
#def Token(secret):
#	return get_hotp_token(secret, intervals_no=int(time.time())//30)

###获取IP形式字符串
def IP_FIN(ip):
   IP_Mid = str(abs(int(ip[0])))
   for i in range(1, 4):
       IP_Mid = (IP_Mid+'.'+str(abs(int(ip[i]))))
   return IP_Mid	
def IP_FIN(ip):
	abs_ip = [int(i) for i in ip]
	IP_FIN = '.'.join(str(i)for i in abs_ip)
	return IP_FIN

def main():
	#user = "liuchenggong"#str(crt.Arguments[0])     # user account for ssh account
	#pwd = "As111@@@" #str(crt.Arguments[2])     # password for ssh
	gtoken = "3NXBYATWGIIZ3LEV" #str(crt.Arguments[1])  # google token value

	#crt.Screen.Send("ssh "+user+"@jumper.izuche.com -p 2222\r")    # ssh command
	#result = crt.Screen.WaitForString("connecting (yes/no)?", 2)
	#if result == 1:
	#    crt.Screen.Send("yes\r")

	####出现[MFA auth]:后输入token
	result = crt.Screen.WaitForString("[MFA auth]:")###出现[MFA auth]:触发条件，最多等待五秒后超时
	crt.Screen.Send(str(Token(gtoken))+"\r")
	#result = crt.Screen.WaitForString("assword:", 5)
	#if result == 0:
	#    return ""
	#crt.Screen.Send(pwd+"\r")

	####从session名称获取主机IP
	objTab = crt.GetScriptTab()
	szSessionName = objTab.Session.Path
	IP_ORI = re.findall(r"\d+", str(szSessionName.split('\\')[1]),re.S)
	IP = IP_FIN(IP_ORI)
	####出现Opt> 后输入主机IP
	result = crt.Screen.WaitForString("Opt> ")
	#for i in range(0, 3):
	#	crt.Screen.Send(str(abs(int(IP[i]))))
	#	crt.Screen.Send(".")
	#crt.Screen.Send(str(abs(int(IP[3])))+"\r")
	crt.Screen.Send(str(IP)+'\r')
	####切换到root: sudo su -
	result = crt.Screen.WaitForString("~]$ ")
	crt.Screen.Send("sudo su -\r")
	####切换到dig: su - dig
	result = crt.Screen.WaitForString("~]# ")
	crt.Screen.Send("su - dig")
main()