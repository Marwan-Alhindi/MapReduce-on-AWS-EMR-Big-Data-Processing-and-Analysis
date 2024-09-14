Here’s the provided text converted into markdown format:

```markdown
# MapReduce Tasks on AWS EMR

This repository contains the code for running three different MapReduce tasks on AWS EMR. Below are the instructions for deploying and running these tasks.

## Prerequisites

- AWS CLI installed and configured
- Hadoop 3.x
- Python 3.x

## Directory Structure

- `/input/` - This directory contains the input files `Trips.txt` and `Taxis.txt`.
- `/output/` - This directory will contain the output of the MapReduce jobs.
  - `/output/task1`
  - `/output/task2`
  - `/output/task3`
- `mapper_t?.py` - The Mapper code where `?` is 1, 2, or 3, indicating the task number.
- `reducer_t?.py` - The Reducer code.
- `run_t?.sh` - Shell script to run the MapReduce jobs.
- `hadoop-streaming-3.1.4.jar` - Hadoop streaming file that allows Python scripts to run.

## Steps to Run the Code on AWS EMR

1. Open terminal.
2. Make sure you are in the home directory by running the following command:

   ```bash
   cd ~
   ```

3. Move the files from the local machine to the jumphost by the following command:

   ```bash
   scp -i "path/to/ssh-key.pem" "path/to/local/files/*" username@remote-server-address:/path/to/remote/directory/
   ```

   For example:

   ```bash
   scp -i "/Users/marwan/Desktop/Big Data/s3969393-cosc2637.pem" /Users/marwan/Desktop/s3969393_BDP_A1/* ec2-user@s3969393.jump.cosc2637.route53.aws.rmit.edu.au:/home/ec2-user/
   ```

4. Enter the jumphost by running the following command:

   ```bash
   ssh jumphost
   ```

5. Create a cluster in the master node by running the following command:

   ```bash
   ./create_cluster.sh
   ```

6. Move all files from the jumphost to the master node by running the following command:

   ```bash
   scp -i "path/to/ssh-key.pem" local-files username@remote-server-address:/path/to/remote/directory/
   ```

   For example:

   ```bash
   scp -i "/home/ec2-user/s3969393-cosc2637.pem" * hadoop@s3969393.emr.cosc2637.route53.aws.rmit.edu.au:/home/hadoop/
   ```

7. Type the following in the jumphost to get the master node command:

   ```bash
   cat instructions
   ```

   For example:

   ```bash
   ssh hadoop@s3969393.emr.cosc2637.route53.aws.rmit.edu.au -i s3969393-cosc2637.pem
   ```

8. Give permission to files by running the following command:

   ```bash
   chmod 700 *
   ```

9. Create directories:

   ```bash
   hdfs dfs -mkdir /input
   hdfs dfs -mkdir /output
   hdfs dfs -mkdir /output/task1
   hdfs dfs -mkdir /output/task2
   hdfs dfs -mkdir /output/task3
   ```

10. Move `Trips.txt` and `Taxis.txt` to the input directory:

   ```bash
   hdfs dfs -copyFromLocal Trips.txt /input/
   hdfs dfs -copyFromLocal Taxis.txt /input/
   ```

11. Run the following commands:

   ```bash
   sudo yum install dos2unix
   dos2unix mapper_t1.py mapper_t2.py mapper_t3.py
   dos2unix reducer_t1.py reducer_t2.py reducer_t3.py
   ```

12. Run tasks:

   ```bash
   ./run_t?.sh  # where ? is either 1, 2, or 3
   ```

13. After running task 1, merge the output and access it:

   ```bash
   hadoop fs -cat /output/task1/part-* | hadoop fs -put - /output/task1/merged_output.txt
   hdfs dfs -cat /output/task1/merged_output.txt
   ```

14. After running task 2, access the output by the following command:

   ```bash
   cat centroids1.txt or access from /output/task2
   ```

15. After running task 3, merge the output and access it:

   - Merge and access join output:

     ```bash
     hadoop fs -cat /output/task3/join/part-* | hadoop fs -put - /output/task3/join/merged_output_join.txt
     hadoop fs -cat /output/task3/join/merged_output.txt
     ```

   - Merge and access count output:

     ```bash
     hadoop fs -cat /output/task3/count/part-* | hadoop fs -put - /output/task3/count/merged_output_count.txt
     hadoop fs -cat /output/task3/count/merged_output_count.txt
     ```

---

Feel free to edit or add additional details if necessary!
