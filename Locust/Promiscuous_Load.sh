#!/usr/bin/env bash
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --master --no-web -c 200 -r 50 -t 20min --csv=p_load.csv&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&