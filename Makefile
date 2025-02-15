

test:
	rm -f /tmp/fred.csv
	python3 src/masters-com-src/03-yes.py  data/masters-com-data/invitees-2025.json /tmp/fred.csv
	sort /tmp/answer.csv > /tmp/sorted-answer.csv
	sort /tmp/fred.csv > /tmp/sorted-fred.csv
	diff /tmp/sorted-answer.csv /tmp/sorted-fred.csv
