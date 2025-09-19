import requests
import os
class lhc:
    def __init__(self):
        self.kj_list = self.get_kj_list()
        self.old_kj_list = self.get_old_kj_list()
        self.kh_kj_list = self.get_kh_kj_list()

    def get_kj_list(self):
        try:
            header = {'content-type':'application/json','referer':'https://history.macaumarksix.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.get('https://history.macaumarksix.com/history/macaujc2/y/2025',headers=header)
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==200:
                    kj_list = []
                    wave = {'green':'🟢','red':'🔴','blue':'🔵'}
                    for item in data.get('data'):
                        kj_list.append({
                            'qs':item.get('expect'),
                            'tm':item.get('openCode').split(',')[-1],
                            'sx':item.get('zodiac')[-1],
                            'pm':item.get('openCode').split(','),
                            'px':item.get('zodiac').split(','),
                            'wave':[wave.get(i) for i in item.get('wave').split(',')]
                        })
                    return kj_list
        except Exception as e:
            print(e)
    def get_old_kj_list(self):
        try:
            header = {'content-type':'application/json','referer':'https://history.macaumarksix.com/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.get('https://history.macaumarksix.com/history/macaujc/y/2025',headers=header)
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==200:
                    kj_list = []
                    wave = {'green':'🟢','red':'🔴','blue':'🔵'}
                    for item in data.get('data'):
                        kj_list.append({
                            'qs':item.get('expect'),
                            'tm':item.get('openCode').split(',')[-1],
                            'sx':item.get('zodiac')[-1],
                            'pm':item.get('openCode').split(','),
                            'px':item.get('zodiac').split(','),
                            'wave':[wave.get(i) for i in item.get('wave').split(',')]
                        })
                    return kj_list
        except Exception as e:
            print(e)
            
    #六合彩开奖
    def get_kh_kj_list(self):
        try:
            header = {'content-type':'application/json','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.get('https://api.macaumarksix.com/history/hkjc/y/2025',headers=header)
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==200:
                    kj_list = []
                    wave = {'green':'🟢','red':'🔴','blue':'🔵'}
                    for item in data.get('data'):
                        kj_list.append({
                            'qs':item.get('expect'),
                            'tm':item.get('openCode').split(',')[-1],
                            'sx':item.get('zodiac')[-1],
                            'pm':item.get('openCode').split(','),
                            'px':item.get('zodiac').split(','),
                            'wave':[wave.get(i) for i in item.get('wave').split(',')]
                        })
                    
                    return kj_list
        except Exception as e:
            print(e)
            
    def kj_show(self):
        kj_list = self.kj_list[0] 
        old_kj_list = self.old_kj_list[0]
        kj_kh_list  = self.kh_kj_list[0]
        msg = f'【新澳门开奖】({kj_list.get("qs")})\n'
        for i in range(len(kj_list.get('pm'))):
            msg +=f'[{kj_list.get("pm")[i]}]'
        msg +='\n'
        for i in range(len(kj_list.get('px'))):
            msg +=f'[{kj_list.get("px")[i]}]'
        msg +='\n'
        for i in range(len(kj_list.get('wave'))):
            msg +=f'{kj_list.get("wave")[i]} '
        msg +='\n\n'    
        
        msg += f'【老澳门开奖】({old_kj_list.get("qs")})\n'
        for i in range(len(old_kj_list.get('pm'))):
            msg +=f'[{old_kj_list.get("pm")[i]}]'
        msg +='\n'
        for i in range(len(old_kj_list.get('px'))):
            msg +=f'[{old_kj_list.get("px")[i]}]'
        msg +='\n'
        for i in range(len(old_kj_list.get('wave'))):
            msg +=f'{old_kj_list.get("wave")[i]} '
        msg +='\n\n'    
        
        msg += f'【香港开奖】({kj_kh_list.get("qs")})\n'
        for i in range(len(kj_kh_list.get('pm'))):
            msg +=f'[{kj_kh_list.get("pm")[i]}]'
        msg +='\n'
        for i in range(len(kj_kh_list.get('px'))):
            msg +=f'[{kj_kh_list.get("px")[i]}]'
        msg +='\n'
        for i in range(len(kj_kh_list.get('wave'))):
            msg +=f'{kj_kh_list.get("wave")[i]} '
        return msg +'\n'+'='*15 + '\n\n'
        
    #澳门三组
    def get_am3z_result(self):
        s3 = [['鼠','牛','雞','豬'],['龍','蛇','馬','羊'],['猴','狗','虎','兔']]
        kj_result = self.kj_list
        newqs = kj_result[0]
        msg = f'澳门三组 ({newqs.get("qs")})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if kj_result[i]['sx'] in item:
                    msg += f'{",".join(item)} 距离开奖期数:{i} { "✅" if i==0 else "❌"}\n'
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
                    msg += f'{zmane[index]} 距离开奖期数: {i} { "✅" if i==0 else "❌"}\n'
                    break
        return msg
    
    def get_am_6q_qs0_result(self):
        kh_result = self.kj_list
        last3_num_list = [] 
        new_kj_results_list = [] 
        next_number_list = []
        for i in kh_result:
            new_kj_results_list.append(i)
            if i.get('qs')[-1]=='0':
                
                pm = int(i.get('pm')[5])
                max_num = pm + 2 + 2
                min_num = pm + 2
                if max_num>49:
                    max_num = max_num - 49
                if min_num>49:
                    min_num = min_num - 49
                last3_num_list = [pm,min_num,max_num]
                if len(new_kj_results_list)==1:
                    next_number_list = last3_num_list
                    continue   
                break
        new_kj_results_list = new_kj_results_list[::-1]
        new_kj_results_list = new_kj_results_list[1:]
        for index,i in enumerate(new_kj_results_list):
            if int(i.get('tm')) in last3_num_list:
                msg = f'澳门期数0平码6({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n已开奖,期数:{index+1} ✅\n'
                return msg
        msg = f'澳门期数0平码6({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
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
                msg = f'澳门8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1} ✅\n'
                return msg
                break 
        msg = f'澳门8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
        return msg     
    #澳门9颗
    def get_am9_result(self):
        s9 = [1,12,10,21,23,32,34,43,45] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s9:
                msg = f'澳门9颗 ({newqs.get("qs")})\n{str(s9)}\n距离开奖期数: {i} { "✅" if i==0 else "❌"}\n'
                return msg
                break
    
    #澳门10颗
    def get_am10_result(self):
        s10 = [28,30,32,33,35,40,43,45,47,48] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s10:
                msg = f'澳门10颗 ({newqs.get("qs")})\n{str(s10)}\n距离开奖期数: {i} { "✅" if i==0 else "❌"}\n'
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
                msg = f'香港12颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1} ✅\n'
                return msg
                break  
        msg = f'香港12颗 ({newqs.get("qs")}){"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
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
                msg = f'香港8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n已开奖,期数: {i+1} ✅\n'
                return msg
                break 
        msg = f'香港8颗 ({newqs.get("qs")}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
        return msg 
    
    #香港期数3平码2
    def get_kh_2q_qs3_result(self):
        kh_result = self.kh_kj_list
        last3_num_list = [] 
        new_kj_results_list = [] 
        next_number_list = []
        for i in kh_result:
            new_kj_results_list.append(i)
            if i.get('qs')[-1]=='3':
                
                pm = int(i.get('pm')[1])
                max_num = pm + 3
                min_num = pm - 3
                if max_num>49:
                    max_num = max_num - 49
                if min_num<1:
                    min_num = 49 + min_num
                last3_num_list = [min_num,pm,max_num]
                if len(new_kj_results_list)==1:
                    next_number_list = last3_num_list
                    continue 
                break
        new_kj_results_list = new_kj_results_list[::-1]
        new_kj_results_list = new_kj_results_list[1:]
        for index,i in enumerate(new_kj_results_list):
            if int(i.get('tm')) in last3_num_list:
                msg = f'香港期数3平码2({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n已开奖,期数:{index+1} ✅\n'
                return msg
        msg = f'香港期数3平码2({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
        return msg
    
    #香港期数3特码
    def get_kh_tm_qs3_result(self):
        kh_result = self.kh_kj_list
        last3_num_list = [] 
        new_kj_results_list = [] 
        next_number_list =[]
        for i in kh_result:
            new_kj_results_list.append(i)
            if i.get('qs')[-1]=='3':
                pm = int(i.get('tm'))
                max_num = pm + 3
                min_num = pm - 3
                if max_num>49:
                    max_num = max_num - 49
                if min_num<1:
                    min_num = 49 + min_num
                last3_num_list = [min_num,pm,max_num]
                if len(new_kj_results_list)==1:
                    next_number_list = last3_num_list
                    continue 
                break
        new_kj_results_list = new_kj_results_list[::-1]
        new_kj_results_list = new_kj_results_list[1:]
        for index,i in enumerate(new_kj_results_list):
            if int(i.get('tm')) in last3_num_list:
                msg = f'香港期数3特码({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n已开奖,期数:{index+1} ✅\n'
                return msg
        msg = f'香港期数3特码({new_kj_results_list[-1].get("qs")})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
        return msg
    
    #老澳门三组
    def get_old_am3z_result(self):
        s3 = [['鼠','牛','雞','豬'],['龍','蛇','馬','羊'],['猴','狗','虎','兔']]
        kj_result = self.old_kj_list
        newqs = kj_result[0]
        msg = f'老澳门三组 ({newqs.get("qs")})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if kj_result[i]['sx'] in item:
                    msg += f'{",".join(item)} 距离开奖期数: {i} { "✅" if i==0 else "❌"}\n'
                    break
        return msg    
            
    
    def send_msg(self, msg): 
        bot = os.getenv("BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        r = requests.post(url=f'https://api.telegram.org/bot{bot}/sendMessage', json={'chat_id': chat_id, 'text': msg})
        
if __name__ == '__main__':
    print('start runing')
    lhc = lhc()
    results = lhc.kj_show()
    results += lhc.get_am3z_result() +'\n'
    results += lhc.get_amabcd_result() +'\n'
    results += lhc.get_am_6q_qs0_result() + '\n'
    results +=lhc.get_am8_result() +'\n'
    results +=lhc.get_am9_result() +'\n'
    results +=lhc.get_am10_result() +'\n'
    results +=lhc.get_kh_8_result() +'\n'
    results +=lhc.get_kh_12_result() +'\n'
    results += lhc.get_kh_2q_qs3_result() +'\n'
    results += lhc.get_kh_tm_qs3_result() + '\n'
    results += lhc.get_old_am3z_result() +'\n'
    lhc.send_msg(results)
    print('end run')

  