from __future__ import print_function

import grpc
import servico_pb2
import servico_pb2_grpc


import logging

def Inicializar():
    print("Encontrando mensagens...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = servico_pb2_grpc.RotaMensagemStub(channel)
        print("-------------- GetMensagem --------------")
        response = stub.GetMensagem(servico_pb2.EnvioMensagem(nome='Felipe'))
        print("Resposta recebida: " + response.mensagem)

        print("-------------- ListMensagemCliente --------------")
        response_iterator = stub.ListMensagemCliente(servico_pb2.EnvioMensagem(nome="Bob"))
        for response in response_iterator:
            print("Resposta do servidor:", response.mensagem)

        print("-------------- ListMensagemAmbos --------------")

        request_iterator = iter([
            servico_pb2.EnvioMensagem(nome="Alice"),
            servico_pb2.EnvioMensagem(nome="Carol"),
            servico_pb2.EnvioMensagem(nome="Dave"),
        ])

        response_iterator = stub.ListMensagemAmbos(request_iterator)
        for response in response_iterator:
            print("Resposta do servidor:", response.mensagem)

        print("-------------- ListMensagemServidor --------------")

        response_iterator = stub.ListMensagemServidor(servico_pb2.EnvioMensagem(nome="Eve"))
        for response in response_iterator:
            print("Resposta do servidor:", response.mensagem)
if __name__ == '__main__':
    logging.basicConfig()
    Inicializar()