#!/bin/bash

#copy init_centroids.txt to centroids.txt
cp /home/ubuntu/k_mean/datagen/init_centroids.txt /home/ubuntu/k_mean/parallel_hdfs/centroids.txt

i=1
CUCUMLATIVE=0
while :
do
	START_TIME=$(date +%s.%N)
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -D mapreduce.job.counters.counter.CPU_MILLISECONDS=true -file /home/ubuntu/k_mean/parallel_hdfs/centroids.txt -file /home/ubuntu/k_mean/parallel_hdfs/mapper.py -mapper /home/ubuntu/k_mean/parallel_hdfs/mapper.py -file /home/ubuntu/k_mean/parallel_hdfs/reducer.py -reducer /home/ubuntu/k_mean/parallel_hdfs/reducer.py -input /data/input/dataset.txt -output /data/output/mapreduce-output$i
	rm -f /home/ubuntu/k_mean/parallel_hdfs/new_centroids.txt
	hadoop fs -copyToLocal /data/output/mapreduce-output$i/part-00000 /home/ubuntu/k_mean/parallel_hdfs/new_centroids.txt
	END_TIME=$(date +%s.%N)
    	ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    	CUCUMLATIVE=$(echo "$CUCUMLATIVE + $ELAPSED_TIME" | bc)
    	python3 /home/ubuntu/k_mean/parallel_hdfs/viz.py &
	seeiftrue=`python3 /home/ubuntu/k_mean/parallel_hdfs/calculate_change.py`
	echo "$seeiftrue"
	if [ $seeiftrue = True ]
	then
		echo "Converged in $i iterations"
		bash /home/ubuntu/k_mean/parallel_hdfs/calculate_cpu_time.sh
		rm /home/ubuntu/k_mean/parallel_hdfs/centroids.txt
		hadoop fs -copyToLocal /data/output/mapreduce-output$i/part-00000 /home/ubuntu/k_mean/parallel_hdfs/centroids.txt
		
		break
	else
		rm /home/ubuntu/k_mean/parallel_hdfs/centroids.txt
		hadoop fs -copyToLocal /data/output/mapreduce-output$i/part-00000 /home/ubuntu/k_mean/parallel_hdfs/centroids.txt
	fi
	i=$((i+1))
done
