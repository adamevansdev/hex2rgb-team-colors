#!/usr/bin/env python
# -*- coding: utf-8 -*-


def hex2rgb(hex):
  hex = hex.lstrip('#')
  hlen = len(hex)
  return ' '.join(
    map(str, tuple(int(hex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3)))
  )
