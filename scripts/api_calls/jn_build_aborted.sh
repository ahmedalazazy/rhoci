#!/bin/bash
# Jenkins Notification build started
curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/api/jenkins_update -d '{"name":"DFG-network-neutron-33-unit-rhos","display_name":"DFG-network-neutron-33-unit-rhos","url":"job/DFG-network-neutron-33-unit-rhos/","build":{"full_url":"https://rhos-qe-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/DFG-network-neutron-33-unit-rhos/292/","number":292,"queue_id":19805,"timestamp":1553709757930,"phase":"COMPLETED","status":"ABORTED","url":"job/DFG-network-neutron-33-unit-rhos/292/","scm":{},"parameters":{"GERRIT_BRANCH":"rhos-10.0-patches","DISABLE_CLEANUP":"false","GERRIT_REFSPEC":"+refs/heads/$GERRIT_BRANCH:refs/remotes/origin/$GERRIT_BRANCH","ANSIBLE_VERBOSITY":"1","OCTARIO_GERRIT_CHANGE":"","IR_GERRIT_CHANGE":""},"log":"","artifacts":{".envrc":{"archive":"https://rhos-qe-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/DFG-network-neutron-33-unit-rhos/292/artifact/.envrc"},".sh/ir-install.log":{"archive":"https://rhos-qe-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/DFG-network-neutron-33-unit-rhos/292/artifact/.sh/ir-install.log"},".sh/run.sh":{"archive":"https://rhos-qe-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/DFG-network-neutron-33-unit-rhos/292/artifact/.sh/run.sh"}}}}'