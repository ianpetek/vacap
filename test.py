msg = 656946
msg_enc = msg.to_bytes(3, 'big')
rid = 16
rid_enc = rid.to_bytes(2, 'big')
full_msg = msg_enc + rid_enc


print(int.from_bytes(full_msg[:3], 'big'))
print(int.from_bytes(full_msg[3:], 'big'))
