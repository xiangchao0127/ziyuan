# 模板数据抓取
import re
import sys
import threading
import requests
from lxml import etree
import excelUtils

thread_datas = threading.local()


def youdao(words,proxyIp,fileDest,window):
    thread_datas.data = set()
    for word in words:
        print(word + "---------------------------------")
        youdao_single("http://www.youdao.com/example/" + word,proxyIp)
    print(thread_datas.data)
    excelUtils.saveToExcel(fileDest+"youdao", thread_datas.data)
    window.callback("youdao")


def bing(words,proxyIp,fileDest,window):
    thread_datas.data = set()
    for word in words:
        print(word + "---------------------------------")
        bing_single("https://cn.bing.com/dict/service?q=" + word + "&offset=10&dtype=sen",proxyIp)
    print(thread_datas.data)
    excelUtils.saveToExcel(fileDest+"bing", thread_datas.data)
    window.callback("bing")


def aiciba(words,proxyIp,fileDest,window):
    thread_datas.data = set()
    for word in words:
        print(word + "---------------------------------")
        aiciba_single("http://dj.iciba.com/" + word + "-1-" + '1' + '-%01-0-0.html',proxyIp)
    excelUtils.saveToExcel(fileDest+"aiciba", thread_datas.data)
    print(thread_datas.data)
    window.callback("aiciba")


def youdao_single(url,proxyIp):
    get = requests.get(url,proxies = proxyIp)
    response = etree.HTML(get.text)
    matchObj = re.match(r'http://www.youdao.com/example/(.*)', url)
    enmode = re.compile(u'^[a-zA-Z]')
    if matchObj:
        word = matchObj.group(1)
        is_english = enmode.search(word)
    sentences = response.xpath("//ul[@class='ol']/li")
    english_list = []
    chinese_list = []
    for sentence in sentences:
        chinese = sentence.xpath("./p[2]/span/text()")
        cn = "".join(chinese)
        chinese_list.append(cn)
        english = sentence.xpath("./p[1]/span/text() | ./p[1]/span/b/text()")
        en = "".join(english)
        english_list.append(en)
    try:
        for sentence_index in range(len(english_list)):
            if is_english:
                thread_datas.data.add((english_list[sentence_index], chinese_list[sentence_index]))
            else:
                thread_datas.data.add((chinese_list[sentence_index], english_list[sentence_index]))
    except:
        print("编码异常")


def bing_single(url,proxyIp):
    get = requests.get(url,proxies = proxyIp)
    response = etree.HTML(get.text)
    english_sentence = response.xpath("//div[@class='sen_en']")
    # 汉语单词
    chinese_sentence = response.xpath("//div[@class='sen_cn']")
    # 判断是否还有下一页
    is_have_next_page = len(response.xpath("//div[@class='b_pag']")) != 0
    # 组装句子
    english_list = []
    for sub_sentence_en in english_sentence:
        sentence_en = sub_sentence_en.xpath('./span/text() | ./a/text()')
        str_en = "".join(sentence_en)
        english_list.append(str_en)
        # print str_en
    chinese_list = []
    for sub_sentence_cn in chinese_sentence:
        sentence_cn = sub_sentence_cn.xpath('./a/text()')
        str_cn = "".join(sentence_cn)
        chinese_list.append(str_cn)
        # print str_cn

    for sentence_index in range(len(english_list)):
        thread_datas.data.add((chinese_list[sentence_index], english_list[sentence_index]))

    matchObj = re.match(r'https://cn.bing.com/dict/service\?q=(.*)&offset=(.*)&(.*)', url)
    if matchObj:
        word = matchObj.group(1)
        # 动态定义偏移量，用于获取下一页
        offset = int(matchObj.group(2))
    if is_have_next_page:
        offset += 10
        bing_single("https://cn.bing.com/dict/service?q=" + word + "&offset=" + str(offset) + "&dtype=sen",proxyIp)


def aiciba_single(url,proxyIp):
    get = requests.get(url,proxies = proxyIp)
    response = etree.HTML(get.text)
    matchObj = re.match(r'http://dj.iciba.com/(.*)-1-(.*)-%01-0-0.html', url)
    if matchObj:
        word = matchObj.group(1)
        # 动态定义偏移量，用于获取下一页
        offset = int(matchObj.group(2))
    # 判断是否还有下一页
    is_have_next_page = len(response.xpath("//li[@class='dj_li']")) == 10
    sentences = response.xpath("//li[@class='dj_li']")
    for sentence in sentences:
        try:
            english = sentence.xpath("./p[@class='stc_en']/span[2]/@con")[0]
            chinese = sentence.xpath("./p[@class='stc_cn']/span[2]/@con")[0]
            thread_datas.data.add((chinese, english))
        except:
            pass
        # 组装分页url给控制器
    if offset < 50:
        if is_have_next_page:
            offset += 1
            url = "http://dj.iciba.com/" + word + "-1-" + str(offset) + '-%01-0-0.html'
            aiciba_single(url,proxyIp)


if __name__ == "__main__":
    urls = ("hello", "heart")
    aiciba(urls)
