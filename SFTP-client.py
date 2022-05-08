# 内外网的数据交换，已经不能使用U盘了，KVM加U盘的神奇早已失效了。
# 基于MAVLINK实现的ftp因为数据保存不当，只找到半成品，非常可惜
# 选中文件，右键发送即可将文件从串口发出去，接收则是自动的。
# 固定长度的包，255（文件名） + 数据 + 结束符号
# 目前使用给ch340转RS232串口，速率应该不高，但是有可能是python库的限制，串口还有很多其他功能，也要想办法用于简化应用
import serial

#由于需要全双工工作，特设立标注位
serial_busyflag = 0

filepath = 'testfile.jpg'

# 读取文件二进制流
with open(filepath,'rb') as f:
    data = f.read()
print(len(data))