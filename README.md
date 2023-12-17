
# K-mean parallel with Map-Reduce
![Python](https://img.shields.io/badge/python-blue)
![Hadoop](https://img.shields.io/badge/hadoop-yellow)
![Map-Reduce](https://img.shields.io/badge/Map-Reduce-yellow)
## Description
This is my project to implement about the K-means parallel using Map-Reduce in Hadoop with Python code.
## Word File
I write some word file to save userful information about my proplems, introduction to K-mean, how map-reduce work with K-mean and also guide to install the Hadoop on Ubuntu 22.04 system.
Here is some information you can get in the Word file (It's only Vietnamese language but you can contact me if you need help).
1. `Install`: Guide to install the Hadoop Single Node on Ubuntu 22.04.
2. `Review-Kmean`: Short review about the K-mean algorithm and how it work.
3. `Case-Study`: This part is talking about the sequential and parallel in K-mean.
4. `Evaluation`: Some evaluation on time speed while running the parallel and sequential.

## How to run demo
Here is the step-by-step how you can run this code in your Ubuntu 22.04 after you install Hadoop follow the `Install` guide above.
1. cd to `~`
2. Clone this repository to your ubuntu server: `git clone git@github.com:tanaha2002/K-means-parallel.git` (may you need to install git on your ubuntu server first).
3. Copy the `k_mean` folder to `/home/ubuntu`.
4. Install the python with command `sudo apt install python3`
5. Cd to `k_mean` and run `pip3 install -r requirements.txt` for install some depedencies python library.
6. Now you can go to `datagen` folder and open the `data_gen_labels.py then change the `num_samples` to how many data row you wanna gen to text. You will also get the init centroids and image about the ground truth cluster.
7. Turn on the HDFS and yarn with command `start-dfs.sh` and `start-yarn.sh`. Then go to the `parallel_hdfs` folder and run command `bash data2hdfs.sh` to put your data to hdfs and remove some old logs if you have.
8. Then run `bash run.sh` for run the parallel K-mean. You will get the visual of the images in each iter.
9. Now go to the `sequential` folder and run `python3 k_means.py` for run the sequential version.
10. After run all two version parallel and sequential. Go to the evaluation folder and run `python3 evaluation` and you will get the plot of time running of two version for evaluation.

__Note:__ This version is just can run with `2 feature` in `data_gen_labels.py`, you can clone this repo and update your own version to let it can run with any `feature-dim` you want, maybe 10-20... for get more true parallel time you can compute with the sequential.

## Demo



https://github.com/tanaha2002/K-means-parallel/assets/98084807/583ad4f6-d0a7-47a3-bcfc-9873e64c6a1a





