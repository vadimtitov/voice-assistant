"""Voice Assistant skills subpackage."""

# flake8: noqa
from voiceassistant.config import Config

from . import examples

if "hass" in Config:
    from . import hass
