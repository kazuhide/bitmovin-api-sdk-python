# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AacChannelLayout(Enum):
    NONE = "NONE"
    MONO = "MONO"
    CL_STEREO = "STEREO"
    CL_SURROUND = "SURROUND"
    CL_4_0 = "4.0"
    CL_5_0_BACK = "5.0_BACK"
    CL_5_1_BACK = "5.1_BACK"
    CL_7_1 = "7.1"
    CL_7_1_WIDE_BACK = "7.1_WIDE_BACK"
