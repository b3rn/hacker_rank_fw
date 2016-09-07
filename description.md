This is an open book (open internet) comprehensive test. Copy/Pasting, however, is not allowed. Your actions on the terminal are being recorded. Note that the purpose is to gauge your technical skills and 100% correctness is not required to successfully pass the interview process, the test covers:

  - System Administration knowledge
  - Ansible Knowledge
  - Python 2 Knowledge


There will be at least three questions for each aforementioned category, one for each of: easy, intermediate and advanced.

It is recommended that you skip any questions you do not feel comfortable with and return to them once you've completed all other questions.

To get familiarized with our coding environment, try our Sample Test

To understand more about the environment, time limits, etc. you can read the FAQ here

You can print to console to debug your code using the appropriate print or echo command


**IMPORTANT. FOR ANSIBLE RELATED CODE:**

  - Do not use the become: yes or sudo: yes play parameters. If you need to run your playbook with privilege escalation do so with the appropriate flag at runtime.
  - Do not use relative paths. Because of the way your work is checked, you MUST use explicit paths in all of your Ansible code or your submission might fail.
  - Python related assignments are allowed to make use of python libraries inside of ansible.module_utils
  - ALL playbooks that you write MUST end in .yml as opposed to .yaml or any other extension/lack thereof.
  - ALL of your playbooks will be executed as root by the evaluator, exactly as
ansible-playbook NAME_OF_PLAYBOOK.yml -i localhost,
 - Grade on ansible code will be based on
   - Efficiency; the amount of tasks used, including the gathering of facts.
   - Idempotence; do things show up as changed only when logical
   - Correctness; can the playbook actually run
   - Properness; does the playbook make use of the proper modules and plugins

