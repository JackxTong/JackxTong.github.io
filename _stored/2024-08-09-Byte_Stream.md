---
layout:     post
title:      Byte Stream
subtitle:   C#的数据流处理
date:       2024-08-09
author:     JY
header-img: img/post-bg-BJJ.jpg
catalog: true
tags:
    - Data Stream
    - C#
---

## 前言

## 正文
### 大端和小端
大端和小端定义的是数据如何存储在物理内存上，比如存储一个long：0X 12 34 56 78

- **大端字节序（Big Endian）**：最高有效字节存储在最小的内存地址 
在内存上就是：12 34 56 78 （地址左边最小）

- **小端字节序（Small Endian）**：最高有效字节存储在最大的内存地址
在内存上就是：78 56 34 12


因为数据的存储是以字节为单位（每个地址可以存储一个字节），将大端转换为小端只需要逆转字节的顺序

值得注意的是，是有数据收到大端和小端的影响，如short，int，long。字符串string的储存方式并不受影响。另外，char也不会受影响，因为本身只有一个字节。

### 网络字节序
不同的机器会有不同的大端小端定义。intel X86架构使用的是小端，而Arm架构的CPU则是大端。如何确保在不同机器之间传输数据不会出错呢？

UDP/TCP/IP协议规定:把接收到的第一个字节当作高位字节看待，也就是统一规定，传输数据的时候使用大端

### C# 中的data stream
C# 中提供了 MemoryStream，Binary Writer, Binary Reader 作为byte流的读写的工具。不过值得注意的是，Binary Writer 和 Binary Reader在读写的时候，并没有考虑网络字节序的问题。这个Java中的ByteBuffer不同，ByteBuffer内部对这些进行了处理

```C#
byte[] byteArray = new byte[] { 0x00, 0x00, 0x00, 0x01 };

using (MemoryStream msIn = new MemoryStream(byteArray))
using (BinaryReader brIn = new BinaryReader(msIn)){
    var result = brIn.ReadInt32();
    Console.Write(result);
}

// output: 16777216
```
上一段代码中，byteArray代表一个Int32的1，是大端的形式。如果网络里传过来一个 1，这就是我们收到的数据。但BinaryReader默认这个byte串用的是本机的存储方式，也就是小端，所以最后哦输出的是对0x 01 00 00 00 的解析：16777216

```C#
Int32 a = 1;
byte[] byteArray;

using (MemoryStream msIn = new MemoryStream(32))
using (BinaryWriter writer = new BinaryWriter(msIn, Encoding.UTF8)){
    writer.Write(a);
    byteArray = msIn.ToArray();
}

foreach (byte b in byteArray)
    Console.Write(b + " ");

// output: 1 0 0 0
```
同样的，使用binary writer向byte stream中写入数字时，也会产生类似的问题。上面的代码中，需要写入的数字是1，而写入的数据是以小端形式存储的

```C#
long a = 1;
var ret = BitConverter.GetBytes(a);

foreach (var c in ret)
    Console.Write($"   {c}");
// output: 1 0 0 0 0 0 0 0
```

BitConverter 也是一样

解决这个问题，你可以使用 ```IPAddress.HostToNetworkOrder```， 或者直接手动```Array.Reverse```。
### 引用

https://www.cnblogs.com/ArrozZhu/p/8384218.html