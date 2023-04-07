#! /usr/bin/env python

# Author: Lu Xu <oliver_lew@outlook.com">
# License: MIT
# Original Repo: https://github.com/OliverLew/fio-cdm
# Packaging: https://github.com/Pythoniasm/pycdm

import argparse
import logging

from cdm.fio_cdm import Job


def get_parser():
    parser = argparse.ArgumentParser(
        description="A python script to show disk test results with fio"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="The path of the directory to test. " "Default to current directory",
    )
    parser.add_argument(
        "-0",
        dest="zero_buffers",
        action="store_true",
        help="Initialize buffers with zeros. " "Default to use random buffers.",
    )
    parser.add_argument(
        "-a",
        metavar="job",
        dest="jobs",
        action="append",
        help="Manually add multiple jobs. Format is "
        '"seq|rnd,<queue depth>,<thread number>". '
        "This overrides the preset jobs. "
        "This option can be used more than once.",
    )
    parser.add_argument(
        "-E",
        dest="extra_info",
        action="store_false",
        help="Disable extra information (iops, latency) for "
        "random IO tests. Default is enabled.",
    )
    parser.add_argument(
        "-f",
        metavar="jobfile",
        dest="dump_jobfile",
        help="Save jobfile and quit without running fio. "
        'Use "-" to print to stdout.',
    )
    parser.add_argument(
        "-n",
        metavar="number",
        dest="number",
        type=int,
        default=5,
        help="Number of tests, default is 5.",
    )
    parser.add_argument(
        "-s",
        metavar="size",
        dest="size",
        default="1G",
        help="The size of file I/O. " "It is directly passed to fio. " "Default is 1G.",
    )
    parser.add_argument(
        "-x",
        metavar="mix",
        dest="mix",
        type=float,
        nargs="?",
        const=70,
        default=0,
        help="Add mixed rw test. Default is disabled. "
        "<mix> is read percentage. Default is 70.",
    )
    # hidden option, enable to show debug information
    parser.add_argument("-g", dest="debug", action="store_true", help=argparse.SUPPRESS)
    return parser


def entrypoint():
    parser = get_parser()
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO, format="%(message)s"
    )

    fio_job = Job(**vars(args))
    if args.jobs:
        for job in args.jobs:
            rnd_type, qd, tn = job.split(",")
            fio_job.create_job(rnd_type, int(qd), int(tn))
    else:
        fio_job.create_job("seq", 8, 1)
        fio_job.create_job("seq", 1, 1)
        fio_job.create_job("rnd", 32, 16)
        fio_job.create_job("rnd", 1, 1)
    fio_job.run()


if __name__ == "__main__":
    entrypoint()
