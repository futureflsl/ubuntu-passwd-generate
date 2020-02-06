import crypt

print('example-----------')
print('USER_NAME="HwHiAiUser"')
print('USER_PWD="HwHiAiUser:\$6\$klSpdQ1K\$4Gm/7HxehX.YSum4Wf3IDFZ3v5L.clybUpGNGaw9zAh3rqzqB4mWbxvSTFcvhbjY/6.tlgHhWsbtbAVNR9TSI/:17795:0:99999:7:::"')
print('ROOT_PWD="root:\$6\$klSpdQ1K\$4Gm/7HxehX.YSum4Wf3IDFZ3v5L.clybUpGNGaw9zAh3rqzqB4mWbxvSTFcvhbjY/6.tlgHhWsbtbAVNR9TSI/:17795:0:99999:7:::"')
print('End----------')
user_name = 'HwHiAiUser'
pwd_user = 'Mind@123'
pwd_rooter = 'Mind@123'
sault = '$6$klSpdQ1K$'
print('USER_NAME="%s"' % user_name)
userpassword = 'USER_PWD="%s:%s:17795:0:99999:7:::"' % (user_name, crypt.crypt(pwd_user,sault))
rootpassword = 'ROOT_PWD="root:%s:17795:0:99999:7:::"' % crypt.crypt(pwd_rooter,sault)
print(userpassword.replace('$','\$'))
print(rootpassword.replace('$','\$'))
