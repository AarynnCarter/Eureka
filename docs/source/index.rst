.. JWST-obsim documentation master file, created by
   sphinx-quickstart on Fri Aug  7 05:07:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Eureka!'s documentation!
====================================

**Welcome to the documentation for Eureka!.**

``Eureka!`` will eventually be capable of reducing data from any JWST instrument and fitting light curves .
At the moment the package is under development, and currently works on NIRCam data only.
The code is not officially associated with JWST or the ERS team.

The code is separated into three parts or "Stages":

- Stage 3: Starts with Stage 2 data and reduces the data (performs background subtraction, etc. in order to convert 2D spectra into 1D information)
- Stage 4: Bins the 1D Spectra and generates light curves
- Stage 5: Fits the light curves (under development)

The full code for ``Eureka!`` is available on `GitHub <http://github.com/kevin218/Eureka>`_


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   ecf
   contribute
   api



.. toctree::
   :maxdepth: 1
   :caption: Examples

   hackathon-day2-tutorial



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
