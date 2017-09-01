#!coding:utf-8
import copy
import time
import sys
import DihttpServletUtil
import json


class newInvestigation(object):
    def __init__(self,url,cookie):
        self.url=url
        self.cookie=cookie
        self.servlet=DihttpServletUtil.Servlet()
        self.starttime=(int(time.time())/518400)*518400
        print "starttime is ",self.starttime

        pass
    #bvt20
    def queryByUserName(self,username,contains=True):
        print  type(username)
        # if(type(username)!='str'):
        #     raise Exception(sys._getframe().f_code.co_name + "方法参数错误")
        date4deviceinfo='{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        diviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']

        date4logquery={"draw": 1,
              "columns":
                  [{"data": 'null',
                    "name": "",
                    "searchable": 'true',
                    "orderable": 'false',
                     "search": {"value": "",
                                "regex": 'false'}
                    },
                    {"data": "timestamp",
                     "name": "",
                     "searchable": 'true',
                     "orderable": 'false',
                     "search": {"value": "",
                                "regex": 'false'}
                     },
                    {"data": "deviceName",
                     "name": "",
                     "searchable": 'true', "orderable": 'false',
                     "search": {"value": "", "regex": 'false'}
                     },
                    {"data": "processUsername", "name": "", "searchable": 'true', "orderable": 'false',
                     "search": {"value": "", "regex": 'false'}
                     },
                    {"data": "rowlog",
                     "name": "",
                     "searchable": 'true',
                     "orderable": 'false',
                     "search": {"value": "", "regex": 'false'}
                     },
                    {"data": "processPath",
                     "name": "",
                     "searchable": 'true',
                     "orderable": 'false',
                     "search": {"value": "", "regex": 'false'}
                     },
                    {"data": "eventType",
                     "name": "",
                     "searchable": 'true',
                     "orderable": 'false',
                     "search": {"value": "", "regex": 'false'}
                     }
                   ],
              "order": [],
              "start": 0,
              "length": 50,
             "search": {"value": "", "regex": 'false'},
              "begin_time": "1504108800",
              "end_time": "1504163338",
             "taskid": "",
              "device_id": [diviceid],
              "timezone": 8,
              "sortedby": 0,
              "reversed": 0,
             "keyword": "",
              "filter_condition": {"process_user": {"include": [username]}
                                   }
              }
        date4logqueryExcule=copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"]={"process_user": {"exclude": [username]}}
        date4logquery=json.dumps(date4logquery)
        date4logqueryExcule=json.dumps(date4logqueryExcule)
        if(contains==True):
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            recordcount=json.loads(response.read())['recordsFiltered']
            print '通过包含用户名关键字"' + username + '"新建调查，返回', recordcount, '条记录'
            return recordcount
        elif(contains==False):
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            recordcount2=json.loads(response2.read())['recordsFiltered']
            print '通过不包含用户名关键字"' + username + '"新建调查，返回', recordcount2, '条记录'
            return  recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name+"方法参数错误")


    #bvt21
    def queryByTaskId(self,taskId,contians=True):
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        diviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']

        date4logquery = {"draw": 1,
                         "columns":
                             [{"data": 'null',
                               "name": "",
                               "searchable": 'true',
                               "orderable": 'false',
                               "search": {"value": "",
                                          "regex": 'false'}
                               },
                              {"data": "timestamp",
                               "name": "",
                               "searchable": 'true',
                               "orderable": 'false',
                               "search": {"value": "",
                                          "regex": 'false'}
                               },
                              {"data": "deviceName",
                               "name": "",
                               "searchable": 'true', "orderable": 'false',
                               "search": {"value": "", "regex": 'false'}
                               },
                              {"data": "processUsername", "name": "", "searchable": 'true', "orderable": 'false',
                               "search": {"value": "", "regex": 'false'}
                               },
                              {"data": "rowlog",
                               "name": "",
                               "searchable": 'true',
                               "orderable": 'false',
                               "search": {"value": "", "regex": 'false'}
                               },
                              {"data": "processPath",
                               "name": "",
                               "searchable": 'true',
                               "orderable": 'false',
                               "search": {"value": "", "regex": 'false'}
                               },
                              {"data": "eventType",
                               "name": "",
                               "searchable": 'true',
                               "orderable": 'false',
                               "search": {"value": "", "regex": 'false'}
                               }
                              ],
                         "order": [],
                         "start": 0,
                         "length": 50,
                         "search": {"value": "", "regex": 'false'},
                         "begin_time": "1504108800",
                         "end_time": "1504163338",
                         "taskid": "",
                         "device_id": [diviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"process_user": {"include": [username]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"process_user": {"exclude": [username]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            recordcount = json.loads(response.read())['recordsFiltered']
            print '通过包含用户名关键字"' + username + '"新建调查，返回', recordcount, '条记录'
            return recordcount
        elif (contains == False):
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            recordcount2 = json.loads(response2.read())['recordsFiltered']
            print '通过不包含用户名关键字"' + username + '"新建调查，返回', recordcount2, '条记录'
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

        pass


    #bvt22
    def queryByTaskName(self,taskName):
        pass
    #bvt23
    def queryByFileName(self, fileName):
        pass
    #bvt24
    def queryByUrl(self, url):
        pass
    #bvt25
    def queryBySourceIp(self, sourceIP):
        pass
    #bvt26
    def queryByToIP(self, toIp):
        pass