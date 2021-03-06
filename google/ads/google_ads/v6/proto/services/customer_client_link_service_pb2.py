# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/services/customer_client_link_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.resources import customer_client_link_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_customer__client__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/services/customer_client_link_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\036CustomerClientLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/ads/googleads/v6/services/customer_client_link_service.proto\x12 google.ads.googleads.v6.services\x1a<google/ads/googleads/v6/resources/customer_client_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"j\n\x1cGetCustomerClientLinkRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+googleads.googleapis.com/CustomerClientLink\"\x92\x01\n\x1fMutateCustomerClientLinkRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12U\n\toperation\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v6.services.CustomerClientLinkOperationB\x03\xe0\x41\x02\"\xed\x01\n\x1b\x43ustomerClientLinkOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12G\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v6.resources.CustomerClientLinkH\x00\x12G\n\x06update\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v6.resources.CustomerClientLinkH\x00\x42\x0b\n\toperation\"t\n MutateCustomerClientLinkResponse\x12P\n\x06result\x18\x01 \x01(\x0b\x32@.google.ads.googleads.v6.services.MutateCustomerClientLinkResult\"7\n\x1eMutateCustomerClientLinkResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xc3\x04\n\x19\x43ustomerClientLinkService\x12\xdd\x01\n\x15GetCustomerClientLink\x12>.google.ads.googleads.v6.services.GetCustomerClientLinkRequest\x1a\x35.google.ads.googleads.v6.resources.CustomerClientLink\"M\x82\xd3\xe4\x93\x02\x37\x12\x35/v6/{resource_name=customers/*/customerClientLinks/*}\xda\x41\rresource_name\x12\xfe\x01\n\x18MutateCustomerClientLink\x12\x41.google.ads.googleads.v6.services.MutateCustomerClientLinkRequest\x1a\x42.google.ads.googleads.v6.services.MutateCustomerClientLinkResponse\"[\x82\xd3\xe4\x93\x02=\"8/v6/customers/{customer_id=*}/customerClientLinks:mutate:\x01*\xda\x41\x15\x63ustomer_id,operation\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v6.servicesB\x1e\x43ustomerClientLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_customer__client__link__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETCUSTOMERCLIENTLINKREQUEST = _descriptor.Descriptor(
  name='GetCustomerClientLinkRequest',
  full_name='google.ads.googleads.v6.services.GetCustomerClientLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetCustomerClientLinkRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A-\n+googleads.googleapis.com/CustomerClientLink', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=422,
)


_MUTATECUSTOMERCLIENTLINKREQUEST = _descriptor.Descriptor(
  name='MutateCustomerClientLinkRequest',
  full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=571,
)


_CUSTOMERCLIENTLINKOPERATION = _descriptor.Descriptor(
  name='CustomerClientLinkOperation',
  full_name='google.ads.googleads.v6.services.CustomerClientLinkOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v6.services.CustomerClientLinkOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v6.services.CustomerClientLinkOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v6.services.CustomerClientLinkOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v6.services.CustomerClientLinkOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=574,
  serialized_end=811,
)


_MUTATECUSTOMERCLIENTLINKRESPONSE = _descriptor.Descriptor(
  name='MutateCustomerClientLinkResponse',
  full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=813,
  serialized_end=929,
)


_MUTATECUSTOMERCLIENTLINKRESULT = _descriptor.Descriptor(
  name='MutateCustomerClientLinkResult',
  full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.MutateCustomerClientLinkResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=931,
  serialized_end=986,
)

_MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['operation'].message_type = _CUSTOMERCLIENTLINKOPERATION
_CUSTOMERCLIENTLINKOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CUSTOMERCLIENTLINKOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_customer__client__link__pb2._CUSTOMERCLIENTLINK
_CUSTOMERCLIENTLINKOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_customer__client__link__pb2._CUSTOMERCLIENTLINK
_CUSTOMERCLIENTLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERCLIENTLINKOPERATION.fields_by_name['create'])
_CUSTOMERCLIENTLINKOPERATION.fields_by_name['create'].containing_oneof = _CUSTOMERCLIENTLINKOPERATION.oneofs_by_name['operation']
_CUSTOMERCLIENTLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERCLIENTLINKOPERATION.fields_by_name['update'])
_CUSTOMERCLIENTLINKOPERATION.fields_by_name['update'].containing_oneof = _CUSTOMERCLIENTLINKOPERATION.oneofs_by_name['operation']
_MUTATECUSTOMERCLIENTLINKRESPONSE.fields_by_name['result'].message_type = _MUTATECUSTOMERCLIENTLINKRESULT
DESCRIPTOR.message_types_by_name['GetCustomerClientLinkRequest'] = _GETCUSTOMERCLIENTLINKREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkRequest'] = _MUTATECUSTOMERCLIENTLINKREQUEST
DESCRIPTOR.message_types_by_name['CustomerClientLinkOperation'] = _CUSTOMERCLIENTLINKOPERATION
DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkResponse'] = _MUTATECUSTOMERCLIENTLINKRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkResult'] = _MUTATECUSTOMERCLIENTLINKRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerClientLinkRequest = _reflection.GeneratedProtocolMessageType('GetCustomerClientLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERCLIENTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetCustomerClientLinkRequest)
  })
_sym_db.RegisterMessage(GetCustomerClientLinkRequest)

MutateCustomerClientLinkRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerClientLinkRequest)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkRequest)

CustomerClientLinkOperation = _reflection.GeneratedProtocolMessageType('CustomerClientLinkOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCLIENTLINKOPERATION,
  '__module__' : 'google.ads.googleads.v6.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CustomerClientLinkOperation)
  })
_sym_db.RegisterMessage(CustomerClientLinkOperation)

MutateCustomerClientLinkResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKRESPONSE,
  '__module__' : 'google.ads.googleads.v6.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerClientLinkResponse)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkResponse)

MutateCustomerClientLinkResult = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKRESULT,
  '__module__' : 'google.ads.googleads.v6.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateCustomerClientLinkResult)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkResult)


DESCRIPTOR._options = None
_GETCUSTOMERCLIENTLINKREQUEST.fields_by_name['resource_name']._options = None
_MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['customer_id']._options = None
_MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['operation']._options = None

_CUSTOMERCLIENTLINKSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerClientLinkService',
  full_name='google.ads.googleads.v6.services.CustomerClientLinkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=989,
  serialized_end=1568,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomerClientLink',
    full_name='google.ads.googleads.v6.services.CustomerClientLinkService.GetCustomerClientLink',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERCLIENTLINKREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_customer__client__link__pb2._CUSTOMERCLIENTLINK,
    serialized_options=b'\202\323\344\223\0027\0225/v6/{resource_name=customers/*/customerClientLinks/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomerClientLink',
    full_name='google.ads.googleads.v6.services.CustomerClientLinkService.MutateCustomerClientLink',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMERCLIENTLINKREQUEST,
    output_type=_MUTATECUSTOMERCLIENTLINKRESPONSE,
    serialized_options=b'\202\323\344\223\002=\"8/v6/customers/{customer_id=*}/customerClientLinks:mutate:\001*\332A\025customer_id,operation',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERCLIENTLINKSERVICE)

DESCRIPTOR.services_by_name['CustomerClientLinkService'] = _CUSTOMERCLIENTLINKSERVICE

# @@protoc_insertion_point(module_scope)
