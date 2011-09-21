// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: custom/protocol/rpc/rpc.proto

package custom.protocol.rpc;

public final class Rpc {
  private Rpc() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public static final class Packet extends
      com.google.protobuf.GeneratedMessage {
    // Use Packet.newBuilder() to construct.
    private Packet() {
      initFields();
    }
    private Packet(boolean noInit) {}
    
    private static final Packet defaultInstance;
    public static Packet getDefaultInstance() {
      return defaultInstance;
    }
    
    public Packet getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return custom.protocol.rpc.Rpc.internal_static_custom_protocol_rpc_Packet_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return custom.protocol.rpc.Rpc.internal_static_custom_protocol_rpc_Packet_fieldAccessorTable;
    }
    
    // optional uint32 size = 1;
    public static final int SIZE_FIELD_NUMBER = 1;
    private boolean hasSize;
    private int size_ = 0;
    public boolean hasSize() { return hasSize; }
    public int getSize() { return size_; }
    
    // optional bytes data = 2;
    public static final int DATA_FIELD_NUMBER = 2;
    private boolean hasData;
    private com.google.protobuf.ByteString data_ = com.google.protobuf.ByteString.EMPTY;
    public boolean hasData() { return hasData; }
    public com.google.protobuf.ByteString getData() { return data_; }
    
    private void initFields() {
    }
    public final boolean isInitialized() {
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (hasSize()) {
        output.writeUInt32(1, getSize());
      }
      if (hasData()) {
        output.writeBytes(2, getData());
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (hasSize()) {
        size += com.google.protobuf.CodedOutputStream
          .computeUInt32Size(1, getSize());
      }
      if (hasData()) {
        size += com.google.protobuf.CodedOutputStream
          .computeBytesSize(2, getData());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static custom.protocol.rpc.Rpc.Packet parseDelimitedFrom(
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
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Packet parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(custom.protocol.rpc.Rpc.Packet prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> {
      private custom.protocol.rpc.Rpc.Packet result;
      
      // Construct using custom.protocol.rpc.Rpc.Packet.newBuilder()
      private Builder() {}
      
      private static Builder create() {
        Builder builder = new Builder();
        builder.result = new custom.protocol.rpc.Rpc.Packet();
        return builder;
      }
      
      protected custom.protocol.rpc.Rpc.Packet internalGetResult() {
        return result;
      }
      
      public Builder clear() {
        if (result == null) {
          throw new IllegalStateException(
            "Cannot call clear() after build().");
        }
        result = new custom.protocol.rpc.Rpc.Packet();
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(result);
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return custom.protocol.rpc.Rpc.Packet.getDescriptor();
      }
      
      public custom.protocol.rpc.Rpc.Packet getDefaultInstanceForType() {
        return custom.protocol.rpc.Rpc.Packet.getDefaultInstance();
      }
      
      public boolean isInitialized() {
        return result.isInitialized();
      }
      public custom.protocol.rpc.Rpc.Packet build() {
        if (result != null && !isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return buildPartial();
      }
      
      private custom.protocol.rpc.Rpc.Packet buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        if (!isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return buildPartial();
      }
      
      public custom.protocol.rpc.Rpc.Packet buildPartial() {
        if (result == null) {
          throw new IllegalStateException(
            "build() has already been called on this Builder.");
        }
        custom.protocol.rpc.Rpc.Packet returnMe = result;
        result = null;
        return returnMe;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof custom.protocol.rpc.Rpc.Packet) {
          return mergeFrom((custom.protocol.rpc.Rpc.Packet)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(custom.protocol.rpc.Rpc.Packet other) {
        if (other == custom.protocol.rpc.Rpc.Packet.getDefaultInstance()) return this;
        if (other.hasSize()) {
          setSize(other.getSize());
        }
        if (other.hasData()) {
          setData(other.getData());
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
            case 8: {
              setSize(input.readUInt32());
              break;
            }
            case 18: {
              setData(input.readBytes());
              break;
            }
          }
        }
      }
      
      
      // optional uint32 size = 1;
      public boolean hasSize() {
        return result.hasSize();
      }
      public int getSize() {
        return result.getSize();
      }
      public Builder setSize(int value) {
        result.hasSize = true;
        result.size_ = value;
        return this;
      }
      public Builder clearSize() {
        result.hasSize = false;
        result.size_ = 0;
        return this;
      }
      
      // optional bytes data = 2;
      public boolean hasData() {
        return result.hasData();
      }
      public com.google.protobuf.ByteString getData() {
        return result.getData();
      }
      public Builder setData(com.google.protobuf.ByteString value) {
        if (value == null) {
    throw new NullPointerException();
  }
  result.hasData = true;
        result.data_ = value;
        return this;
      }
      public Builder clearData() {
        result.hasData = false;
        result.data_ = getDefaultInstance().getData();
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:custom.protocol.rpc.Packet)
    }
    
    static {
      defaultInstance = new Packet(true);
      custom.protocol.rpc.Rpc.internalForceInit();
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:custom.protocol.rpc.Packet)
  }
  
  public static final class Varint extends
      com.google.protobuf.GeneratedMessage {
    // Use Varint.newBuilder() to construct.
    private Varint() {
      initFields();
    }
    private Varint(boolean noInit) {}
    
    private static final Varint defaultInstance;
    public static Varint getDefaultInstance() {
      return defaultInstance;
    }
    
    public Varint getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return custom.protocol.rpc.Rpc.internal_static_custom_protocol_rpc_Varint_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return custom.protocol.rpc.Rpc.internal_static_custom_protocol_rpc_Varint_fieldAccessorTable;
    }
    
    // optional uint32 value = 1;
    public static final int VALUE_FIELD_NUMBER = 1;
    private boolean hasValue;
    private int value_ = 0;
    public boolean hasValue() { return hasValue; }
    public int getValue() { return value_; }
    
    private void initFields() {
    }
    public final boolean isInitialized() {
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (hasValue()) {
        output.writeUInt32(1, getValue());
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (hasValue()) {
        size += com.google.protobuf.CodedOutputStream
          .computeUInt32Size(1, getValue());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static custom.protocol.rpc.Rpc.Varint parseDelimitedFrom(
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
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static custom.protocol.rpc.Rpc.Varint parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(custom.protocol.rpc.Rpc.Varint prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> {
      private custom.protocol.rpc.Rpc.Varint result;
      
      // Construct using custom.protocol.rpc.Rpc.Varint.newBuilder()
      private Builder() {}
      
      private static Builder create() {
        Builder builder = new Builder();
        builder.result = new custom.protocol.rpc.Rpc.Varint();
        return builder;
      }
      
      protected custom.protocol.rpc.Rpc.Varint internalGetResult() {
        return result;
      }
      
      public Builder clear() {
        if (result == null) {
          throw new IllegalStateException(
            "Cannot call clear() after build().");
        }
        result = new custom.protocol.rpc.Rpc.Varint();
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(result);
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return custom.protocol.rpc.Rpc.Varint.getDescriptor();
      }
      
      public custom.protocol.rpc.Rpc.Varint getDefaultInstanceForType() {
        return custom.protocol.rpc.Rpc.Varint.getDefaultInstance();
      }
      
      public boolean isInitialized() {
        return result.isInitialized();
      }
      public custom.protocol.rpc.Rpc.Varint build() {
        if (result != null && !isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return buildPartial();
      }
      
      private custom.protocol.rpc.Rpc.Varint buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        if (!isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return buildPartial();
      }
      
      public custom.protocol.rpc.Rpc.Varint buildPartial() {
        if (result == null) {
          throw new IllegalStateException(
            "build() has already been called on this Builder.");
        }
        custom.protocol.rpc.Rpc.Varint returnMe = result;
        result = null;
        return returnMe;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof custom.protocol.rpc.Rpc.Varint) {
          return mergeFrom((custom.protocol.rpc.Rpc.Varint)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(custom.protocol.rpc.Rpc.Varint other) {
        if (other == custom.protocol.rpc.Rpc.Varint.getDefaultInstance()) return this;
        if (other.hasValue()) {
          setValue(other.getValue());
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
            case 8: {
              setValue(input.readUInt32());
              break;
            }
          }
        }
      }
      
      
      // optional uint32 value = 1;
      public boolean hasValue() {
        return result.hasValue();
      }
      public int getValue() {
        return result.getValue();
      }
      public Builder setValue(int value) {
        result.hasValue = true;
        result.value_ = value;
        return this;
      }
      public Builder clearValue() {
        result.hasValue = false;
        result.value_ = 0;
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:custom.protocol.rpc.Varint)
    }
    
    static {
      defaultInstance = new Varint(true);
      custom.protocol.rpc.Rpc.internalForceInit();
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:custom.protocol.rpc.Varint)
  }
  
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_custom_protocol_rpc_Packet_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_custom_protocol_rpc_Packet_fieldAccessorTable;
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_custom_protocol_rpc_Varint_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_custom_protocol_rpc_Varint_fieldAccessorTable;
  
  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\035custom/protocol/rpc/rpc.proto\022\023custom." +
      "protocol.rpc\"$\n\006Packet\022\014\n\004size\030\001 \001(\r\022\014\n\004" +
      "data\030\002 \001(\014\"\027\n\006Varint\022\r\n\005value\030\001 \001(\r"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          internal_static_custom_protocol_rpc_Packet_descriptor =
            getDescriptor().getMessageTypes().get(0);
          internal_static_custom_protocol_rpc_Packet_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_custom_protocol_rpc_Packet_descriptor,
              new java.lang.String[] { "Size", "Data", },
              custom.protocol.rpc.Rpc.Packet.class,
              custom.protocol.rpc.Rpc.Packet.Builder.class);
          internal_static_custom_protocol_rpc_Varint_descriptor =
            getDescriptor().getMessageTypes().get(1);
          internal_static_custom_protocol_rpc_Varint_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_custom_protocol_rpc_Varint_descriptor,
              new java.lang.String[] { "Value", },
              custom.protocol.rpc.Rpc.Varint.class,
              custom.protocol.rpc.Rpc.Varint.Builder.class);
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
