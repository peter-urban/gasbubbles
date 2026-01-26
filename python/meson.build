# SPDX-FileCopyrightText: 2026 Peter Urban
#
# SPDX-License-Identifier: CC0-1.0

# -- python sources --
sources = [
    'gasbubbles/__init__.py',
    'gasbubbles/parameters.py',
    'gasbubbles/backscatter/__init__.py',
    'gasbubbles/backscatter/echosms_wrapper.py',
    'gasbubbles/backscatter/ai_created/__init__.py',
    'gasbubbles/backscatter/ai_created/medwin.py',
    'gasbubbles/backscatter/ai_created/anderson.py',
    'gasbubbles/backscatter/ai_created/ainslie_leighton.py',
    'gasbubbles/backscatter/ai_created/li.py',
    'gasbubbles/backscatter/ai_created/thuraisingham.py',
    'gasbubbles/backscatter/ai_created/stanton.py',
    'gasbubbles/backscatter/ai_created/spheroidal.py',
    'gasbubbles/dissolution/__init__.py',
    'gasbubbles/dissolution/environment.py',
    'gasbubbles/dissolution/bubble_shape.py',
    'gasbubbles/dissolution/rise_velocity.py',
    'gasbubbles/dissolution/dissolution.py',
]

init_configuration = configuration_data({
    'PROJECT_VERSION' : meson.project_version(),
})

if get_option('build_pythonmodule').enabled()
    
    if get_option('pydev_install').disabled()
        foreach source : sources
            # Create install path for file
            fields = []
            foreach field : source.split('/')
                if not field.endswith('.py')
                    fields += [field]
                endif
            endforeach
            pth = '/'.join(fields)

            pymod.install_sources(source, subdir: pth, install_tag: 'python-runtime')
                
        endforeach
    endif
endif
