# Instructions

## How to execute

### Installing the dependencies
I added one Makefile with useful commands:

- To install the dependencies
```bash
make install
```

- To install the dependencies using virtualenv
```bash
make install-virtual-env
```

### Testing
- To run the test suit:
```bash
make test
```

### Execution
- To execute one of the examples:
```bash
make run EXAMPLE=1 DATE=2021-01-01 PRECISION=1
```

- To execute one of the examples without make
```bash
python3 vesting_program.py example1.csv 2020-04-01
```
```bash
python3 vesting_program.py example2.csv 2021-01-01
```
```
python3 vesting_program.py example3.csv 2021-01-01 1
```