protoc.exe --descriptor_set_out=bin/all.descriptor --include_imports service/user_manager/user_manager.proto service/toon/toon.proto service/toon/toon_external.proto service/storage/storage.proto service/server_pool/server_pool.proto service/search/search.proto service/search/search_types.proto service/presence/presence.proto service/presence/presence_types.proto service/notification/notification.proto service/game_utilities/game_utilities.proto service/game_master/game_factory.proto service/game_master/game_master.proto service/game_master/game_master_types.proto service/friends/friends_types.proto service/friends/definition/friends.proto service/exchange/exchange.proto service/exchange/exchange_types.proto service/channel_invitation/channel_invitation_types.proto service/channel_invitation/definition/channel_invitation.proto service/channel/channel_types.proto service/channel/definition/channel.proto service/authentication/authentication.proto lib/rpc/connection.proto lib/rpc/rpc.proto lib/protocol/attribute.proto lib/protocol/content_handle.proto lib/protocol/descriptor.proto lib/protocol/entity.proto lib/protocol/exchange.proto lib/protocol/exchange_object_provider.proto lib/protocol/invitation.proto lib/protocol/resource.proto lib/profanity/profanity.proto lib/config/process_config.proto google/protobuf/descriptor.proto service/exchange/exchange_types.proto service/game_master/game_master_types.proto service/channel/channel_types.proto service/friends/friends_types.proto lib/protocol/exchange.proto lib/protocol/entity.proto lib/protocol/attribute.proto lib/protocol/invitation.proto lib/protocol/content_handle.proto service/presence/presence_types.proto d3/Account.proto d3/OnlineService.proto d3/ItemCrafting.proto d3/PartyMessage.proto d3/Quest.proto d3/GameMessage.proto d3/Hero.proto d3/Settings.proto d3/Stats.proto d3/Items.proto d3/GBHandle.proto d3/Hireling.proto d3/AttributeSerializer.proto 

protoc.exe service/user_manager/user_manager.proto --cpp_out=bin/cpp/
protoc.exe service/toon/toon.proto --cpp_out=bin/cpp/
protoc.exe service/toon/toon_external.proto --cpp_out=bin/cpp/
protoc.exe service/storage/storage.proto --cpp_out=bin/cpp/
protoc.exe service/server_pool/server_pool.proto --cpp_out=bin/cpp/
protoc.exe service/search/search.proto --cpp_out=bin/cpp/
protoc.exe service/search/search_types.proto --cpp_out=bin/cpp/
protoc.exe service/presence/presence.proto --cpp_out=bin/cpp/
protoc.exe service/presence/presence_types.proto --cpp_out=bin/cpp/
protoc.exe service/notification/notification.proto --cpp_out=bin/cpp/
protoc.exe service/game_utilities/game_utilities.proto --cpp_out=bin/cpp/
protoc.exe service/game_master/game_factory.proto --cpp_out=bin/cpp/
protoc.exe service/game_master/game_master.proto --cpp_out=bin/cpp/
protoc.exe service/game_master/game_master_types.proto --cpp_out=bin/cpp/
protoc.exe service/friends/friends_types.proto --cpp_out=bin/cpp/
protoc.exe service/friends/definition/friends.proto --cpp_out=bin/cpp/
protoc.exe service/exchange/exchange.proto --cpp_out=bin/cpp/
protoc.exe service/exchange/exchange_types.proto --cpp_out=bin/cpp/
protoc.exe service/channel_invitation/channel_invitation_types.proto --cpp_out=bin/cpp/
protoc.exe service/channel_invitation/definition/channel_invitation.proto --cpp_out=bin/cpp/
protoc.exe service/channel/channel_types.proto --cpp_out=bin/cpp/
protoc.exe service/channel/definition/channel.proto --cpp_out=bin/cpp/
protoc.exe service/authentication/authentication.proto --cpp_out=bin/cpp/
protoc.exe lib/rpc/connection.proto --cpp_out=bin/cpp/
protoc.exe lib/rpc/rpc.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/attribute.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/content_handle.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/descriptor.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/entity.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/exchange.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/exchange_object_provider.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/invitation.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/resource.proto --cpp_out=bin/cpp/
protoc.exe lib/profanity/profanity.proto --cpp_out=bin/cpp/
protoc.exe lib/config/process_config.proto --cpp_out=bin/cpp/
protoc.exe google/protobuf/descriptor.proto --cpp_out=bin/cpp/
protoc.exe Items.proto --cpp_out=bin/cpp/
protoc.exe GBHandle.proto --cpp_out=bin/cpp/
protoc.exe service/exchange/exchange_types.proto --cpp_out=bin/cpp/
protoc.exe service/game_master/game_master_types.proto --cpp_out=bin/cpp/
protoc.exe service/channel/channel_types.proto --cpp_out=bin/cpp/
protoc.exe service/friends/friends_types.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/exchange.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/entity.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/attribute.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/invitation.proto --cpp_out=bin/cpp/
protoc.exe Quest.proto --cpp_out=bin/cpp/
protoc.exe GameMessage.proto --cpp_out=bin/cpp/
protoc.exe Hero.proto --cpp_out=bin/cpp/
protoc.exe Settings.proto --cpp_out=bin/cpp/
protoc.exe Stats.proto --cpp_out=bin/cpp/
protoc.exe lib/protocol/content_handle.proto --cpp_out=bin/cpp/
protoc.exe Hireling.proto --cpp_out=bin/cpp/
protoc.exe AttributeSerializer.proto --cpp_out=bin/cpp/
protoc.exe Account.proto --cpp_out=bin/cpp/
protoc.exe OnlineService.proto --cpp_out=bin/cpp/
protoc.exe ItemCrafting.proto --cpp_out=bin/cpp/
protoc.exe PartyMessage.proto --cpp_out=bin/cpp/
protoc.exe service/presence/presence_types.proto --cpp_out=bin/cpp/

pause