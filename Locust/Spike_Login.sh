#!/usr/bin/env bash
locust -H http://192.168.0.2:8000 -f Spike_Login.py --master& #--no-web -c 200 -r 200 -t 5min --csv=spike_login&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&
locust -H http://192.168.0.2:8000 -f Spike_Login.py --slave&