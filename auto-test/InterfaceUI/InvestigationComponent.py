#!coding:utf-8
import copy
import time
import sys
import DihttpServletUtil
import json
import ParamsUtil
import DiErrorUtil


class InvestigationComponent(object):
    def __init__(self, url, cookie):
        self.url = url
        self.cookie = cookie
        self.servlet = DihttpServletUtil.Servlet()
        self.taskid = ''

    # bvt20
    def queryByUserName(self, username, contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(username) == False):
            raise DiErrorUtil.ParamsError(methodName, 'username')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']

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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
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
            print "= = = = = = =开始包含用户名关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 用户名 关键字"' + username + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含用户名关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 用户名 关键字"' + username + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise DiErrorUtil.ParamsError(methodName, 'contains')

    # bvt21
    def queryByTaskId(self, taskId, contains=True):
        starttime = int(int(time.time())/86400) * 86400-8*3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isAId(taskId) == False):
            raise DiErrorUtil.ParamsError(methodName, 'taskId')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"pid": {"include": [taskId]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"pid": {"exclude": [taskId]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始进程ID关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 进程id 关键字"' + taskId + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含进程ID关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 进程id 关键字"' + taskId + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    # bvt22
    def queryByProcessName(self, processName,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(processName) == False):
            raise DiErrorUtil.ParamsError(methodName, 'processName')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"process_name": {"include": [processName]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"process_name": {"exclude": [processName]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始进程名关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 进程名 关键字"' + processName + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']

            print "= = = = = = =开始不包含进程名关键字新建调查= = = = = = ="
            print '通过不包含 进程名 关键字"' + processName + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    # bvt23
    def queryByFileName(self, fileName,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(fileName) == False):
            raise DiErrorUtil.ParamsError(methodName, 'filename')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"file_name": {"include": [fileName]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"file_name": {"exclude": [fileName]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始文件名关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 文件名 关键字"' + fileName + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print "= = = = = = =开始不包含文件名关键字新建调查= = = = = = ="
            print '通过不包含 文件名 关键字"' + fileName + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    # bvt24
    def queryByUrl(self, url,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(url) == False):
            raise DiErrorUtil.ParamsError(methodName, 'URL')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"http_url": {"include": [url]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"http_url": {"exclude": [url]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始URL关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 URL 关键字"' + url + '"新建调查，返回', recordcount, '条记录。'
            print "查询时间范围为",time.strftime('%m-%d %H:%M:%S',time.localtime(starttime)),"至",time.strftime('%m-%d %H:%M:%S',time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含URL关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 URL 关键字"' + url + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime('%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    # bvt25
    def queryBySourceIp(self, sourceIP=None,sourcePort=None,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (sourceIP!=None and (ParamsUtil.isAIp(sourceIP) == False)):
            raise DiErrorUtil.ParamsError(methodName, 'sourceIP')
        if (sourcePort!=None and (ParamsUtil.isAPort(sourcePort) == False)):
            raise DiErrorUtil.ParamsError(methodName, 'sourcePort')
        if(sourceIP==None and sourcePort == None):
            raise  DiErrorUtil.ParamsError(methodName=methodName,msg='源ip和源端口不能同时为空')
        if(sourceIP==None):
            sourceIP=''
        if (sourcePort == None):
            sourcePort = ''
        sourceIPDecimal=ParamsUtil.ipToDecimal(sourceIP)
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"src_ip": {"include": [sourceIPDecimal]},"src_port":{"include":[sourcePort]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"http_url": {"exclude": [sourceIPDecimal]},"src_port":{"exclude":[sourcePort]}
                                              }
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始源IP及源端口关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 源IP"' + str(sourceIP) + '"以及 源端口 "'+sourcePort +'"关键字新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含源IP及源端口关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 源IP"' + str(sourceIP) + '"以及 源端口 "' + sourcePort + '"关键字新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    # bvt26
    def queryByDestIP(self, desIp=None,desPort=None,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (desIp!=None and (ParamsUtil.isAIp(desIp) == False)):
            raise DiErrorUtil.ParamsError(methodName, 'desIp')
        if (desPort!=None and (ParamsUtil.isAPort(desPort) == False)):
            raise DiErrorUtil.ParamsError(methodName, 'desPort')
        if(desIp==None and desPort == None):
            raise  DiErrorUtil.ParamsError(methodName=methodName,msg='目标ip和目标端口不能同时为空')
        if(desIp==None):
            desIp=''
        if (desPort == None):
            desPort = ''
        desIPDecimal = ParamsUtil.ipToDecimal(desIp)
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"dst_ip": {"include": [desIPDecimal],"dst_port": {"include": [desPort]}}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"dst_ip": {"exclude": [desIPDecimal]},
                                                   "dst_port": {"exclude": [desPort]}
                                                   }
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始包含目标IP及目标端口关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 目标IP"' + str(desIp) + '"以及 目标端口 "' + str(desPort) + '"关键字新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含目标IP及目标端口关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 目标IP"' + str(desIp) + '"以及 目标IP "' + str(desPort) + '"关键字新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    def queryByRegistryKey(self,registryKey,contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(registryKey) == False):
            raise DiErrorUtil.ParamsError(methodName, 'registryKey')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"registry_key": {"include": [registryKey]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"registry_key": {"exclude": [registryKey]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始包含注册表项关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 注册表项 关键字"' + registryKey + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含注册表项关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule, cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 注册表项 关键字"' + registryKey + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    def queryByRegistryValue(self, registryValue, contains=True):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(registryValue) == False):
            raise DiErrorUtil.ParamsError(methodName, 'registryValue')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {"registry_value": {"include": [registryValue]}
                                              }
                         }
        date4logqueryExcule = copy.deepcopy(date4logquery)
        date4logqueryExcule["filter_condition"] = {"registry_value": {"exclude": [registryValue]}}
        date4logquery = json.dumps(date4logquery)
        date4logqueryExcule = json.dumps(date4logqueryExcule)
        if (contains == True):
            print "= = = = = = =开始包含注册表值关键字新建调查= = = = = = ="
            response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
            result = json.loads(response.read())
            recordcount = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过包含 注册表值 关键字"' + registryValue + '"新建调查，返回', recordcount, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount
        elif (contains == False):
            print "= = = = = = =开始不包含注册表值关键字新建调查= = = = = = ="
            response2 = self.servlet.doPost(url=self.url + '/logquery', data=date4logqueryExcule,
                                            cookie=self.cookie)
            result = json.loads(response2.read())
            recordcount2 = result['recordsFiltered']
            self.taskid = result['tid']
            print '通过不包含 注册表值 关键字"' + registryValue + '"新建调查，返回', recordcount2, '条记录'
            print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
                '%m-%d %H:%M:%S', time.localtime(endtime))
            print "= = = = = = =调查成功返回= = = = = = ="
            return recordcount2
        else:
            raise Exception(sys._getframe().f_code.co_name + "方法参数错误")

    def queryByDefault(self):
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
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
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": "",
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": "",
                         "filter_condition": {}
                         }
        date4logquery = json.dumps(date4logquery)
        print "= = = = = = =开始默认条件新建调查= = = = = = ="
        response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
        result = json.loads(response.read())
        recordcount = result['recordsFiltered']
        self.taskid = result['tid']
        print '通过 默认条件 新建调查，返回', recordcount, '条记录'
        print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
            '%m-%d %H:%M:%S', time.localtime(endtime))
        print "= = = = = = =调查成功返回= = = = = = ="
        return recordcount

    def queryByDefaultAndSort(self, sortColumn='1', asc=True):
        self.queryByDefault()
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        sortFlag=0
        sortString='升序'
        columnString=['时间戳','探针名','进程用户名','进程ID','进程名','事件类型']
        if(asc==False):
            sortFlag = 1
            sortString = '降序'
        if (ParamsUtil.isAId(sortColumn) == False):
            raise DiErrorUtil.ParamsError(methodName, 'sortColumn')
        if(int(sortColumn)<1 or int(sortColumn)>6):
            raise DiErrorUtil.ParamsError(methodName, 'sortColumn')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
        date4logquery = {"draw":1,
                         "columns":[
                             {"data":'null',"name":"",
                              "searchable":'true',"orderable":'false',"search":
                                  {"value":"","regex":'false'}},
                             {"data":"timestamp","name":"","searchable":'true',"orderable":'false',"search":
                                 {"value":"","regex":'false'}},
                             {"data":"deviceName","name":"","searchable":'true',"orderable":'false',"search":
                                 {"value":"","regex":'false'}},
                             {"data":"processUsername","name":"","searchable":'true',"orderable":'false',"search":
                                 {"value":"","regex":'false'}},
                             {"data":"rowlog","name":"","searchable":'true',"orderable":'false',"search":
                                 {"value":"","regex":'false'}},
                             {"data":"processPath","name":"","searchable":'true',"orderable":'false',"search":
                                 {"value":"","regex":'false'}},
                             {"data":"eventType","name":"","searchable":'true',"orderable":'false',"search":{"value":"","regex":'false'}}],
                         "order":[],
                         "start":0,
                         "length":50,
                         "search":{"value":"","regex":'false'},
                         "begin_time":starttime,
                         "end_time":endtime,
                         "taskid":self.taskid,
                         "device_id":[deviceid],
                         "timezone":8,
                         "sortedby":sortColumn,
                         "reversed":sortFlag,
                         "keyword":"",
                         "filter_condition":{
                             
                         }}
        date4logquery = json.dumps(date4logquery)
        print "= = = = = = =开始按照默认条件新建调查，并按照列",columnString[int(sortColumn)-1],"进行",sortString,"排列= = = = = = ="
        response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
        result = json.loads(response.read())
        recordcount = result['recordsFiltered']
        self.taskid = result['tid']
        print '排序请求成功返回，返回的数据条数为',recordcount,'条'
        print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
            '%m-%d %H:%M:%S', time.localtime(endtime))
        print "= = = = = = =接口成功返回= = = = = = ="
        return recordcount

    def queryByDefaultAndFilter(self, filterName, filterValue):
        self.queryByDefault()
        starttime = int(int(time.time()) / 86400) * 86400 - 8 * 3600
        endtime = int(time.time())
        methodName = sys._getframe().f_code.co_name
        if (ParamsUtil.isString(filterName) == False):
            raise DiErrorUtil.ParamsError(methodName, 'filterName')
        if (ParamsUtil.isString(filterValue) == False):
            raise DiErrorUtil.ParamsError(methodName, 'filterValue')
        date4deviceinfo = '{"infotype":"1"}'
        response = self.servlet.doPost(url=self.url + '/deviceinfo', data=date4deviceinfo, cookie=self.cookie)
        deviceid = json.loads(json.loads(json.dumps(response.read())))['data'][0]['devices'][0]['deviceid']
        date4logquery = {"draw": 1,
                         "columns": [
                             {"data": 'null', "name": "",
                              "searchable": 'true', "orderable": 'false', "search":
                                  {"value": "", "regex": 'false'}},
                             {"data": "timestamp", "name": "", "searchable": 'true', "orderable": 'false', "search":
                                 {"value": "", "regex": 'false'}},
                             {"data": "deviceName", "name": "", "searchable": 'true', "orderable": 'false', "search":
                                 {"value": "", "regex": 'false'}},
                             {"data": "processUsername", "name": "", "searchable": 'true', "orderable": 'false',
                              "search":
                                  {"value": "", "regex": 'false'}},
                             {"data": "rowlog", "name": "", "searchable": 'true', "orderable": 'false', "search":
                                 {"value": "", "regex": 'false'}},
                             {"data": "processPath", "name": "", "searchable": 'true', "orderable": 'false', "search":
                                 {"value": "", "regex": 'false'}},
                             {"data": "eventType", "name": "", "searchable": 'true', "orderable": 'false',
                              "search": {"value": "", "regex": 'false'}}],
                         "order": [],
                         "start": 0,
                         "length": 50,
                         "search": {"value": "", "regex": 'false'},
                         "begin_time": starttime,
                         "end_time": endtime,
                         "taskid": self.taskid,
                         "device_id": [deviceid],
                         "timezone": 8,
                         "sortedby": 0,
                         "reversed": 0,
                         "keyword": {filterName:filterValue},
                         "filter_condition": {

                         }}
        date4logquery = json.dumps(date4logquery)
        print "= = = = = = =开始按照默认条件新建调查，并按照", filterName, "包含",filterValue,"进行过滤= = = = = = ="
        response = self.servlet.doPost(url=self.url + '/logquery', data=date4logquery, cookie=self.cookie)
        result = json.loads(response.read())
        recordcount = result['recordsFiltered']
        self.taskid = result['tid']
        print '过滤请求成功返回，返回的数据条数为', recordcount, '条'
        print "查询时间范围为", time.strftime('%m-%d %H:%M:%S', time.localtime(starttime)), "至", time.strftime(
            '%m-%d %H:%M:%S', time.localtime(endtime))
        print "= = = = = = =接口成功返回= = = = = = ="
        return recordcount

