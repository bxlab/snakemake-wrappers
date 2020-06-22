__author__ = "Michael Sauria"
__copyright__ = "Copyright 2020, Michael Sauria"
__email__ = "mike.sauria@gmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell


java_opts = snakemake.params.get("java_opts", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' IndexFeatureFile -I {snakemake.input}"
    "{log}"
)
