import hmac

def pa_jm(username,password):
    
    str1=hmac.new(username.encode('utf8'),password.encode('utf8'),'MD5')
    return str1.hexdigest()

if __name__=='__main__':
    x=pa_jm('admin','admin')
    print(x)