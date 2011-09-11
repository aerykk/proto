// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service/toon/toon.proto

package bnet.protocol.toon;

public final class Toon {
  private Toon() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public static final class ToonHandle extends
      com.google.protobuf.GeneratedMessage {
    // Use ToonHandle.newBuilder() to construct.
    private ToonHandle() {
      initFields();
    }
    private ToonHandle(boolean noInit) {}
    
    private static final ToonHandle defaultInstance;
    public static ToonHandle getDefaultInstance() {
      return defaultInstance;
    }
    
    public ToonHandle getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonHandle_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonHandle_fieldAccessorTable;
    }
    
    // required fixed64 id = 1;
    public static final int ID_FIELD_NUMBER = 1;
    private boolean hasId;
    private long id_ = 0L;
    public boolean hasId() { return hasId; }
    public long getId() { return id_; }
    
    // required fixed32 program = 2;
    public static final int PROGRAM_FIELD_NUMBER = 2;
    private boolean hasProgram;
    private int program_ = 0;
    public boolean hasProgram() { return hasProgram; }
    public int getProgram() { return program_; }
    
    // required uint32 region = 3;
    public static final int REGION_FIELD_NUMBER = 3;
    private boolean hasRegion;
    private int region_ = 0;
    public boolean hasRegion() { return hasRegion; }
    public int getRegion() { return region_; }
    
    // required uint32 realm = 4;
    public static final int REALM_FIELD_NUMBER = 4;
    private boolean hasRealm;
    private int realm_ = 0;
    public boolean hasRealm() { return hasRealm; }
    public int getRealm() { return realm_; }
    
    private void initFields() {
    }
    public final boolean isInitialized() {
      if (!hasId) return false;
      if (!hasProgram) return false;
      if (!hasRegion) return false;
      if (!hasRealm) return false;
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (hasId()) {
        output.writeFixed64(1, getId());
      }
      if (hasProgram()) {
        output.writeFixed32(2, getProgram());
      }
      if (hasRegion()) {
        output.writeUInt32(3, getRegion());
      }
      if (hasRealm()) {
        output.writeUInt32(4, getRealm());
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (hasId()) {
        size += com.google.protobuf.CodedOutputStream
          .computeFixed64Size(1, getId());
      }
      if (hasProgram()) {
        size += com.google.protobuf.CodedOutputStream
          .computeFixed32Size(2, getProgram());
      }
      if (hasRegion()) {
        size += com.google.protobuf.CodedOutputStream
          .computeUInt32Size(3, getRegion());
      }
      if (hasRealm()) {
        size += com.google.protobuf.CodedOutputStream
          .computeUInt32Size(4, getRealm());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input, extensionRegistry)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonHandle parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(bnet.protocol.toon.Toon.ToonHandle prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> {
      private bnet.protocol.toon.Toon.ToonHandle result;
      
      // Construct using bnet.protocol.toon.Toon.ToonHandle.newBuilder()
      private Builder() {}
      
      private static Builder create() {
        Builder builder = new Builder();
        builder.result = new bnet.protocol.toon.Toon.ToonHandle();
        return builder;
      }
      
      protected bnet.protocol.toon.Toon.ToonHandle internalGetResult() {
        return result;
      }
      
      public Builder clear() {
        if (result == null) {
          throw new IllegalStateException(
            "Cannot call clear() after build().");
        }
        result = new bnet.protocol.toon.Toon.ToonHandle();
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(result);
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return bnet.protocol.toon.Toon.ToonHandle.getDescriptor();
      }
      
      public bnet.protocol.toon.Toon.ToonHandle getDefaultInstanceForType() {
        return bnet.protocol.toon.Toon.ToonHandle.getDefaultInstance();
      }
      
      public boolean isInitialized() {
        return result.isInitialized();
      }
      public bnet.protocol.toon.Toon.ToonHandle build() {
        if (result != null && !isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return buildPartial();
      }
      
      private bnet.protocol.toon.Toon.ToonHandle buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        if (!isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return buildPartial();
      }
      
      public bnet.protocol.toon.Toon.ToonHandle buildPartial() {
        if (result == null) {
          throw new IllegalStateException(
            "build() has already been called on this Builder.");
        }
        bnet.protocol.toon.Toon.ToonHandle returnMe = result;
        result = null;
        return returnMe;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof bnet.protocol.toon.Toon.ToonHandle) {
          return mergeFrom((bnet.protocol.toon.Toon.ToonHandle)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(bnet.protocol.toon.Toon.ToonHandle other) {
        if (other == bnet.protocol.toon.Toon.ToonHandle.getDefaultInstance()) return this;
        if (other.hasId()) {
          setId(other.getId());
        }
        if (other.hasProgram()) {
          setProgram(other.getProgram());
        }
        if (other.hasRegion()) {
          setRegion(other.getRegion());
        }
        if (other.hasRealm()) {
          setRealm(other.getRealm());
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }
      
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder(
            this.getUnknownFields());
        while (true) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              this.setUnknownFields(unknownFields.build());
              return this;
            default: {
              if (!parseUnknownField(input, unknownFields,
                                     extensionRegistry, tag)) {
                this.setUnknownFields(unknownFields.build());
                return this;
              }
              break;
            }
            case 9: {
              setId(input.readFixed64());
              break;
            }
            case 21: {
              setProgram(input.readFixed32());
              break;
            }
            case 24: {
              setRegion(input.readUInt32());
              break;
            }
            case 32: {
              setRealm(input.readUInt32());
              break;
            }
          }
        }
      }
      
      
      // required fixed64 id = 1;
      public boolean hasId() {
        return result.hasId();
      }
      public long getId() {
        return result.getId();
      }
      public Builder setId(long value) {
        result.hasId = true;
        result.id_ = value;
        return this;
      }
      public Builder clearId() {
        result.hasId = false;
        result.id_ = 0L;
        return this;
      }
      
      // required fixed32 program = 2;
      public boolean hasProgram() {
        return result.hasProgram();
      }
      public int getProgram() {
        return result.getProgram();
      }
      public Builder setProgram(int value) {
        result.hasProgram = true;
        result.program_ = value;
        return this;
      }
      public Builder clearProgram() {
        result.hasProgram = false;
        result.program_ = 0;
        return this;
      }
      
      // required uint32 region = 3;
      public boolean hasRegion() {
        return result.hasRegion();
      }
      public int getRegion() {
        return result.getRegion();
      }
      public Builder setRegion(int value) {
        result.hasRegion = true;
        result.region_ = value;
        return this;
      }
      public Builder clearRegion() {
        result.hasRegion = false;
        result.region_ = 0;
        return this;
      }
      
      // required uint32 realm = 4;
      public boolean hasRealm() {
        return result.hasRealm();
      }
      public int getRealm() {
        return result.getRealm();
      }
      public Builder setRealm(int value) {
        result.hasRealm = true;
        result.realm_ = value;
        return this;
      }
      public Builder clearRealm() {
        result.hasRealm = false;
        result.realm_ = 0;
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:bnet.protocol.toon.ToonHandle)
    }
    
    static {
      defaultInstance = new ToonHandle(true);
      bnet.protocol.toon.Toon.internalForceInit();
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:bnet.protocol.toon.ToonHandle)
  }
  
  public static final class ToonName extends
      com.google.protobuf.GeneratedMessage {
    // Use ToonName.newBuilder() to construct.
    private ToonName() {
      initFields();
    }
    private ToonName(boolean noInit) {}
    
    private static final ToonName defaultInstance;
    public static ToonName getDefaultInstance() {
      return defaultInstance;
    }
    
    public ToonName getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonName_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonName_fieldAccessorTable;
    }
    
    // required string full_name = 1;
    public static final int FULL_NAME_FIELD_NUMBER = 1;
    private boolean hasFullName;
    private java.lang.String fullName_ = "";
    public boolean hasFullName() { return hasFullName; }
    public java.lang.String getFullName() { return fullName_; }
    
    private void initFields() {
    }
    public final boolean isInitialized() {
      if (!hasFullName) return false;
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (hasFullName()) {
        output.writeString(1, getFullName());
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (hasFullName()) {
        size += com.google.protobuf.CodedOutputStream
          .computeStringSize(1, getFullName());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonName parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input, extensionRegistry)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonName parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(bnet.protocol.toon.Toon.ToonName prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> {
      private bnet.protocol.toon.Toon.ToonName result;
      
      // Construct using bnet.protocol.toon.Toon.ToonName.newBuilder()
      private Builder() {}
      
      private static Builder create() {
        Builder builder = new Builder();
        builder.result = new bnet.protocol.toon.Toon.ToonName();
        return builder;
      }
      
      protected bnet.protocol.toon.Toon.ToonName internalGetResult() {
        return result;
      }
      
      public Builder clear() {
        if (result == null) {
          throw new IllegalStateException(
            "Cannot call clear() after build().");
        }
        result = new bnet.protocol.toon.Toon.ToonName();
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(result);
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return bnet.protocol.toon.Toon.ToonName.getDescriptor();
      }
      
      public bnet.protocol.toon.Toon.ToonName getDefaultInstanceForType() {
        return bnet.protocol.toon.Toon.ToonName.getDefaultInstance();
      }
      
      public boolean isInitialized() {
        return result.isInitialized();
      }
      public bnet.protocol.toon.Toon.ToonName build() {
        if (result != null && !isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return buildPartial();
      }
      
      private bnet.protocol.toon.Toon.ToonName buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        if (!isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return buildPartial();
      }
      
      public bnet.protocol.toon.Toon.ToonName buildPartial() {
        if (result == null) {
          throw new IllegalStateException(
            "build() has already been called on this Builder.");
        }
        bnet.protocol.toon.Toon.ToonName returnMe = result;
        result = null;
        return returnMe;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof bnet.protocol.toon.Toon.ToonName) {
          return mergeFrom((bnet.protocol.toon.Toon.ToonName)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(bnet.protocol.toon.Toon.ToonName other) {
        if (other == bnet.protocol.toon.Toon.ToonName.getDefaultInstance()) return this;
        if (other.hasFullName()) {
          setFullName(other.getFullName());
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }
      
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder(
            this.getUnknownFields());
        while (true) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              this.setUnknownFields(unknownFields.build());
              return this;
            default: {
              if (!parseUnknownField(input, unknownFields,
                                     extensionRegistry, tag)) {
                this.setUnknownFields(unknownFields.build());
                return this;
              }
              break;
            }
            case 10: {
              setFullName(input.readString());
              break;
            }
          }
        }
      }
      
      
      // required string full_name = 1;
      public boolean hasFullName() {
        return result.hasFullName();
      }
      public java.lang.String getFullName() {
        return result.getFullName();
      }
      public Builder setFullName(java.lang.String value) {
        if (value == null) {
    throw new NullPointerException();
  }
  result.hasFullName = true;
        result.fullName_ = value;
        return this;
      }
      public Builder clearFullName() {
        result.hasFullName = false;
        result.fullName_ = getDefaultInstance().getFullName();
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:bnet.protocol.toon.ToonName)
    }
    
    static {
      defaultInstance = new ToonName(true);
      bnet.protocol.toon.Toon.internalForceInit();
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:bnet.protocol.toon.ToonName)
  }
  
  public static final class ToonInfo extends
      com.google.protobuf.GeneratedMessage {
    // Use ToonInfo.newBuilder() to construct.
    private ToonInfo() {
      initFields();
    }
    private ToonInfo(boolean noInit) {}
    
    private static final ToonInfo defaultInstance;
    public static ToonInfo getDefaultInstance() {
      return defaultInstance;
    }
    
    public ToonInfo getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonInfo_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return bnet.protocol.toon.Toon.internal_static_bnet_protocol_toon_ToonInfo_fieldAccessorTable;
    }
    
    // required .bnet.protocol.toon.ToonName name = 1;
    public static final int NAME_FIELD_NUMBER = 1;
    private boolean hasName;
    private bnet.protocol.toon.Toon.ToonName name_;
    public boolean hasName() { return hasName; }
    public bnet.protocol.toon.Toon.ToonName getName() { return name_; }
    
    private void initFields() {
      name_ = bnet.protocol.toon.Toon.ToonName.getDefaultInstance();
    }
    public final boolean isInitialized() {
      if (!hasName) return false;
      if (!getName().isInitialized()) return false;
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (hasName()) {
        output.writeMessage(1, getName());
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (hasName()) {
        size += com.google.protobuf.CodedOutputStream
          .computeMessageSize(1, getName());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input, extensionRegistry)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static bnet.protocol.toon.Toon.ToonInfo parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(bnet.protocol.toon.Toon.ToonInfo prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> {
      private bnet.protocol.toon.Toon.ToonInfo result;
      
      // Construct using bnet.protocol.toon.Toon.ToonInfo.newBuilder()
      private Builder() {}
      
      private static Builder create() {
        Builder builder = new Builder();
        builder.result = new bnet.protocol.toon.Toon.ToonInfo();
        return builder;
      }
      
      protected bnet.protocol.toon.Toon.ToonInfo internalGetResult() {
        return result;
      }
      
      public Builder clear() {
        if (result == null) {
          throw new IllegalStateException(
            "Cannot call clear() after build().");
        }
        result = new bnet.protocol.toon.Toon.ToonInfo();
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(result);
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return bnet.protocol.toon.Toon.ToonInfo.getDescriptor();
      }
      
      public bnet.protocol.toon.Toon.ToonInfo getDefaultInstanceForType() {
        return bnet.protocol.toon.Toon.ToonInfo.getDefaultInstance();
      }
      
      public boolean isInitialized() {
        return result.isInitialized();
      }
      public bnet.protocol.toon.Toon.ToonInfo build() {
        if (result != null && !isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return buildPartial();
      }
      
      private bnet.protocol.toon.Toon.ToonInfo buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        if (!isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return buildPartial();
      }
      
      public bnet.protocol.toon.Toon.ToonInfo buildPartial() {
        if (result == null) {
          throw new IllegalStateException(
            "build() has already been called on this Builder.");
        }
        bnet.protocol.toon.Toon.ToonInfo returnMe = result;
        result = null;
        return returnMe;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof bnet.protocol.toon.Toon.ToonInfo) {
          return mergeFrom((bnet.protocol.toon.Toon.ToonInfo)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(bnet.protocol.toon.Toon.ToonInfo other) {
        if (other == bnet.protocol.toon.Toon.ToonInfo.getDefaultInstance()) return this;
        if (other.hasName()) {
          mergeName(other.getName());
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }
      
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder(
            this.getUnknownFields());
        while (true) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              this.setUnknownFields(unknownFields.build());
              return this;
            default: {
              if (!parseUnknownField(input, unknownFields,
                                     extensionRegistry, tag)) {
                this.setUnknownFields(unknownFields.build());
                return this;
              }
              break;
            }
            case 10: {
              bnet.protocol.toon.Toon.ToonName.Builder subBuilder = bnet.protocol.toon.Toon.ToonName.newBuilder();
              if (hasName()) {
                subBuilder.mergeFrom(getName());
              }
              input.readMessage(subBuilder, extensionRegistry);
              setName(subBuilder.buildPartial());
              break;
            }
          }
        }
      }
      
      
      // required .bnet.protocol.toon.ToonName name = 1;
      public boolean hasName() {
        return result.hasName();
      }
      public bnet.protocol.toon.Toon.ToonName getName() {
        return result.getName();
      }
      public Builder setName(bnet.protocol.toon.Toon.ToonName value) {
        if (value == null) {
          throw new NullPointerException();
        }
        result.hasName = true;
        result.name_ = value;
        return this;
      }
      public Builder setName(bnet.protocol.toon.Toon.ToonName.Builder builderForValue) {
        result.hasName = true;
        result.name_ = builderForValue.build();
        return this;
      }
      public Builder mergeName(bnet.protocol.toon.Toon.ToonName value) {
        if (result.hasName() &&
            result.name_ != bnet.protocol.toon.Toon.ToonName.getDefaultInstance()) {
          result.name_ =
            bnet.protocol.toon.Toon.ToonName.newBuilder(result.name_).mergeFrom(value).buildPartial();
        } else {
          result.name_ = value;
        }
        result.hasName = true;
        return this;
      }
      public Builder clearName() {
        result.hasName = false;
        result.name_ = bnet.protocol.toon.Toon.ToonName.getDefaultInstance();
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:bnet.protocol.toon.ToonInfo)
    }
    
    static {
      defaultInstance = new ToonInfo(true);
      bnet.protocol.toon.Toon.internalForceInit();
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:bnet.protocol.toon.ToonInfo)
  }
  
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_bnet_protocol_toon_ToonHandle_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_bnet_protocol_toon_ToonHandle_fieldAccessorTable;
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_bnet_protocol_toon_ToonName_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_bnet_protocol_toon_ToonName_fieldAccessorTable;
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_bnet_protocol_toon_ToonInfo_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_bnet_protocol_toon_ToonInfo_fieldAccessorTable;
  
  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\027service/toon/toon.proto\022\022bnet.protocol" +
      ".toon\"H\n\nToonHandle\022\n\n\002id\030\001 \002(\006\022\017\n\007progr" +
      "am\030\002 \002(\007\022\016\n\006region\030\003 \002(\r\022\r\n\005realm\030\004 \002(\r\"" +
      "\035\n\010ToonName\022\021\n\tfull_name\030\001 \002(\t\"6\n\010ToonIn" +
      "fo\022*\n\004name\030\001 \002(\0132\034.bnet.protocol.toon.To" +
      "onNameB\003\200\001\001"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          internal_static_bnet_protocol_toon_ToonHandle_descriptor =
            getDescriptor().getMessageTypes().get(0);
          internal_static_bnet_protocol_toon_ToonHandle_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_bnet_protocol_toon_ToonHandle_descriptor,
              new java.lang.String[] { "Id", "Program", "Region", "Realm", },
              bnet.protocol.toon.Toon.ToonHandle.class,
              bnet.protocol.toon.Toon.ToonHandle.Builder.class);
          internal_static_bnet_protocol_toon_ToonName_descriptor =
            getDescriptor().getMessageTypes().get(1);
          internal_static_bnet_protocol_toon_ToonName_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_bnet_protocol_toon_ToonName_descriptor,
              new java.lang.String[] { "FullName", },
              bnet.protocol.toon.Toon.ToonName.class,
              bnet.protocol.toon.Toon.ToonName.Builder.class);
          internal_static_bnet_protocol_toon_ToonInfo_descriptor =
            getDescriptor().getMessageTypes().get(2);
          internal_static_bnet_protocol_toon_ToonInfo_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_bnet_protocol_toon_ToonInfo_descriptor,
              new java.lang.String[] { "Name", },
              bnet.protocol.toon.Toon.ToonInfo.class,
              bnet.protocol.toon.Toon.ToonInfo.Builder.class);
          return null;
        }
      };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
  }
  
  public static void internalForceInit() {}
  
  // @@protoc_insertion_point(outer_class_scope)
}
