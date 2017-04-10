# -*- coding=utf-8 -*-

from urllib.request import urlopen
import json
import datetime


def main():
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
    u = urlopen('http://api.cntv.cn/epg/epginfo?serviceId=tvcctv&c=cctv6&d=' + tomorrow + '&cb=?&t=jsonp')
    data = json.loads(u.read().decode('utf-8')[2:-2])
    programs = data['cctv6']['program']

    output = ""
    for program in programs:
        # 把可能不是电影的节目过滤掉
        if len(program['t']) > 3 and (program['t'][3] == ':' or program['t'][4] == ';'):
            output += '播出时间：{}    时长：{:>3}分钟    节目名：{}'.\
                          format(program['showTime'],int(program['duration']/60), program['t']) + '\n'

    print(output)

if __name__ == "__main__":
    main()
