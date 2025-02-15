# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chatbot_pb2 as chatbot__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.Greeter/SayHello',
                request_serializer=chatbot__pb2.HelloRequest.SerializeToString,
                response_deserializer=chatbot__pb2.HelloReply.FromString,
                )
        self.SayHelloStreamReply = channel.unary_stream(
                '/helloworld.Greeter/SayHelloStreamReply',
                request_serializer=chatbot__pb2.HelloRequest.SerializeToString,
                response_deserializer=chatbot__pb2.HelloReply.FromString,
                )
        self.SayHelloBidiStream = channel.stream_stream(
                '/helloworld.Greeter/SayHelloBidiStream',
                request_serializer=chatbot__pb2.HelloRequest.SerializeToString,
                response_deserializer=chatbot__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloStreamReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloBidiStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=chatbot__pb2.HelloRequest.FromString,
                    response_serializer=chatbot__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloStreamReply': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloStreamReply,
                    request_deserializer=chatbot__pb2.HelloRequest.FromString,
                    response_serializer=chatbot__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloBidiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.SayHelloBidiStream,
                    request_deserializer=chatbot__pb2.HelloRequest.FromString,
                    response_serializer=chatbot__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/SayHello',
            chatbot__pb2.HelloRequest.SerializeToString,
            chatbot__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloStreamReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.Greeter/SayHelloStreamReply',
            chatbot__pb2.HelloRequest.SerializeToString,
            chatbot__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloBidiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/helloworld.Greeter/SayHelloBidiStream',
            chatbot__pb2.HelloRequest.SerializeToString,
            chatbot__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
