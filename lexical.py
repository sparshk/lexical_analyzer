#Basic one line syntax checker for JAVA. To start,open main.py and run the code.

def lexic(s):
        list1=["if","import","for","while","boolean","int","float","double","String","long"]
        st=""
        y=0
        x=0
        check=False
        for x in range(len(s)):
            if(s[x] is '(' or s[x] is ' '):
                for y in range(10):
                    if(st==list1[y]):
                        check=True
                        break
            else:
                st=st+s[x]
            if(check==True):
                break
            elif(y==10):
                print("invalid")
                break

        if(x==(len(s)-1) and check==False):
            print("invalid")
        ch=s[x]
        if(st=="if"):
            while(ch!='('):
                ch=s[x]
                x=x+1
                if(x==len(s)):
                    print("invalid")
                    check=False
                    break
            if(check==True):
                var=""
                ch=s[x]
                while(ch.isalpha()==False and ch.isdigit()==False):
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False
                        break
          
            if(check==True):
                ch=s[x]
                while(ch.isalpha()==True or ch.isdigit()==True):
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False
                        break
            
            if(check==True):
                if(ch!='=' and ch!='<' and ch!='>' and ch!='!' and ch!='&' and ch!='|'):
                        while(ch!='=' and ch!='<' and ch!='>' and ch!='!' and ch!='&' and ch!='|'):
                            ch=s[x]
                            x=x+1
                            if(x==len(s)):
                                print("invalid")
                                check=False
                                break
                else:
                    x=x+1
            if(check==True):
                if(ch=='=' or ch=='!'):
                    if(x==(len(s)-1)):
                        print("invalid")
                        check=False
                    else:
                        ch=s[x]
                        if(ch!='='):
                            print("invalid")
                            check=False
                if(ch=='&'):
                    if(x==(len(s)-1)):
                        print("invalid")
                        check=False
                    else:
                        ch=s[x]
                        if(ch!='&'):
                            print("invalid")
                            check=False
                
                if(ch=='|'):
                    if(x==(len(s)-1)):
                        print("invalid")
                        check=False
                    else:
                        ch=s[x]
                        if(ch!='|'):
                            print("invalid")
                            check=False
            
            if(check==True):
                if(ch=='!' or ch=='&' or ch=='=' or ch=='|'):     
                    x=x+1
                    ch=s[x]
                    if(s[x]=='=' or s[x]=='&' or s[x]=='|'):
                        check=False;
                        print("invalid")
                      
            if(check==True):
                while(ch.isalpha()==False and ch.isdigit()==False):
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False
                        break
            
            if(check==True):
                while(ch.isalpha()==True or ch.isdigit()==True):
                    ch=s[x]
                    x=x+1
                    if(x==len(s) and ch!=')'):
                        print("invalid")
                        check=False
                        break
                    elif(x==len(s) and ch==')'):
                        print("valid")
                        check=False
                        break
            
            if(check==True):
                while(ch!=')'):
                    ch=s[x]
                    x=x+1
                    if(x==len(s) and ch!=')'):
                        print("invalid")
                        check=False
                        break
                    elif(x==len(s) and ch==')'):
                        print("valid")
                        break
            if(x!=len(s)):
                    print("invalid")

        if(st=="boolean" or st=="int" or st=="float" or st=="double" or st=="String" or st=="long"):
            if(ch==' '):
                x=x+1
                ch=s[x]
                if(ch==' '):
                    check=False
                    print("invalid")

            if(check==True):
                while(ch.isalpha()==True or ch.isdigit()==True):
                    ch=s[x]
                    x=x+1
                    if(x==len(s) and ch==';'):
                        print("valid")
                        check=False
                        break
                    if(x==len(s) and ch!=';'):
                        print("invalid")
                        check=False
                        break
            
            if(check==True):
                while(ch!='='):
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False;
                        break

            if(check==True):
                 if(st=="int" or st=="long"):
                     ch=s[x]
                     while(ch.isdigit()!=True):
                         ch=s[x]
                         x=x+1
                         if(x==len(s)):
                             check=False
                             print("invalid")
                             break
                    
                     while(ch.isdigit()==True):
                            ch=s[x]
                            x=x+1
                            if(x==len(s) and ch==';'):
                                print("valid")
                                break
                            elif(x==len(s) and ch!=';'):
                                print("invalid")
                                break
                     if(x!=len(s) and ch!=';'):
                         print("invalid")
                         check=False

                 if(st=="double" or st=="float"):
                     ch=s[x]
                     while(ch.isdigit()!=True):
                         ch=s[x]
                         x=x+1
                         if(x==len(s)):
                             check=False
                             print("invalid")
                             break
                     
                                   
                     while(ch.isdigit()==True):
                            ch=s[x]
                            x=x+1
                            if(x==len(s) and ch==';'):
                                print("valid")
                                break
                            elif(x==len(s) and ch!=';'):
                                print("invalid")
                                check=False
                                break
                     if(check==True):
                         if(ch=='.'):
                             x=x+1
                             ch=s[x]
                         while(ch.isdigit()==True):
                             ch=s[x]
                             x=x+1
                             if(x==len(s) and ch==';'):
                                 print("valid")
                                 break
                             elif(x==len(s) and ch!=';'):
                                 print("invalid")
                                 break
                         if(x!=len(s)):
                             print("invalid")
                             check=False

                 if(st=="String"):
                     ch=s[x]
                     
                             
                     if(ch=='"'):
                         x=x+1;
         
                     else:
                        while(ch!='"'):
                            ch=s[x]
                            x=x+1
                            if(x==len(s)):
                                check=False
                                print("invalid")
                                break
                     if(x!=len(s)):
                         ch=s[x]
                     if(ch=='"'):
                         x=x+1
                     else:
                         while(ch!='"'):
                             ch=s[x]
                             x=x+1
                             if(x==len(s)):
                                 print("invalid")
                                 check=False
                                 break
                            
                     if(check==True):
                         if(s[x]==';'):
                             print("valid")

                 if(st=="boolean"):
                     ch=s[x]
                     sr=""
                     sr1=""
                     if(ch!=' '):
                         x=x+1
                     else:
                         while(ch==' '):
                             ch=s[x]
                             x=x+1
                             if(x==len(s)):
                                 check=False
                                 print("invalid")
                                 break
                     
                     if(ch.isalpha()!=True):
                         print("invalid")
                         check=False

                     if(check==True):
                             while(ch.isalpha()!=False):
                                 sr=sr+ch
                                 ch=s[x]
                                 x=x+1
                             
                                 if(x==len(s) and ch!=';'):
                                     print("invalid")
                                     check=False
                                     break
                     if(check==True):
                         if((sr=="true" or sr=="false") and ch==';'):
                             print("valid")
                         else:
                             print("invalid")

        if(st=="import"):
            ch=s[x]
            ctr=0;
            if(ch==' '):
                x=x+1
                sr=""
                while(ch!='.'):
                    sr=sr+ch
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False
                        break
                
                if(ch=='.'):
                    ctr=ctr+1
                    x=x+1
                    ch=s[x]
                if(check==True):
                    if(sr==" java"):
                        while(ch!='.'):
                            ch=s[x]
                            x=x+1
                            if(x==len(s)):
                                print("invalid")
                                check=False
                                break
                    else:
                        print("invalid")
                        check=False
                                      
                if(ch=='.'):
                    ctr=ctr+1
                if(ctr==2):
                    while(ch.isalpha()!=True):
                        ch=s[x]
                        x=x+1
                        if(x==len(s) and ch==';'):
                            print("valid")
                            break
                        elif(x==len(s) and ch!=';'):
                            print("invalid")
                            break

            else:
                print("invalid")

        if(st=="for"):
            ch=s[x]
            ctr=0
            while(ch!='('):
                ch=s[x]
                x=x+1
                if(x==len(s)):
                    print("invalid")
                    check=False
                    break

            if(check==True):
                ch=s[x]
                while(x!=len(s)-2):
                    if(ch==';'):
                        ctr=ctr+1;
                    x=x+1
                    ch=s[x]

            if(ctr==2 and s[len(s)-1]==')'):
                print("valid")
            else:
                print("invalid")

        if(st=="while"):
            ch=s[x]
            if(s[len(s)-1]==';'):
                print("invalid")
            while(ch!='('):
                ch=s[x]
                x=x+1
                if(x==len(s)):
                    print("invalid")
                    check=False
                    break
            if(check==True):
                ch=s[x]
                
                while(ch!='!' and ch!='='):
                    ch=s[x]
                    x=x+1
                    if(x==len(s)):
                        print("invalid")
                        check=False
            
            
            if(check==True):
                ch=s[x]
                x=x+1
                if(ch!='='):
                    print("invalid")
                    check=False

            if(check==True):
                ch=s[x]
                x=x+1
                sr=""
                while(ch.isalpha()!=False):
                    sr=sr+ch
                    ch=s[x]
                    x=x+1
                    if(x==len(s) and ch==')' and (sr=="true" or sr=="false")):
                        print("valid")
                        check=False
                        break
                    elif(x==len(s) and (ch!=')' or(sr!="true" or sr!="false"))):
                        print("invalid")
                        break
            
                
        
    
    
        
        
    
            
                
            
            

                     
                     
                  

                
                         
             
             

         
                 
                    
        
                      
                

    
    

        
        
            

    
        
            
    
                
        
        
            
    
    

    
            
    
        
    
        
    
        
               

    
    
        
    
    
    
        
    


    

        
    
        
    
            
        
        
    
    
