# BugDemoPythonDoxygen
Demonstrating bugs in doxygen generation for python

This repository contains a sample python project to demonstrate some unexpected behaviour, when generating documentation for python.

## Preparation
This demonstration needs python and some packages installed.

You can install python and pip on Ubuntu by executing the following script:

```sh
./install_python.sh
```

If you just installed python and installed your first packages please reboot your machine.

To install the script requirements execute

```sh
./install_dependencies.sh
```

## Reproduce
please execute following command to run doxygen for the project from the root of this repository:

```sh
doxygen .doxyfile
```

it will produce the documentation in `./docs/doxygen`


## Bugs
### 1. package references
If you look into the generated Class Hierarchy you will find MathOperation twice.

Because of using the package aproach with `__init__.py` doxygen doesn't correctly detect the dependency between interface and implementations.

Expected Behaviour:

properly detect the connection between interfaces and implementations

### 2. data classes
If you look into the ComplexNumber class there won't be any members.
The @dataclass annotation in the python file will generate the fields but doxygen doesn't show them.

Expected Behaviour:

display the members that are defined for the dataclass