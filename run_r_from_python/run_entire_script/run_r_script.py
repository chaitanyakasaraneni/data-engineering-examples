import subprocess

# path to your Rscript executable
# RSCRIPT_PATH = "/usr/local/bin/Rscript"

# path to your R script
R_SCRIPT = "sample_r_script.R"

# call R script using subprocess module
subprocess.call(['Rscript', R_SCRIPT])