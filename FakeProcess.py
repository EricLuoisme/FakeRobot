import Client

# 超时
Client.send('对本期完成的凭证进行提交处理')
print(Client.receive())
print(Client.receive())
print(Client.receive())

# # 执行查看
# Client.send('对本期完成的凭证进行提交处理')
# print(Client.receive())
# print(Client.receive())
# Client.send('好')
# print(Client.receive())

