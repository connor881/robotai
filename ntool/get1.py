from urllib import request

with request.urlopen('http://10.7.5.88:8080/gs-robot/real_time_data/protector') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


