# SSEannouncement
version 0.1

Download SSE announcement from http://www.sse.com.cn/disclosure/listedinfo/announcement

    邮箱： drifthua#gmail.com
--------------------------------------------------------------------------------
# 开发环境：
  python3 selenium wget BeautifulSoup4

--------------------------------------------------------------------------------
# run program:

  python SSEannouncement.py

--------------------------------------------------------------------------------
# 下载最新上市公司公告

深圳上市公司公告：
http://disclosure.szse.cn/m/search0425.jsp
提交数据：
Host=disclosure.szse.cn
User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0
Accept=text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language=en-US,en;q=0.5
Accept-Encoding=gzip, deflate
DNT=1
Referer=http://disclosure.szse.cn/m/search0425.jsp
Cookie=JSESSIONID=4F4D26C8A9BCFC8C9B6115361F6F5B20
Connection=keep-alive
Content-Type=application/x-www-form-urlencoded
Content-Length=141
POSTDATA=leftid=1&lmid=drgg&pageNo=1&stockCode=000737&keyword=&noticeType=&startTime=2002-09-01&endTime=2015-10-02&imageField.x=52&imageField.y=2&tzy=


--------------------------------------------------------------------------------
上证公司公告

<textarea rows="15" cols="100">
当有分页时
（http://www.sse.com.cn/assortment/stock/list/stockdetails/announcement/index.shtml?COMPANY_CODE=600359&startDate=2015-06-03&endDate=2015-10-03&productId=600359&startDate=2015-07-03&endDate=2015-10-03&reportType=ALL&reportType2=%E5%85%A8%E9%83%A8&reportType=ALL&moreConditions=true）：
<div id="announcementDiv_container_pagination" class="paging">
<div id="abId0.42829732394412534" class="paging-bottom">
<span id="abId0.7259081873547838" class="paging_input" abineguid="57035F88081A4B7589FBC26189264B9C">
 共5页 转到第
<input id="announcementDiv_container_pageid" type="text" value="" size="3" name="jumpto" title="指定页码">
页
<img id="announcementDiv_container_togo" title="指定页码" src="/images/button_go.gif">
</span>
<span class="paging_text">
</div>
</div>

（http://www.sse.com.cn/assortment/stock/list/stockdetails/announcement/index.shtml?COMPANY_CODE=600351&startDate=2015-06-03&endDate=2015-10-03&productId=600351&startDate=2015-07-03&endDate=2015-10-03&reportType=ALL&reportType2=%E5%85%A8%E9%83%A8&reportType=ALL&moreConditions=true）：
  <div class="paging" id="announcementDiv_container_pagination">
   <div class="paging-bottom" id="abId0.1464835436745655">
    <span abineguid="88786D0310D1487ABA7B4A0A895898B9" class="paging_input" id="abId0.9838209436649801">
     共3页 转到第
     <input id="announcementDiv_container_pageid" name="jumpto" size="3" title="指定页码" type="text" value=""/>
     页
     <img id="announcementDiv_container_togo" src="/images/button_go.gif" title="指定页码"/>
    </span>
    <span class="paging_text">
     <span class="paging_num_on">
      1
     </span>
     <a class="announcementDiv_container_paginationNumLink" href="#" pageno="2">
      2
     </a>
     <a class="announcementDiv_container_paginationNumLink" href="#" pageno="3">
      3
     </a>
     <a class="paging_next" href="javascript:void(0)" id="announcementDiv_container_next" pageno="2" title="下页">
      <span>
       下一页
      </span>
     </a>
    </span>
   </div>
  </div>
--------------------------------------------------
深圳公司公告
http://disclosure.szse.cn/m/search0425.jsp
http://disclosure.szse.cn/m/search0425.jsp?stockCode=000998&startTime=2013-10-02&endTime=2015-10-18


--------------------------------------------------

</textarea>

## todolist

# 需要获取公告的股票代码从文本中读取

# 重构为类调用，根据股票代码自动调用对应函数

# 定时自动调用

# 使用worker client 模式加快处理速度
