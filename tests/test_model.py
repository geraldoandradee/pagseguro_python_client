#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

import unittest


class ModelTest(unittest.TestCase):
    def test_model_pagseguro_exists(self):
        try:
            from pagseguro_python_client.models import Pagseguro
        except ImportError:
            self.fail("Model Pagseguro must exists")

    def test_model_base_exists(self):
        try:
            from pagseguro_python_client.models import Base
        except ImportError:
            self.fail("Model Base must exists")

    def test_model_address_exists(self):
        try:
            from pagseguro_python_client.models import Address
        except ImportError:
            self.fail("Model Address must exists")


class BaseModelTest(unittest.TestCase):

    def setUp(self):
        try:
            from pagseguro_python_client.models import Address
        except ImportError:
            self.fail("Address must exists to this test work properly")

        self.address = Address(senderName='Jose Comprador', senderAreaCode=11, senderPhone='56273440',
                  senderEmail='comprador@uol.com.br', shippingType=1,
                  shippingAddressStreet='Av. Brig. Faria Lima', shippingAddressNumber=1384,
                  shippingAddressComplement='5o andar',
                  shippingAddressDistrict='Jardim Paulistano', shippingAddressPostalCode='01452002',
                  shippingAddressCity='Sao Paulo',
                  shippingAddressState='SP', shippingAddressCountry='BRA')

    def test_dict_conversion_exists(self):
        self.assertTrue("__dict__" in dir(self.address))

    def test_dict_conversion(self):
        result = self.address.__dict__()
        self.assertTrue('senderName' in result, msg="sender_name must exist in address object")
        self.assertEqual(result['senderName'], 'Jose Comprador', msg="sender_name must be equals to 'Jose Comprador'")

    def test_get_pure_attributes(self):
        attributes = self.address._get_pure_attributes()
        self.assertEqual(len(attributes), 13, msg="Address must have 13 attributes")
        for attr in attributes:
            # attr[0]: key
            # attr[1]: value
            self.assertIsInstance(attr, tuple, msg="Return of this iteraction must be a tuple (attr_name, value)")
            self.assertEqual(attr[1], getattr(self.address, attr[0]), msg="Attribute not found in object address")


    def test_underscore_to_camelcase(self):
        # for attr in ['', 'senderAreaCode', 'senderPhone', ]
        self.assertEqual('senderName', self.address.underscore_to_camelcase('senderName'), msg="The camelization must work either with camelized names")
        self.assertEqual('senderName', self.address.underscore_to_camelcase('sender_name'), msg="The camelization must translate sender_name to senderName")
        self.assertEqual('senderName', self.address.underscore_to_camelcase('sender_Name'), msg="The camelization must translate sender_Name to senderName")
        self.assertEqual('seNderName', self.address.underscore_to_camelcase('seNder_Name'), msg="The camelization must translate seNder_Name to seNderName")
