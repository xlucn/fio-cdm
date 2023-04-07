# Author: Lu Xu <oliver_lew@outlook.com">
# License: MIT
# Original Repo: https://github.com/OliverLew/fio-cdm
# Packaging: https://github.com/Pythoniasm/pycdm

from cdm import Job, get_parser


def test_job():
    parser = get_parser()
    args = parser.parse_args()

    job = Job(**vars(args))
    job.create_job("rnd", 1, 1)
    job.run()
