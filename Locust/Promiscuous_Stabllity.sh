#!/usr/bin/env bash
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --master --no-web -c 30 -r 30 -t 12h --csv=p_stability&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Load.py --slave&