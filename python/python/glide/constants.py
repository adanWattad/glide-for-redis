from typing import Dict, List, Literal, Set, TypeVar, Union

from glide.protobuf.connection_request_pb2 import ConnectionRequest
from glide.protobuf.redis_request_pb2 import RedisRequest
from glide.routes import RandomNode, SlotIdRoute, SlotKeyRoute

OK: str = "OK"
DEFAULT_READ_BYTES_SIZE: int = pow(2, 16)
# Typing
T = TypeVar("T")
TOK = Literal["OK"]
TResult = Union[
    TOK,
    str,
    List[str],
    List[List[str]],
    int,
    None,
    Dict[str, T],
    float,
    Set[T],
]
TRequest = Union[RedisRequest, ConnectionRequest]
# When routing to a single node, response will be T
# Otherwise, response will be : {Address : response , ... } with type of Dict[str, T].
TClusterResponse = Union[T, Dict[str, T]]
TSingleNodeRoute = Union[RandomNode, SlotKeyRoute, SlotIdRoute]
