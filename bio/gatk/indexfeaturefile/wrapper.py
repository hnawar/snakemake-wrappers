__author__ = "Hatem Nawar"
__copyright__ = "Copyright 2021, Hatem Nawar"
__email__ = "hnawar@google.com"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' IndexFeatureFile"
        " --feature-file {snakemake.input.feature}"
        " --mode {snakemake.params.mode}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.idx}"
        " {log}"
    )
