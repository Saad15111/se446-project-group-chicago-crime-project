# SE446 - Chicago Crime Analytics with MapReduce

## Team Members

| Name | Student ID |
|------|-----------|
| Saad Abdullah Al Sufayan | salsufayan |
| Fahad Sami Alhomaidhi | fsalhomaidhi |

## Executive Summary

This project analyzes the Chicago Crime dataset using Hadoop MapReduce streaming jobs. We built four separate MapReduce pipelines to extract insights about crime type distribution, location hotspots, yearly crime trends, and arrest rates. Each mapper reads CSV records from stdin, extracts the relevant field using Python's csv module, and emits key-value pairs. A shared reducer aggregates the counts for each key. All jobs were executed on the SE446 HDFS cluster against the full dataset (`/data/chicago_crimes.csv`).

---

## Task 2: Crime Type Distribution

**Research Question:** What are the most common types of crimes in Chicago?

**Mapper:** `src/mapper_crime_type.py` — Extracts the Primary Type field (column index 5) from each CSV row.

**Command:**
```bash
mapred streaming \
    -files mapper_crime_type.py,reducer.py \
    -mapper "python3 mapper_crime_type.py" \
    -reducer "python3 reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/salsufayan/project/m1/task2
```

**Top 5 Results:**

| Crime Type | Count |
|-----------|-------|
| THEFT | 162,688 |
| BATTERY | 151,930 |
| CRIMINAL DAMAGE | 91,241 |
| NARCOTICS | 74,127 |
| ASSAULT | 54,070 |

**Interpretation:** Theft is the most prevalent crime type in Chicago with 162,688 occurrences, closely followed by Battery at 151,930, indicating that property crimes and violent offenses are the primary categories requiring resource allocation.

**Execution Log:**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob8888122685202502690.jar tmpDir=null
2026-04-03 12:41:28,024 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:41:28,401 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:41:28,882 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/salsufayan/.staging/job_1771402826595_0276
2026-04-03 12:41:30,699 INFO mapred.FileInputFormat: Total input files to process : 1
2026-04-03 12:41:30,734 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-04-03 12:41:30,735 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-04-03 12:41:31,369 INFO mapreduce.JobSubmitter: number of splits:2
2026-04-03 12:41:32,337 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0276
2026-04-03 12:41:32,337 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-04-03 12:41:32,690 INFO conf.Configuration: resource-types.xml not found
2026-04-03 12:41:32,691 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-04-03 12:41:32,816 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0276
2026-04-03 12:41:32,878 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0276/
2026-04-03 12:41:32,880 INFO mapreduce.Job: Running job: job_1771402826595_0276
2026-04-03 12:41:50,549 INFO mapreduce.Job: Job job_1771402826595_0276 running in uber mode : false
2026-04-03 12:41:50,552 INFO mapreduce.Job:  map 0% reduce 0%
2026-04-03 12:42:19,197 INFO mapreduce.Job:  map 67% reduce 0%
2026-04-03 12:42:20,432 INFO mapreduce.Job:  map 100% reduce 0%
2026-04-03 12:42:32,399 INFO mapreduce.Job:  map 100% reduce 100%
2026-04-03 12:42:36,353 INFO mapreduce.Job: Job job_1771402826595_0276 completed successfully
2026-04-03 12:42:36,590 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=11798790
		FILE: Number of bytes written=24540800
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=690
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
	Map-Reduce Framework
		Map input records=793074
		Map output records=793072
		Reduce input groups=34
		Reduce output records=34
2026-04-03 12:42:36,591 INFO streaming.StreamJob: Output directory: /user/salsufayan/project/m1/task2
```

---

## Task 3: Location Hotspots

**Research Question:** Where do most crimes occur?

**Mapper:** `src/mapper_location.py` — Extracts the Location Description field (column index 7) from each CSV row.

**Command:**
```bash
mapred streaming \
    -files mapper_location.py,reducer.py \
    -mapper "python3 mapper_location.py" \
    -reducer "python3 reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/salsufayan/project/m1/task3
```

**Top 5 Results:**

| Location | Count |
|----------|-------|
| STREET | 248,326 |
| RESIDENCE | 136,393 |
| APARTMENT | 61,235 |
| SIDEWALK | 47,506 |
| OTHER | 29,671 |

**Interpretation:** Streets are by far the highest-risk crime location with 248,326 incidents, followed by residences at 136,393, suggesting that patrol units should prioritize street-level presence and residential area coverage.

**Execution Log:**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob13957996443282103957.jar tmpDir=null
2026-04-03 12:42:56,808 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:42:57,168 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:42:57,690 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/salsufayan/.staging/job_1771402826595_0277
2026-04-03 12:42:59,550 INFO mapred.FileInputFormat: Total input files to process : 1
2026-04-03 12:42:59,580 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-04-03 12:42:59,581 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-04-03 12:43:00,214 INFO mapreduce.JobSubmitter: number of splits:2
2026-04-03 12:43:01,326 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0277
2026-04-03 12:43:01,326 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-04-03 12:43:01,740 INFO conf.Configuration: resource-types.xml not found
2026-04-03 12:43:01,741 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-04-03 12:43:01,891 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0277
2026-04-03 12:43:01,964 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0277/
2026-04-03 12:43:01,967 INFO mapreduce.Job: Running job: job_1771402826595_0277
2026-04-03 12:43:19,800 INFO mapreduce.Job: Job job_1771402826595_0277 running in uber mode : false
2026-04-03 12:43:19,803 INFO mapreduce.Job:  map 0% reduce 0%
2026-04-03 12:43:49,210 INFO mapreduce.Job:  map 67% reduce 0%
2026-04-03 12:43:50,477 INFO mapreduce.Job:  map 100% reduce 0%
2026-04-03 12:44:06,537 INFO mapreduce.Job:  map 100% reduce 100%
2026-04-03 12:44:09,475 INFO mapreduce.Job: Job job_1771402826595_0277 completed successfully
2026-04-03 12:44:09,746 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=12719805
		FILE: Number of bytes written=26382809
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=4761
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
	Map-Reduce Framework
		Map input records=793074
		Map output records=791479
		Reduce input groups=212
		Reduce output records=212
2026-04-03 12:44:09,746 INFO streaming.StreamJob: Output directory: /user/salsufayan/project/m1/task3
```

---

## Task 4: Crime Trends Over the Years

**Research Question:** How has the total number of crimes changed over the years?

**Mapper:** `src/mapper_year.py` — Extracts the year from the Date field (column index 2) by splitting the date string.

**Command:**
```bash
mapred streaming \
    -files mapper_year.py,reducer.py \
    -mapper "python3 mapper_year.py" \
    -reducer "python3 reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/fsalhomaidhi/project/m1/task4
```

**Top 5 Results (by volume):**

| Year | Count |
|------|-------|
| 2001 | 467,301 |
| 2002 | 205,267 |
| 2023 | 81,461 |
| 2025 | 12,710 |
| 2022 | 4,678 |

**Interpretation:** The year 2001 had the highest recorded crime volume at 467,301 incidents, with a significant decline in subsequent years, suggesting that overall crime has been on a downward trend over the past two decades.

**Execution Log:**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob4518118507501130622.jar tmpDir=null
2026-04-03 12:44:57,197 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:44:57,510 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:44:58,046 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/fsalhomaidhi/.staging/job_1771402826595_0278
2026-04-03 12:44:59,885 INFO mapred.FileInputFormat: Total input files to process : 1
2026-04-03 12:44:59,917 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-04-03 12:44:59,918 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-04-03 12:45:00,660 INFO mapreduce.JobSubmitter: number of splits:2
2026-04-03 12:45:01,573 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0278
2026-04-03 12:45:01,573 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-04-03 12:45:02,385 INFO conf.Configuration: resource-types.xml not found
2026-04-03 12:45:02,386 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-04-03 12:45:02,574 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0278
2026-04-03 12:45:02,661 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0278/
2026-04-03 12:45:02,671 INFO mapreduce.Job: Running job: job_1771402826595_0278
2026-04-03 12:45:20,560 INFO mapreduce.Job: Job job_1771402826595_0278 running in uber mode : false
2026-04-03 12:45:20,562 INFO mapreduce.Job:  map 0% reduce 0%
2026-04-03 12:45:49,167 INFO mapreduce.Job:  map 67% reduce 0%
2026-04-03 12:45:50,427 INFO mapreduce.Job:  map 100% reduce 0%
2026-04-03 12:46:05,341 INFO mapreduce.Job:  map 100% reduce 100%
2026-04-03 12:46:08,291 INFO mapreduce.Job: Job job_1771402826595_0278 completed successfully
2026-04-03 12:46:08,578 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=7137663
		FILE: Number of bytes written=15218552
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=245
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
	Map-Reduce Framework
		Map input records=793074
		Map output records=793073
		Reduce input groups=25
		Reduce output records=25
2026-04-03 12:46:08,578 INFO streaming.StreamJob: Output directory: /user/fsalhomaidhi/project/m1/task4
```

---

## Task 5: Law Enforcement Analysis

**Research Question:** What percentage of crimes result in an arrest?

**Mapper:** `src/mapper_arrest.py` — Extracts the Arrest field (column index 8) and normalizes it to lowercase.

**Command:**
```bash
mapred streaming \
    -files mapper_arrest.py,reducer.py \
    -mapper "python3 mapper_arrest.py" \
    -reducer "python3 reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/fsalhomaidhi/project/m1/task5
```

**Results:**

| Arrest Status | Count | Percentage |
|--------------|-------|------------|
| false | 571,140 | 72.0% |
| true | 221,932 | 28.0% |

**Interpretation:** Only about 28% of reported crimes result in an arrest, meaning nearly three-quarters of incidents do not lead to an apprehension, highlighting a significant gap in law enforcement coverage.

**Execution Log:**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob2841441248028415988.jar tmpDir=null
2026-04-03 12:46:37,812 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:46:38,176 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-04-03 12:46:38,663 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/fsalhomaidhi/.staging/job_1771402826595_0279
2026-04-03 12:46:40,448 INFO mapred.FileInputFormat: Total input files to process : 1
2026-04-03 12:46:40,486 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-04-03 12:46:40,488 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-04-03 12:46:41,141 INFO mapreduce.JobSubmitter: number of splits:2
2026-04-03 12:46:41,969 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0279
2026-04-03 12:46:41,970 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-04-03 12:46:42,268 INFO conf.Configuration: resource-types.xml not found
2026-04-03 12:46:42,269 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-04-03 12:46:42,385 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0279
2026-04-03 12:46:42,454 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0279/
2026-04-03 12:46:42,456 INFO mapreduce.Job: Running job: job_1771402826595_0279
2026-04-03 12:47:01,223 INFO mapreduce.Job: Job job_1771402826595_0279 running in uber mode : false
2026-04-03 12:47:01,225 INFO mapreduce.Job:  map 0% reduce 0%
2026-04-03 12:47:28,451 INFO mapreduce.Job:  map 100% reduce 0%
2026-04-03 12:47:42,059 INFO mapreduce.Job:  map 100% reduce 100%
2026-04-03 12:47:44,982 INFO mapreduce.Job: Job job_1771402826595_0279 completed successfully
2026-04-03 12:47:45,285 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=7708794
		FILE: Number of bytes written=16360838
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=25
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
	Map-Reduce Framework
		Map input records=793074
		Map output records=793072
		Reduce input groups=2
		Reduce output records=2
2026-04-03 12:47:45,285 INFO streaming.StreamJob: Output directory: /user/fsalhomaidhi/project/m1/task5
```

---

## Member Contribution

| Member | Contribution |
|--------|-------------|
| Saad Abdullah Al Sufayan | Wrote mapper and scripts for Task 2 (Crime Type Distribution) and Task 3 (Location Hotspots). Wrote the shared reducer. |
| Fahad Sami Alhomaidhi | Wrote mapper and scripts for Task 4 (Crime Trends by Year) and Task 5 (Arrest Analysis). |
