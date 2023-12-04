#!/bin/bash

LOG_DIR="/home/ubuntu/hadoop-3.3.6/logs/userlogs"
TOTAL=0

for app in $LOG_DIR/application_*; do
    for container in "$app"/container_*; do
        if [ -f "$container/syslog" ]; then

            CPU_TIME=$(grep "CPU time spent (ms)=" "$container/syslog")
            
            TIME=$(echo $CPU_TIME | awk -F'=' '{print $2}')

            # Check if TIME is empty
            if [ -n "$TIME" ]; then
                TOTAL=$(($TOTAL + $TIME))
            fi
            
        fi

    done
done

echo "Total CPU time: $TOTAL ms"
echo "$TOTAL" > total_time.txt
