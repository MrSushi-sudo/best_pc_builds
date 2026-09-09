from typing import Annotated
from uuid import UUID

from django_bolt.param_functions import Path

UUIDPathParameter = Annotated[UUID, Path(description="Уникальный идентификатор объекта")]
