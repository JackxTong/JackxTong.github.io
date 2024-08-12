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
大端和小端定义的是数据如何存储在物理内存上，比如存储一个long：0X12 34 56 78

- **大端字节序（Big Endian）**：最高有效字节存储在最小的内存地址 

- **小端字节序（Small Endian）**：最高有效字节存储在最大的内存地址


因为数据的存储是以字节为单位（每个地址可以存储一个字节），将大端转换为小端只需要逆转字节的顺序

值得注意的是，是有数据收到大端和小端的影响，如short，int，long。字符串string的储存方式并不受影响。另外，char也不会受影响，因为本身只有一个字节。

### 网络字节序
不同的机器会有不同的大端小端定义。intel X86架构使用的是小端，而Arm架构的CPU则是大端。如何确保在不同机器之间传输数据不会出错呢？

UDP/TCP/IP协议规定:把接收到的第一个字节当作高位字节看待，也就是统一规定，传输数据的时候使用大端

### C# 中的data stream

### 引用

https://www.cnblogs.com/ArrozZhu/p/8384218.html