#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:49:47 2017

@author: rotemgura

This script detects an AWS instance and saves its IP to .bash_aws_alias, which is sourced by .bashrc
"""
import sys
import json

instance_name = sys.argv[1]
jsonstr = sys.stdin.read()
d = json.loads(jsonstr)

for instance in d['Reservations']:
    for tag in instance['Instances'][0]['Tags']:
        if tag['Key'] == 'Name':
            if tag['Value'] == instance_name:
                    dns = instance['Instances'][0]['PublicDnsName']
print(dns)
with open('/Users/rotemgura/.bash_aws_alias','w') as f:
    f.write('dns=' + dns)
                    