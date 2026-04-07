# SPDX-FileCopyrightText: 2026 Peter Urban
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
project(
    'gasbubbles',
    license: 'MPL-2.0',
    version: '0.1.0',
    default_options: ['warning_level=0', 'buildtype=release'],
    meson_version: '>=1.2.3'
)

projectnamespace = 'gasbubbles'

# -- python modules --
if get_option('build_pythonmodule').enabled()
    pymod = import('python').find_installation(get_option('python_path'), pure: false)

    # Optional: for future C++ bindings
    # python3_dep = pymod.dependency()
    # pybind11_dep = dependency('pybind11', version : '>=2.10.0', required: false)

    message('python module install directory:', pymod.get_install_dir(subdir: projectnamespace))
endif

# add src (future C++ code)
subdir('src')

# add python files
subdir('python')
