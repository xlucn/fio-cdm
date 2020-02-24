# fio-cdm

A python script to generate [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/)-style test result with [fio](https://github.com/axboe/fio). Should work across multi platforms as long as you have `fio` and `python` (need version 3.3 and above) in case you want to compare the results with CrystalDiskMark.

This is still WIP. I am a novice python coder and not familiar with fio, so the test result is expected to be imprecise. Correction and advices are welcome.

## Feature

- Using Python
- Try to provide some options of CrystalDiskMark, e.g., number of test runs, test file size, mixed r/w tests, zero buffers, etc
- Show IOPS and latency results for random read/write tests.
  This actually combines the "default", "peak performance" and "real world performance" tests in CrystalDiskMark 7.0.0
- Easy to add/customize new tests in command-line arguments
- Parse `fio` result in json format to achieve more stability

TODO

See `grep TODO fio-cdm`

## Usage

```
usage: fio-cdm [target] [-h] [-n number] [-s size] [-x [mix]] [-0] [-a job [job ...]] [-f dump-jobfile]

positional arguments:
  target            The path of the directory to test, default to current directory.

optional arguments:
  -n number         Number of tests, default is 5.
  -s size           The size of file I/O, same as the fio parameter, default is 1G.
  -x [mix]          Add mixed rw test, default is disabled. <mix> is read percentage,
                    default is 70 if not specified.
  -0                Initialize buffers with zeros instead of random data
  -a job [job ...]  Manually add multiple jobs. Override default. Format is
                    "seq|rnd,<queue depth>,<thread number>".
  -f dump-jobfile   Save jobfile and quit without running fio. Use '-' to print to
                    stdout.
```

### Sample output

The default tests are same as [CrystalDiskMark 7.0.0](https://crystalmark.info/en/software/crystaldiskmark/crystaldiskmark-main-menu/)

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

    fio-cdm -s 512m -n 5 -x

Manually add jobs to replace the default ones:

    fio-cdm -a seq,1,1 seq,32,1 rnd,16,8

Show the equivalent command directly with fio (without running the test):

    fio-cdm -f - | fio --showcmd -

### Note

Recommend to put the `<target>` argument as the first one since some of the optional arguments will consume it. See [this bug of Python](https://bugs.python.org/issue9338).

## Similar projects

**Shell version**: https://github.com/buty4649/fio-cdm
