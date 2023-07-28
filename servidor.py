import servico_pb2
import servico_pb2_grpc
from concurrent import futures
import grpc


class Servidor(servico_pb2_grpc.RotaMensagemServicer):
    def GetMensagem(self, request, context):
        print("Recebendo pedido de mensagem")
        return servico_pb2.Resposta(mensagem = f'mensagem recebida, {request.nome}')

    def ListMensagemCliente(self, request, context):
        print("Recebendo pedido de lista de mensagens")
       
        mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3"]

        for mensagem in mensagens:
            
            yield servico_pb2.Resposta(mensagem=mensagem)

    def ListMensagemAmbos(self, request_iterator, context):
        print("Recebendo pedido de lista de mensagens bidirecional")
        for request in request_iterator:
            
            mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3"]

            for mensagem in mensagens:
                
                yield servico_pb2.Resposta(mensagem=mensagem)

    def ListMensagemServidor(self, request, context):
        print("Recebendo pedido de lista de mensagens do cliente")
        
        mensagens = ["Mensagem 1", "Mensagem 2", "Mensagem 3"]

        for mensagem in mensagens:
            
            yield servico_pb2.Resposta(mensagem=mensagem)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servico_pb2_grpc.add_RotaMensagemServicer_to_server(Servidor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()