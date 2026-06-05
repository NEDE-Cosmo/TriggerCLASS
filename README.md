TriggerCLASS
==============================================
forked from CLASS by Julien Lesgourgues and Thomas Tram; see http://class-code.net and https://github.com/lesgourg/class_public

TriggerCLASS is a modification of CLASS that implements an instant phase transition in a new fluid component that goes from a cosmological constant phase to a decaying phase. The transition is triggered by a sub-dominant clock field that carries adiabatic fluctiations. As such, it describes the physics of the New Early Dark Energy (NEDE) and Hybrid Early Dark Energy model. The details of the implementation have been explained in the methodology part of https://arxiv.org/abs/2006.06686 and through many additional comments in the code tagged with "NEDE".

The version used for the publications ArXiv: 1910.10739, 2006.06686, 2009.00006 has been tagged with "NewEDEv3.0".
The version used for the publication ArXiv: 2209.02708 has been tagged with "NewEDEv4".

__New in version 7.0 [31 July 2024]__: Rebased TriggerCLASS on version 3.2.1 of class_public with the SHA 997d1ac0b64d11439948a0cc13f719ef427f87be (older versions of TriggerCLASS are based on the older version 2 of class_public). This comes with the following modifications (thanks to Emil Holm and Thomas Tram for implementing this):
* New precision parameters: In CLASS versions >3, the implicit ndf15 integrator is used for the background evolution. This automatically increases precision around the NEDE decay time, so the precision parameters "decay_res_enhancement" and "trigger_resolution" have been removed.
* Added a background approximation switching logic that splits up the background evolution into two phases (before and after the trigger fluid approximation).
Ultimately, version 7.0 is faster than v6.1 by a factor of about 10 in the background and between 5 and 8 in the perturbations. The two codes have been tested against each other, and produce similar results in Cls and matter power spectrum to within 5 permille, a difference coming from the LambdaCDM sector difference in the two CLASS codes. with the precision settings given in input/NewEDE.ini and the NEDE notebook in the notebooks directory.

__New in version 6.1 [7 May 2023]__: TriggerCLASS now allows for Omega0_NEDE_trigger_DM as input, controlling the trigger abundance today (which contributes to DM).

__New in version 5 [12 Oct 2022]__: TriggerCLASS now takes the decay redshift z_decay_NEDE (rather than the trigger mass) as input. The trigger mass is then determined via a shooting method.  Output improvments and more detailed comments. 

__New in version 4 [20 Dec 2020]__: TriggerCLASS now accepts f_NEDE as input parameter (replaces Omega_NEDE). Introduced "tracking mode" for which the rest-frame sound speed equals the adiabatic sound speed (this feature has not been tested intensively yet). Output improvments and more detailed comments. 


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

MCMC analyses can be performed with MontePython, https://github.com/brinckmann/montepython_public, or with Cobaya, https://cobaya.readthedocs.io. Our baseline MontePython run (as discussed in https://arxiv.org/abs/2006.06686) can be found under input/run_NEDE_canonical.param. To make it run, you first need to update MontePython with the files from the folder montepython_tree. In particular, this will update the data.py to translate the NEDE input parameters. The corresponding covariance matrix and bestfit file can be found in the respective subfolders covmat and bestfit. There is also a Cobaya example run file together with a covariance matrix in the cobaya folder that can be used as a starting point for Cobaya runs.

Support
-------

To get support, please open a new issue on

https://github.com/NEDE-Cosmo/TriggerCLASS
