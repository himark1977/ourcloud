<p align="center">
<img src="https://github.com/himark1977/ourcloud/blob/master/data/icons/hicolor/scalable/apps/svgviewer-png-output.png" width="150" height="150" border="10"/>
</p>

# ourcloud

iCloud but for Linux.

For all of the features you will need server being open.

> [!CAUTION]
> *Disclaimer:* This is not the Apple iCloud that is working on linux, this is an open source interpretation of a service cloud, let's say it iCloud.
> Please be careful this is highly broken.
> Nothing is encrypted (yet) use on your own.
> This app, now, is mostly for demonstration purpose.

## Build
1. Download [Gnome Builder](https://apps.gnome.org/ro/Builder/).
2. Open the project.
3. Build.
4. Open server file from server folder.

```
$ ./server/server
```

5. Open the app.

## Configure
### Create subprojects for blueprint

```
mkdir -p subprojects 
```

### Config subprojects
Blueprint [config](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/setup.html).

```
cat <<EOT >> subprojects/blueprint-compiler.wrap
[wrap-git]
directory = blueprint-compiler
url = https://gitlab.gnome.org/jwestman/blueprint-compiler.git
revision = main
depth = 1

[provide]
program_names = blueprint-compiler
EOT
```

### Meson add
Add before gnome.compile_resources

```
# Add a reference to the compiler to use
blueprint_compiler = find_program('blueprint-compiler')

# The blueprint files to be converted
blueprint_files = files(
    'BLABla.blp'
)
```

```
# The list of the converted .ui files to inject into the build
ui_files = []

foreach blueprint_file : blueprint_files
  path_as_string = '@0@'.format(blueprint_file)
  filename = path_as_string.split('/')[-1]

  ui_file = custom_target(path_as_string.underscorify(),
    input: blueprint_file,
    output: filename.replace('.blp', '.ui'),
    command: [blueprint_compiler, 'compile', '--output', '@OUTPUT@', '@INPUT@'])
  ui_files += ui_file
endforeach
```

```
gnome.compile_resources('ourcloud',
  'ourcloud.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: [ui_files]

)
```

```
ourcloud_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'BLABLA.py'
]
```

### Edit ourcloud.gresource.xml

```
<!-- TODO: Change here from .blp to .ui -->
<?xml version="1.0" encoding="UTF-8"?>
<gresources>
  <gresource prefix="/com/evokzh/ourcloud">
    <file preprocess="xml-stripblanks">gtk/window.ui</file>
    <file preprocess="xml-stripblanks">BLABla.ui</file>
    <file preprocess="xml-stripblanks">gtk/help-overlay.ui</file>
  </gresource>
</gresources>
```

### Pip config, edit com.evokzh.ourcloud.json, add before meson

```
 {
        "name": "pip",
        "buildsystem": "simple",
        "build-options": {
          "build-args": [
            "--share=network"
          ]
        },
        "build-commands": [
            "pip3 install --prefix=/app requests urllib3 chardet idna certifi"
        ]

       },

       ....
       "buildsystem" : "meson"
       ......
```
