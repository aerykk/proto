# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='service/authentication/authentication.proto',
  package='bnet.protocol.authentication',
  serialized_pb='\n+service/authentication/authentication.proto\x12\x1c\x62net.protocol.authentication\x1a\x11lib/rpc/rpc.proto\x1a!lib/protocol/content_handle.proto\x1a\x19lib/protocol/entity.proto\x1a\x1flib/config/process_config.proto\"Y\n\x11ModuleLoadRequest\x12\x33\n\rmodule_handle\x18\x01 \x02(\x0b\x32\x1c.bnet.protocol.ContentHandle\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"\'\n\x12ModuleLoadResponse\x12\x11\n\tmodule_id\x18\x02 \x01(\x05\":\n\x14ModuleMessageRequest\x12\x11\n\tmodule_id\x18\x01 \x02(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"v\n\x0cLogonRequest\x12\x0f\n\x07program\x18\x01 \x01(\t\x12\x10\n\x08platform\x18\x02 \x01(\t\x12\x0e\n\x06locale\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x13\n\x0blistener_id\x18\x05 \x01(\x04\x12\x0f\n\x07version\x18\x06 \x01(\t\"h\n\rLogonResponse\x12(\n\x07\x61\x63\x63ount\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12-\n\x0cgame_account\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.EntityId\"\xa6\x01\n\x14\x41uthenticationConfig\x12.\n\x06module\x18\x01 \x03(\x0b\x32\x1e.bnet.protocol.config.Resource\x12\x15\n\rallow_version\x18\x02 \x03(\t\x12\x14\n\x0c\x64\x65ny_version\x18\x03 \x03(\t\x12\x31\n\tagreement\x18\x04 \x03(\x0b\x32\x1e.bnet.protocol.config.Resource\"5\n\x11\x41uthModuleVariant\x12\x10\n\x08platform\x18\x01 \x02(\t\x12\x0e\n\x06handle\x18\x02 \x02(\t\"T\n\x10\x41uthModuleConfig\x12@\n\x07variant\x18\x01 \x03(\x0b\x32/.bnet.protocol.authentication.AuthModuleVariant\"1\n\x13\x41uthAgreementLocale\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0e\n\x06handle\x18\x02 \x02(\t\"\x81\x01\n\rAuthAgreement\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0f\n\x07program\x18\x02 \x02(\t\x12\x0e\n\x06scheme\x18\x03 \x02(\r\x12\x41\n\x06locale\x18\x04 \x03(\x0b\x32\x31.bnet.protocol.authentication.AuthAgreementLocale2\xe3\x01\n\x14\x41uthenticationClient\x12o\n\nModuleLoad\x12/.bnet.protocol.authentication.ModuleLoadRequest\x1a\x30.bnet.protocol.authentication.ModuleLoadResponse\x12Z\n\rModuleMessage\x12\x32.bnet.protocol.authentication.ModuleMessageRequest\x1a\x15.bnet.protocol.NoData2\xd4\x01\n\x14\x41uthenticationServer\x12`\n\x05Logon\x12*.bnet.protocol.authentication.LogonRequest\x1a+.bnet.protocol.authentication.LogonResponse\x12Z\n\rModuleMessage\x12\x32.bnet.protocol.authentication.ModuleMessageRequest\x1a\x15.bnet.protocol.NoDataB\x03\x80\x01\x01')




_MODULELOADREQUEST = descriptor.Descriptor(
  name='ModuleLoadRequest',
  full_name='bnet.protocol.authentication.ModuleLoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='module_handle', full_name='bnet.protocol.authentication.ModuleLoadRequest.module_handle', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='bnet.protocol.authentication.ModuleLoadRequest.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=191,
  serialized_end=280,
)


_MODULELOADRESPONSE = descriptor.Descriptor(
  name='ModuleLoadResponse',
  full_name='bnet.protocol.authentication.ModuleLoadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='module_id', full_name='bnet.protocol.authentication.ModuleLoadResponse.module_id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=282,
  serialized_end=321,
)


_MODULEMESSAGEREQUEST = descriptor.Descriptor(
  name='ModuleMessageRequest',
  full_name='bnet.protocol.authentication.ModuleMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='module_id', full_name='bnet.protocol.authentication.ModuleMessageRequest.module_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='bnet.protocol.authentication.ModuleMessageRequest.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=323,
  serialized_end=381,
)


_LOGONREQUEST = descriptor.Descriptor(
  name='LogonRequest',
  full_name='bnet.protocol.authentication.LogonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.authentication.LogonRequest.program', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='platform', full_name='bnet.protocol.authentication.LogonRequest.platform', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='locale', full_name='bnet.protocol.authentication.LogonRequest.locale', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='email', full_name='bnet.protocol.authentication.LogonRequest.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='listener_id', full_name='bnet.protocol.authentication.LogonRequest.listener_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version', full_name='bnet.protocol.authentication.LogonRequest.version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=383,
  serialized_end=501,
)


_LOGONRESPONSE = descriptor.Descriptor(
  name='LogonResponse',
  full_name='bnet.protocol.authentication.LogonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='account', full_name='bnet.protocol.authentication.LogonResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_account', full_name='bnet.protocol.authentication.LogonResponse.game_account', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=503,
  serialized_end=607,
)


_AUTHENTICATIONCONFIG = descriptor.Descriptor(
  name='AuthenticationConfig',
  full_name='bnet.protocol.authentication.AuthenticationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='module', full_name='bnet.protocol.authentication.AuthenticationConfig.module', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='allow_version', full_name='bnet.protocol.authentication.AuthenticationConfig.allow_version', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='deny_version', full_name='bnet.protocol.authentication.AuthenticationConfig.deny_version', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='agreement', full_name='bnet.protocol.authentication.AuthenticationConfig.agreement', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=610,
  serialized_end=776,
)


_AUTHMODULEVARIANT = descriptor.Descriptor(
  name='AuthModuleVariant',
  full_name='bnet.protocol.authentication.AuthModuleVariant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='platform', full_name='bnet.protocol.authentication.AuthModuleVariant.platform', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handle', full_name='bnet.protocol.authentication.AuthModuleVariant.handle', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=778,
  serialized_end=831,
)


_AUTHMODULECONFIG = descriptor.Descriptor(
  name='AuthModuleConfig',
  full_name='bnet.protocol.authentication.AuthModuleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='variant', full_name='bnet.protocol.authentication.AuthModuleConfig.variant', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=833,
  serialized_end=917,
)


_AUTHAGREEMENTLOCALE = descriptor.Descriptor(
  name='AuthAgreementLocale',
  full_name='bnet.protocol.authentication.AuthAgreementLocale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.authentication.AuthAgreementLocale.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handle', full_name='bnet.protocol.authentication.AuthAgreementLocale.handle', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=919,
  serialized_end=968,
)


_AUTHAGREEMENT = descriptor.Descriptor(
  name='AuthAgreement',
  full_name='bnet.protocol.authentication.AuthAgreement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='bnet.protocol.authentication.AuthAgreement.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.authentication.AuthAgreement.program', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scheme', full_name='bnet.protocol.authentication.AuthAgreement.scheme', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='locale', full_name='bnet.protocol.authentication.AuthAgreement.locale', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=971,
  serialized_end=1100,
)

import lib.rpc.rpc_pb2
import lib.protocol.content_handle_pb2
import lib.protocol.entity_pb2
import lib.config.process_config_pb2

_MODULELOADREQUEST.fields_by_name['module_handle'].message_type = lib.protocol.content_handle_pb2._CONTENTHANDLE
_LOGONRESPONSE.fields_by_name['account'].message_type = lib.protocol.entity_pb2._ENTITYID
_LOGONRESPONSE.fields_by_name['game_account'].message_type = lib.protocol.entity_pb2._ENTITYID
_AUTHENTICATIONCONFIG.fields_by_name['module'].message_type = lib.config.process_config_pb2._RESOURCE
_AUTHENTICATIONCONFIG.fields_by_name['agreement'].message_type = lib.config.process_config_pb2._RESOURCE
_AUTHMODULECONFIG.fields_by_name['variant'].message_type = _AUTHMODULEVARIANT
_AUTHAGREEMENT.fields_by_name['locale'].message_type = _AUTHAGREEMENTLOCALE

class ModuleLoadRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODULELOADREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.ModuleLoadRequest)

class ModuleLoadResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODULELOADRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.ModuleLoadResponse)

class ModuleMessageRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODULEMESSAGEREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.ModuleMessageRequest)

class LogonRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGONREQUEST
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.LogonRequest)

class LogonResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGONRESPONSE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.LogonResponse)

class AuthenticationConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHENTICATIONCONFIG
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.AuthenticationConfig)

class AuthModuleVariant(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHMODULEVARIANT
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.AuthModuleVariant)

class AuthModuleConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHMODULECONFIG
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.AuthModuleConfig)

class AuthAgreementLocale(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHAGREEMENTLOCALE
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.AuthAgreementLocale)

class AuthAgreement(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHAGREEMENT
  
  # @@protoc_insertion_point(class_scope:bnet.protocol.authentication.AuthAgreement)


_AUTHENTICATIONCLIENT = descriptor.ServiceDescriptor(
  name='AuthenticationClient',
  full_name='bnet.protocol.authentication.AuthenticationClient',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1103,
  serialized_end=1330,
  methods=[
  descriptor.MethodDescriptor(
    name='ModuleLoad',
    full_name='bnet.protocol.authentication.AuthenticationClient.ModuleLoad',
    index=0,
    containing_service=None,
    input_type=_MODULELOADREQUEST,
    output_type=_MODULELOADRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ModuleMessage',
    full_name='bnet.protocol.authentication.AuthenticationClient.ModuleMessage',
    index=1,
    containing_service=None,
    input_type=_MODULEMESSAGEREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
])

class AuthenticationClient(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _AUTHENTICATIONCLIENT
class AuthenticationClient_Stub(AuthenticationClient):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _AUTHENTICATIONCLIENT


_AUTHENTICATIONSERVER = descriptor.ServiceDescriptor(
  name='AuthenticationServer',
  full_name='bnet.protocol.authentication.AuthenticationServer',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1333,
  serialized_end=1545,
  methods=[
  descriptor.MethodDescriptor(
    name='Logon',
    full_name='bnet.protocol.authentication.AuthenticationServer.Logon',
    index=0,
    containing_service=None,
    input_type=_LOGONREQUEST,
    output_type=_LOGONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ModuleMessage',
    full_name='bnet.protocol.authentication.AuthenticationServer.ModuleMessage',
    index=1,
    containing_service=None,
    input_type=_MODULEMESSAGEREQUEST,
    output_type=lib.rpc.rpc_pb2._NODATA,
    options=None,
  ),
])

class AuthenticationServer(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _AUTHENTICATIONSERVER
class AuthenticationServer_Stub(AuthenticationServer):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _AUTHENTICATIONSERVER

# @@protoc_insertion_point(module_scope)
