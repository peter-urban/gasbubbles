# SPDX-FileCopyrightText: 2026 Peter Urban
#
# SPDX-License-Identifier: MPL-2.0

"""
Environmental parameters for gas bubble models.

This module defines default environmental conditions for gas bubble
acoustic calculations including temperature, pressure, and gas properties.
"""

from dataclasses import dataclass


@dataclass
class EnvironmentalParameters:
    """Parameters for gas bubble backscatter models.
    
    Default values are typical for methane (CH4) bubbles in seawater.
    
    Attributes
    ----------
    T : float
        Temperature (K), default 8.14°C = 281.29 K
    tau : float
        Surface tension (N/m), default 0.0745
    pv : float
        Vapor pressure (Pa) at 10°C, default 872.0
    eta_s : float
        Shear viscosity (Pa·s), default 1.5e-3
    K_gas : float
        Thermal conductivity of the gas CH4 (W/(m·K)), default 8e-2
    Cp : float
        Specific heat capacity at constant pressure (J/(kg·K)), default 2191.0
    g : float
        Gravity (m/s²), default 9.81
    rho_liq : float
        Seawater density (kg/m³), default 1025.0
    P_atm : float
        Atmospheric pressure (Pa), default 101e3
    cw : float
        Sound speed in water (m/s), default 1485.0
    gamma : float
        Specific heat ratio of the gas CH4, default 1.299
    Mm : float
        Molar mass of the gas CH4 (kg/mol), default 0.016
    R : float
        Gas constant (m²·kg·s⁻²·K⁻¹·mol⁻¹), default 8.31
        
    Examples
    --------
    >>> params = EnvironmentalParameters()
    >>> params.T
    281.29
    >>> # Create custom parameters for a different temperature
    >>> cold_params = EnvironmentalParameters(T=275.0)
    """
    
    T: float = 281.29
    """Temperature (K), default 8.14°C = 281.29 K"""
    
    tau: float = 0.0745
    """Surface tension (N/m)"""
    
    pv: float = 872.0
    """Vapor pressure (Pa) at 10°C"""
    
    eta_s: float = 1.5e-3
    """Shear viscosity (Pa·s)"""
    
    K_gas: float = 8e-2
    """Thermal conductivity of the gas CH4 (W/(m·K))"""
    
    Cp: float = 2191.0
    """Specific heat capacity at constant pressure (J/(kg·K))"""
    
    g: float = 9.81
    """Gravity (m/s²)"""
    
    rho_liq: float = 1025.0
    """Seawater density (kg/m³)"""
    
    P_atm: float = 101e3
    """Atmospheric pressure (Pa)"""
    
    cw: float = 1485.0
    """Sound speed in water (m/s)"""
    
    gamma: float = 1.299
    """Specific heat ratio of the gas CH4"""
    
    Mm: float = 0.016
    """Molar mass of the gas CH4 (kg/mol)"""
    
    R: float = 8.31
    """Gas constant (m²·kg·s⁻²·K⁻¹·mol⁻¹)"""
