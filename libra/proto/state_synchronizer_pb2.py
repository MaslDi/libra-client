# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_synchronizer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ledger_info_pb2 as ledger__info__pb2
import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='state_synchronizer.proto',
  package='network',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18state_synchronizer.proto\x12\x07network\x1a\x11ledger_info.proto\x1a\x11transaction.proto\"\x88\x01\n\x0fGetChunkRequest\x12\x15\n\rknown_version\x18\x01 \x01(\x04\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x0f\n\x07timeout\x18\x03 \x01(\x04\x12>\n\x15ledger_info_with_sigs\x18\x04 \x01(\x0b\x32\x1f.types.LedgerInfoWithSignatures\"\x90\x01\n\x10GetChunkResponse\x12>\n\x15ledger_info_with_sigs\x18\x01 \x01(\x0b\x32\x1f.types.LedgerInfoWithSignatures\x12<\n\x13txn_list_with_proof\x18\x02 \x01(\x0b\x32\x1f.types.TransactionListWithProof\"\x89\x01\n\x14StateSynchronizerMsg\x12\x31\n\rchunk_request\x18\x01 \x01(\x0b\x32\x18.network.GetChunkRequestH\x00\x12\x33\n\x0e\x63hunk_response\x18\x02 \x01(\x0b\x32\x19.network.GetChunkResponseH\x00\x42\t\n\x07messageb\x06proto3')
  ,
  dependencies=[ledger__info__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,])




_GETCHUNKREQUEST = _descriptor.Descriptor(
  name='GetChunkRequest',
  full_name='network.GetChunkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='known_version', full_name='network.GetChunkRequest.known_version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='network.GetChunkRequest.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='network.GetChunkRequest.timeout', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='network.GetChunkRequest.ledger_info_with_sigs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=212,
)


_GETCHUNKRESPONSE = _descriptor.Descriptor(
  name='GetChunkResponse',
  full_name='network.GetChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_info_with_sigs', full_name='network.GetChunkResponse.ledger_info_with_sigs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txn_list_with_proof', full_name='network.GetChunkResponse.txn_list_with_proof', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=359,
)


_STATESYNCHRONIZERMSG = _descriptor.Descriptor(
  name='StateSynchronizerMsg',
  full_name='network.StateSynchronizerMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_request', full_name='network.StateSynchronizerMsg.chunk_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_response', full_name='network.StateSynchronizerMsg.chunk_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='network.StateSynchronizerMsg.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=362,
  serialized_end=499,
)

_GETCHUNKREQUEST.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
_GETCHUNKRESPONSE.fields_by_name['ledger_info_with_sigs'].message_type = ledger__info__pb2._LEDGERINFOWITHSIGNATURES
_GETCHUNKRESPONSE.fields_by_name['txn_list_with_proof'].message_type = transaction__pb2._TRANSACTIONLISTWITHPROOF
_STATESYNCHRONIZERMSG.fields_by_name['chunk_request'].message_type = _GETCHUNKREQUEST
_STATESYNCHRONIZERMSG.fields_by_name['chunk_response'].message_type = _GETCHUNKRESPONSE
_STATESYNCHRONIZERMSG.oneofs_by_name['message'].fields.append(
  _STATESYNCHRONIZERMSG.fields_by_name['chunk_request'])
_STATESYNCHRONIZERMSG.fields_by_name['chunk_request'].containing_oneof = _STATESYNCHRONIZERMSG.oneofs_by_name['message']
_STATESYNCHRONIZERMSG.oneofs_by_name['message'].fields.append(
  _STATESYNCHRONIZERMSG.fields_by_name['chunk_response'])
_STATESYNCHRONIZERMSG.fields_by_name['chunk_response'].containing_oneof = _STATESYNCHRONIZERMSG.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['GetChunkRequest'] = _GETCHUNKREQUEST
DESCRIPTOR.message_types_by_name['GetChunkResponse'] = _GETCHUNKRESPONSE
DESCRIPTOR.message_types_by_name['StateSynchronizerMsg'] = _STATESYNCHRONIZERMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetChunkRequest = _reflection.GeneratedProtocolMessageType('GetChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHUNKREQUEST,
  '__module__' : 'state_synchronizer_pb2'
  # @@protoc_insertion_point(class_scope:network.GetChunkRequest)
  })
_sym_db.RegisterMessage(GetChunkRequest)

GetChunkResponse = _reflection.GeneratedProtocolMessageType('GetChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHUNKRESPONSE,
  '__module__' : 'state_synchronizer_pb2'
  # @@protoc_insertion_point(class_scope:network.GetChunkResponse)
  })
_sym_db.RegisterMessage(GetChunkResponse)

StateSynchronizerMsg = _reflection.GeneratedProtocolMessageType('StateSynchronizerMsg', (_message.Message,), {
  'DESCRIPTOR' : _STATESYNCHRONIZERMSG,
  '__module__' : 'state_synchronizer_pb2'
  # @@protoc_insertion_point(class_scope:network.StateSynchronizerMsg)
  })
_sym_db.RegisterMessage(StateSynchronizerMsg)


# @@protoc_insertion_point(module_scope)
