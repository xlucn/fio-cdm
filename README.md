# fio-cdm

WIP

A python script to generate CrystalDiskMark-style test result with [fio](https://github.com/axboe/fio). Should work across multi platforms as long as you have `fio` and `python`.

## Usage

```
usage: fio-cdm [-h] [-n number] [-s size] [-x [mix]] [-f dump-jobfile] target

positional arguments:
  target           The path of the directory to test

optional arguments:
  -h, --help       show this help message and exit
  -n number        Number of tests, default to 1
  -s size          The size of file I/O, same as the fio parameter, default to 1G
  -x [mix]         Add mixed rw test, default is not add it. <mix> is read percentage (integer), default to 70.
  -f dump-jobfile  Save jobfile and quit without running fio. Use '-' to print to stdout.
```

###  Tip

Show the equivalent command only using `fio` options:

```sh
fio-cdm -f - | fio --showcmd -
```

## Similar projects

**Shell version**: https://github.com/buty4649/fio-cdm

### Difference

- Using python instead of shell
- Try to mimic more of CrystalDiskMark, e.g., number of test runs, test file size, mixed r/w tests.
- Easier to add new tests
- Parse `fio` result in json format for stability
