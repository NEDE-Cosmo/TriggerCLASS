import os
import numpy as np
from montepython.likelihood_class import Likelihood
import scipy.constants as conts

class H0_local(Likelihood):

    # initialization routine

    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)


        # end of initialization

    # compute likelihood

    def loglkl(self, cosmo, data):

        chi2 = 0.

        theo = cosmo.Hubble(0.)*conts.c / 1000.0

        chi2 += ((theo - self.H0) / self.error) ** 2

        # return ln(L)
        lkl = - 0.5 * chi2

        return lkl
