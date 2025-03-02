from astropy.table import QTable
from astropy.table import Table
from astropy.io import ascii
import numpy as np
import os

def savetable_S3(meta, bjdtdb, wave_1d, stdspec, stdvar, optspec, opterr):
    """
      Saves data in an event as .txt using astropy

      Parameters
      ----------
      event    : An Event instance.

    Description
    -----------
    Saves data stored in an event object as an table

      Returns
      -------
      .txt file

      Revisions
      ---------

    """

    filename = meta.workdir + '/S3_' + meta.eventlabel + "_Table_Save.txt"

    dims = stdspec.shape #tuple (integration, wavelength position)

    bjdtdb = np.repeat(bjdtdb, dims[1])
    wave_1d = np.tile(wave_1d, dims[0])
    stdspec = stdspec.flatten()
    stdvar = stdvar.flatten()
    optspec = optspec.flatten()
    opterr = opterr.flatten()

    arr = [bjdtdb, wave_1d, stdspec, stdvar, optspec, opterr]
    table = QTable(arr, names=('bjdtdb', 'wave_1d', 'stdspec', 'stdvar', 'optspec', 'opterr'))
    ascii.write(table, filename, format='ecsv', overwrite=True, fast_writer=True)

def readtable(meta):
    t = ascii.read(meta.workdir+'/S3_' + meta.eventlabel+'_Table_Save.txt', format='ecsv')
    return t