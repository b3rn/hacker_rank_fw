from hackerrank import HackerRankClient

import requests
from pypandoc import convert_file 
import json
from urlparse import urljoin
import os

# Begin Test Run
# Export your API key as an env var first
hr = HackerRankClient(token=os.environ.get('HR_KEY'))

all_tests = hr.get_tests_list()
instructions = convert_file('./description.md', 'html')
templates_q = convert_file('./ansible_templates.md', 'html')
setup_script = open('./test.sh', 'r').read()
templates_script = open('./ansible_templates_check.sh').read()

tags = ["TALENT ACQUISITION", "CONSULTING SERVICES", "NA", "ANSIBLE", "AUTOMATION"]
n_tags = ['ANSIBLE TOWER']
put_data = dict( 
    instructions=instructions,
    tags = n_tags,
    duration = 130,
    sudorank_setupscript = setup_script,
)

q_update = dict(
    name="My great question",
    question = templates_q,
    score = 80,
    visible_tags_array = ['ansible', 'playbooks', 'Config Management', 'intermediate'],
    internal_notes = "This question is being managed programatically",
    type = 'sudorank',
    check = templates_script,
)

qname = "Ansible Templates"

for test in all_tests['data']:
    if test['name'] == "Dummy Test":
        test_id = test['id']
        #result = hr.update_test(test_id, put_data, purge_tags=True)
        #result = hr.update_test(test_id, put_data)
        #question = [question['id'] for question in result['data']['questions_data'] if question['name'] == qname][0]
        update_question_result = hr.create_question(test_id, **q_update)
        try:
            print 'SUCCESS' 
        except TypeError:
            print result




#print json.dumps(all_tests, indent=2)


