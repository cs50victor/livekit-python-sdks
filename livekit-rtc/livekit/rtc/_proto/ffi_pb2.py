# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ffi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import e2ee_pb2 as e2ee__pb2
from . import track_pb2 as track__pb2
from . import room_pb2 as room__pb2
from . import video_frame_pb2 as video__frame__pb2
from . import audio_frame_pb2 as audio__frame__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tffi.proto\x12\rlivekit.proto\x1a\ne2ee.proto\x1a\x0btrack.proto\x1a\nroom.proto\x1a\x11video_frame.proto\x1a\x11\x61udio_frame.proto\"\xf4\x0c\n\nFfiRequest\x12\x36\n\ninitialize\x18\x01 \x01(\x0b\x32 .livekit.proto.InitializeRequestH\x00\x12\x30\n\x07\x64ispose\x18\x02 \x01(\x0b\x32\x1d.livekit.proto.DisposeRequestH\x00\x12\x30\n\x07\x63onnect\x18\x03 \x01(\x0b\x32\x1d.livekit.proto.ConnectRequestH\x00\x12\x36\n\ndisconnect\x18\x04 \x01(\x0b\x32 .livekit.proto.DisconnectRequestH\x00\x12;\n\rpublish_track\x18\x05 \x01(\x0b\x32\".livekit.proto.PublishTrackRequestH\x00\x12?\n\x0funpublish_track\x18\x06 \x01(\x0b\x32$.livekit.proto.UnpublishTrackRequestH\x00\x12\x39\n\x0cpublish_data\x18\x07 \x01(\x0b\x32!.livekit.proto.PublishDataRequestH\x00\x12=\n\x0eset_subscribed\x18\x08 \x01(\x0b\x32#.livekit.proto.SetSubscribedRequestH\x00\x12J\n\x15update_local_metadata\x18\t \x01(\x0b\x32).livekit.proto.UpdateLocalMetadataRequestH\x00\x12\x42\n\x11update_local_name\x18\n \x01(\x0b\x32%.livekit.proto.UpdateLocalNameRequestH\x00\x12\x44\n\x12\x63reate_video_track\x18\x0b \x01(\x0b\x32&.livekit.proto.CreateVideoTrackRequestH\x00\x12\x44\n\x12\x63reate_audio_track\x18\x0c \x01(\x0b\x32&.livekit.proto.CreateAudioTrackRequestH\x00\x12\x33\n\tget_stats\x18\r \x01(\x0b\x32\x1e.livekit.proto.GetStatsRequestH\x00\x12\x44\n\x12\x61lloc_video_buffer\x18\x0e \x01(\x0b\x32&.livekit.proto.AllocVideoBufferRequestH\x00\x12@\n\x10new_video_stream\x18\x0f \x01(\x0b\x32$.livekit.proto.NewVideoStreamRequestH\x00\x12@\n\x10new_video_source\x18\x10 \x01(\x0b\x32$.livekit.proto.NewVideoSourceRequestH\x00\x12\x46\n\x13\x63\x61pture_video_frame\x18\x11 \x01(\x0b\x32\'.livekit.proto.CaptureVideoFrameRequestH\x00\x12/\n\x07to_i420\x18\x12 \x01(\x0b\x32\x1c.livekit.proto.ToI420RequestH\x00\x12/\n\x07to_argb\x18\x13 \x01(\x0b\x32\x1c.livekit.proto.ToArgbRequestH\x00\x12\x44\n\x12\x61lloc_audio_buffer\x18\x14 \x01(\x0b\x32&.livekit.proto.AllocAudioBufferRequestH\x00\x12@\n\x10new_audio_stream\x18\x15 \x01(\x0b\x32$.livekit.proto.NewAudioStreamRequestH\x00\x12@\n\x10new_audio_source\x18\x16 \x01(\x0b\x32$.livekit.proto.NewAudioSourceRequestH\x00\x12\x46\n\x13\x63\x61pture_audio_frame\x18\x17 \x01(\x0b\x32\'.livekit.proto.CaptureAudioFrameRequestH\x00\x12\x46\n\x13new_audio_resampler\x18\x18 \x01(\x0b\x32\'.livekit.proto.NewAudioResamplerRequestH\x00\x12\x44\n\x12remix_and_resample\x18\x19 \x01(\x0b\x32&.livekit.proto.RemixAndResampleRequestH\x00\x12*\n\x04\x65\x32\x65\x65\x18\x1a \x01(\x0b\x32\x1a.livekit.proto.E2eeRequestH\x00\x42\t\n\x07message\"\x8f\r\n\x0b\x46\x66iResponse\x12\x37\n\ninitialize\x18\x01 \x01(\x0b\x32!.livekit.proto.InitializeResponseH\x00\x12\x31\n\x07\x64ispose\x18\x02 \x01(\x0b\x32\x1e.livekit.proto.DisposeResponseH\x00\x12\x31\n\x07\x63onnect\x18\x03 \x01(\x0b\x32\x1e.livekit.proto.ConnectResponseH\x00\x12\x37\n\ndisconnect\x18\x04 \x01(\x0b\x32!.livekit.proto.DisconnectResponseH\x00\x12<\n\rpublish_track\x18\x05 \x01(\x0b\x32#.livekit.proto.PublishTrackResponseH\x00\x12@\n\x0funpublish_track\x18\x06 \x01(\x0b\x32%.livekit.proto.UnpublishTrackResponseH\x00\x12:\n\x0cpublish_data\x18\x07 \x01(\x0b\x32\".livekit.proto.PublishDataResponseH\x00\x12>\n\x0eset_subscribed\x18\x08 \x01(\x0b\x32$.livekit.proto.SetSubscribedResponseH\x00\x12K\n\x15update_local_metadata\x18\t \x01(\x0b\x32*.livekit.proto.UpdateLocalMetadataResponseH\x00\x12\x43\n\x11update_local_name\x18\n \x01(\x0b\x32&.livekit.proto.UpdateLocalNameResponseH\x00\x12\x45\n\x12\x63reate_video_track\x18\x0b \x01(\x0b\x32\'.livekit.proto.CreateVideoTrackResponseH\x00\x12\x45\n\x12\x63reate_audio_track\x18\x0c \x01(\x0b\x32\'.livekit.proto.CreateAudioTrackResponseH\x00\x12\x34\n\tget_stats\x18\r \x01(\x0b\x32\x1f.livekit.proto.GetStatsResponseH\x00\x12\x45\n\x12\x61lloc_video_buffer\x18\x0e \x01(\x0b\x32\'.livekit.proto.AllocVideoBufferResponseH\x00\x12\x41\n\x10new_video_stream\x18\x0f \x01(\x0b\x32%.livekit.proto.NewVideoStreamResponseH\x00\x12\x41\n\x10new_video_source\x18\x10 \x01(\x0b\x32%.livekit.proto.NewVideoSourceResponseH\x00\x12G\n\x13\x63\x61pture_video_frame\x18\x11 \x01(\x0b\x32(.livekit.proto.CaptureVideoFrameResponseH\x00\x12\x30\n\x07to_i420\x18\x12 \x01(\x0b\x32\x1d.livekit.proto.ToI420ResponseH\x00\x12\x30\n\x07to_argb\x18\x13 \x01(\x0b\x32\x1d.livekit.proto.ToArgbResponseH\x00\x12\x45\n\x12\x61lloc_audio_buffer\x18\x14 \x01(\x0b\x32\'.livekit.proto.AllocAudioBufferResponseH\x00\x12\x41\n\x10new_audio_stream\x18\x15 \x01(\x0b\x32%.livekit.proto.NewAudioStreamResponseH\x00\x12\x41\n\x10new_audio_source\x18\x16 \x01(\x0b\x32%.livekit.proto.NewAudioSourceResponseH\x00\x12G\n\x13\x63\x61pture_audio_frame\x18\x17 \x01(\x0b\x32(.livekit.proto.CaptureAudioFrameResponseH\x00\x12G\n\x13new_audio_resampler\x18\x18 \x01(\x0b\x32(.livekit.proto.NewAudioResamplerResponseH\x00\x12\x45\n\x12remix_and_resample\x18\x19 \x01(\x0b\x32\'.livekit.proto.RemixAndResampleResponseH\x00\x12+\n\x04\x65\x32\x65\x65\x18\x1a \x01(\x0b\x32\x1b.livekit.proto.E2eeResponseH\x00\x42\t\n\x07message\"\xe1\x06\n\x08\x46\x66iEvent\x12.\n\nroom_event\x18\x01 \x01(\x0b\x32\x18.livekit.proto.RoomEventH\x00\x12\x30\n\x0btrack_event\x18\x02 \x01(\x0b\x32\x19.livekit.proto.TrackEventH\x00\x12=\n\x12video_stream_event\x18\x03 \x01(\x0b\x32\x1f.livekit.proto.VideoStreamEventH\x00\x12=\n\x12\x61udio_stream_event\x18\x04 \x01(\x0b\x32\x1f.livekit.proto.AudioStreamEventH\x00\x12\x31\n\x07\x63onnect\x18\x05 \x01(\x0b\x32\x1e.livekit.proto.ConnectCallbackH\x00\x12\x37\n\ndisconnect\x18\x06 \x01(\x0b\x32!.livekit.proto.DisconnectCallbackH\x00\x12\x31\n\x07\x64ispose\x18\x07 \x01(\x0b\x32\x1e.livekit.proto.DisposeCallbackH\x00\x12<\n\rpublish_track\x18\x08 \x01(\x0b\x32#.livekit.proto.PublishTrackCallbackH\x00\x12@\n\x0funpublish_track\x18\t \x01(\x0b\x32%.livekit.proto.UnpublishTrackCallbackH\x00\x12:\n\x0cpublish_data\x18\n \x01(\x0b\x32\".livekit.proto.PublishDataCallbackH\x00\x12G\n\x13\x63\x61pture_audio_frame\x18\x0b \x01(\x0b\x32(.livekit.proto.CaptureAudioFrameCallbackH\x00\x12K\n\x15update_local_metadata\x18\x0c \x01(\x0b\x32*.livekit.proto.UpdateLocalMetadataCallbackH\x00\x12\x43\n\x11update_local_name\x18\r \x01(\x0b\x32&.livekit.proto.UpdateLocalNameCallbackH\x00\x12\x34\n\tget_stats\x18\x0e \x01(\x0b\x32\x1f.livekit.proto.GetStatsCallbackH\x00\x42\t\n\x07message\"/\n\x11InitializeRequest\x12\x1a\n\x12\x65vent_callback_ptr\x18\x01 \x01(\x04\"\x14\n\x12InitializeResponse\"\x1f\n\x0e\x44isposeRequest\x12\r\n\x05\x61sync\x18\x01 \x01(\x08\"5\n\x0f\x44isposeResponse\x12\x15\n\x08\x61sync_id\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\x0b\n\t_async_id\"#\n\x0f\x44isposeCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ffi_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_FFIREQUEST']._serialized_start=104
  _globals['_FFIREQUEST']._serialized_end=1756
  _globals['_FFIRESPONSE']._serialized_start=1759
  _globals['_FFIRESPONSE']._serialized_end=3438
  _globals['_FFIEVENT']._serialized_start=3441
  _globals['_FFIEVENT']._serialized_end=4306
  _globals['_INITIALIZEREQUEST']._serialized_start=4308
  _globals['_INITIALIZEREQUEST']._serialized_end=4355
  _globals['_INITIALIZERESPONSE']._serialized_start=4357
  _globals['_INITIALIZERESPONSE']._serialized_end=4377
  _globals['_DISPOSEREQUEST']._serialized_start=4379
  _globals['_DISPOSEREQUEST']._serialized_end=4410
  _globals['_DISPOSERESPONSE']._serialized_start=4412
  _globals['_DISPOSERESPONSE']._serialized_end=4465
  _globals['_DISPOSECALLBACK']._serialized_start=4467
  _globals['_DISPOSECALLBACK']._serialized_end=4502
# @@protoc_insertion_point(module_scope)
