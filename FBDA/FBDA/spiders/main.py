# coding=utf-8

from requests.exceptions import RequestException
import requests
import json
import csv
import re
import os

class Spider(object):

    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh; q = 0.9',
            'Connection': 'keep - alive',
            'Host': 'www.renrendai.com',
            'Referer': 'https://www.renrendai.com/',
            'User - Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest',
            'Cookie': 'rrdid=97a7e787-9ddf-4182-9622-a9d37020b0e4; __jsluid_s=e1aa41528c5cb79af05fde8530900452; gr_user_id=3a6c3add-ad06-4cba-847c-1155021cda43; grwng_uid=82cb1941-ce90-4824-9a3e-56c934763ebd; _ga=GA1.2.1517765865.1603711246; registerSource=web_top; _gid=GA1.2.1522634968.1603933709; loginMethod=sms; renrendaiUsername=17306445213; jforumUserInfo=TEZxUXSaBc%2By6bLjOd0IBRY7Q9PXR0j%2FFJN6FcAwPsE%3D%0A; Qs_lvt_181814=1603933708%2C1603966589%2C1603969624%2C1604020163%2C1604023550; Hm_lvt_a00f46563afb7c779eef47b5de48fcde=1603969625,1604020164,1604023550,1604036428; activeTimestamp=19320192; IS_MOBLIE_IDPASS=true-false; we_token=WG1EQnJqMVpkUmhjU3BiRUdoT3MzelRYd3FyYVE3eU06MTkzMjAxOTI6MjQ3MmMyOTNjYTBmOGRmOWIyMzNmMGQ4NGRlMDZiZWYwYjA5YTcwOQ%3D%3D; we_sid=s%3ADYcBhhpE_0cL573YId4qD30f9Ve0xQB_.M1A6R3ht5s0WKSFNgTR8DlCspKbzAZCKszuDsaHJV7Q; 9199126ed94d770d_gr_last_sent_sid_with_cs1=02e26ecb-642e-4b73-a52c-9951a3d0fbf4; 9199126ed94d770d_gr_last_sent_cs1=19320192; 9199126ed94d770d_gr_session_id=02e26ecb-642e-4b73-a52c-9951a3d0fbf4; 9199126ed94d770d_gr_session_id_02e26ecb-642e-4b73-a52c-9951a3d0fbf4=true; JSESSIONID=3A62E573FB77F1B2F2D7D896F6C6FC77; Qs_pv_181814=852484596927216500%2C2295503303876376600%2C4342495844457035300%2C1031981478543316100%2C3177497334737962500; 9199126ed94d770d_gr_cs1=19320192; Hm_lpvt_a00f46563afb7c779eef47b5de48fcde=1604038741; mediav=%7B%22eid%22%3A%22301358%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A1%2C%22_refnf%22%3A1%7D'
        }
        self.count = 0 # 记录成功爬取的条数


    # 获取散标信息
    def get_sanbiao(self):
        # 一共1000条，爬10次，每次100条
        for page in range(2):
            url = 'https://www.renrendai.com/loan/list/loanList?startNum={}&limit=100'.format(page)
            try:
                response = requests.get(url, headers=self.headers)
                if response.status_code == 200:
                    self.parse_sanbian(response.text)
            except RequestException as e:
                print(e)


    # 解析散标信息
    def parse_sanbian(self, data):
        data = json.loads(data)
        for item in data['data']['list']:
            url = 'https://www.renrendai.com/loan-{}.html'.format(item['obscureId'])
            self.get_detailinfo(url)


    # 获取详细信息
    def get_detailinfo(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                self.count += 1
                print('成功爬取第 {} 条'.format(self.count))
                self.parse_detailinfo(response.text)
            else:
                print('failure: {}'.format(url))
        except RequestException as e:
            print(e)


    # 解析详细信息
    def parse_detailinfo(self, data):
        data = data.replace(u'\xa9', u'').replace('\\u0022', '"').replace('\\u005C', '\\')  # gbk无法对u'\xa9'代表的字符进行编码，在Unicode中u'\xa9'代表的是©。因此直接忽略掉。
        data = re.compile("var info = '({.*?})'", re.S).findall(data)
        data = json.loads(data[0])
       # print(data['borrower'])
        result = {}
        # 顶部信息
        result['loanId'] = data['loan']['loanId'] # Number
        result['borrowType'] = data['loan']['borrowType'] # 贷款类型
        result['amount'] = data['loan']['amount'] #标的总额
        result['interest'] = data['loan']['interest'] # 年利率
        result['months'] = data['loan']['months'] # 还款期限
        result['creditLevel'] = data['borrower']['creditLevel']  # 风险等级
        result['repayType'] = '按季还款' if int(data['loan']['repayType']) else '按月还款' # 还款方式
        result['loanType'] = '等额本息' if data['loan']['loanType'] == 'DEBX' else '付息还本' #借贷方式
        result['repaySource'] = data['repaySource']  # 还款来源
        # 借贷人信息
        result['realName'] = data['borrower']['realName']  # 姓名
        result['gender'] = data['borrower']['gender'] # 性别
        result['age'] = 2019-int(data['borrower']['birthDay'][:4]) # 年龄
        result['marriage'] = '已婚' if data['borrower']['marriage'] else '未婚' # 婚姻
        result['graduation'] = data['borrower']['graduation']  # 学历
        result['salary'] = data['borrower']['salary'] # 收入
        result['houseLoan'] = '有' if data['borrower']['houseLoan'] else '无'  # 房贷
        result['carLoan'] = '有' if  data['borrower']['carLoan'] else '无' # 车贷
        result['officeDomain'] = data['borrower']['officeDomain'] # 公司行业
        result['hasOthDebt'] =data['hasOthDebt'] # 其他负债
        # 信用信息
        result['totalCount'] = data['userLoanRecord']['totalCount'] # 申请借款
        result['successCount'] = data['userLoanRecord']['successCount']  # 成功借款
        result['alreadyPayCount'] = data['userLoanRecord']['alreadyPayCount']   # 还清笔数
        result['availableCredits'] = data['borrower']['availableCredits']  #信用额度
        result['borrowAmount'] = data['userLoanRecord']['borrowAmount']  # 借款总额
        result['notPayTotalAmount'] = data['userLoanRecord']['notPayPrincipal']+data['userLoanRecord']['notPayInterest']  # 待还本息
        result['overdueTotalAmount'] = data['userLoanRecord']['overdueTotalAmount']   # 逾期金额
        result['overdueCount'] = data['userLoanRecord']['overdueCount']  # 逾期次数
        result['failedCount'] = data['userLoanRecord']['failedCount']  # 严重逾期
        self.save_excel(list(result.values()))


    # 存到excel
    def save_excel(self, data):
        out = open('./人人贷.csv', 'a', newline='')
        write = csv.writer(out, dialect='excel')
        write.writerow(data)


    def run(self):
        if os.path.exists('./人人贷.csv'):
            os.remove('./人人贷.csv')
        self.save_excel('序号 贷款类型 标的总额 年利率 还款期限 风险等级 还款方式 借贷方式 还款来源'
              ' 姓名 性别 年龄 婚姻 学历 收入 房贷 车贷 公司行业 其他负债'
              ' 申请借款 成功借款 还清笔数 信用额度 借款总额 待还本息 逾期金额 逾期次数 严重逾期'.split(' '))
        while True:
            self.get_sanbiao()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
