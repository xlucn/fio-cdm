# fio-cdm

WIP

A python script to generate [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/)-style test result with [fio](https://github.com/axboe/fio). Should work across multi platforms as long as you have `fio` and `python` (need version 3.3 and above).

## Usage

```
usage: fio-cdm [-h] [-n number] [-s size] [-x [mix]] [-a job [job ...]]
               [-f dump-jobfile] target

positional arguments:
  target            The path of the directory to test

optional arguments:
  -h, --help        show this help message and exit
  -a job [job ...]  Manually add multiple jobs. Override default. Format is
                    "seq|rand,queue depth,thread number".
  -f dump-jobfile   Save jobfile and quit without running fio. Use '-' to print to
                    stdout.
  -n number         Number of tests, default is 1
  -s size           The size of file I/O, same as the fio parameter, default is 1G
  -x [mix]          Add mixed rw test, default is disabled.
                    <mix> is read percentage (integer), default is 70.
```

### Note

Do not add argument `<target>` after -x (as in `fio-cdm -x <target>`), it will be regarded as `<mix>` but an error will pop up since -x only accepts an integer.

### Examples

Set test file size to 512MB, run 5 times with read, write and mix tests (specify the mix percentage to be 60%):

    fio-cdm -s 512m -n 5 -x 60

Manually add jobs:

    fio-cdm -a seq,1,1 seq,32,1 rand,16,8

Show the equivalent command directly with fio:

    fio-cdm -f - | fio --showcmd -

## Similar projects

**Shell version**: https://github.com/buty4649/fio-cdm

### Difference

- Using python instead of shell
- Try to add more features of CrystalDiskMark, e.g., number of test runs, test file size, mixed r/w tests
- Easier to add new tests in command arguments
- Parse `fio` result in json format for stability
