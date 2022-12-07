'''import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('')
for key, val in res.items():
    print('%s : %s' % (key,val))'''
