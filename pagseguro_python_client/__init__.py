#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
import os

ENDPOINT = os.getenv("PAGSEGURO_PYTHON_CLIENT_ENDPOINT", 'https://ws.pagseguro.uol.com.br/v2/checkout')
ENCODING = os.getenv("PAGSEGURO_PYTHON_CLIENT_ENCODING", 'UTF-8')
CONTENT_TYPE = 'application/x-www-form-urlencoded'

