#!/usr/bin/env bash
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --master --no-web -c 500 -r 100 -t 20min --csv=p_Xtreme&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&
locust -H http://192.168.0.2:8000 -f Promiscuous_Xtreme.py --slave&