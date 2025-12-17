import requests
import os
import time
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
            kj_list = []
            sx = {'鼠':'鼠','牛':'牛','虎':'虎','兔':'兔','龙':'龍','蛇':'蛇','马':'馬','羊':'羊','猴':'猴','鸡':'雞','狗':'狗','猪':'豬'}
            age_zodiac_map_2025 = {
                "01": "蛇", "02": "龙", "03": "兔", "04": "虎", "05": "牛", "06": "鼠", "07": "猪", "08": "狗", "09": "鸡",
                "10": "猴", "11": "羊", "12": "马", "13": "蛇", "14": "龙", "15": "兔", "16": "虎", "17": "牛",
                "18": "鼠", "19": "猪", "20": "狗", "21": "鸡", "22": "猴", "23": "羊", "24": "马", "25": "蛇",
                "26": "龙", "27": "兔", "28": "虎", "29": "牛", "30": "鼠", "31": "猪", "32": "狗", "33": "鸡",
                "34": "猴", "35": "羊", "36": "马", "37": "蛇", "38": "龙", "39": "兔", "40": "虎", "41": "牛",
                "42": "鼠", "43": "猪", "44": "狗", "45": "鸡", "46": "猴", "47": "羊", "48": "马", "49": "蛇"
            }
            header = {'content-type':'application/json','referer':'https://zhibo.77kj.vip/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
            r = requests.post(f'https://zhibo.77kj.vip/tools/submit_ajax.ashx?action=getkjrecords&code=48am',headers=header)#http://api.bjjfnet.com/data/opencode/2032
            if r.status_code == 200:
                data = r.json()
                if data.get('code')==1:
                    wave = {'green':'🟢','red':'🔴','blue':'🔵'}
                    wave_list_dict = {'red':[1,2,7,8,12,13,18,19,23,24,29,30,34,35,40,45,46],'blue':[3,4,9,10,14,15,20,25,26,31,36,37,41,42,47,48],'green':[5,6,11,16,17,21,22,27,28,32,33,38,39,43,44,49]}
                    for item in data.get('data'):
                        temp_dict ={
                            'qs':item.get('qishu'),
                            'tm':item.get('num').split(',')[-1],
                            'sx':item.get('shengxiao')[-1],
                            'pm':item.get('num').split(','),
                            'px':item.get('shengxiao').split(','),    
                            
                        }
                        temp_list = []
                        
                        for number in item.get('num').split(','):
                            for key,val in wave_list_dict.items():
                                if int(number) in val:  
                                    temp_list.append(wave.get(key))
                        temp_dict['wave'] = temp_list
                        kj_list.append(temp_dict)
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
        msg = f'【<b>新澳门开奖</b>】({self.make_url(kj_list.get("qs"),0)})\n'
        for i in range(len(kj_list.get('pm'))):
            msg +=f'[{kj_list.get("pm")[i]}]'
        msg +='\n'
        for i in range(len(kj_list.get('px'))):
            msg +=f'[{kj_list.get("px")[i]}]'
        msg +='\n'
        for i in range(len(kj_list.get('wave'))):
            msg +=f'{kj_list.get("wave")[i]} '
        msg +='\n\n'    
        
        msg += f'【<b>老澳门开奖</b>】({self.make_url(old_kj_list.get("qs"),1)})\n'
        for i in range(len(old_kj_list.get('pm'))):
            msg +=f'[{old_kj_list.get("pm")[i]}]'
        msg +='\n'
        for i in range(len(old_kj_list.get('px'))):
            msg +=f'[{old_kj_list.get("px")[i]}]'
        msg +='\n'
        for i in range(len(old_kj_list.get('wave'))):
            msg +=f'{old_kj_list.get("wave")[i]} '
        msg +='\n\n'    
        
        msg += f'【<b>香港开奖</b>】({self.make_url(kj_kh_list.get("qs"),2)})\n'
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
        msg = f'<b>澳门三组</b> ({self.make_url(newqs.get("qs"),0)})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if kj_result[i]['sx'] in item:
                    msg += f'<s>{",".join(item)} 距上次开奖期数:{i} { "✅" if i==0 else "❌"}</s>\n' if i==0 else f'{",".join(item)} 距上次开奖期数:{i} { "✅" if i==0 else "❌"}\n'
                    break
        return msg
        
    #澳门ABCD           
    def get_amabcd_result(self):
        s3 = [[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36],[37,38,39,40,41,42,43,44,45,46,47,48,49]]
        kj_result = self.kj_list
        newqs = kj_result[0]
        zmane = ['A组1-12','B组13-24','C组25-36','D组37-49']
        msg = f'<b>澳门ABCD</b> ({self.make_url(newqs.get("qs"),0)})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if int(kj_result[i]['tm']) in item:
                    msg += f'<s>{zmane[index]} 距上次开奖期数: {i} { "✅" if i==0 else "❌"}</s>\n' if i==0 else f'{zmane[index]} 距上次开奖期数: {i} { "✅" if i==0 else "❌"}\n'
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
                msg = f'<b>澳门期数0平码6</b>({self.make_url(new_kj_results_list[-1].get("qs"),0)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n<s>已开奖,期数:{index+1} ✅</s>\n'
                return msg
        msg = f'<b>澳门期数0平码6</b>({self.make_url(new_kj_results_list[-1].get("qs"),0)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
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
                msg = f'<b>澳门8颗</b> ({self.make_url(newqs.get("qs"),0)}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n<s>已开奖,期数: {i+1} ✅</s>\n'
                return msg
                break 
        msg = f'<b>澳门8颗</b> ({self.make_url(newqs.get("qs"),0)}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
        return msg     
    #澳门9颗
    def get_am9_result(self):
        s9 = [1,12,10,21,23,32,34,43,45] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s9:
                msg = f'<b>澳门9颗</b> ({self.make_url(newqs.get("qs"),0)})\n{str(s9)}\n{f"<s>距上次开奖期数: {i} ✅</s>" if i==0 else f"距上次开奖期数: {i} ❌"}\n'
                return msg
                
    
    #澳门10颗
    def get_am10_result(self):
        s10 = [28,30,32,33,35,40,43,45,47,48] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s10:
                msg = f'<b>澳门10颗</b> ({self.make_url(newqs.get("qs"),0)})\n{str(s10)}\n{f"<s>距上次开奖期数: {i} ✅</s>" if i==0 else f"距上次开奖期数: {i} ❌"}\n'
                return msg
                
            
    #澳门17粒
    def get_am17_result(self):
        s17 = [1,2,3,4,5,6,43,44,45,46,47,48,49,10,20,30,40] 
        kj_result = self.kj_list
        newqs = kj_result[0]
        for i in range(0,100):
            if int(kj_result[i]['tm']) in s17:
                msg = f'<b>澳门17粒</b> ({self.make_url(newqs.get("qs"),0)})\n{str(s17)}\n{f"<s>距上次开奖期数: {i} ✅</s>" if i==0 else f"距上次开奖期数: {i} ❌"}\n'
                return msg
                
                
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
                msg = f'<b>香港12颗</b> ({self.make_url(newqs.get("qs"),2)}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n<s>已开奖,期数: {i+1} ✅</s>\n'
                return msg
                break  
        msg = f'<b>香港12颗</b> ({self.make_url(newqs.get("qs"),2)}){"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
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
                msg = f'<b>香港8颗</b> ({self.make_url(newqs.get("qs"),2)}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n<s>已开奖,期数: {i+1} ✅</s>\n'
                return msg
                break 
        msg = f'<b>香港8颗</b> ({self.make_url(newqs.get("qs"),2)}) {"1-5期" if qs_index in [1,2,3,4,5] else "6-10期"}\n{str(kh12)}\n未开奖期数: {qs_list[qs_index]} ❌\n'
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
                msg = f'<b>香港期数3平码2</b>({self.make_url(new_kj_results_list[-1].get("qs"),2)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n<s>已开奖,期数:{index+1} ✅</s>\n'
                return msg
        msg = f'<b>香港期数3平码2</b>({self.make_url(new_kj_results_list[-1].get("qs"),2)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
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
                msg = f'<b>香港期数3特码</b>({self.make_url(new_kj_results_list[-1].get("qs"),2)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n<s>已开奖,期数:{index+1} ✅</s>\n'
                return msg
        msg = f'<b>香港期数3特码</b>({self.make_url(new_kj_results_list[-1].get("qs"),2)})\n下期号码:{str(next_number_list) if len(next_number_list)>0 else str(last3_num_list)}\n本期号码:{str(last3_num_list)}\n未开奖期数:{len(new_kj_results_list)} ❌\n'
        return msg
    
    #老澳门三组
    def get_old_am3z_result(self):
        s3 = [['鼠','牛','雞','豬'],['龍','蛇','馬','羊'],['猴','狗','虎','兔']]
        kj_result = self.old_kj_list
        newqs = kj_result[0]
        msg = f'<b>老澳门三组</b> ({self.make_url(newqs.get("qs"),1)})\n'
        for index,item in enumerate(s3): 
            for i in range(0,40):
                if kj_result[i]['sx'] in item:
                    msg += f'<s>{",".join(item)} 距上次开奖期数: {i} { "✅" if i==0 else "❌"}</s>\n' if i==0 else f'{",".join(item)} 距上次开奖期数: {i} { "✅" if i==0 else "❌"}\n'
                    break
        return msg    
            
    
    def send_msg(self, msg): 
        bot = os.getenv("BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        r = requests.post(url=f'https://api.telegram.org/bot{bot}/sendMessage', json={'chat_id': chat_id, 'text': msg,'parse_mode': 'html','disable_web_page_preview': True})
        
    def make_url(self,qs,type_name=None):
        if type_name==1:
            link = f'https://video2m6-qq.dldydn.com/lottery/video/2025/2032/{qs}.mp4'
        elif type_name==0:
            link = f'https://macaujc.com/video2/{qs}.mp4'
        elif type_name==2:
            link = f'https://135ka.com/index.php/index/lhc.html?t=gl'
        return f'<a href="{link}">{qs}</a>'
   

        
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
    results += lhc.get_am17_result() + '\n'
    results +=lhc.get_kh_8_result() +'\n'
    results +=lhc.get_kh_12_result() +'\n'
    results += lhc.get_kh_2q_qs3_result() +'\n'
    results += lhc.get_kh_tm_qs3_result() + '\n'
    results += lhc.get_old_am3z_result() +'\n'
    #print(results)
    lhc.send_msg(results)
    print('end run')

  