// Generated by the protocol buffer compiler.  DO NOT EDIT!

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "AttributeSerializer.pb.h"
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace D3 {
namespace AttributeSerializer {

namespace {

const ::google::protobuf::Descriptor* SavedAttribute_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  SavedAttribute_reflection_ = NULL;
const ::google::protobuf::Descriptor* SavedAttributes_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  SavedAttributes_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_AttributeSerializer_2eproto() {
  protobuf_AddDesc_AttributeSerializer_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "AttributeSerializer.proto");
  GOOGLE_CHECK(file != NULL);
  SavedAttribute_descriptor_ = file->message_type(0);
  static const int SavedAttribute_offsets_[2] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttribute, key_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttribute, value_),
  };
  SavedAttribute_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      SavedAttribute_descriptor_,
      SavedAttribute::default_instance_,
      SavedAttribute_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttribute, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttribute, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(SavedAttribute));
  SavedAttributes_descriptor_ = file->message_type(1);
  static const int SavedAttributes_offsets_[2] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttributes, gb_handle_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttributes, attributes_),
  };
  SavedAttributes_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      SavedAttributes_descriptor_,
      SavedAttributes::default_instance_,
      SavedAttributes_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttributes, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SavedAttributes, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(SavedAttributes));
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_AttributeSerializer_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    SavedAttribute_descriptor_, &SavedAttribute::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    SavedAttributes_descriptor_, &SavedAttributes::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_AttributeSerializer_2eproto() {
  delete SavedAttribute::default_instance_;
  delete SavedAttribute_reflection_;
  delete SavedAttributes::default_instance_;
  delete SavedAttributes_reflection_;
}

void protobuf_AddDesc_AttributeSerializer_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::D3::GameBalance::protobuf_AddDesc_GBHandle_2eproto();
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\031AttributeSerializer.proto\022\026D3.Attribut"
    "eSerializer\032\016GBHandle.proto\",\n\016SavedAttr"
    "ibute\022\013\n\003key\030\001 \002(\021\022\r\n\005value\030\002 \002(\021\"x\n\017Sav"
    "edAttributes\022)\n\tgb_handle\030\001 \002(\0132\026.D3.Gam"
    "eBalance.Handle\022:\n\nattributes\030\002 \003(\0132&.D3"
    ".AttributeSerializer.SavedAttribute", 235);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "AttributeSerializer.proto", &protobuf_RegisterTypes);
  SavedAttribute::default_instance_ = new SavedAttribute();
  SavedAttributes::default_instance_ = new SavedAttributes();
  SavedAttribute::default_instance_->InitAsDefaultInstance();
  SavedAttributes::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_AttributeSerializer_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_AttributeSerializer_2eproto {
  StaticDescriptorInitializer_AttributeSerializer_2eproto() {
    protobuf_AddDesc_AttributeSerializer_2eproto();
  }
} static_descriptor_initializer_AttributeSerializer_2eproto_;


// ===================================================================

#ifndef _MSC_VER
const int SavedAttribute::kKeyFieldNumber;
const int SavedAttribute::kValueFieldNumber;
#endif  // !_MSC_VER

SavedAttribute::SavedAttribute()
  : ::google::protobuf::Message() {
  SharedCtor();
}

void SavedAttribute::InitAsDefaultInstance() {
}

SavedAttribute::SavedAttribute(const SavedAttribute& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
}

void SavedAttribute::SharedCtor() {
  _cached_size_ = 0;
  key_ = 0;
  value_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

SavedAttribute::~SavedAttribute() {
  SharedDtor();
}

void SavedAttribute::SharedDtor() {
  if (this != default_instance_) {
  }
}

void SavedAttribute::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* SavedAttribute::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return SavedAttribute_descriptor_;
}

const SavedAttribute& SavedAttribute::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_AttributeSerializer_2eproto();  return *default_instance_;
}

SavedAttribute* SavedAttribute::default_instance_ = NULL;

SavedAttribute* SavedAttribute::New() const {
  return new SavedAttribute;
}

void SavedAttribute::Clear() {
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    key_ = 0;
    value_ = 0;
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool SavedAttribute::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) return false
  ::google::protobuf::uint32 tag;
  while ((tag = input->ReadTag()) != 0) {
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required sint32 key = 1;
      case 1: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_SINT32>(
                 input, &key_)));
          _set_bit(0);
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(16)) goto parse_value;
        break;
      }
      
      // required sint32 value = 2;
      case 2: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
         parse_value:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_SINT32>(
                 input, &value_)));
          _set_bit(1);
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectAtEnd()) return true;
        break;
      }
      
      default: {
      handle_uninterpreted:
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          return true;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
  return true;
#undef DO_
}

void SavedAttribute::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // required sint32 key = 1;
  if (_has_bit(0)) {
    ::google::protobuf::internal::WireFormatLite::WriteSInt32(1, this->key(), output);
  }
  
  // required sint32 value = 2;
  if (_has_bit(1)) {
    ::google::protobuf::internal::WireFormatLite::WriteSInt32(2, this->value(), output);
  }
  
  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
}

::google::protobuf::uint8* SavedAttribute::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // required sint32 key = 1;
  if (_has_bit(0)) {
    target = ::google::protobuf::internal::WireFormatLite::WriteSInt32ToArray(1, this->key(), target);
  }
  
  // required sint32 value = 2;
  if (_has_bit(1)) {
    target = ::google::protobuf::internal::WireFormatLite::WriteSInt32ToArray(2, this->value(), target);
  }
  
  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  return target;
}

int SavedAttribute::ByteSize() const {
  int total_size = 0;
  
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // required sint32 key = 1;
    if (has_key()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::SInt32Size(
          this->key());
    }
    
    // required sint32 value = 2;
    if (has_value()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::SInt32Size(
          this->value());
    }
    
  }
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void SavedAttribute::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const SavedAttribute* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const SavedAttribute*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void SavedAttribute::MergeFrom(const SavedAttribute& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from._has_bit(0)) {
      set_key(from.key());
    }
    if (from._has_bit(1)) {
      set_value(from.value());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void SavedAttribute::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SavedAttribute::CopyFrom(const SavedAttribute& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SavedAttribute::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000003) != 0x00000003) return false;
  
  return true;
}

void SavedAttribute::Swap(SavedAttribute* other) {
  if (other != this) {
    std::swap(key_, other->key_);
    std::swap(value_, other->value_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata SavedAttribute::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = SavedAttribute_descriptor_;
  metadata.reflection = SavedAttribute_reflection_;
  return metadata;
}


// ===================================================================

#ifndef _MSC_VER
const int SavedAttributes::kGbHandleFieldNumber;
const int SavedAttributes::kAttributesFieldNumber;
#endif  // !_MSC_VER

SavedAttributes::SavedAttributes()
  : ::google::protobuf::Message() {
  SharedCtor();
}

void SavedAttributes::InitAsDefaultInstance() {
  gb_handle_ = const_cast< ::D3::GameBalance::Handle*>(&::D3::GameBalance::Handle::default_instance());
}

SavedAttributes::SavedAttributes(const SavedAttributes& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
}

void SavedAttributes::SharedCtor() {
  _cached_size_ = 0;
  gb_handle_ = NULL;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

SavedAttributes::~SavedAttributes() {
  SharedDtor();
}

void SavedAttributes::SharedDtor() {
  if (this != default_instance_) {
    delete gb_handle_;
  }
}

void SavedAttributes::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* SavedAttributes::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return SavedAttributes_descriptor_;
}

const SavedAttributes& SavedAttributes::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_AttributeSerializer_2eproto();  return *default_instance_;
}

SavedAttributes* SavedAttributes::default_instance_ = NULL;

SavedAttributes* SavedAttributes::New() const {
  return new SavedAttributes;
}

void SavedAttributes::Clear() {
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (_has_bit(0)) {
      if (gb_handle_ != NULL) gb_handle_->::D3::GameBalance::Handle::Clear();
    }
  }
  attributes_.Clear();
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool SavedAttributes::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) return false
  ::google::protobuf::uint32 tag;
  while ((tag = input->ReadTag()) != 0) {
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required .D3.GameBalance.Handle gb_handle = 1;
      case 1: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_gb_handle()));
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(18)) goto parse_attributes;
        break;
      }
      
      // repeated .D3.AttributeSerializer.SavedAttribute attributes = 2;
      case 2: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
         parse_attributes:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
                input, add_attributes()));
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(18)) goto parse_attributes;
        if (input->ExpectAtEnd()) return true;
        break;
      }
      
      default: {
      handle_uninterpreted:
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          return true;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
  return true;
#undef DO_
}

void SavedAttributes::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // required .D3.GameBalance.Handle gb_handle = 1;
  if (_has_bit(0)) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, this->gb_handle(), output);
  }
  
  // repeated .D3.AttributeSerializer.SavedAttribute attributes = 2;
  for (int i = 0; i < this->attributes_size(); i++) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      2, this->attributes(i), output);
  }
  
  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
}

::google::protobuf::uint8* SavedAttributes::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // required .D3.GameBalance.Handle gb_handle = 1;
  if (_has_bit(0)) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        1, this->gb_handle(), target);
  }
  
  // repeated .D3.AttributeSerializer.SavedAttribute attributes = 2;
  for (int i = 0; i < this->attributes_size(); i++) {
    target = ::google::protobuf::internal::WireFormatLite::
      WriteMessageNoVirtualToArray(
        2, this->attributes(i), target);
  }
  
  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  return target;
}

int SavedAttributes::ByteSize() const {
  int total_size = 0;
  
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // required .D3.GameBalance.Handle gb_handle = 1;
    if (has_gb_handle()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          this->gb_handle());
    }
    
  }
  // repeated .D3.AttributeSerializer.SavedAttribute attributes = 2;
  total_size += 1 * this->attributes_size();
  for (int i = 0; i < this->attributes_size(); i++) {
    total_size +=
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        this->attributes(i));
  }
  
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void SavedAttributes::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const SavedAttributes* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const SavedAttributes*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void SavedAttributes::MergeFrom(const SavedAttributes& from) {
  GOOGLE_CHECK_NE(&from, this);
  attributes_.MergeFrom(from.attributes_);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from._has_bit(0)) {
      mutable_gb_handle()->::D3::GameBalance::Handle::MergeFrom(from.gb_handle());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void SavedAttributes::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SavedAttributes::CopyFrom(const SavedAttributes& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SavedAttributes::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000001) != 0x00000001) return false;
  
  if (has_gb_handle()) {
    if (!this->gb_handle().IsInitialized()) return false;
  }
  for (int i = 0; i < attributes_size(); i++) {
    if (!this->attributes(i).IsInitialized()) return false;
  }
  return true;
}

void SavedAttributes::Swap(SavedAttributes* other) {
  if (other != this) {
    std::swap(gb_handle_, other->gb_handle_);
    attributes_.Swap(&other->attributes_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata SavedAttributes::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = SavedAttributes_descriptor_;
  metadata.reflection = SavedAttributes_reflection_;
  return metadata;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace AttributeSerializer
}  // namespace D3

// @@protoc_insertion_point(global_scope)
