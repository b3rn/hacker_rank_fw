# -*- coding: utf-8 -*-
import requests
from pypandoc import convert_file 
import json
from urlparse import urljoin

class HackerRankAuthError(Exception):
    pass

class HackerRankValueError(Exception):
    pass

class HackerRankClient(object):
    def __init__(self, token):
        self.headers = {'Content-Type' : 'application/json'} 
        self.base_url = 'https://www.hackerrank.com/x/api/v1/'
        self.query_string = {'access_token': token}
        self.validate_auth()

    def validate_auth(self):
        """Validates token by doing a GET for timezones which any kind of user should have access to"""
        endpoint = urljoin(self.base_url, 'users/timezones')
        test_req = requests.get(endpoint, params=self.query_string, headers=self.headers) 
        resp = test_req.json()
        try:
            if 'Invalid' in resp['message']:
                raise HackerRankAuthError("Invalid Access Token specified") 
        except KeyError:
            # No error
            pass

    def _caller(self, endpoint, query_string=None, data=None, headers=None, method='GET'):
        url = urljoin(self.base_url, endpoint)
        if query_string:
            self.query_string.update(query_string)

        if headers:
            self.headers.update(headers)

        if not data:
            data = dict()

        if method == 'POST':
            r = requests.post(url, params=self.query_string, data=data, headers=self.headers)
        elif method == 'PUT':
            r = requests.put(url, params=self.query_string, data=data, headers=self.headers)
        elif method == 'GET':
            r = requests.get(url, params=self.query_string, headers=self.headers)

        try:
            return r.json()
        except ValueError:
            return r.status_code


    def get_tests_list(self):
        params = dict(access='live', limit=100)
        endpoint = 'tests'
        return self._caller(endpoint, query_string=params)


    def get_test(self, test_id):
        endpoint = 'tests/%s' % test_id
        return self._caller(endpoint)


    def update_test(self, test_id, data, purge_tags=False):
        """
        # Note that other kwargs may still work, these are simply the ones that have been tested
        VALID KWARGS:
            key: name, val_type: string, desc: The name you want the test to have.
            key: instructions, val_type: string, desc: The instructions for the test
            key: duration, val_type: integer, desc: The number, in mintues, of the test time limit
            key: purge_tags, val_type: boolean, desc: When 'tags' in 'data' whether to add to existing tags or purge current tags
            key: collect_candidate_details, val_type: list, desc: The info you wish to collect from a candidate. Valid values are: full_name, work_experience, city, roll_number, email_address, year_of_graduation, cgpa, gpa, univ, phone_number, contact_recruiter, branch, major, degree, gender, role, resume, pgdegree, city_graduation
            key: custom_acknowledge_text, val_type: str, desc: Any statement you wish candidates to acknowledge prior to commencing a test
            key: test_admins, val_type: str, desc: the email address of the test administrator
            key: sudorank_setupscript, val_type: str, desc: the setup script to run to bootstrap test VMs for SudoRank questions
            key: sudorank_disable_check_agent, val_type: str, desc: sets up the Hacker Rank checking agent which allows for VMs to still be graded even if candidates leave the machine in an unreachable state
        """
        endpoint = 'tests/%s' % test_id

        if 'custom_acknowledge_text' in data.keys():
            data['enable_acknowledgement'] = True

        if not purge_tags and 'tags' in data.keys():
            current_test = self.get_test(test_id)
            data['tags'] += current_test['data']['tags']
            # If purge_tags is true when can just leave the normal behavior which is to purge when PUT

        if 'collect_info' in data.keys():
            data['collect_info'] = '|'.join(data['collect_info'])

        if 'sudorank_os' in data.keys():
            if data['sudorank_os'] not in ('rhel7', 'ubuntu'):
                #TODO: Validation for when questions require RH OS and a user attempts to update the os value to ubuntu
                raise HackerRankValueError("You specified a bad OS option, only 'rhel7' and 'ubuntu' are valid options")

        return self._caller(endpoint, method='PUT', data=json.dumps(data))

    def get_all_questions(self, question_type='all', qfilter='sudorank'):
        """
        Get all the questions available to the authenticated account

        key: question_type, type: str, desc: Whether to get personal, hackerrank, or all questions
        key: qfilter, type: str, desc: What type of questions to get. It can only be one value. Valid values are sudorank, coding, database, design (aka Front End), android, project (aka Java Project), multiple (Generic multiple choice), text (Subjective), and diagram
        """
        # Yes, 'undefined' is actually a part of the URI
        endpoint = 'tests/undefined/library'
        questions = []
        if question_type in ('personal', 'all'):
            p_query = dict(library='personal_all', filter=qfilter)
            personal_questions = self._caller(endpoint, query_string=p_query)['model']['questions']
            questions += personal_questions

        if question_type in ('hackerrank', 'all'):
            hr_query = dict(library='hackerrank', filter=qfilter)
            hr_questions = self._caller(endpoint, query_string=hr_query)['model']['questions']
            questions += hr_questions

        return questions


    def update_question(self, test_id, question_id, **kwargs):
        pass


