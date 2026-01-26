# SPDX-FileCopyrightText: 2026 Peter Urban
#
# SPDX-License-Identifier: MPL-2.0

"""
Gas bubble acoustic backscattering and dissolution models.

This package provides implementations of various acoustic backscatter models
for gas bubbles in water, as well as bubble dissolution/rise models.

Subpackages
-----------
backscatter
    Acoustic backscattering cross-section models for gas bubbles.
    
dissolution
    Bubble dissolution and rise velocity models.

Classes
-------
EnvironmentalParameters
    Environmental parameters for gas bubble acoustic models.

Quick Start
-----------
>>> from gasbubbles import EnvironmentalParameters
>>> from gasbubbles.backscatter import li
>>> 
>>> # Calculate backscatter cross-section for a 1mm bubble at 300 kHz
>>> sigma_bs = li.calculate_sigma_bs(
...     frequency=300e3,      # 300 kHz
...     bubble_radius=0.5e-3, # 0.5 mm radius = 1 mm diameter
...     waterdepth=50.0,      # 50 m depth
... )
>>> print(f"Backscatter cross-section: {sigma_bs:.2e} m²")

References
----------
- Medwin, H. (1977). "Counting bubbles acoustically." Ultrasonics 15, 7-13.
- Anderson, V.C. (1950). JASA 22(4), 426-431.
- Ainslie, M.A. & Leighton, T.G. (2009, 2011). JASA 126, 130.
- Li, J. et al. (2020). JGR Oceans 125(9), e2020JC016360.
- Stanton, T.K. (1989). JASA 86(4), 1499-1510.
- Thuraisingham, R.A. (1997). Ultrasonics 35, 357-366.
- Clift, R., Grace, J.R. & Weber, M.E. (1978). Bubbles, Drops, and Particles.
"""

__version__ = '0.1.0'

from .parameters import EnvironmentalParameters

from . import backscatter
from . import dissolution

__all__ = [
    '__version__',
    'EnvironmentalParameters',
    'backscatter',
    'dissolution',
]
