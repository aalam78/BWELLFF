# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_gpt_pb2 as chat__gpt__pb2


class ChatGPTStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChatWithGPT = channel.unary_unary(
                '/ChatGPT/ChatWithGPT',
                request_serializer=chat__gpt__pb2.ChatRequest.SerializeToString,
                response_deserializer=chat__gpt__pb2.ChatResponse.FromString,
                )


class ChatGPTServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChatWithGPT(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatGPTServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChatWithGPT': grpc.unary_unary_rpc_method_handler(
                    servicer.ChatWithGPT,
                    request_deserializer=chat__gpt__pb2.ChatRequest.FromString,
                    response_serializer=chat__gpt__pb2.ChatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatGPT', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatGPT(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChatWithGPT(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatGPT/ChatWithGPT',
            chat__gpt__pb2.ChatRequest.SerializeToString,
            chat__gpt__pb2.ChatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)