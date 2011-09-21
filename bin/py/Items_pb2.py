# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='Items.proto',
  package='D3.Items',
  serialized_pb='\n\x0bItems.proto\x12\x08\x44\x33.Items\x1a\x0eGBHandle.proto\x1a\x13OnlineService.proto\"\x8b\x01\n\x0cRareItemName\x12\x1b\n\x13item_name_is_prefix\x18\x01 \x02(\x08\x12\x1d\n\x15sno_affix_string_list\x18\x02 \x02(\x0f\x12\x1f\n\x17\x61\x66\x66ix_string_list_index\x18\x03 \x02(\x11\x12\x1e\n\x16item_string_list_index\x18\x04 \x02(\x11\"\x96\x03\n\tGenerator\x12\x0c\n\x04seed\x18\x01 \x02(\r\x12)\n\tgb_handle\x18\x02 \x02(\x0b\x32\x16.D3.GameBalance.Handle\x12\x14\n\x0c\x62\x61se_affixes\x18\x03 \x03(\x0f\x12.\n\x0erare_item_name\x18\x04 \x02(\x0b\x32\x16.D3.Items.RareItemName\x12\x15\n\renchant_affix\x18\x05 \x02(\x0f\x12\x14\n\x0csocket_affix\x18\x06 \x02(\x0f\x12\r\n\x05\x66lags\x18\x07 \x02(\r\x12\x12\n\ndurability\x18\x08 \x02(\r\x12\x12\n\nstack_size\x18\t \x02(\x04\x12\x10\n\x08\x64ye_type\x18\n \x02(\r\x12\x1a\n\x12item_quality_level\x18\x0b \x02(\x11\x12\x1a\n\x12item_binding_level\x18\x0c \x02(\x11\x12\x16\n\x0emax_durability\x18\r \x02(\r\x12-\n\x08\x63ontents\x18\x0e \x03(\x0b\x32\x1b.D3.Items.EmbeddedGenerator\x12\x15\n\rattuned_skill\x18\x0f \x01(\x0f\"a\n\x11\x45mbeddedGenerator\x12$\n\x02id\x18\x01 \x02(\x0b\x32\x18.D3.OnlineService.ItemId\x12&\n\tgenerator\x18\x02 \x02(\x0b\x32\x13.D3.Items.Generator\"\x97\x02\n\tSavedItem\x12$\n\x02id\x18\x01 \x02(\x0b\x32\x18.D3.OnlineService.ItemId\x12\x33\n\x0fowner_entity_id\x18\x02 \x01(\x0b\x32\x1a.D3.OnlineService.EntityId\x12+\n\tsocket_id\x18\x03 \x01(\x0b\x32\x18.D3.OnlineService.ItemId\x12\x16\n\x0ehireling_class\x18\x04 \x02(\x11\x12\x11\n\titem_slot\x18\x05 \x02(\x11\x12\x14\n\x0csquare_index\x18\x06 \x02(\x11\x12\x19\n\x11used_socket_count\x18\x07 \x02(\r\x12&\n\tgenerator\x18\x08 \x01(\x0b\x32\x13.D3.Items.Generator\"s\n\x12\x41uctionAccountInfo\x12.\n\naccount_id\x18\x01 \x02(\x0b\x32\x1a.D3.OnlineService.EntityId\x12-\n\tescrow_id\x18\x02 \x02(\x0b\x32\x1a.D3.OnlineService.EntityId\"[\n\x0b\x41uctionItem\x12$\n\x02id\x18\x01 \x02(\x0b\x32\x18.D3.OnlineService.ItemId\x12&\n\tgenerator\x18\x02 \x02(\x0b\x32\x13.D3.Items.Generator\"W\n\x0b\x41uctionInfo\x12$\n\x02id\x18\x01 \x02(\x0b\x32\x18.D3.OnlineService.ItemId\x12\"\n\x05owner\x18\x02 \x01(\x0b\x32\x13.D3.Items.Ownership\".\n\x08ItemList\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.D3.Items.SavedItem\"\x84\x01\n\tOwnership\x12\x33\n\x0fowner_entity_id\x18\x01 \x02(\x0b\x32\x1a.D3.OnlineService.EntityId\x12\x13\n\x0b\x64\x65lete_time\x18\x02 \x01(\x12\x12-\n\tescrow_id\x18\x03 \x01(\x0b\x32\x1a.D3.OnlineService.EntityId')




_RAREITEMNAME = descriptor.Descriptor(
  name='RareItemName',
  full_name='D3.Items.RareItemName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item_name_is_prefix', full_name='D3.Items.RareItemName.item_name_is_prefix', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sno_affix_string_list', full_name='D3.Items.RareItemName.sno_affix_string_list', index=1,
      number=2, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affix_string_list_index', full_name='D3.Items.RareItemName.affix_string_list_index', index=2,
      number=3, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_string_list_index', full_name='D3.Items.RareItemName.item_string_list_index', index=3,
      number=4, type=17, cpp_type=1, label=2,
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
  serialized_start=63,
  serialized_end=202,
)


_GENERATOR = descriptor.Descriptor(
  name='Generator',
  full_name='D3.Items.Generator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seed', full_name='D3.Items.Generator.seed', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gb_handle', full_name='D3.Items.Generator.gb_handle', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='base_affixes', full_name='D3.Items.Generator.base_affixes', index=2,
      number=3, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rare_item_name', full_name='D3.Items.Generator.rare_item_name', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enchant_affix', full_name='D3.Items.Generator.enchant_affix', index=4,
      number=5, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='socket_affix', full_name='D3.Items.Generator.socket_affix', index=5,
      number=6, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='flags', full_name='D3.Items.Generator.flags', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='durability', full_name='D3.Items.Generator.durability', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stack_size', full_name='D3.Items.Generator.stack_size', index=8,
      number=9, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dye_type', full_name='D3.Items.Generator.dye_type', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_quality_level', full_name='D3.Items.Generator.item_quality_level', index=10,
      number=11, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_binding_level', full_name='D3.Items.Generator.item_binding_level', index=11,
      number=12, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_durability', full_name='D3.Items.Generator.max_durability', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contents', full_name='D3.Items.Generator.contents', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attuned_skill', full_name='D3.Items.Generator.attuned_skill', index=14,
      number=15, type=15, cpp_type=1, label=1,
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
  serialized_start=205,
  serialized_end=611,
)


_EMBEDDEDGENERATOR = descriptor.Descriptor(
  name='EmbeddedGenerator',
  full_name='D3.Items.EmbeddedGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='D3.Items.EmbeddedGenerator.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator', full_name='D3.Items.EmbeddedGenerator.generator', index=1,
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
  serialized_start=613,
  serialized_end=710,
)


_SAVEDITEM = descriptor.Descriptor(
  name='SavedItem',
  full_name='D3.Items.SavedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='D3.Items.SavedItem.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='owner_entity_id', full_name='D3.Items.SavedItem.owner_entity_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='socket_id', full_name='D3.Items.SavedItem.socket_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hireling_class', full_name='D3.Items.SavedItem.hireling_class', index=3,
      number=4, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_slot', full_name='D3.Items.SavedItem.item_slot', index=4,
      number=5, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='square_index', full_name='D3.Items.SavedItem.square_index', index=5,
      number=6, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='used_socket_count', full_name='D3.Items.SavedItem.used_socket_count', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator', full_name='D3.Items.SavedItem.generator', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=713,
  serialized_end=992,
)


_AUCTIONACCOUNTINFO = descriptor.Descriptor(
  name='AuctionAccountInfo',
  full_name='D3.Items.AuctionAccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='account_id', full_name='D3.Items.AuctionAccountInfo.account_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='escrow_id', full_name='D3.Items.AuctionAccountInfo.escrow_id', index=1,
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
  serialized_start=994,
  serialized_end=1109,
)


_AUCTIONITEM = descriptor.Descriptor(
  name='AuctionItem',
  full_name='D3.Items.AuctionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='D3.Items.AuctionItem.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator', full_name='D3.Items.AuctionItem.generator', index=1,
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
  serialized_start=1111,
  serialized_end=1202,
)


_AUCTIONINFO = descriptor.Descriptor(
  name='AuctionInfo',
  full_name='D3.Items.AuctionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='D3.Items.AuctionInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='owner', full_name='D3.Items.AuctionInfo.owner', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1204,
  serialized_end=1291,
)


_ITEMLIST = descriptor.Descriptor(
  name='ItemList',
  full_name='D3.Items.ItemList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='items', full_name='D3.Items.ItemList.items', index=0,
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
  serialized_start=1293,
  serialized_end=1339,
)


_OWNERSHIP = descriptor.Descriptor(
  name='Ownership',
  full_name='D3.Items.Ownership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='owner_entity_id', full_name='D3.Items.Ownership.owner_entity_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delete_time', full_name='D3.Items.Ownership.delete_time', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='escrow_id', full_name='D3.Items.Ownership.escrow_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1342,
  serialized_end=1474,
)

import GBHandle_pb2
import OnlineService_pb2

_GENERATOR.fields_by_name['gb_handle'].message_type = GBHandle_pb2._HANDLE
_GENERATOR.fields_by_name['rare_item_name'].message_type = _RAREITEMNAME
_GENERATOR.fields_by_name['contents'].message_type = _EMBEDDEDGENERATOR
_EMBEDDEDGENERATOR.fields_by_name['id'].message_type = OnlineService_pb2._ITEMID
_EMBEDDEDGENERATOR.fields_by_name['generator'].message_type = _GENERATOR
_SAVEDITEM.fields_by_name['id'].message_type = OnlineService_pb2._ITEMID
_SAVEDITEM.fields_by_name['owner_entity_id'].message_type = OnlineService_pb2._ENTITYID
_SAVEDITEM.fields_by_name['socket_id'].message_type = OnlineService_pb2._ITEMID
_SAVEDITEM.fields_by_name['generator'].message_type = _GENERATOR
_AUCTIONACCOUNTINFO.fields_by_name['account_id'].message_type = OnlineService_pb2._ENTITYID
_AUCTIONACCOUNTINFO.fields_by_name['escrow_id'].message_type = OnlineService_pb2._ENTITYID
_AUCTIONITEM.fields_by_name['id'].message_type = OnlineService_pb2._ITEMID
_AUCTIONITEM.fields_by_name['generator'].message_type = _GENERATOR
_AUCTIONINFO.fields_by_name['id'].message_type = OnlineService_pb2._ITEMID
_AUCTIONINFO.fields_by_name['owner'].message_type = _OWNERSHIP
_ITEMLIST.fields_by_name['items'].message_type = _SAVEDITEM
_OWNERSHIP.fields_by_name['owner_entity_id'].message_type = OnlineService_pb2._ENTITYID
_OWNERSHIP.fields_by_name['escrow_id'].message_type = OnlineService_pb2._ENTITYID

class RareItemName(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAREITEMNAME
  
  # @@protoc_insertion_point(class_scope:D3.Items.RareItemName)

class Generator(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GENERATOR
  
  # @@protoc_insertion_point(class_scope:D3.Items.Generator)

class EmbeddedGenerator(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EMBEDDEDGENERATOR
  
  # @@protoc_insertion_point(class_scope:D3.Items.EmbeddedGenerator)

class SavedItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDITEM
  
  # @@protoc_insertion_point(class_scope:D3.Items.SavedItem)

class AuctionAccountInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTIONACCOUNTINFO
  
  # @@protoc_insertion_point(class_scope:D3.Items.AuctionAccountInfo)

class AuctionItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTIONITEM
  
  # @@protoc_insertion_point(class_scope:D3.Items.AuctionItem)

class AuctionInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTIONINFO
  
  # @@protoc_insertion_point(class_scope:D3.Items.AuctionInfo)

class ItemList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMLIST
  
  # @@protoc_insertion_point(class_scope:D3.Items.ItemList)

class Ownership(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OWNERSHIP
  
  # @@protoc_insertion_point(class_scope:D3.Items.Ownership)

# @@protoc_insertion_point(module_scope)
