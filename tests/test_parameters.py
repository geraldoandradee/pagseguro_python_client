#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

import unittest

class ParametersTest(unittest.TestCase):

    def test_parameter_exists(self):
        try:
            from pagseguro_python_client import ENDPOINT
        except ImportError:
            self.fail("Parameter endpoint does not exists")

    def test_default_encoding_existance(self):
        try:
            from pagseguro_python_client import ENCODING
        except ImportError:
            self.fail("Parameter encoding does not exists")

    def test_default_content_type_existance(self):
        try:
            from pagseguro_python_client import CONTENT_TYPE
        except ImportError:
            self.fail("Parameter content_type does not exists")

    def test_default_content_type_value(self):
        try:
            from pagseguro_python_client import CONTENT_TYPE
            self.assertEqual(CONTENT_TYPE, 'application/x-www-form-urlencoded', msg='Wrong content type value')
        except ImportError:
            self.fail("Parameter content_type does not exists")

    def test_default_encoding_must_be_utf_8(self):
        try:
            from pagseguro_python_client import ENCODING
            self.assertEqual(ENCODING, 'UTF-8', msg='Wrong default encoding declaration')

        except ImportError:
            self.fail("Parameter encoding does not exists")

    def test_content_type_possibilities(self):
        """
        https://pagseguro.uol.com.br/v2/guia-de-integracao/api-de-pagamentos.html#!v2-item-api-de-pagamentos-parametros-http

        Codificação de caracteres.

        Especifica a codificação de caracteres usada nos parâmetros enviados.

        Presença: Opcional.
        Tipo: Texto.
        Formato: Os valores aceitos são ISO-8859-1 e UTF-8.

        :return:
        """
        try:
            from pagseguro_python_client import ENCODING
            self.assertTrue(ENCODING == 'ISO-8859-1' or ENCODING == 'UTF-8', msg='Wrong content type value')
        except ImportError:
            self.fail("Parameter content_type does not exists")