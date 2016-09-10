# hacker_rank_fw
A Python SDK for Programmatically Interfacing with Hacker Rank for Work

## Usage

For now, you'll want to reference the docstrings of each method in `hackerrank/hackerrank.py` as they are quite descriptive in how to use them.

```python
import os

from hackerrank.hackerrank import HackerRankClient
from pypandoc import convert_file 

# First create an instance of a HackerRankClient object

hr = HackerRankClient(token=os.environ.get('HR_KEY'))

# Now you can use pretty much any method
# Here is an example of creating a question

# Get all the tests
all_tests = hr.get_tests_list()

# All 'pretty' text-like values in Hacker Rank are HTML based so here we take a markdown file 
# (which is what I happen to like for writing) and we convert it to HTML using the pandoc library

nice_markdown_question = convert_file('./test_question_a.md', 'html')

# And since this will show how to make a sudorank type question we will need to add a check script

my_bash_script = open('./check.sh').read()

question_data = dict(
    name="My Great Question Title" 
    question = nice_markdown_question,
    score = 80,
    visible_tags_array = ['ansible', 'playbooks'],
    internal_notes = "This question is being managed programatically",
    type = 'sudorank',
    check = my_bash_script,
)

for test in all_tests['data']:
    # This example assumes you already have a test titled "My Test"
    if test['name'] == "My Test":
        test_id = test['id']
        create_question_result = hr.create_question(test_id, **question_data)
        print create_question_result

```

And that's all there is to it.

## Biggest Needs for help (in no particular order)

* More robust exception handling
* More robust support for other test types
* Fancier documentation
* Unittests
