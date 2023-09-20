import itertools
import zipfile

def unzip(pwString, minLen, maxLen, zFile):
    for i in range(minLen,maxLen+1):
        toAttempt = itertools.product(passwd_string, repeat=i)
        for attempt in toAttempt:
            passwd = " ".join(attempt)
            print(passwd)
            try: 
                zFile.extractall(pwd = passwd.encode())
                print(f"The password is : {passwd}")
                return 1
            except:
                pass

passwd_string = "0123456789"

zFile = zipfile.ZipFile(r"test.zip")

minLen=1
maxLen=5

unzip_result = unzip(passwd_string,minLen,maxLen,zFile)

if unzip_result == 1:
    print("You've succeded.")
else:
    print("You've failed.")

# for len in range(1,6):
#     toAttempt = itertools.product(passwd_string, repeat=len)
#     for attempt in toAttempt:
#         passwd = ''.join(attempt)
#         print(passwd)
#         try: 
#             zFile.extractall(pwd = passwd.encode())
#             print(f"The password is : {passwd}")
#             break
#         except:
#             pass