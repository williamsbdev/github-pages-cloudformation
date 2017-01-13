#!/usr/bin/python

import json
import urllib2

response = urllib2.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json')

ip_ranges_json = json.loads(response.read())

prefixes = ip_ranges_json['prefixes']

cloudfront_ips = [item['ip_prefix'] for item in prefixes if item['service'] == 'CLOUDFRONT']

with open("cloudfront-ip-ranges.json", "w") as f:
    for index, cidr in enumerate(cloudfront_ips):
        f.write('"{}"'.format(cidr))
        if index != len(cloudfront_ips) - 1:
            f.write(',')
            f.write('\n')
