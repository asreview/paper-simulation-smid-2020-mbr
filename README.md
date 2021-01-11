This repository contains scripts to reproduce the results from the study:

Gerbrich Ferdinands (2020) AI-Assisted Systematic Reviewing: Selecting Studies to Compare Bayesian Versus Frequentist SEM for Small Sample Sizes, Multivariate Behavioral Research, DOI: [10.1080/00273171.2020.1853501](https://doi.org/10.1080/00273171.2020.1853501)

The persistent version of these scripts, the data, and results can be found at the Open Science Framework:

Ferdinands, G. (2021). Supplementary material for publication in Multivariate Behavioural Research (Ferdinands, 2020). Retrieved from [osf.io/re3cd](https://osf.io/re3cd/)

# Simulation study
To reproduce the results presented in this study, run the following in your
terminal:

```
# install required software (such as ASReview)
pip install requirements.txt

# run all simulations
./simulation_scripts.sh

# get statistics
asreview stat simoutput/nb
asreview stat simoutput/logistic

# create figure
python plots.py
```

# License
This repository has an MIT license.
