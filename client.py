#!/usr/bin/env python2.7

from wallet import MyIOTA
import sys
import random
import time
from MAM import MAM

# wallet.py
# MAM.py

def send_file(iota, filename, source_addr, dest_addr):
    mam = MAM(iota)

    transfer_value = 0

    # These values really don't matter when transfer value = 0
    inputs, change_addr = iota.get_inputs(transfer_value)

    task_id = random.randint(0, 1000)

    #output1 = iota.prepare_transfer(transfer_value, dest_addr, tag = 'TEST', msg = 'HELLO')
    outputs = mam.get_transactions_as_file_buffer(filename, 500, task_id, source_addr, dest_addr)

    iota.send_transfer(transfer_value, inputs, outputs, change_addr)

    return task_id

def send_iota(iota, transfer_value, dest_addr):
    pass

# Set your SEED.
SEED = 'G9OJZJEJFHFDRET9VBMSJEQEJSMPJHTSEZHYSXIFASRQFHDWMQHVGBSHHKIVXBTVDOLBYZCQJMFYEWTEB'

if len(sys.argv) < 2:
    print '[use] ./client.py task_file.py dest_addr'
    sys.exit(0)

# Let's create our connection.
iota = MyIOTA('http://localhost:14265', SEED)

filename = sys.argv[1]
dest_addr = iota.Address(sys.argv[2])

# Init the wallet
iota.init_wallet()

if iota.is_empty_wallet() or iota.is_all_addr_used():
    #iota.make_addr_list(start_index = 0, n = 10)
    iota.get_more_addr(n = 10)

print 'Your total fund is: ', iota.get_total_fund()

# any addr for source addr
source_addr = iota.get_any_addr()

print 'Sending {0} to {1}...'.format(0, iota.s_addr(dest_addr))
task_file = './{0}'.format(sys.argv[1])
task_id = send_file(iota, task_file, source_addr, dest_addr)

sys.exit()
while True:
    print 'Receving...'

    txn_list = iota.find_transactions()

    for txn in iota.get_info_transactions(txn_list):
        confirmed_t, addr_t, value_t, tag_t, msg_t = txn

        t = TryteString(tag_t)
        tag = t.decode()

        if tasks.check_tag(tag):
            m = TryteString(msg_t)
            msg = m.decode()

            tasks.add_task(tag, msg)


        #print '------', confirmed_t, addr_t, value_t

        print msg_t

    time.sleep(5)