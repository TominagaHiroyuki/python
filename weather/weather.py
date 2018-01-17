"""weather module"""
#!/usr/bin python
#-*-coding:utf-8-*-

from sources import daily, weekly

if __name__ == '__main__':
    print('Daily Weather is', daily.forecast())
    print('Weekly Weather is')

    for number, outlook in enumerate(weekly.forecast(), 1):
        print(number, outlook)
