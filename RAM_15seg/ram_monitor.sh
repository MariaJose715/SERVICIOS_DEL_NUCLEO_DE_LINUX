#!/bin/bash

while true
do
    echo "Fecha: $(date)" >> /tmp/ram_usage.log
    free -h >> /tmp/ram_usage.log
    echo "-----------------------------" >> /tmp/ram_usage.log
    sleep 15
done
