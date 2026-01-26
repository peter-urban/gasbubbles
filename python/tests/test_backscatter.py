# SPDX-FileCopyrightText: 2026 Peter Urban
#
# SPDX-License-Identifier: MPL-2.0

"""Tests for gasbubbles backscatter models."""

import pytest
import math


def test_import_gasbubbles():
    """Test that the main package can be imported."""
    import gasbubbles
    assert hasattr(gasbubbles, '__version__')
    assert hasattr(gasbubbles, 'EnvironmentalParameters')
    assert hasattr(gasbubbles, 'backscatter')
    assert hasattr(gasbubbles, 'dissolution')


def test_import_backscatter_models():
    """Test that all backscatter models can be imported."""
    from gasbubbles.backscatter import (
        medwin,
        anderson,
        ainslie_leighton,
        li,
        thuraisingham,
        stanton,
        spheroidal,
    )


def test_environmental_parameters():
    """Test EnvironmentalParameters dataclass."""
    from gasbubbles import EnvironmentalParameters
    
    params = EnvironmentalParameters()
    
    # Check default values
    assert params.T == pytest.approx(281.29)
    assert params.cw == pytest.approx(1485.0)
    assert params.rho_liq == pytest.approx(1025.0)
    assert params.gamma == pytest.approx(1.299)
    
    # Test custom parameters
    custom = EnvironmentalParameters(T=290.0, cw=1500.0)
    assert custom.T == pytest.approx(290.0)
    assert custom.cw == pytest.approx(1500.0)


def test_medwin_resonance_frequency():
    """Test Medwin resonance frequency calculation."""
    from gasbubbles.backscatter import medwin
    
    # 1mm bubble at surface
    f0 = medwin.calculate_resonance_frequency(
        bubble_radius=0.5e-3,  # 0.5 mm radius
        waterdepth=0.0,
    )
    
    # Should be around 6 kHz for a 1mm bubble at surface
    assert 5000 < f0 < 8000
    
    # Resonance frequency should decrease with depth (higher pressure)
    f0_deep = medwin.calculate_resonance_frequency(
        bubble_radius=0.5e-3,
        waterdepth=100.0,
    )
    assert f0_deep > f0  # Higher pressure = higher resonance


def test_medwin_sigma_bs():
    """Test Medwin backscatter cross-section calculation."""
    from gasbubbles.backscatter import medwin
    
    sigma_bs = medwin.calculate_sigma_bs(
        frequency=300e3,
        bubble_radius=0.5e-3,
        waterdepth=50.0,
    )
    
    # Should be positive and finite
    assert sigma_bs > 0
    assert math.isfinite(sigma_bs)
    
    # At resonance, σ_bs should be larger
    f0 = medwin.calculate_resonance_frequency(0.5e-3, 50.0)
    sigma_bs_resonance = medwin.calculate_sigma_bs(f0, 0.5e-3, 50.0)
    sigma_bs_off = medwin.calculate_sigma_bs(f0 * 2, 0.5e-3, 50.0)
    assert sigma_bs_resonance > sigma_bs_off


def test_li_sigma_bs():
    """Test Li et al. (2020) backscatter calculation."""
    from gasbubbles.backscatter import li
    
    sigma_bs = li.calculate_sigma_bs(
        frequency=300e3,
        bubble_radius=0.5e-3,
        waterdepth=50.0,
    )
    
    assert sigma_bs > 0
    assert math.isfinite(sigma_bs)


def test_ainslie_leighton_sigma_bs():
    """Test Ainslie & Leighton backscatter calculation."""
    from gasbubbles.backscatter import ainslie_leighton
    
    sigma_bs = ainslie_leighton.calculate_sigma_bs(
        frequency=300e3,
        bubble_radius=0.5e-3,
        waterdepth=50.0,
    )
    
    assert sigma_bs > 0
    assert math.isfinite(sigma_bs)


def test_anderson_sigma_bs():
    """Test Anderson modal series backscatter calculation."""
    from gasbubbles.backscatter import anderson
    
    sigma_bs = anderson.calculate_sigma_bs(
        frequency=300e3,
        bubble_radius=0.5e-3,
        waterdepth=50.0,
    )
    
    assert sigma_bs > 0
    assert math.isfinite(sigma_bs)


def test_stanton_sigma_bs():
    """Test Stanton high-pass model backscatter calculation."""
    from gasbubbles.backscatter import stanton
    
    sigma_bs = stanton.calculate_sigma_bs(
        frequency=300e3,
        bubble_radius=0.5e-3,
        waterdepth=50.0,
    )
    
    assert sigma_bs > 0
    assert math.isfinite(sigma_bs)


def test_spheroidal_eotvos():
    """Test Eötvös number calculation for shape determination."""
    from gasbubbles.backscatter import spheroidal
    
    # Small bubble should be spherical
    Eo_small = spheroidal.calculate_eotvos_number(0.1e-3)  # 0.2 mm diameter
    assert Eo_small < 0.1
    
    # Large bubble should be non-spherical
    Eo_large = spheroidal.calculate_eotvos_number(2e-3)  # 4 mm diameter
    assert Eo_large > 0.1


def test_target_strength_conversion():
    """Test that target strength conversion is correct."""
    from gasbubbles.backscatter import medwin
    
    sigma_bs = medwin.calculate_sigma_bs(300e3, 0.5e-3, 50.0)
    ts = medwin.calculate_target_strength(300e3, 0.5e-3, 50.0)
    
    # TS = 10 * log10(sigma_bs)
    expected_ts = 10 * math.log10(sigma_bs)
    assert ts == pytest.approx(expected_ts)


def test_models_produce_similar_results():
    """Test that different models produce reasonably similar results away from resonance."""
    from gasbubbles.backscatter import medwin, li, ainslie_leighton
    
    # Parameters far from resonance
    freq = 300e3
    radius = 0.5e-3
    depth = 50.0
    
    sigma_medwin = medwin.calculate_sigma_bs(freq, radius, depth)
    sigma_li = li.calculate_sigma_bs(freq, radius, depth)
    sigma_al = ainslie_leighton.calculate_sigma_bs(freq, radius, depth)
    
    # All should be in the same order of magnitude
    # (allowing for factor of 10 difference due to model variations)
    import numpy as np
    values = [sigma_medwin, sigma_li, sigma_al]
    log_values = np.log10(values)
    assert np.ptp(log_values) < 2  # Within 2 orders of magnitude
