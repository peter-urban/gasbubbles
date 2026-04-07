# Gas Bubbles

Some test code, wrapping existing bubble dissolution and backscatter models in Python. 

⚠️ **Warning**: Some parts of this code (especially in the `backscatter` module) contains AI-generated code that has not been fully validated. 

## Getting started

### 1. Install pixi

Easiest way is to use pixi to manage python dependencies/installation, 
there is different ways to install pixi (some do not require admin rights)
https://pixi.prefix.dev/latest/installation/

### 2. Clone and initialize

```bash
git clone --recurse-submodules https://github.com/peter-urban/gasbubbles.git
cd gasbubbles

#this builds e.g. the tamoc library and installs the python dependencies
pixi run init
```

### 3. Run the notebooks

```bash
pixi run jupyter
(or pixi run jupyterlab ipynb)
```

This opens JupyterLab with the following notebooks:

| Notebook | Description |
|----------|-------------|
| `bubble_backscatter.ipynb` | Acoustic backscatter cross-sections vs. bubble radius, comparing models |
| `rising_bubble.ipynb` | Single rising bubble simulation (size, speed, dissolution + backscatter along trajectory) |
| `sbm.ipynb` | TAMOC Single Bubble Model — full workflow with shape diagnostics |

### Run tests

```bash
pixi run test_notebooks

pixi run clean_notebooks
```

## License

None so far

