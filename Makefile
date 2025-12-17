start:
	python3 main.py --files source/employees1.csv source/employees2.csv --report $(or $(arg), performance)
	
start1:
	python3 main.py --files source/employees1.csv --report performance

start2:
	python3 main.py --files source/employees2.csv --report performance

test:
	python3 tests/main.py