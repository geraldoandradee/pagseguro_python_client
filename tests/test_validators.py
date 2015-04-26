#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

import unittest
from pagseguro_python_client.models import Item
from pagseguro_python_client.validators import StatusValidator


class ItemValidatorTest(unittest.TestCase):

    def test_item_validator_existence(self):
        try:
            from pagseguro_python_client.validators import ItemValidator
        except ImportError:
            self.fail("ItemValidator must exists")

    def test_item_validator_true_return(self):
        try:
            from pagseguro_python_client.validators import ItemValidator
        except ImportError:
            self.fail("Parameter encoding does not exists")

        validator = ItemValidator.validate(Item(itemId=625, itemDescription="One description here", itemAmount=12.09,
                                                itemQuantity=1, itemWeight=1.00))

        self.assertTrue(validator, msg="This item is valid and needs to return True")

    def test_item_validator_false_return(self):
        try:
            from pagseguro_python_client.validators import ItemValidator
        except ImportError:
            self.fail("Parameter encoding does not exists")

        validator = ItemValidator.validate(Item(None, None, None, None, None))
        self.assertFalse(validator, msg="This item is valid and needs to return False")


class StatusValidatorTest(unittest.TestCase):

    MESSAGES = {
        1: "Aguardando pagamento: o comprador iniciou a transação, mas até o momento o PagSeguro não recebeu nenhuma informação sobre o pagamento.",
        2: "Em análise: o comprador optou por pagar com um cartão de crédito e o PagSeguro está analisando o risco da transação.",
        3: "Paga: a transação foi paga pelo comprador e o PagSeguro já recebeu uma confirmação da instituição financeira responsável pelo processamento.",
        4: "Disponível: a transação foi paga e chegou ao final de seu prazo de liberação sem ter sido retornada e sem que haja nenhuma disputa aberta.",
        5: "Em disputa: o comprador, dentro do prazo de liberação da transação, abriu uma disputa.",
        6: "Devolvida: o valor da transação foi devolvido para o comprador.",
        7: "Cancelada: a transação foi cancelada sem ter sido finalizada.",
        8: "Chargeback debitado: o valor da transação foi devolvido para o comprador.",
        9: "Em contestação: o comprador abriu uma solicitação de chargeback junto à operadora do cartão de crédito.",
    }

    def test_status_validator_existence(self):
        try:
            from pagseguro_python_client.validators import StatusValidator
        except ImportError:
            self.fail("StatusValidator must exists")

    def test_status_validator_get_messages(self):
        for message in range(1, 10):
            self.assertTrue(StatusValidator.get_message(message) == self.MESSAGES[message])

    def test_status_validator_validations_code(self):
        for code in range(1,10): # de 1 a 9
            self.assertTrue(StatusValidator.validate(code), msg="Invalid code %s" % code)