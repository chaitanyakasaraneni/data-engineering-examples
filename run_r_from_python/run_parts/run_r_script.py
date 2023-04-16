try:
    import rpy2.robjects as robjects
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rpy2"])

# Load the R script
robjects.r['source']('sample_r_script.R')


# Call a specific method from the R script
method = robjects.r['factorial']
print(method(5))
