commit: test
	git commit -a -m "03-yes past test"


test:
	rm -f /tmp/fred.csv
	python3 src/masters-com-src/python-version-of-convert-categories-to-binary.py  data/masters-com-data/invitees-2025.json /tmp/fred.csv
	sort /tmp/answer.csv > /tmp/sorted-answer.csv
	sort /tmp/fred.csv > /tmp/sorted-fred.csv
	diff /tmp/sorted-answer.csv /tmp/sorted-fred.csv


compare:
	python3 src/compare_invitees.py /tmp/fred.json data/masters-com-data/invitees-2025.json 
