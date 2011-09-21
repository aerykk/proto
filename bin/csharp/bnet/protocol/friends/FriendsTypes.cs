// Generated by ProtoGen, Version=2.3.0.277, Culture=neutral, PublicKeyToken=8fd7408b07f8d2cd.  DO NOT EDIT!

using pb = global::Google.ProtocolBuffers;
using pbc = global::Google.ProtocolBuffers.Collections;
using pbd = global::Google.ProtocolBuffers.Descriptors;
using scg = global::System.Collections.Generic;
namespace bnet.protocol.friends {
  
  public static partial class FriendsTypes {
  
    #region Extension registration
    public static void RegisterAllExtensions(pb::ExtensionRegistry registry) {
      registry.Add(global::bnet.protocol.friends.FriendInvitation.FriendInvitation);
    }
    #endregion
    #region Static variables
    internal static pbd::MessageDescriptor internal__static_bnet_protocol_friends_Friend__Descriptor;
    internal static pb::FieldAccess.FieldAccessorTable<global::bnet.protocol.friends.Friend, global::bnet.protocol.friends.Friend.Builder> internal__static_bnet_protocol_friends_Friend__FieldAccessorTable;
    internal static pbd::MessageDescriptor internal__static_bnet_protocol_friends_FriendInvitation__Descriptor;
    internal static pb::FieldAccess.FieldAccessorTable<global::bnet.protocol.friends.FriendInvitation, global::bnet.protocol.friends.FriendInvitation.Builder> internal__static_bnet_protocol_friends_FriendInvitation__FieldAccessorTable;
    #endregion
    #region Descriptor
    public static pbd::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbd::FileDescriptor descriptor;
    
    static FriendsTypes() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          "CiNzZXJ2aWNlL2ZyaWVuZHMvZnJpZW5kc190eXBlcy5wcm90bxIVYm5ldC5w" + 
          "cm90b2NvbC5mcmllbmRzGhxsaWIvcHJvdG9jb2wvYXR0cmlidXRlLnByb3Rv" + 
          "GhlsaWIvcHJvdG9jb2wvZW50aXR5LnByb3RvGh1saWIvcHJvdG9jb2wvaW52" + 
          "aXRhdGlvbi5wcm90byJkCgZGcmllbmQSIwoCaWQYASACKAsyFy5ibmV0LnBy" + 
          "b3RvY29sLkVudGl0eUlkEjUKCWF0dHJpYnV0ZRgCIAMoCzIiLmJuZXQucHJv" + 
          "dG9jb2wuYXR0cmlidXRlLkF0dHJpYnV0ZSKbAQoQRnJpZW5kSW52aXRhdGlv" + 
          "bhIdCg5maXJzdF9yZWNlaXZlZBgBIAEoCDoFZmFsc2UyaAoRZnJpZW5kX2lu" + 
          "dml0YXRpb24SJC5ibmV0LnByb3RvY29sLmludml0YXRpb24uSW52aXRhdGlv" + 
          "bhhnIAEoCzInLmJuZXQucHJvdG9jb2wuZnJpZW5kcy5GcmllbmRJbnZpdGF0" + 
          "aW9u");
      pbd::FileDescriptor.InternalDescriptorAssigner assigner = delegate(pbd::FileDescriptor root) {
        descriptor = root;
        internal__static_bnet_protocol_friends_Friend__Descriptor = Descriptor.MessageTypes[0];
        internal__static_bnet_protocol_friends_Friend__FieldAccessorTable = 
            new pb::FieldAccess.FieldAccessorTable<global::bnet.protocol.friends.Friend, global::bnet.protocol.friends.Friend.Builder>(internal__static_bnet_protocol_friends_Friend__Descriptor,
                new string[] { "Id", "Attribute", });
        internal__static_bnet_protocol_friends_FriendInvitation__Descriptor = Descriptor.MessageTypes[1];
        internal__static_bnet_protocol_friends_FriendInvitation__FieldAccessorTable = 
            new pb::FieldAccess.FieldAccessorTable<global::bnet.protocol.friends.FriendInvitation, global::bnet.protocol.friends.FriendInvitation.Builder>(internal__static_bnet_protocol_friends_FriendInvitation__Descriptor,
                new string[] { "FirstReceived", });
        global::bnet.protocol.friends.FriendInvitation.FriendInvitation = pb::GeneratedSingleExtension<global::bnet.protocol.friends.FriendInvitation>.CreateInstance(global::bnet.protocol.friends.FriendInvitation.Descriptor.Extensions[0]);
        return null;
      };
      pbd::FileDescriptor.InternalBuildGeneratedFileFrom(descriptorData,
          new pbd::FileDescriptor[] {
          global::bnet.protocol.attribute.Proto.Attribute.Descriptor, 
          global::bnet.protocol.Entity.Descriptor, 
          global::bnet.protocol.invitation.Proto.Invitation.Descriptor, 
          }, assigner);
    }
    #endregion
    
  }
  #region Messages
  public sealed partial class Friend : pb::GeneratedMessage<Friend, Friend.Builder> {
    private static readonly Friend defaultInstance = new Builder().BuildPartial();
    public static Friend DefaultInstance {
      get { return defaultInstance; }
    }
    
    public override Friend DefaultInstanceForType {
      get { return defaultInstance; }
    }
    
    protected override Friend ThisMessage {
      get { return this; }
    }
    
    public static pbd::MessageDescriptor Descriptor {
      get { return global::bnet.protocol.friends.FriendsTypes.internal__static_bnet_protocol_friends_Friend__Descriptor; }
    }
    
    protected override pb::FieldAccess.FieldAccessorTable<Friend, Friend.Builder> InternalFieldAccessors {
      get { return global::bnet.protocol.friends.FriendsTypes.internal__static_bnet_protocol_friends_Friend__FieldAccessorTable; }
    }
    
    public const int IdFieldNumber = 1;
    private bool hasId;
    private global::bnet.protocol.EntityId id_ = global::bnet.protocol.EntityId.DefaultInstance;
    public bool HasId {
      get { return hasId; }
    }
    public global::bnet.protocol.EntityId Id {
      get { return id_; }
    }
    
    public const int AttributeFieldNumber = 2;
    private pbc::PopsicleList<global::bnet.protocol.attribute.Attribute> attribute_ = new pbc::PopsicleList<global::bnet.protocol.attribute.Attribute>();
    public scg::IList<global::bnet.protocol.attribute.Attribute> AttributeList {
      get { return attribute_; }
    }
    public int AttributeCount {
      get { return attribute_.Count; }
    }
    public global::bnet.protocol.attribute.Attribute GetAttribute(int index) {
      return attribute_[index];
    }
    
    public override bool IsInitialized {
      get {
        if (!hasId) return false;
        if (!Id.IsInitialized) return false;
        foreach (global::bnet.protocol.attribute.Attribute element in AttributeList) {
          if (!element.IsInitialized) return false;
        }
        return true;
      }
    }
    
    public override void WriteTo(pb::CodedOutputStream output) {
      int size = SerializedSize;
      if (HasId) {
        output.WriteMessage(1, Id);
      }
      foreach (global::bnet.protocol.attribute.Attribute element in AttributeList) {
        output.WriteMessage(2, element);
      }
      UnknownFields.WriteTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public override int SerializedSize {
      get {
        int size = memoizedSerializedSize;
        if (size != -1) return size;
        
        size = 0;
        if (HasId) {
          size += pb::CodedOutputStream.ComputeMessageSize(1, Id);
        }
        foreach (global::bnet.protocol.attribute.Attribute element in AttributeList) {
          size += pb::CodedOutputStream.ComputeMessageSize(2, element);
        }
        size += UnknownFields.SerializedSize;
        memoizedSerializedSize = size;
        return size;
      }
    }
    
    public static Friend ParseFrom(pb::ByteString data) {
      return ((Builder) CreateBuilder().MergeFrom(data)).BuildParsed();
    }
    public static Friend ParseFrom(pb::ByteString data, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(data, extensionRegistry)).BuildParsed();
    }
    public static Friend ParseFrom(byte[] data) {
      return ((Builder) CreateBuilder().MergeFrom(data)).BuildParsed();
    }
    public static Friend ParseFrom(byte[] data, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(data, extensionRegistry)).BuildParsed();
    }
    public static Friend ParseFrom(global::System.IO.Stream input) {
      return ((Builder) CreateBuilder().MergeFrom(input)).BuildParsed();
    }
    public static Friend ParseFrom(global::System.IO.Stream input, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(input, extensionRegistry)).BuildParsed();
    }
    public static Friend ParseDelimitedFrom(global::System.IO.Stream input) {
      return CreateBuilder().MergeDelimitedFrom(input).BuildParsed();
    }
    public static Friend ParseDelimitedFrom(global::System.IO.Stream input, pb::ExtensionRegistry extensionRegistry) {
      return CreateBuilder().MergeDelimitedFrom(input, extensionRegistry).BuildParsed();
    }
    public static Friend ParseFrom(pb::CodedInputStream input) {
      return ((Builder) CreateBuilder().MergeFrom(input)).BuildParsed();
    }
    public static Friend ParseFrom(pb::CodedInputStream input, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(input, extensionRegistry)).BuildParsed();
    }
    public static Builder CreateBuilder() { return new Builder(); }
    public override Builder ToBuilder() { return CreateBuilder(this); }
    public override Builder CreateBuilderForType() { return new Builder(); }
    public static Builder CreateBuilder(Friend prototype) {
      return (Builder) new Builder().MergeFrom(prototype);
    }
    
    public sealed partial class Builder : pb::GeneratedBuilder<Friend, Builder> {
      protected override Builder ThisBuilder {
        get { return this; }
      }
      public Builder() {}
      
      Friend result = new Friend();
      
      protected override Friend MessageBeingBuilt {
        get { return result; }
      }
      
      public override Builder Clear() {
        result = new Friend();
        return this;
      }
      
      public override Builder Clone() {
        return new Builder().MergeFrom(result);
      }
      
      public override pbd::MessageDescriptor DescriptorForType {
        get { return global::bnet.protocol.friends.Friend.Descriptor; }
      }
      
      public override Friend DefaultInstanceForType {
        get { return global::bnet.protocol.friends.Friend.DefaultInstance; }
      }
      
      public override Friend BuildPartial() {
        if (result == null) {
          throw new global::System.InvalidOperationException("build() has already been called on this Builder");
        }
        result.attribute_.MakeReadOnly();
        Friend returnMe = result;
        result = null;
        return returnMe;
      }
      
      public override Builder MergeFrom(pb::IMessage other) {
        if (other is Friend) {
          return MergeFrom((Friend) other);
        } else {
          base.MergeFrom(other);
          return this;
        }
      }
      
      public override Builder MergeFrom(Friend other) {
        if (other == global::bnet.protocol.friends.Friend.DefaultInstance) return this;
        if (other.HasId) {
          MergeId(other.Id);
        }
        if (other.attribute_.Count != 0) {
          base.AddRange(other.attribute_, result.attribute_);
        }
        this.MergeUnknownFields(other.UnknownFields);
        return this;
      }
      
      public override Builder MergeFrom(pb::CodedInputStream input) {
        return MergeFrom(input, pb::ExtensionRegistry.Empty);
      }
      
      public override Builder MergeFrom(pb::CodedInputStream input, pb::ExtensionRegistry extensionRegistry) {
        pb::UnknownFieldSet.Builder unknownFields = null;
        while (true) {
          uint tag = input.ReadTag();
          switch (tag) {
            case 0: {
              if (unknownFields != null) {
                this.UnknownFields = unknownFields.Build();
              }
              return this;
            }
            default: {
              if (pb::WireFormat.IsEndGroupTag(tag)) {
                if (unknownFields != null) {
                  this.UnknownFields = unknownFields.Build();
                }
                return this;
              }
              if (unknownFields == null) {
                unknownFields = pb::UnknownFieldSet.CreateBuilder(this.UnknownFields);
              }
              ParseUnknownField(input, unknownFields, extensionRegistry, tag);
              break;
            }
            case 10: {
              global::bnet.protocol.EntityId.Builder subBuilder = global::bnet.protocol.EntityId.CreateBuilder();
              if (HasId) {
                subBuilder.MergeFrom(Id);
              }
              input.ReadMessage(subBuilder, extensionRegistry);
              Id = subBuilder.BuildPartial();
              break;
            }
            case 18: {
              global::bnet.protocol.attribute.Attribute.Builder subBuilder = global::bnet.protocol.attribute.Attribute.CreateBuilder();
              input.ReadMessage(subBuilder, extensionRegistry);
              AddAttribute(subBuilder.BuildPartial());
              break;
            }
          }
        }
      }
      
      
      public bool HasId {
       get { return result.HasId; }
      }
      public global::bnet.protocol.EntityId Id {
        get { return result.Id; }
        set { SetId(value); }
      }
      public Builder SetId(global::bnet.protocol.EntityId value) {
        pb::ThrowHelper.ThrowIfNull(value, "value");
        result.hasId = true;
        result.id_ = value;
        return this;
      }
      public Builder SetId(global::bnet.protocol.EntityId.Builder builderForValue) {
        pb::ThrowHelper.ThrowIfNull(builderForValue, "builderForValue");
        result.hasId = true;
        result.id_ = builderForValue.Build();
        return this;
      }
      public Builder MergeId(global::bnet.protocol.EntityId value) {
        pb::ThrowHelper.ThrowIfNull(value, "value");
        if (result.HasId &&
            result.id_ != global::bnet.protocol.EntityId.DefaultInstance) {
            result.id_ = global::bnet.protocol.EntityId.CreateBuilder(result.id_).MergeFrom(value).BuildPartial();
        } else {
          result.id_ = value;
        }
        result.hasId = true;
        return this;
      }
      public Builder ClearId() {
        result.hasId = false;
        result.id_ = global::bnet.protocol.EntityId.DefaultInstance;
        return this;
      }
      
      public pbc::IPopsicleList<global::bnet.protocol.attribute.Attribute> AttributeList {
        get { return result.attribute_; }
      }
      public int AttributeCount {
        get { return result.AttributeCount; }
      }
      public global::bnet.protocol.attribute.Attribute GetAttribute(int index) {
        return result.GetAttribute(index);
      }
      public Builder SetAttribute(int index, global::bnet.protocol.attribute.Attribute value) {
        pb::ThrowHelper.ThrowIfNull(value, "value");
        result.attribute_[index] = value;
        return this;
      }
      public Builder SetAttribute(int index, global::bnet.protocol.attribute.Attribute.Builder builderForValue) {
        pb::ThrowHelper.ThrowIfNull(builderForValue, "builderForValue");
        result.attribute_[index] = builderForValue.Build();
        return this;
      }
      public Builder AddAttribute(global::bnet.protocol.attribute.Attribute value) {
        pb::ThrowHelper.ThrowIfNull(value, "value");
        result.attribute_.Add(value);
        return this;
      }
      public Builder AddAttribute(global::bnet.protocol.attribute.Attribute.Builder builderForValue) {
        pb::ThrowHelper.ThrowIfNull(builderForValue, "builderForValue");
        result.attribute_.Add(builderForValue.Build());
        return this;
      }
      public Builder AddRangeAttribute(scg::IEnumerable<global::bnet.protocol.attribute.Attribute> values) {
        base.AddRange(values, result.attribute_);
        return this;
      }
      public Builder ClearAttribute() {
        result.attribute_.Clear();
        return this;
      }
    }
    static Friend() {
      object.ReferenceEquals(global::bnet.protocol.friends.FriendsTypes.Descriptor, null);
    }
  }
  
  public sealed partial class FriendInvitation : pb::GeneratedMessage<FriendInvitation, FriendInvitation.Builder> {
    private static readonly FriendInvitation defaultInstance = new Builder().BuildPartial();
    public static FriendInvitation DefaultInstance {
      get { return defaultInstance; }
    }
    
    public override FriendInvitation DefaultInstanceForType {
      get { return defaultInstance; }
    }
    
    protected override FriendInvitation ThisMessage {
      get { return this; }
    }
    
    public static pbd::MessageDescriptor Descriptor {
      get { return global::bnet.protocol.friends.FriendsTypes.internal__static_bnet_protocol_friends_FriendInvitation__Descriptor; }
    }
    
    protected override pb::FieldAccess.FieldAccessorTable<FriendInvitation, FriendInvitation.Builder> InternalFieldAccessors {
      get { return global::bnet.protocol.friends.FriendsTypes.internal__static_bnet_protocol_friends_FriendInvitation__FieldAccessorTable; }
    }
    
    public const int FriendInvitationFieldNumber = 103;
    public static pb::GeneratedExtensionBase<global::bnet.protocol.friends.FriendInvitation> FriendInvitation;
    public const int FirstReceivedFieldNumber = 1;
    private bool hasFirstReceived;
    private bool firstReceived_ = false;
    public bool HasFirstReceived {
      get { return hasFirstReceived; }
    }
    public bool FirstReceived {
      get { return firstReceived_; }
    }
    
    public override bool IsInitialized {
      get {
        return true;
      }
    }
    
    public override void WriteTo(pb::CodedOutputStream output) {
      int size = SerializedSize;
      if (HasFirstReceived) {
        output.WriteBool(1, FirstReceived);
      }
      UnknownFields.WriteTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public override int SerializedSize {
      get {
        int size = memoizedSerializedSize;
        if (size != -1) return size;
        
        size = 0;
        if (HasFirstReceived) {
          size += pb::CodedOutputStream.ComputeBoolSize(1, FirstReceived);
        }
        size += UnknownFields.SerializedSize;
        memoizedSerializedSize = size;
        return size;
      }
    }
    
    public static FriendInvitation ParseFrom(pb::ByteString data) {
      return ((Builder) CreateBuilder().MergeFrom(data)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(pb::ByteString data, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(data, extensionRegistry)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(byte[] data) {
      return ((Builder) CreateBuilder().MergeFrom(data)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(byte[] data, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(data, extensionRegistry)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(global::System.IO.Stream input) {
      return ((Builder) CreateBuilder().MergeFrom(input)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(global::System.IO.Stream input, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(input, extensionRegistry)).BuildParsed();
    }
    public static FriendInvitation ParseDelimitedFrom(global::System.IO.Stream input) {
      return CreateBuilder().MergeDelimitedFrom(input).BuildParsed();
    }
    public static FriendInvitation ParseDelimitedFrom(global::System.IO.Stream input, pb::ExtensionRegistry extensionRegistry) {
      return CreateBuilder().MergeDelimitedFrom(input, extensionRegistry).BuildParsed();
    }
    public static FriendInvitation ParseFrom(pb::CodedInputStream input) {
      return ((Builder) CreateBuilder().MergeFrom(input)).BuildParsed();
    }
    public static FriendInvitation ParseFrom(pb::CodedInputStream input, pb::ExtensionRegistry extensionRegistry) {
      return ((Builder) CreateBuilder().MergeFrom(input, extensionRegistry)).BuildParsed();
    }
    public static Builder CreateBuilder() { return new Builder(); }
    public override Builder ToBuilder() { return CreateBuilder(this); }
    public override Builder CreateBuilderForType() { return new Builder(); }
    public static Builder CreateBuilder(FriendInvitation prototype) {
      return (Builder) new Builder().MergeFrom(prototype);
    }
    
    public sealed partial class Builder : pb::GeneratedBuilder<FriendInvitation, Builder> {
      protected override Builder ThisBuilder {
        get { return this; }
      }
      public Builder() {}
      
      FriendInvitation result = new FriendInvitation();
      
      protected override FriendInvitation MessageBeingBuilt {
        get { return result; }
      }
      
      public override Builder Clear() {
        result = new FriendInvitation();
        return this;
      }
      
      public override Builder Clone() {
        return new Builder().MergeFrom(result);
      }
      
      public override pbd::MessageDescriptor DescriptorForType {
        get { return global::bnet.protocol.friends.FriendInvitation.Descriptor; }
      }
      
      public override FriendInvitation DefaultInstanceForType {
        get { return global::bnet.protocol.friends.FriendInvitation.DefaultInstance; }
      }
      
      public override FriendInvitation BuildPartial() {
        if (result == null) {
          throw new global::System.InvalidOperationException("build() has already been called on this Builder");
        }
        FriendInvitation returnMe = result;
        result = null;
        return returnMe;
      }
      
      public override Builder MergeFrom(pb::IMessage other) {
        if (other is FriendInvitation) {
          return MergeFrom((FriendInvitation) other);
        } else {
          base.MergeFrom(other);
          return this;
        }
      }
      
      public override Builder MergeFrom(FriendInvitation other) {
        if (other == global::bnet.protocol.friends.FriendInvitation.DefaultInstance) return this;
        if (other.HasFirstReceived) {
          FirstReceived = other.FirstReceived;
        }
        this.MergeUnknownFields(other.UnknownFields);
        return this;
      }
      
      public override Builder MergeFrom(pb::CodedInputStream input) {
        return MergeFrom(input, pb::ExtensionRegistry.Empty);
      }
      
      public override Builder MergeFrom(pb::CodedInputStream input, pb::ExtensionRegistry extensionRegistry) {
        pb::UnknownFieldSet.Builder unknownFields = null;
        while (true) {
          uint tag = input.ReadTag();
          switch (tag) {
            case 0: {
              if (unknownFields != null) {
                this.UnknownFields = unknownFields.Build();
              }
              return this;
            }
            default: {
              if (pb::WireFormat.IsEndGroupTag(tag)) {
                if (unknownFields != null) {
                  this.UnknownFields = unknownFields.Build();
                }
                return this;
              }
              if (unknownFields == null) {
                unknownFields = pb::UnknownFieldSet.CreateBuilder(this.UnknownFields);
              }
              ParseUnknownField(input, unknownFields, extensionRegistry, tag);
              break;
            }
            case 8: {
              FirstReceived = input.ReadBool();
              break;
            }
          }
        }
      }
      
      
      public bool HasFirstReceived {
        get { return result.HasFirstReceived; }
      }
      public bool FirstReceived {
        get { return result.FirstReceived; }
        set { SetFirstReceived(value); }
      }
      public Builder SetFirstReceived(bool value) {
        result.hasFirstReceived = true;
        result.firstReceived_ = value;
        return this;
      }
      public Builder ClearFirstReceived() {
        result.hasFirstReceived = false;
        result.firstReceived_ = false;
        return this;
      }
    }
    static FriendInvitation() {
      object.ReferenceEquals(global::bnet.protocol.friends.FriendsTypes.Descriptor, null);
    }
  }
  
  #endregion
  
}
