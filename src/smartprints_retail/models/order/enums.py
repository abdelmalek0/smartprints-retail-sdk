from enum import Enum


class OrderStatus(str, Enum):
    ANY = "any"
    INITIATED = "initiated"
    PLACED = "placed"
    ACTIVE = "active"
    DONE = "done"
    FINISHED = "finished"
    CANCELED = "canceled"
    ABORTED = "aborted"
    HOLD = "hold"
    REFUNDED = "refunded"
    PREQUEUED = "prequeued"
    QUEUED = "queued"
    HOLDQUEUED = "holdqueued"
    PUNCHED = "punched"
    DISPATCHED = "dispatched"


EXCLUDED_STATUSES = {
    OrderStatus.PLACED,
    OrderStatus.CANCELED,
    OrderStatus.ABORTED,
    OrderStatus.INITIATED,
}
