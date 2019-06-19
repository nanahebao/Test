import  yagmail
#链接邮箱服务器
yag = yagmail.SMTP( user="294714025", password="lnqhygbmqqlycb89", host='mail.qq.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件
yag.send('294714025', 'subject', contents)