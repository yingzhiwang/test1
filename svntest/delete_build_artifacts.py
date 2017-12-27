# coding=utf-8

# 执行命令python delete_artifacts.py razzil_endpoint start_time end_time user_token bucket_name
# razzil_endpoint是razzil组件的访问地址
# start_time是查询的起始时间，格式为2017-11-11
# end_time是查询的结束时间，格式为2017-11-11
# user_token是用户的token
# bucket_name是minio的储存桶，一般填写为根账户名称

import requests
import json
import time
from sys import argv

razzil_endpoint = argv[1]
start_time = argv[2]
end_time = argv[3]
user_token = argv[4]
bucket_name = argv[5]

query_param = {
    "start_time" : time.mktime(time.strptime(start_time, "%Y-%m-%d")),
    "end_time" : time.mktime(time.strptime(end_time, "%Y-%m-%d")),
    "user_token" : user_token,
    "bucket_name" : bucket_name
}

get_url = razzil_endpoint + '/v1/private_builds/artifacts'

def delete_artifacts():
    r = requests.get(get_url, params=query_param)
    for result in json.loads(r.text):
        build_id = result['build_id']
        delete_url = razzil_endpoint + '/v1/private_builds/' + build_id + '/artifacts'
        r = requests.delete(delete_url)
        if r.status_code == 204:
            print build_id + 'deleted successfully...'
        else:
            print build_id + 'deleted failed...'


if __name__ == '__main__':
    delete_artifacts()