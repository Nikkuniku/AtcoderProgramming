d={
    "a":''
    ,"b":'1'
    ,"c":'1'
    ,"d":'2'
    ,"e":''
    ,"f":'4'
    ,"g":'9'
    ,"h":'8'
    ,"i":''
    ,"j":'3'
    ,"k":'8'
    ,"l":'5'
    ,"m":'7'
    ,"n":'9'
    ,"o":''
    ,"p":'7'
    ,"q":'4'
    ,"r":'0'
    ,"s":'6'
    ,"t":'3'
    ,"u":''
    ,"v":'5'
    ,"w":'2'
    ,"x":'6'
    ,"y":''
    ,"z":'0'
    ," ":' '
    ,".":''
    ,",":''
}
n=int(input())
s=input()
ans=''
for i in range(len(s)):
    p=s[i].lower()
    ans+=d[p]
ans=" ".join(ans.split())
print(ans)