# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='D3/ItemCrafting.proto',
  package='D3.ItemCrafting',
  serialized_pb='\n\x15\x44\x33/ItemCrafting.proto\x12\x0f\x44\x33.ItemCrafting\"_\n\x0b\x43rafterData\x12\x0f\n\x07recipes\x18\x01 \x03(\x0f\x12\x1a\n\x12\x61vailable_enchants\x18\x02 \x03(\x0f\x12\r\n\x05level\x18\x03 \x02(\x05\x12\x14\n\x0c\x63ooldown_end\x18\x04 \x02(\x10\"F\n\x10\x43rafterSavedData\x12\x32\n\x0c\x63rafter_data\x18\x01 \x03(\x0b\x32\x1c.D3.ItemCrafting.CrafterData')




_CRAFTERDATA = descriptor.Descriptor(
  name='CrafterData',
  full_name='D3.ItemCrafting.CrafterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='recipes', full_name='D3.ItemCrafting.CrafterData.recipes', index=0,
      number=1, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='available_enchants', full_name='D3.ItemCrafting.CrafterData.available_enchants', index=1,
      number=2, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='D3.ItemCrafting.CrafterData.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cooldown_end', full_name='D3.ItemCrafting.CrafterData.cooldown_end', index=3,
      number=4, type=16, cpp_type=2, label=2,
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
  serialized_start=42,
  serialized_end=137,
)


_CRAFTERSAVEDDATA = descriptor.Descriptor(
  name='CrafterSavedData',
  full_name='D3.ItemCrafting.CrafterSavedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='crafter_data', full_name='D3.ItemCrafting.CrafterSavedData.crafter_data', index=0,
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
  serialized_start=139,
  serialized_end=209,
)


_CRAFTERSAVEDDATA.fields_by_name['crafter_data'].message_type = _CRAFTERDATA

class CrafterData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CRAFTERDATA
  
  # @@protoc_insertion_point(class_scope:D3.ItemCrafting.CrafterData)

class CrafterSavedData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CRAFTERSAVEDDATA
  
  # @@protoc_insertion_point(class_scope:D3.ItemCrafting.CrafterSavedData)

# @@protoc_insertion_point(module_scope)
