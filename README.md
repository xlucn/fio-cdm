# fio-cdm

WIP

A python script to generate [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/)-style test result with [fio](https://github.com/axboe/fio). Should work across multi platforms as long as you have `fio` and `python` (need version 3.3 and above).

## Feature

- Using Python
- Try to provide some options of CrystalDiskMark, e.g., number of test runs, test file size, mixed r/w tests, zero buffers, etc
- Show IOPS and latency results for random read/write tests (thus combining the default, peak performance and real world performance tests in CrystalDiskMark 7.0.0)
- Easy to add/customize new tests in command-line arguments
- Parse `fio` result in json format to achieve more stability

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
|Name        | Read(MB/s)|Write(MB/s)|
|------------|-----------|-----------|
|SEQ1M Q8 T1 |    3076.62|    1605.00|
|SEQ1M Q1 T1 |    2084.94|    1392.66|
|RND4K Q32T16|    1780.82|     465.35|
|... IOPS    |  434665.02|  113591.83|
|... latency |    1159.69|    4476.99|
|RND4K Q1 T1 |      48.27|     178.48|
|... IOPS    |   11784.71|   43574.09|
|... latency |      83.94|      21.38|
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
