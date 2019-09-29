#!/bin/bash

alias dc="docker-compose"
alias run_basic="docker-compose up -d esa kibana"
alias dev_log="docker-compose run --rm logstash logstash"
alias make_certs="docker-compose -f cert-control.yml run --rm create_certs"
alias clean_up="sudo rm -rf local_certs/"
