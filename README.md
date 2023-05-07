TriggerCLASS
==============================================
forked from CLASS by Julien Lesgourgues and Thomas Tram; see http://class-code.net and https://github.com/lesgourg/class_public

TriggerCLASS is a modification of CLASS that implements an instant phase transition in a new fluid component that goes from a cosmological constant phase to a decaying phase. The transition is triggered by a sub-dominant clock field that carries adiabatic fluctiations. As such, it describes the physics of the New Early Dark Energy (NEDE) and Hybrid Early Dark Energy model. The details of the implementation have been explained in the methodology part of https://arxiv.org/abs/2006.06686 and through many additional comments in the code tagged with "NEDE".

The version used for the publications ArXiv: 1910.10739, 2006.06686, 2009.00006 has been tagged with "NewEDEv3.0".
The version used for the publication ArXiv: 2209.02708 has been tagged with "NewEDEv4"

New in version 4 [20 Dec 2020]: TriggerCLASS now accepts f_NEDE as input parameter (replaces Omega_NEDE). Introduced "tracking mode" for which the rest-frame sound speed equals the adiabatic sound speed (this feature has not been tested intensively yet). Output improvments and more detailed comments. 

New in version 5 [12 Oct 2022]: TriggerCLASS now takes the decay redshift z_decay_NEDE (rather than the trigger mass) as input. The trigger mass is then determined via a shooting method.  Output improvments and more detailed comments. 

New in version 6.1 [7 May 2023]: TriggerCLASS now allows for Omega0_NEDE_trigger_DM as input, controlling the trigger abundance today (which contributes to DM).


Compiling TriggerCLASS and getting started
-----------------------------------

In order to install TriggerCLASS, clone the branch "NewEDEv4" in a new folder and follow the same steps as required for the installation of the base CLASS code detailed in https://github.com/lesgourg/class_public. Also see the Wiki page:

https://github.com/lesgourg/class_public/wiki/Installation

For a successfull compilation adapt the compiler information in "Makefile" and "./python/setup.py".  After compiling it, check that TriggerCLASS has been properly set up by running first
    
    ./class input/explanatory.ini

This corresponds to a standard LambdaCDM run. To check that the trigger component works correctly, type:

    ./class input/NewEDE.ini

This should result in a run with a non-vanishing fraction of NEDE. The output should provide a detailed account of the NEDE parameters.
The NewEDE.ini also explains the NEDE input parameters.

MCMC analysis
------

In order to perform a MCMC analysis, we recommend using MontePython, https://github.com/brinckmann/montepython_public, and follow their installation instructions. Our baseline MCMC run (as discussed in https://arxiv.org/abs/2006.06686) can be found under input/run_NEDE_canonical.param. To make it run, you first need to update MontePython with the files from the folder montepython_tree. In particular, this will update the data.py to translate the NEDE input parameters. The corresponding covariance matrix and bestfit file can be found in the respective subfolders covmat and bestfit.

Support
-------

To get support, please open a new issue on

https://github.com/NEDE-Cosmo/TriggerCLASS

