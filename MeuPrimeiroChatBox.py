import os
from typing import Sized

def processar_resposta(resposta,nome):
    if resposta == '1':
        print('A Lei Maria da Penha foi sancionada em 7 de agosto de 2006 pelo presidente Luiz Inácio Lula da Silva.{os.linesep} Com 46 artigos distribuídos em sete títulos, ela cria mecanismos para prevenire coibir a violência doméstica e familiar contra a mulher em conformidade com a Constituição Federal e os tratados internacionais ratificados pelo Estado brasileiro.')
    if resposta == '2':
        print(f'- Polícia Rodoviária Federa{os.linesep}- Polícia Federal{os.linesep}- Polícias Civis{os.linesep}- Polícias Militares{os.linesep}- Corpos de Bombeiros Militares{os.linesep}- Guardas Municipais{os.linesep}- Órgãos do Sistema Penitenciário{os.linesep}- Institutos Oficiais de Criminalística, Medicina Legal e Identificação{os.linesep}- Secretaria Nacional de Segurança Pública{os.linesep}- Secretarias Estaduais de Segurança Pública ou congêneres{os.linesep}- Secretaria Nacional de Proteção e Defesa Civil{os.linesep}- Secretaria Nacional de Política Sobre Drogas{os.linesep}- Agentes de Trânsito{os.linesep}- Guarda Portuária')
    if resposta == '3':
        print(f'Ao registrar uma ocorrência com informações semelhantes, mesmo bairro, telefone e natureza, é apresentado ao atendente uma relação de ocorrências com essas semelhanças.{os.linesep}O usuário poderá conferir e verificando que se trata da mesma ocorrência, poderá marcar a opção de ocorrência complementar. Dessa forma a ocorrência chegará na tela do operador, vinculada a ocorrência anterior. ')
    if resposta == '4':
        print('A exclusão de um BO somente é permitida se ele estiver na situação RASCUNHO. BO´s na situação REGISTRADO ou FINALIZADO não poderão ser excluídos')
    if resposta == 'Resposta':
        print('R:')
        

def start():
    #Apresentar o chatbox
    print('Olá! Bem vindo ao ChatBox da Segurança Pública! Aqui você encontra as respostas das perguntas mais recorrentes relacionadas ao tema.')
    # Pedir o nome
    nome = input('Digite seu nome:')
    # Pedir o e-mail
    email = input('Digite seu e-mail:')
    # Pedir CPF
    cpf = input('CPF:')
    while True:
        # Oferecer o menu de opções
        resposta = input(f' Qual a sua dúvida a respeito da Segurança Pública?{os.linesep} [1] - Qual resumo da Lei Maria da Penha?{os.linesep} [2] - Quem são os integrantes do Sistema Único de Segurança Pública?{os.linesep} [3] - É possível registrar uma ocorrência a uma outra que já foi registrada?{os.linesep} [4] - Como excluir um BO?{os.linesep} Resposta:')
        # Processar a resposta enviada
        processar_resposta(resposta,nome)
    
if __name__ == '__main__':
    start()