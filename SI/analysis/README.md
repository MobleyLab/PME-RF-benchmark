This folder contains packages, scripts and data for analysis.

- [`xvg_files/`](xvg_files): *xvg files generated from simulations to compute ddG values for each edge. 
- packages.zip: Packages (PLBenchmarks and pmx) with specific version used for analysis in this work. 

To install these packages, follow these steps:

1. First unzip this file. 

2. Create a conda environment and activate it:
```
conda create -n pmxworkflow -c conda-forge -c omnia  python=3.7 openforcefield numpy pandas future pint

conda activate pmxworkflow
```

3. Install each package:

```
cd PLBenchmarks
pip install -e .

cd ../pmx
pip install -e .
```

Then you should be able to run `run_analysis.py` (in [`xvg_files/cdk2`](xvg_files/cdk2) and [`xvg_files/tyk2`](xvg_files/tyk2)) to compute ddG values for each edge using *xvg files in [`xvg_files/`](xvg_files) folders. Specify `path` in the scripts to change the data directory for specific simulations (PME_CPU, PME_GPU, RF_CPU, RF_GPU). 
