# new day,new diff
# written in: 2020/11/5 11:45
import requests
from lxml import etree
# 列表用来保存所有公交信息
items = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}


# 导航页爬取（以1,2,3·······开头）
def parse_navigation():
    url = 'https://foshan.8684.cn/'
    r = requests.get(url, headers=headers)
    # 解析内容，获取所有的导航链接
    tree = etree.HTML(r.text)
    # 查找以数字开头的所有链接
    number_href_list = tree.xpath('//div[@class="bus-layer depth w120"]/div[1]/div/a/@href')
    # 查找以字母开头的所有链接
    char_href_list = tree.xpath('//div[@class="bus-layer depth w120"]/div[2]/div/a/@href')
    # 以列表形式返回所有链接
    return number_href_list + char_href_list


def parse_second_route(content):
    tree = etree.HTML(content)
    # 写xpath，获取每一个线路
    route_list = tree.xpath('//div[@class="list clearfix"]/a/@href')
    route_name = tree.xpath('//div[@class="list clearfix"]/a/text()')
    i = 0
    # 遍历上边的列表
    for route in route_list:
        print('开始爬取%s线路······' % route_name[i])
        route = 'https://foshan.8684.cn'+route
        r = requests.get(url=route,headers=headers)
        # 解析内容，获取每一路公交车的详细信息
        parse_third_route(r.text)
        print('结束爬取%s线路······' % route_name[i])
        i += 1


def parse_third_route(content):
    tree = etree.HTML(content)
    # -------------------依次获取内容--------------------
    # 获取公交信息
    bus_number = tree.xpath('//div[@class="info"]/h1/text()')[0]
    # 获取运行时间
    run_time = tree.xpath('//ul[@class="bus-desc"]/li[1]/text()')[0]
    # 获取票价信息
    ticket_info = tree.xpath('//ul[@class="bus-desc"]/li[2]/text()')[0]
    # 获取更新时间
    laster_time = tree.xpath('//ul[@class="bus-desc"]/li[4]/text()')[0]
    if tree.xpath('//div[@class="layout-left"]/div[5]/@class')[0] == 'bus-excerpt mb15':
        # 获取上行总站数
        up_total = tree.xpath('//div[@class="layout-left"]/div[5]/div/div[@class="total"]/text()')[0]
        # 获取上行所有站名
        up_route = tree.xpath('//div[@class="layout-left"]/div[6]/ol/li/a/text()')
        try:
            # 获取下行总站数
            down_total = tree.xpath('//div[@class="layout-left"]/div[7]/div/div[@class="total"]/text()')[0]
            # 获取下行所有站名
            down_route = tree.xpath('//div[@class="layout-left"]/div[8]/ol/li/a/text()')
        except Exception as e:
            down_total = ''
            down_route = ''
    else:
        up_total = tree.xpath('//div[@class="layout-left"]/div[4]/div/div[@class="total"]/text()')[0]
        up_route = tree.xpath('//div[@class="layout-left"]/div[5]/ol/li/a/text()')
        try:
            down_total = tree.xpath('//div[@class="layout-left"]/div[6]/div/div[@class="total"]/text()')[0]
            down_route = tree.xpath('//div[@class="layout-left"]/div[7]/ol/li/a/text()')
        except Exception as e:
            down_total = ''
            down_route = ''

        # 将每一条公交信息存放到字典中
    item = {
        '线路名称': bus_number,
        '运行时间': run_time,
        '票价信息': ticket_info,
        '更新时间': laster_time,
        '上行总站数': up_total,
        '上行所有站名': up_route,
        '下行总站数': down_total,
        '下行所有站名': down_route
    }
    items.append(item)


def parse_second(navi_list):
    # 遍历上面的列表，依次发送请求，解析内容，获取每个页面所有的公交路线url
    for first_url in navi_list:
        first_url = 'https://foshan.8684.cn' + first_url
        print('开始爬取%s所有的公交信息' % first_url)
        r = requests.get(url=first_url, headers=headers)
        # 解析内容，获取每一路公交的详细url
        parse_second_route(r.text)
        # 爬取完毕
        fp = open('佛山公交.txt', 'w', encoding='utf8')
        for item in items:
            fp.write(str(item) + '\n')
        fp.close()


def main():
    # 爬取第一页所有的导航链接
    navi_list = parse_navigation()
    # 爬取二级页面，需要找到以1开头的所有公交路线
    parse_second(navi_list)


if __name__ == '__main__':
        main()

