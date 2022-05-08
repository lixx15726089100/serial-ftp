# 内外网的数据交换，已经不能使用U盘了，KVM加U盘的神奇早已失效了。
# 基于MAVLINK实现的ftp因为数据保存不当，只找到半成品，非常可惜
# 选中文件，右键发送即可将文件从串口发出去，接收则是自动的。
# 固定长度的包，255（文件名） + 数据 + 结束符号
# 目前使用给ch340转RS232串口，速率应该不高，但是有可能是python库的限制，串口还有很多其他功能，也要想办法用于简化应用
import serial
import os

#由于需要全双工工作，特设立标注位
serial_busyflag = 0

filepath = os.getcwd() + '\\testfile.jpg'

# 读取文件二进制流
with open(filepath, 'rb') as f:
    data = f.read()
# 建立一个列表
bytes_stream = []
# 先把文件名字作为第一个包，该包需要有一定的特征，方便检查确认未文件名
filename = filepath.split('\\')[-1] + '|' + str(len(data))
filename_bytesstream = (bytes(filename, encoding='UTF-8')).rjust(256, bytes('$', encoding='UTF-8'))
bytes_stream.append(filename_bytesstream)

# 将数据打包，最后一个数据包是极其难以处理的，所以还得把数据流的长度加入第一个包中，方便解析
if len(data) % 256 == 0:
    pack_count = int(len(data) / 256)
else:
    pack_count = int(len(data) / 256) + 1

for i in range(0,pack_count):



print(bytes_stream)
# 读取二进制流长度，拆分打包
print(len(data),type(data))
print(data[110974])
# print(data)
# 由于电脑的资源非常丰富，不需要指针之类的东西，完全可以直接多占内存，将数据一下子制备好
# 制备未列表，内容是文件的字节流，256个一包