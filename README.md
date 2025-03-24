# oae-data-protocol (⚠️ work in progress ⚠️)

Base ontology and data schemas for ocean alkalinity enhancement projects, experiments, and field trails. This project aims to be a technical complement to Submarine Scientific's [OAE Data Protocol](https://www.carbontosea.org/oae-data-protocol/), developed in conjunction with Carbon To Sea and NOAA.

## Website

[https://clevinson.github.io/oae-data-protocol](https://clevinson.github.io/oae-data-protocol)

## Repository Structure

- [examples/](examples/) - example data
- [project/](project/) - project files (do not edit these)
- [src/](src/) - source files (edit these)
  - [oae_data_protocol](src/oae_data_protocol)
    - [schema](src/oae_data_protocol/schema) -- LinkML schema
      (edit this)
    - [datamodel](src/oae_data_protocol/datamodel) -- generated
      Python datamodel
- [tests/](tests/) - Python tests

## Developer Documentation

<details>
To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
