"""test python"""

#!/usr/bin python
#pylint: disable-msg=C0103
#-*-coding:utf-8-*-

if __name__ == '__main__':
    testlist = ['one', 'two']
    testlist1 = ['three', 'four']
    testlist2 = ['five', 'six']

    for item in testlist:
        #print value
        print(item)

        #print FirstValue is Capitalize
        print(item.capitalize())

        #print reverse
        print(item[::-1])

    #結合
    testlist.extend(testlist1)
    testlist.extend(testlist2)

    print("-----------------------")
    #dictionary
    dic = {}
    dic['one'] = testlist
    dic['two'] = testlist1
    dic['three'] = testlist2

    dic2 = dic.copy()
    for key, value in dic2.items():
        print(key, value)
        del dic[key]

    print(dic2)
    print('end function')
