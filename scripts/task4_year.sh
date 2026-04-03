#!/bin/bash
source /etc/profile.d/hadoop.sh

OUTPUT_DIR="/user/${USER}/project/m1/task4"
hdfs dfs -rm -r ${OUTPUT_DIR} 2>/dev/null

mapred streaming \
    -files mapper_year.py,reducer.py \
    -mapper "python3 mapper_year.py" \
    -reducer "python3 reducer.py" \
    -input /data/chicago_crimes.csv \
    -output ${OUTPUT_DIR}

echo "--- Task 4 Results ---"
hdfs dfs -cat ${OUTPUT_DIR}/part-00000
