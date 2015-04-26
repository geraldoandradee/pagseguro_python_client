#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
from pagseguro_python_client.validators import ItemValidator
import inspect
import inflection
import json


class Base(object):
    def underscore_to_camelcase(self, value, uppercase_first_letter=False):
        return inflection.camelize(value, uppercase_first_letter)

    def __dict__(self):
        data = {}
        for attribute in self._get_pure_attributes():
            data[self.underscore_to_camelcase(attribute[0])] = attribute[1]
        return data

    def serialize(self):
        data = {}
        for attribute in self._get_pure_attributes():
            data[self.underscore_to_camelcase(attribute[0])] = attribute[1]
        return json.dumps(data)

    def _get_pure_attributes(self):
        """
        Borrowed from http://stackoverflow.com/questions/9058305/getting-attributes-of-a-class
        """
        return [(i, getattr(self, i)) for i in self.__attributes__]


class Address(Base):
    __attributes__ = ['sender_name', 'sender_area_code', 'sender_phone', 'sender_email', 'shipping_type',
                      'shipping_address_street', 'shipping_address_number', 'shipping_address_complement',
                      'shipping_address_district', 'shipping_address_postal_code', 'shipping_address_city',
                      'shipping_address_state', 'shipping_address_country']

    def __init__(self, senderName=None, senderAreaCode=None, senderPhone=None, senderEmail=None, shippingType=None,
                 shippingAddressStreet=None, shippingAddressNumber=None, shippingAddressComplement=None,
                 shippingAddressDistrict=None, shippingAddressPostalCode=None, shippingAddressCity=None,
                 shippingAddressState=None, shippingAddressCountry=None):
        # dados do comprador
        self.sender_name = senderName
        self.sender_area_code = senderAreaCode
        self.sender_phone = senderPhone
        self.sender_email = senderEmail

        # endereco do comprador
        self.shipping_type = shippingType
        self.shipping_address_street = shippingAddressStreet
        self.shipping_address_number = shippingAddressNumber
        self.shipping_address_complement = shippingAddressComplement
        self.shipping_address_district = shippingAddressDistrict
        self.shipping_address_postal_code = shippingAddressPostalCode
        self.shipping_address_city = shippingAddressCity
        self.shipping_address_state = shippingAddressState
        self.shipping_address_country = shippingAddressCountry


class Item(Base):
    __attributes__ = ['item_id', 'sender_area_code', 'sender_phone', 'sender_email', 'shipping_type',
                      'shipping_address_street', 'shipping_address_number', 'shipping_address_complement',
                      'shipping_address_district', 'shipping_address_postal_code', 'shipping_address_city',
                      'shipping_address_state', 'shipping_address_country']

    def __init__(self, itemId, itemDescription, itemAmount, itemQuantity, itemWeight):
        self.itemId = itemId
        self.itemDescription = itemDescription
        self.itemAmount = itemAmount
        self.itemQuantity = itemQuantity
        self.itemWeight = itemWeight


class Status(object):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class Pagseguro(object):
    def __init__(self, email=None, token=None, currency=None, items=None, reference=None, senderName=None,
                 senderAreaCode=None, senderPhone=None, senderEmail=None, shippingType=None, shippingAddressStreet=None,
                 shippingAddressNumber=None, shippingAddressComplement=None, shippingAddressDistrict=None,
                 shippingAddressPostalCode=None, shippingAddressCity=None, shippingAddressState=None,
                 shippingAddressCountry=None):
        self.email = email
        self.token = token
        self.currency = currency
        self.items = [] if items is None else items
        self.reference = reference
        self.senderName = senderName
        self.senderAreaCode = senderAreaCode
        self.senderPhone = senderPhone
        self.senderEmail = senderEmail
        self.shippingType = shippingType
        self.shippingAddressStreet = shippingAddressStreet
        self.shippingAddressNumber = shippingAddressNumber
        self.shippingAddressComplement = shippingAddressComplement
        self.shippingAddressDistrict = shippingAddressDistrict
        self.shippingAddressPostalCode = shippingAddressPostalCode
        self.shippingAddressCity = shippingAddressCity
        self.shippingAddressState = shippingAddressState
        self.shippingAddressCountry = shippingAddressCountry

    def add_item(self, item):
        if ItemValidator.validate(item):
            for i in self.items:
                if i.itemId == item.itemId:
                    return False

            self.items.append(item)
            return True


"""
"email=suporte@lojamodelo.com.br\
    &token=95112EE828D94278BD394E91C4388F20\
    &currency=BRL\
    &itemId1=0001\
    &itemDescription1=Notebook Prata\
    &itemAmount1=24300.00\
    &itemQuantity1=1\
    &itemWeight1=1000\
    &itemId2=0002\
    &itemDescription2=Notebook Rosa\
    &itemAmount2=25600.00\
    &itemQuantity2=2\
    &itemWeight2=750\
    &reference=REF1234\
    &senderName=Jose Comprador\
    &senderAreaCode=11\
    &senderPhone=56273440\
    &senderEmail=comprador@uol.com.br\
    &shippingType=1\
    &shippingAddressStreet=Av. Brig. Faria Lima\
    &shippingAddressNumber=1384\
    &shippingAddressComplement=5o andar\
    &shippingAddressDistrict=Jardim Paulistano\
    &shippingAddressPostalCode=01452002\
    &shippingAddressCity=Sao Paulo\
    &shippingAddressState=SP\
    &shippingAddressCountry=BRA"
"""


class CheckoutResponse(Base):
    """
        <?xml version="1.0" encoding="ISO-8859-1"?>
        <checkout>
            <code>8CF4BE7DCECEF0F004A6DFA0A8243412</code>
            <date>2010-12-02T10:11:28.000-02:00</date>
        </checkout>
    """

    def __init__(self, code=None, date=None):
        self.code = code
        self.date = date


class Error(Base):
    """
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <errors>
        <error>
            <code>11004</code>
            <message>Currency is required.</message>
        </error>
        <error>
            <code>11005</code>
            <message>Currency invalid value: 100</message>
        </error>
    </errors>
    """

    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message