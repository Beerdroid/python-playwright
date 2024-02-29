from dataclasses import dataclass
from typing import Optional


@dataclass
class CheckoutInfo:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    zip_postal: Optional[str] = None
