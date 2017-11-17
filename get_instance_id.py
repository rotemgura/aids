#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:01:13 2017

@author: rotemgura
"""

import sys
import json

instance_name = sys.argv[1]
jsonstr = sys.stdin.read()
d = json.loads(jsonstr)

for instance in d['Reservations']:
    if 'Tags' in instance['Instances'][0]:
        for tag in instance['Instances'][0]['Tags']:
            if tag['Key'] == 'Name':
                if tag['Value'] == instance_name:
                    print(instance['Instances'][0]['InstanceId'])
