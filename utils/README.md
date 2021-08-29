# Scripts utility

[![bash](https://github.com/HakumenNC/logo-gallery/raw/0.0.5/img/b/bash/square-1-60.png)](bash)
[![bash](https://github.com/HakumenNC/logo-gallery/raw/0.0.5/img/t/terminal/square-1-60.png)](terminal)

## Main script

### Generate main README

Copy the md file `main-content.md` and append the logo array.

```sh
sh md-square-table-generator.sh
```

## Optional

### Create folders A to Z

```sh
sh az-folders.sh
```

### Exemples extraction path's elements

```sh
cat files-util.sh
```

```sh
input="/home/vivek/work/config.ini"

# extract config.ini
file_name="${input##*/}"

# get .ini 
file_extension="${file_name##*.}"

# get config 
file="${file_name%.*}"

# print it
echo "Full input file : $input"
echo "Filename only : $file_name"
echo "File extension only: $file_extension"
echo "First part of filename only: $file"
```

### Renaming files

```sh
sh rename-files-to-logo.sh
```
