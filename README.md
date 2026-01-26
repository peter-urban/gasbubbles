# Gas Bubbles

Gas bubble acoustic backscattering and dissolution models for underwater acoustics research.

⚠️ **Warning**: Some parts of this code (especially in the `dissolution` module) contain AI-generated code that has not been fully validated. Please verify results independently before using in production research.

## Installation

### From GitHub (recommended)

```bash
pip install git+https://github.com/themachinethatgoesping/gasbubbles.git
```

### Development installation

```bash
git clone https://github.com/themachinethatgoesping/gasbubbles.git
cd gasbubbles
pip install -e .
```

## Features

### Backscatter Models

Various acoustic backscatter models for spherical and non-spherical gas bubbles:

- **medwin**: Medwin (1977) / Clay & Medwin - Classic damped resonant bubble model
- **anderson**: Anderson (1950) - Fluid sphere scattering (modal/partial wave solution)  
- **ainslie_leighton**: Ainslie & Leighton (2009, 2011) - Comprehensive model with complex polytropic index
- **li**: Li et al. (2020) - Based on Ainslie-Leighton with Thuraisingham correction
- **thuraisingham**: Thuraisingham (1997) - High-frequency correction model
- **stanton**: Stanton (1989) - High-pass heuristic model
- **spheroidal**: Non-spherical bubble corrections for oblate spheroid bubbles
- **echosms_wrapper**: Wrapper for echoSMs library (exact modal solutions)

### Dissolution Models

Models for bubble dissolution and rise behavior:

- **environment**: Environmental parameters (temperature, salinity, gas composition)
- **rise_velocity**: Rise velocity correlations based on bubble size and shape
- **dissolution**: Mass transfer and dissolution simulation
- **bubble_shape**: Shape prediction based on dimensionless numbers

## Quick Start

### Calculating Backscatter

```python
from gasbubbles import EnvironmentalParameters
from gasbubbles.backscatter import li

# Calculate backscatter cross-section for a 1mm bubble at 300 kHz
sigma_bs = li.calculate_sigma_bs(
    frequency=300e3,      # 300 kHz
    bubble_radius=0.5e-3, # 0.5 mm radius = 1 mm diameter
    waterdepth=50.0,      # 50 m depth
)
print(f"Backscatter cross-section: {sigma_bs:.2e} m²")

# Convert to target strength (dB)
ts = li.calculate_target_strength(300e3, 0.5e-3, 50.0)
print(f"Target strength: {ts:.1f} dB")
```

### Comparing Models

```python
from gasbubbles.backscatter import plot_bs_comparison
import matplotlib.pyplot as plt

ax = plot_bs_comparison(
    frequency_hz=300e3,
    water_depth_m=50.0,
    bubble_diameter_min_mm=0.01,
    bubble_diameter_max_mm=10.0,
    models=['li', 'medwin', 'ainslie_leighton']
)
plt.show()
```

### Bubble Dissolution Simulation

```python
from gasbubbles.dissolution import BubbleEnvironment, simulate_bubble_rise

env = BubbleEnvironment()  # 100% methane, ~8°C
result = simulate_bubble_rise(
    initial_radius=0.002,  # 2 mm bubble
    initial_depth=100.0,   # Released at 100 m
    env=env,
)
print(f"Reached surface: {result.reached_surface}")
print(f"Final radius: {result.final_radius*1000:.2f} mm")
```

## Shape Regimes

The appropriate model depends on bubble size (characterized by Eötvös number):

| Eötvös Number | Shape | Typical Radius | Recommended Model |
|---------------|-------|----------------|-------------------|
| Eo < 0.1 | Spherical | < ~0.35 mm | Any spherical model |
| 0.1 < Eo < 10 | Ellipsoidal | 0.35–3.5 mm | spheroidal module |
| Eo > 10 | Spherical cap | > ~3.5 mm | Complex regime |

## Dependencies

**Required:**
- numpy >= 1.26.0
- scipy >= 1.10.0
- matplotlib >= 3.6.0

**Optional:**
- echosms (for exact modal solutions)

## References

- Anderson, V.C. (1950). JASA 22(4), 426-431.
- Medwin, H. (1977). Ultrasonics 15, 7-13.
- Stanton, T.K. (1989). JASA 86(4), 1499-1510.
- Thuraisingham, R.A. (1997). Ultrasonics 35, 357-366.
- Ainslie, M.A. & Leighton, T.G. (2009). JASA 126(5), 2163-2175.
- Ainslie, M.A. & Leighton, T.G. (2011). JASA 130(5), 3184-3208.
- Li, J. et al. (2020). JGR Oceans 125(9), e2020JC016360.
- Clift, R., Grace, J.R. & Weber, M.E. (1978). Bubbles, Drops, and Particles.
- Jech, J.M. et al. (2015). JASA 138, 3742-3764.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Acknowledgments

This package was developed as part of the [themachinethatgoesping](https://github.com/themachinethatgoesping) ecosystem for multibeam and singlebeam echosounder data processing.
