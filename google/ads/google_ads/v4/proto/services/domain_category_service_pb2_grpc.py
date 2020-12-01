# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import domain_category_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_domain__category__pb2
from google.ads.google_ads.v4.proto.services import domain_category_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_domain__category__service__pb2


class DomainCategoryServiceStub(object):
  """Proto file describing the DomainCategory Service.

  Service to fetch domain categories.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDomainCategory = channel.unary_unary(
        '/google.ads.googleads.v4.services.DomainCategoryService/GetDomainCategory',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_domain__category__service__pb2.GetDomainCategoryRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_domain__category__pb2.DomainCategory.FromString,
        )


class DomainCategoryServiceServicer(object):
  """Proto file describing the DomainCategory Service.

  Service to fetch domain categories.
  """

  def GetDomainCategory(self, request, context):
    """Returns the requested domain category.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DomainCategoryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDomainCategory': grpc.unary_unary_rpc_method_handler(
          servicer.GetDomainCategory,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_domain__category__service__pb2.GetDomainCategoryRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_domain__category__pb2.DomainCategory.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.DomainCategoryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))