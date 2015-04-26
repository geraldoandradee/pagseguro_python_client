#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

class StatusValidator():
    CODES = [1,2,3,4,5,6,7,8,9]
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

    @classmethod
    def validate(cls, code):
        return code in cls.CODES

    @classmethod
    def get_message(cls, code):
        return cls.MESSAGES[code]

class ItemValidator():

    @classmethod
    def validate(cls, item):
        if item.itemId and item.itemWeight and item.itemQuantity and item.itemAmount and item.itemDescription:
            return True

        return False

class PagseguroValidator():

    @classmethod
    def validate(cls, item):
        pass

    @staticmethod
    def validate_cpf(self, cpf):

        if (len(cpf) != 11 or not cpf.isdigit()):
            return False

        digito = {}
        digito[0] = 0
        digito[1] = 0
        a=10
        total=0
        for c in range(0,2):
            for i in range(0,(8+c+1)):
                total=total+int(cpf[i])*a
                a=a-1
            digito[c]=int(11-(total%11))
            a=11
        total=0

        if (int(cpf[9]) == int(digito[0]) and int(cpf[10]) == int(digito[1])):
            return True
