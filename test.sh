# To enable additional repos:
#yum-config-manager --enable rhui-REGION-rhel-server-optional rhui-REGION-rhel-server-extras

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm git gcc python-devel sshpass
yum -y install python-pip
pip install ansible
yum -y remove epel-release
chown tasker:tasker /home/tasker/.ssh/config
git clone https://github.com/defionscode/HR_candidate.git /home/tasker/fubar
chown tasker:tasker -R /home/tasker/fubar

# Common functions for all question scripts
mkdir -p /var/lib/hacker/
cat << EOF >> /var/lib/hacker/common-libs
qresponse() {
        TEXT=\$1
        POINTS=\$2

        if [[ "\${POINTS}" == "0" ]]
        then
                echo "QUESTION\${QUESTION}: ERROR: \${TEXT}"
                ERROR=1
        else
                echo "QUESTION\${QUESTION}: CORRECT: \${TEXT}"
                SCORE=\$((\${SCORE} + \${POINTS}))
                echo "Partial Credit: \${POINTS}%"
        fi
}
EOF

# SSH keys to inject for testing
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLxLr+y4202uYQDBpqySF4sjO/e9Csn9mVTRxYOXTqlcoW8FVodvNPYNhOxJW2wX/nVZLVxVMmnh0Uc4DgdvYSf/NYdJtaix/RmkVPPJ/HoLZiN0/xGuE3Kp4k7BlEaeX72LRo2SI1yYZAZXD6PmGjWJnI1BCNxatJPAgCB/Bt1w78woFT0gOmM8B7RwKesF+hhzDiyQ23BGLYk0cr0P5NmGoSUN9kVJuo5u7QTptdHKQUBJYU2Eda8QXKyufy8D7cTL/87uBs4IFe42l8Wx4dbF54uuzPjPvOLwR4JEBd/LFg2YXFCwfnTsU66z9uQVoFSjWhx2tBv+mMPEYz5kKP
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDKFb8Ma1e2bGWA8t0ZXhgXTRjByF+8LfQ3SdKLHVlgnmiMtEHYqtvp2yH3wQzTxlSDMXzoWV4ZlS4U7SzylyAEtl3/ByfpQ9h3VzH6eo98eRovZP9gdcaN3698R/p+PrBPbn25lY2+Wa/qdk8NDT7uqMEaRZwlT8IzMVQIz/ACaTbxE3EPTnbKyiJkWlOVafoN044WJvvU/x6yJR6F+g7HwJIOuAyj8AATZuC1ZimY9TIIkSRmxoJk9SVvHv88EXKIk/oXr9p6G5zMZilfWWj87YfL8Ytg/WseGGUy2AeR/6HKvQTAMu77y7aZtpP7MmtP2UDse2udAoN0ngXXoU/kLGrUOrwOuCJutZ6bIVry03RGSYRXACduRydcAx6MsW2ufEhw3kF9WL+WSpE8JLmt2771pfAuoWoVJwKRnLDUkLlh4ZEJEZ2GJPvHLnCxsl22FqkgL16qCo7GAmLZ/vFs64sicpRsNmuqrTxUtx8/9oaWxwkCDaxoxbOzM1KgckGIqFbtKUPTeANs7CcGVt8xTH1Z1P4kFI24/cInns4IPUkZBi6+q5a8lp3nwKBxmmVCSZJb4621llQF9RtEVqww0eae+k1vX79nnDaP/5maD9vgvG1L4AG9ecbcoGaAscKQDYYswSVZAnUOXyjgD0LxVMC15cuqToe6Sn4nBlrKjQ=="
