#!/usr/bin/env bash
ps -ef | grep locust | grep -v grep | awk '{print $2}' | xargs kill -9