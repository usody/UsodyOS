# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Calendar Versioning](https://calver.org/#scheme) scheme (`YYYY.MINOR.MICRO`).

----
## [Unreleased]


## [2023.3.0-alpha] - 2023-06-06
_(hardware_metadata = 1.0.0b2 | sanitize = 0.1.0b7)_
- [added] upgrade ISO system to Debian 12
- [added] hardware_metadata folder
- [added] nvme-cli sanitize requirements
- [added] hwmd version in snapshot
- [changed] installation folder name to usody
- [changed] rename project to UsodyOS
- [changed] settings class and file
- [fixed] python packages installation in Debian 12

## [2023.2.0-alpha] - 2023-05-05
_(hardware_metadata = 1.0.0b2 | sanitize = 0.1.0b7)_
- [added] sanitize v0.1.0b7 ([+info](https://github.com/usody/sanitize/blob/dev/CHANGELOG.md#010-beta7))
- [added] hardware_metadata v1.0.0b2 ([+info](https://github.com/usody/hardware_metadata/blob/testing/CHANGELOG.md#100-beta2---2023-05-05))
- [added] SanatizeSettings class
- [added] print sanitize result 
- [changed] software and software_version vars
- [fixed] build_clean Makefile command

## [2023.1.0-alpha] - 2023-04-21
_(hardware_metadata = 1.0.0b1 | sanitize = 0.1.0b6)_
- [added] git submodule hardware_metadata v1.0.0b1 ([+info](https://github.com/usody/hardware_metadata/blob/testing/CHANGELOG.md#100-beta1))
- [added] build shell script to generate ISOs
- [added] README.md
- [added] LICENSE file with AGPLv3
- [added] Makefile
- [added] sanitizeOS.py file
- [added] sanitize v0.1.0b6 ([+info](https://github.com/usody/sanitize/blob/prod/CHANGELOG.md#010-beta6))
