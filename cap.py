#!/bin/python3.9
import os,requests,json,sys,urllib.request,subprocess,shlex,time 

# todo.
#      func.kill running procs and delete temp data for session(s)
#      proc.std to /dev/null
#      exit.code checks
#      err.handling

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

def chromi(proxy):
    stype=proxy[1]
    chrun='chromium --temp-profile --proxy-server="https='+stype.lower()+'://'+proxy[0]+';http='+stype.lower()+'://'+proxy[0]+'" https://cleanip.xyz'
    print(chrun)
    args = shlex.split(chrun)
    ret=0
    try:
        ret = subprocess.Popen(args)
    except:
        print('err.c38 ')
    return ret
    

def menu(xp):
    os.system('clear')
    print("#"*50)
    print(str(xp)+ " procs running")
    print("inputs\nc\t exec chromium->proc(rand(proxy))\nk\tkills proc[0]\nq\tquitt\n")
    print('#'*50)
    
def cleanup():
  ## code
  return false

def main():
    xp=0
    pkill=0
    chp=[]
    while True:
        menu(xp)
        ui=input('>>')
        
        if str(ui) == 'c':
            try:
                proxy = newProxy()
            except:
                print('err.p1')
            try:  
                tp=chromi(proxy)
                if tp != 0:
                    xp+=1
                    chp.append(tp)
            except:
                print("err.r74")
    
            time.sleep(3)
    
        if str(ui) == 'k':
            if xp>=1:
                xp = cleanup()
            else:
                print('>> nothing to kill')
                time.sleep(3)
        if str(ui) == 'q':
            cleanup()
        

if __name__ == '__main__':
    main()
