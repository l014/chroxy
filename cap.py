#!/usr/bin/python3.9

# todo.
#      cleanup->kill specific proc & rm tmp profile for proc 
#      err.handling

import os,requests,json,sys,urllib.request,socket,subprocess,shlex,time 

def newProxy():
    url = 'https://www.proxyscan.io/api/proxy?level=anonymous&ping=40&format=json'
    resp = requests.get(url)
    jstr = json.dumps(resp.json())
    resp = json.loads(jstr)
    ipv4 = resp[0]['Ip'].strip()
    stype = str(resp[0]['Type'][0]).strip()
    port = str(resp[0]['Port']).strip()
    proxy=str(ipv4)+":"+str(port)
    return [proxy,stype]

def chromi(proxy,cv):
    stype=proxy[1]
    chrun=str(cv)+' --temp-profile --proxy-server="https='+stype.lower()+'://'+proxy[0]+';http='+stype.lower()+'://'+proxy[0]+'" https://cleanip.xyz'
    args = shlex.split(chrun)
    ret=0
    try:
        ret = subprocess.Popen(args)
    except:
        print('err.c38 ')   
    return ret
    

def menu(xp,cv):
    os.system('clear')
    print("#"*50)
    print('[i]\t'+str(xp)+ " procs running\n")
    print("\t--USE--\n  p\tstart a new "+str(cv)+"->proc with a random proxy\n  q\tquitt\n")
    print('#'*50)

def cleanup(xp,cv,chp):
    if xp <= 0:
        sys.exit('[+] no proc started\nbye!')
    
    kill = 'pkill ' + str(cv)
    dtmp = 'rm -rf /tmp/tmp*'
    kt = input('[i] this will kill all '+cv+' procs(including) procs not started by this script and delete the temporary profile(s) in /tmp/\n[i] data will be lost if not saved before this action\ncontinue (y/n)\n>')
    
    if kt == 'y':
        for p in chp:
            p.kill()
        os.system('rm -rf /tmp/tmp.*')
        subprocess.Popen(shlex.split(kill))
        #subprocess.Popen(shlex.split(dtmp))
        sys.exit('bye')
    if kt == 'n':
        main()
    else:
        print('[-] check input, returning to main\n')
        time.sleep(3)

def bin():
    os.system('clear')
    cv = input('[+]set bin to use\n c\tchrome\n i\tchromeium\n>')
    if cv == 'c':
        cmd = 'type chrome &>/dev/null'
        try:
            bin = subprocess.check_output(cmd, shell=True)
            cv='chrome'
        except subprocess.CalledProcessError as isbin:                                                                         print('error code', isbin.returncode)
            sys.exit('chrome not found it PATH')
    if cv == 'i':
        cmd = 'type chromium &>/dev/null'
        try:
            bin = subprocess.check_output(cmd, shell=True)
            cv='chromium'
        except subprocess.CalledProcessError as isbin:                                                                                                   
            print('error code', isbin.returncode)
            sys.exit('chromium not found it PATH')
    else:
        return 0
    return cv

def main():
    cv = bin()    
    if cv == 0:
        print('[-] check input')
        main()
    print('[+] using ', cv)
    time.sleep(3)
    xp=0
    pkill=0
    chp=[]
    while True:
        menu(xp,cv)
        ui=input('>>') 
        if str(ui) == 'p':
            try:
                proxy = newProxy()
            except:
                print('err.p1')
            try:  
                tp=chromi(proxy,cv)
                if tp != 0:
                    xp+=1
                    chp.append(tp)
            except:
                print("err.r74")
    
            time.sleep(3)
        if str(ui) == 'q':
            cleanup(xp,cv,chp)

if __name__ == '__main__':
    main()
