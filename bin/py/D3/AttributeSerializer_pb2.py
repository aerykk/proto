# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='D3/AttributeSerializer.proto',
  package='D3.AttributeSerializer',
  serialized_pb='\n\x1c\x44\x33/AttributeSerializer.proto\x12\x16\x44\x33.AttributeSerializer\x1a\x11\x44\x33/GBHandle.proto\",\n\x0eSavedAttribute\x12\x0b\n\x03key\x18\x01 \x02(\x11\x12\r\n\x05value\x18\x02 \x02(\x11\"x\n\x0fSavedAttributes\x12)\n\tgb_handle\x18\x01 \x02(\x0b\x32\x16.D3.GameBalance.Handle\x12:\n\nattributes\x18\x02 \x03(\x0b\x32&.D3.AttributeSerializer.SavedAttribute')




_SAVEDATTRIBUTE = descriptor.Descriptor(
  name='SavedAttribute',
  full_name='D3.AttributeSerializer.SavedAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='D3.AttributeSerializer.SavedAttribute.key', index=0,
      number=1, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='D3.AttributeSerializer.SavedAttribute.value', index=1,
      number=2, type=17, cpp_type=1, label=2,
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
  serialized_start=75,
  serialized_end=119,
)


_SAVEDATTRIBUTES = descriptor.Descriptor(
  name='SavedAttributes',
  full_name='D3.AttributeSerializer.SavedAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gb_handle', full_name='D3.AttributeSerializer.SavedAttributes.gb_handle', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attributes', full_name='D3.AttributeSerializer.SavedAttributes.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=121,
  serialized_end=241,
)

import D3.GBHandle_pb2

_SAVEDATTRIBUTES.fields_by_name['gb_handle'].message_type = D3.GBHandle_pb2._HANDLE
_SAVEDATTRIBUTES.fields_by_name['attributes'].message_type = _SAVEDATTRIBUTE

class SavedAttribute(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDATTRIBUTE
  
  # @@protoc_insertion_point(class_scope:D3.AttributeSerializer.SavedAttribute)

class SavedAttributes(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDATTRIBUTES
  
  # @@protoc_insertion_point(class_scope:D3.AttributeSerializer.SavedAttributes)

# @@protoc_insertion_point(module_scope)