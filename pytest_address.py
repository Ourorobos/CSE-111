from address import extract_city, extract_state, extract_zipcode
import pytest

print(extract_city(
    "525 S Center St, Rexburg, ID 83460"
    )
      )

print(extract_state(
    "525 S Center St, Rexburg, ID 83460"
    )
      )

print(extract_zipcode(
    "525 S Center St, Rexburg, ID 83460"
    )
      )

print(extract_city(
    "924 Trabing Rd, Buffalo, Wy 82834"
    )
      )

print(extract_state(
    "924 Trabing Rd, Buffalo, Wy 82834"
    )
      )

print(extract_zipcode(
    "924 Trabing Rd, Buffalo, Wy 82834"
    )
      )
