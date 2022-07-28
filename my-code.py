import tagui as r
r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'KPMG Ignition Tokyo[enter]')
print(r.read('result-stats'))

