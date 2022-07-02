from mail import Gmail

subject = '[Weblog-TEST] Report'
body = open('./mail_in.html').read()
print(body)

to_list = ['username@hostname', ]

for index, to in enumerate(to_list):
    ret =  Gmail().send(to=to, subject=subject, html_body=body, attach=None)
    ret = ret and ret or 'Okay'
    print('{} : {}'.format(index+1, ret))

print('Done')