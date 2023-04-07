# PyCDM

Python script packaging of [fio-cdm](https://github.com/OliverLew/fio-cdm), a python script to generate [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/)-style test result with [fio](https://github.com/axboe/fio). Should work across multi platforms.

## Requirement

- fio
- python3

## Feature

- Provide some options of CrystalDiskMark, e.g., number of test runs, test file size, mixed r/w tests, zero buffers, etc
- Show IOPS and latency results for random read/write tests.
  This actually combines the "default", "peak performance" and "real world performance" tests in CrystalDiskMark
- Easy to add/customize new tests in command-line arguments
- Parse `fio` result in json format to achieve more stability

## Installation

Install via Python `pip install .`

## Usage

Call script via `cdm` after pip installation from anywhere.

```
usage: cdm [target] [-h] [-0] [-a job] [-E] [-f jobfile] [-n number] [-s size] [-x [mix]]

positional arguments:
  target      The path of the directory to test. Default to current directory.

optional arguments:
  -h, --help  show this help message and exit
  -0          Initialize buffers with zeros. Default to use random buffers.
  -a job      Manually add multiple jobs. Format is "seq|rnd,<queue depth>,<thread number>".
              This overrides the preset jobs. This option can be used more than once.
  -E          Disable extra information (iops, latency) for random IO tests. Default is enabled.
  -f jobfile  Save jobfile and quit without running fio. Use "-" to print to stdout.
  -n number   Number of tests, default is 5.
  -s size     The size of file I/O. It is directly passed to fio. Default is 1G.
  -x [mix]    Add mixed rw test. Default is disabled. <mix> is read percentage. Default is 70.

Note:
Recommend to put the <target> argument as the first one since some of the optional arguments will consume it.
```

### Sample output

The default tests are same as [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/crystaldiskmark-main-menu/)

```
tests: 5, size: 1G, target: . 173.3GiB/405.1GiB
|Name        | Read(MB/s)|Write(MB/s)|  Mix(MB/s)|
|------------|-----------|-----------|-----------|
|SEQ1M Q8 T1 |    2997.60|    2056.19|    1438.19|
|SEQ1M Q1 T1 |    1986.94|    1461.67|     941.04|
|RND4K Q32T16|    1816.04|     456.98|     434.18|
|... IOPS    |  443350.17|  111546.75|  105987.62|
|... latency |    1153.89|    4587.90|    2800.43|
|RND4K Q1 T1 |      54.20|     164.86|      34.43|
|... IOPS    |   13232.15|   40248.87|    8405.20|
|... latency |      74.76|      23.04|      67.78|
```

### Examples

Set test file size to 512MB, 5 test runs with read, write and mix tests:

    cdm -s 512m -n 5 -x

Manually add jobs to replace the default ones:

    cdm -a seq,1,1 -a seq,32,1 -a rnd,16,8

Show the equivalent fio command directly (without running the test):

    cdm -f - | fio --showcmd -

## Similar projects

**Shell version**: https://github.com/buty4649/fio-cdm
