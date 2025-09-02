import requests
import os
class lhc:
    def __init__(self):
        self.kj_list = self.get_kj_list()
        self.kh_kj_list = self.get_kh_kj_list()

    def get_kj_list(self):
        try:
            header = {'content-type':'application/json','referer':'https://history.macaumarksix.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.get('https://history.macaumarksix.com/history/macaujc2/y/2025',headers=header)
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==200:
                    kj_list = []
                    for item in data.get('data'):
                        kj_list.append({
                            'qs':item.get('expect'),
                            'tm':item.get('openCode').split(',')[-1],
                            'sx':item.get('zodiac')[-1]
                        })
                    return kj_list
        except Exception as e:
            print(e)
            
    #六合彩开奖
    def get_kh_kj_list(self):
        try:
            header = {'content-type':'application/x-www-form-urlencoded','referer':'https://www.1234kj.tv/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.post('https://www.1234kj.tv/api/HistoryOpenInfo',headers=header,data={'lotteryId':2034,'issueNum':2025})
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==0:
                    kj_list = []
                    for item in data.get('data'):
                        kj_list.append({
                            'qs':item.get('issue'),
                            'tm':item.get('openCode').split(',')[-1]
                        })
                    
                    return kj_list
        except Exception as e:
            print(e)
            
    #澳门三组
    def get_am3z_result(self):
        s3 = [['鼠','牛','雞','豬'],['龍','蛇','馬','羊'],['猴','狗','虎','兔']]
        kj_result = self.kj_list
        newqs = kj_result[0]
        msg = f'澳门三组 ({newqs.get("qs")})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if kj_result[i]['sx'] in item:
                    msg += f'{",".join(item)} 未开奖期数: {i}\n'
                    break
        return msg
        
    #澳门ABCD           
    def get_amabcd_result(self):
        s3 = [[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36],[37,38,39,40,41,42,43,44,45,46,47,48,49]]
        kj_result = self.kj_list
        newqs = kj_result[0]
        zmane = ['A组1-12','B组13-24','C组25-36','D组37-49']
        msg = f'澳门ABCD ({newqs.get("qs")})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if int(kj_result[i]['tm']) in item:
                    msg += f'{zmane[index]} 未开奖期数: {i}\n'
                    break
        return msg
    #澳门8颗
    def get_am8_result(self):
        kh_result = self.kj_list
        kh12 = [2,9,13,23,25,38,44,45]
        newqs = kh_result[0]
        qs_index = int(str(newqs.get('qs'))[-1])
        qs_list = [5,1,2,3,4,5,1,2,3,4]
        kh_result = kh_result[0:qs_list[qs_index]]
        kh_result = kh_result[::-1]
        for i in range(0,qs_list[qs_index]):
            if int(kh_result[i]['tm']) in kh12:
                msg = f'澳门8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1}\n'
                return msg
                break 
        msg = f'澳门8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]}\n'
        return msg     
    #澳门9颗
    def get_am9_result(self):
        s9 = [1,12,10,21,23,32,34,43,45] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s9:
                msg = f'澳门9颗 ({newqs.get("qs")})\n{str(s9)}\n未开奖期数: {i}\n'
                return msg
                break
    
    #澳门10颗
    def get_am10_result(self):
        s10 = [28,30,32,33,35,40,43,45,47,48] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s10:
                msg = f'澳门10颗 ({newqs.get("qs")})\n{str(s10)}\n未开奖期数: {i}\n'
                return msg
                break
    
    #香港12颗
    def get_kh_12_result(self):
        kh_result = self.kh_kj_list
        kh12 = [1,2,3,4,5,6,7,8,9,10,11,12]
        newqs = kh_result[0]
        qs_index = int(str(newqs.get('qs'))[-1])
        qs_list = [5,1,2,3,4,5,1,2,3,4]
        kh_result = kh_result[0:qs_list[qs_index]]
        kh_result = kh_result[::-1]
        for i in range(0,qs_list[qs_index]):
            if int(kh_result[i]['tm']) in kh12:
                msg = f'香港12颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1}\n'
                return msg
                break  
        msg = f'香港12颗 ({newqs.get("qs")}){"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]}\n'
        return msg  
    
    #香港8颗
    def get_kh_8_result(self):
        kh_result = self.kh_kj_list
        kh12 = [2,9,13,23,25,38,44,45]
        newqs = kh_result[0]
        qs_index = int(str(newqs.get('qs'))[-1])
        qs_list = [5,1,2,3,4,5,1,2,3,4]
        kh_result = kh_result[0:qs_list[qs_index]]
        kh_result = kh_result[::-1]
        for i in range(0,qs_list[qs_index]):
            if int(kh_result[i]['tm']) in kh12:
                msg = f'香港8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1}\n'
                return msg
                break 
        msg = f'香港8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]}\n'
        return msg 
    
    def send_msg(self, msg): 
        bot = os.getenv("BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        super_chat_id = os.getenv("TELEGRAM_SUPER_CHAT_ID")
        r = requests.post(url=f'https://api.telegram.org/bot{bot}/sendMessage', json={'chat_id': chat_id, 'text': msg})
        
if __name__ == '__main__':
    print('start runing')
    lhc = lhc()
    results = lhc.get_am3z_result() +'\n'
    results += lhc.get_amabcd_result() +'\n'
    results +=lhc.get_am8_result() +'\n'
    results +=lhc.get_am9_result() +'\n'
    results +=lhc.get_am10_result() +'\n'
    results +=lhc.get_kh_8_result() +'\n'
    results +=lhc.get_kh_12_result()
    lhc.send_msg(results)


  

