from os import read 
import tagui as r
r.init(visual_automation = True, chrome_browser = False)
r.keyboard('[cmd][space]')
r.keyboard('safari[enter]')
r.keyboard('[cmd]t')
r.type('//*[@name="q"]', 'https://auditws-dev.jp.kworld.kpmg.com[enter]')
r.url('https://auditws-dev.jp.kworld.kpmg.com')
