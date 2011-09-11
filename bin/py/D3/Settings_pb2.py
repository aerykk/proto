# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='D3/Settings.proto',
  package='D3.Client',
  serialized_pb='\n\x11\x44\x33/Settings.proto\x12\tD3.Client\" \n\x0cToonSettings\x12\x10\n\x08ui_flags\x18\x01 \x01(\r\"H\n\x13GameAccountSettings\x12\x15\n\ruse_last_hero\x18\x01 \x01(\x05\x12\x1a\n\x12show_offline_toast\x18\x02 \x01(\x05')




_TOONSETTINGS = descriptor.Descriptor(
  name='ToonSettings',
  full_name='D3.Client.ToonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_flags', full_name='D3.Client.ToonSettings.ui_flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=32,
  serialized_end=64,
)


_GAMEACCOUNTSETTINGS = descriptor.Descriptor(
  name='GameAccountSettings',
  full_name='D3.Client.GameAccountSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='use_last_hero', full_name='D3.Client.GameAccountSettings.use_last_hero', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='show_offline_toast', full_name='D3.Client.GameAccountSettings.show_offline_toast', index=1,
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
  serialized_start=66,
  serialized_end=138,
)



class ToonSettings(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TOONSETTINGS
  
  # @@protoc_insertion_point(class_scope:D3.Client.ToonSettings)

class GameAccountSettings(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMEACCOUNTSETTINGS
  
  # @@protoc_insertion_point(class_scope:D3.Client.GameAccountSettings)

# @@protoc_insertion_point(module_scope)