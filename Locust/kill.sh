#!/usr/bin/env bash
ps -ax | grep locust | cut -d ' ' -f 2 | xargs kill -9