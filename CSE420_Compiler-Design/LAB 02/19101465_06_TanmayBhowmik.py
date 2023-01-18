list = []

char=('#','%','&','.','!','/','=')
number=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
domain=('.ac', '.ac.uk', '.ad', '.ae', '.aero', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.arpa', '.as', '.asia', '.at', '.au', '.aw', '.ax', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.biz', '.bj', '.bm', '.bn', '.bo', '.br', '.bs', '.bt', '.bv', '.bw', '.by', '.bz', '.ca', '.cat', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.co.uk', '.com', '.coop', '.cr', '.cs', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz', '.dd', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.edu', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu', '.fi', '.firm', '.fj', '.fk', '.fm', '.fo', '.fr', '.fx', '.ga', '.gb', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gn', '.gov', '.gov.uk', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.il', '.im', '.in', '.info', '.int', '.io', '.iq', '.ir', '.is', '.it', '.je', '.jm', '.jo', '.jobs', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz', '.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.ltd.uk', '.lu', '.lv', '.ly', '.ma', '.mc', '.md', '.me', '.me.uk', '.mg', '.mh', '.mil', '.mk', '.ml', '.mm', '.mn', '.mo', '.mobi', '.mod.uk', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.museum', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.name', '.nato', '.nc', '.ne', '.net', '.net', '.net.uk', '.nf', '.ng', '.nhs.uk', '.ni', '.nl', '.no', '.nom', '.np', '.nr', '.nt', '.nu', '.nz', '.om', '.org', '.org.uk', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pl', '.plc.uk', '.pm', '.pn', '.post', '.pr', '.pro', '.ps', '.pt', '.pw', '.py', '.qa', '.re', '.ro', '.rs', '.ru', '.rw', '.sa', '.sb', '.sc', '.sch.uk', '.sd', '.se', '.sg', '.sh', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.store', '.su', '.sv', '.sy', '.sz', '.tc', '.td', '.tel', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tp', '.tr', '.travel', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.web', '.wf', '.ws', '.xxx', '.ye', '.yt', '.yu', '.za', '.zm', '.zr', '.zw')

count = input('Enter an integer value for lines of strings: ')
for i in range(int(count)):
    Check = input()
    list.append(Check)



for x in list:
    if "@" in x and "www." not in x and " " not in x:
        if (x.count('@')==1):
            dom=x.split('@',2)
            if not x.startswith(number) and not x.startswith(char): 
                if x.endswith(domain): 
                    if x.count('_')<=1 and ".." not in x: 
                        if  len(dom[0])!=0 and len(dom[1])!=0 :
                            print("Email,", list.index(x)+1)
            
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")
            
            
    elif "@" not in x and "www" in x and " " not in x:
        if(x.count('www.')==1):
            dom=x.split('www',2)
            y=dom[1]
            if(x.startswith("https://www.") or x.startswith("www.")): 
              if x.endswith(domain) and y not in domain:
                 print("Web,", list.index(x)+1)
              else:
                  print("Invalid Web,",list.index(x)+1 )
        else:
            print("Invalid Web")
    else:
        print("Invalid,",list.index(x)+1 )