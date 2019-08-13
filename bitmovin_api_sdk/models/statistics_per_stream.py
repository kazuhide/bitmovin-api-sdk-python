# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.codec_config_type import CodecConfigType
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.psnr_per_stream_mode import PsnrPerStreamMode
from bitmovin_api_sdk.models.statistics_per_title_stream import StatisticsPerTitleStream
from bitmovin_api_sdk.models.statistics_resolution import StatisticsResolution
import pprint
import six


class StatisticsPerStream(object):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 codec_config_id=None,
                 multiplicator=None,
                 encoded_bytes=None,
                 encoded_seconds=None,
                 billable_minutes=None,
                 width=None,
                 height=None,
                 rate=None,
                 bitrate=None,
                 codec=None,
                 resolution=None,
                 encoding_mode=None,
                 encoding_mode_multiplicator=None,
                 per_title_result_stream=None,
                 per_title_multiplicator=None,
                 psnr_mode=None,
                 psnr_multiplicator=None):
        # type: (string_types, string_types, float, int, float, float, int, int, float, int, CodecConfigType, StatisticsResolution, EncodingMode, float, StatisticsPerTitleStream, float, PsnrPerStreamMode, float) -> None

        self._stream_id = None
        self._codec_config_id = None
        self._multiplicator = None
        self._encoded_bytes = None
        self._encoded_seconds = None
        self._billable_minutes = None
        self._width = None
        self._height = None
        self._rate = None
        self._bitrate = None
        self._codec = None
        self._resolution = None
        self._encoding_mode = None
        self._encoding_mode_multiplicator = None
        self._per_title_result_stream = None
        self._per_title_multiplicator = None
        self._psnr_mode = None
        self._psnr_multiplicator = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if codec_config_id is not None:
            self.codec_config_id = codec_config_id
        if multiplicator is not None:
            self.multiplicator = multiplicator
        if encoded_bytes is not None:
            self.encoded_bytes = encoded_bytes
        if encoded_seconds is not None:
            self.encoded_seconds = encoded_seconds
        if billable_minutes is not None:
            self.billable_minutes = billable_minutes
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if rate is not None:
            self.rate = rate
        if bitrate is not None:
            self.bitrate = bitrate
        if codec is not None:
            self.codec = codec
        if resolution is not None:
            self.resolution = resolution
        if encoding_mode is not None:
            self.encoding_mode = encoding_mode
        if encoding_mode_multiplicator is not None:
            self.encoding_mode_multiplicator = encoding_mode_multiplicator
        if per_title_result_stream is not None:
            self.per_title_result_stream = per_title_result_stream
        if per_title_multiplicator is not None:
            self.per_title_multiplicator = per_title_multiplicator
        if psnr_mode is not None:
            self.psnr_mode = psnr_mode
        if psnr_multiplicator is not None:
            self.psnr_multiplicator = psnr_multiplicator

    @property
    def openapi_types(self):
        types = {
            'stream_id': 'string_types',
            'codec_config_id': 'string_types',
            'multiplicator': 'float',
            'encoded_bytes': 'int',
            'encoded_seconds': 'float',
            'billable_minutes': 'float',
            'width': 'int',
            'height': 'int',
            'rate': 'float',
            'bitrate': 'int',
            'codec': 'CodecConfigType',
            'resolution': 'StatisticsResolution',
            'encoding_mode': 'EncodingMode',
            'encoding_mode_multiplicator': 'float',
            'per_title_result_stream': 'StatisticsPerTitleStream',
            'per_title_multiplicator': 'float',
            'psnr_mode': 'PsnrPerStreamMode',
            'psnr_multiplicator': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'codec_config_id': 'codecConfigId',
            'multiplicator': 'multiplicator',
            'encoded_bytes': 'encodedBytes',
            'encoded_seconds': 'encodedSeconds',
            'billable_minutes': 'billableMinutes',
            'width': 'width',
            'height': 'height',
            'rate': 'rate',
            'bitrate': 'bitrate',
            'codec': 'codec',
            'resolution': 'resolution',
            'encoding_mode': 'encodingMode',
            'encoding_mode_multiplicator': 'encodingModeMultiplicator',
            'per_title_result_stream': 'perTitleResultStream',
            'per_title_multiplicator': 'perTitleMultiplicator',
            'psnr_mode': 'psnrMode',
            'psnr_multiplicator': 'psnrMultiplicator'
        }
        return attributes

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this StatisticsPerStream.

        ID of the stream (required)

        :return: The stream_id of this StatisticsPerStream.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this StatisticsPerStream.

        ID of the stream (required)

        :param stream_id: The stream_id of this StatisticsPerStream.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def codec_config_id(self):
        # type: () -> string_types
        """Gets the codec_config_id of this StatisticsPerStream.

        ID of the condec configuration (required)

        :return: The codec_config_id of this StatisticsPerStream.
        :rtype: string_types
        """
        return self._codec_config_id

    @codec_config_id.setter
    def codec_config_id(self, codec_config_id):
        # type: (string_types) -> None
        """Sets the codec_config_id of this StatisticsPerStream.

        ID of the condec configuration (required)

        :param codec_config_id: The codec_config_id of this StatisticsPerStream.
        :type: string_types
        """

        if codec_config_id is not None:
            if not isinstance(codec_config_id, string_types):
                raise TypeError("Invalid type for `codec_config_id`, type has to be `string_types`")

        self._codec_config_id = codec_config_id

    @property
    def multiplicator(self):
        # type: () -> float
        """Gets the multiplicator of this StatisticsPerStream.

        Multiplier for the encoded minutes. Depends on muxing type. (required)

        :return: The multiplicator of this StatisticsPerStream.
        :rtype: float
        """
        return self._multiplicator

    @multiplicator.setter
    def multiplicator(self, multiplicator):
        # type: (float) -> None
        """Sets the multiplicator of this StatisticsPerStream.

        Multiplier for the encoded minutes. Depends on muxing type. (required)

        :param multiplicator: The multiplicator of this StatisticsPerStream.
        :type: float
        """

        if multiplicator is not None:
            if not isinstance(multiplicator, (float, int)):
                raise TypeError("Invalid type for `multiplicator`, type has to be `float`")

        self._multiplicator = multiplicator

    @property
    def encoded_bytes(self):
        # type: () -> int
        """Gets the encoded_bytes of this StatisticsPerStream.

        Encoded bytes. (required)

        :return: The encoded_bytes of this StatisticsPerStream.
        :rtype: int
        """
        return self._encoded_bytes

    @encoded_bytes.setter
    def encoded_bytes(self, encoded_bytes):
        # type: (int) -> None
        """Sets the encoded_bytes of this StatisticsPerStream.

        Encoded bytes. (required)

        :param encoded_bytes: The encoded_bytes of this StatisticsPerStream.
        :type: int
        """

        if encoded_bytes is not None:
            if not isinstance(encoded_bytes, int):
                raise TypeError("Invalid type for `encoded_bytes`, type has to be `int`")

        self._encoded_bytes = encoded_bytes

    @property
    def encoded_seconds(self):
        # type: () -> float
        """Gets the encoded_seconds of this StatisticsPerStream.

        Length of the stream. (required)

        :return: The encoded_seconds of this StatisticsPerStream.
        :rtype: float
        """
        return self._encoded_seconds

    @encoded_seconds.setter
    def encoded_seconds(self, encoded_seconds):
        # type: (float) -> None
        """Sets the encoded_seconds of this StatisticsPerStream.

        Length of the stream. (required)

        :param encoded_seconds: The encoded_seconds of this StatisticsPerStream.
        :type: float
        """

        if encoded_seconds is not None:
            if not isinstance(encoded_seconds, (float, int)):
                raise TypeError("Invalid type for `encoded_seconds`, type has to be `float`")

        self._encoded_seconds = encoded_seconds

    @property
    def billable_minutes(self):
        # type: () -> float
        """Gets the billable_minutes of this StatisticsPerStream.

        Minutes you will be charged for (billableMinutes = encodedSeconds * multiplicator) (required)

        :return: The billable_minutes of this StatisticsPerStream.
        :rtype: float
        """
        return self._billable_minutes

    @billable_minutes.setter
    def billable_minutes(self, billable_minutes):
        # type: (float) -> None
        """Sets the billable_minutes of this StatisticsPerStream.

        Minutes you will be charged for (billableMinutes = encodedSeconds * multiplicator) (required)

        :param billable_minutes: The billable_minutes of this StatisticsPerStream.
        :type: float
        """

        if billable_minutes is not None:
            if not isinstance(billable_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_minutes`, type has to be `float`")

        self._billable_minutes = billable_minutes

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this StatisticsPerStream.

        Video width, only if video stream

        :return: The width of this StatisticsPerStream.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this StatisticsPerStream.

        Video width, only if video stream

        :param width: The width of this StatisticsPerStream.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this StatisticsPerStream.

        Video height, only if video stream

        :return: The height of this StatisticsPerStream.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this StatisticsPerStream.

        Video height, only if video stream

        :param height: The height of this StatisticsPerStream.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def rate(self):
        # type: () -> float
        """Gets the rate of this StatisticsPerStream.

        If it' a video stream this value is the FPS, for audio it's the sample rate. (required)

        :return: The rate of this StatisticsPerStream.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (float) -> None
        """Sets the rate of this StatisticsPerStream.

        If it' a video stream this value is the FPS, for audio it's the sample rate. (required)

        :param rate: The rate of this StatisticsPerStream.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, (float, int)):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

        self._rate = rate

    @property
    def bitrate(self):
        # type: () -> int
        """Gets the bitrate of this StatisticsPerStream.

        Bitrate of the stream (required)

        :return: The bitrate of this StatisticsPerStream.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (int) -> None
        """Sets the bitrate of this StatisticsPerStream.

        Bitrate of the stream (required)

        :param bitrate: The bitrate of this StatisticsPerStream.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

        self._bitrate = bitrate

    @property
    def codec(self):
        # type: () -> CodecConfigType
        """Gets the codec of this StatisticsPerStream.


        :return: The codec of this StatisticsPerStream.
        :rtype: CodecConfigType
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (CodecConfigType) -> None
        """Sets the codec of this StatisticsPerStream.


        :param codec: The codec of this StatisticsPerStream.
        :type: CodecConfigType
        """

        if codec is not None:
            if not isinstance(codec, CodecConfigType):
                raise TypeError("Invalid type for `codec`, type has to be `CodecConfigType`")

        self._codec = codec

    @property
    def resolution(self):
        # type: () -> StatisticsResolution
        """Gets the resolution of this StatisticsPerStream.


        :return: The resolution of this StatisticsPerStream.
        :rtype: StatisticsResolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        # type: (StatisticsResolution) -> None
        """Sets the resolution of this StatisticsPerStream.


        :param resolution: The resolution of this StatisticsPerStream.
        :type: StatisticsResolution
        """

        if resolution is not None:
            if not isinstance(resolution, StatisticsResolution):
                raise TypeError("Invalid type for `resolution`, type has to be `StatisticsResolution`")

        self._resolution = resolution

    @property
    def encoding_mode(self):
        # type: () -> EncodingMode
        """Gets the encoding_mode of this StatisticsPerStream.


        :return: The encoding_mode of this StatisticsPerStream.
        :rtype: EncodingMode
        """
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, encoding_mode):
        # type: (EncodingMode) -> None
        """Sets the encoding_mode of this StatisticsPerStream.


        :param encoding_mode: The encoding_mode of this StatisticsPerStream.
        :type: EncodingMode
        """

        if encoding_mode is not None:
            if not isinstance(encoding_mode, EncodingMode):
                raise TypeError("Invalid type for `encoding_mode`, type has to be `EncodingMode`")

        self._encoding_mode = encoding_mode

    @property
    def encoding_mode_multiplicator(self):
        # type: () -> float
        """Gets the encoding_mode_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for the given encodingMode

        :return: The encoding_mode_multiplicator of this StatisticsPerStream.
        :rtype: float
        """
        return self._encoding_mode_multiplicator

    @encoding_mode_multiplicator.setter
    def encoding_mode_multiplicator(self, encoding_mode_multiplicator):
        # type: (float) -> None
        """Sets the encoding_mode_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for the given encodingMode

        :param encoding_mode_multiplicator: The encoding_mode_multiplicator of this StatisticsPerStream.
        :type: float
        """

        if encoding_mode_multiplicator is not None:
            if not isinstance(encoding_mode_multiplicator, (float, int)):
                raise TypeError("Invalid type for `encoding_mode_multiplicator`, type has to be `float`")

        self._encoding_mode_multiplicator = encoding_mode_multiplicator

    @property
    def per_title_result_stream(self):
        # type: () -> StatisticsPerTitleStream
        """Gets the per_title_result_stream of this StatisticsPerStream.


        :return: The per_title_result_stream of this StatisticsPerStream.
        :rtype: StatisticsPerTitleStream
        """
        return self._per_title_result_stream

    @per_title_result_stream.setter
    def per_title_result_stream(self, per_title_result_stream):
        # type: (StatisticsPerTitleStream) -> None
        """Sets the per_title_result_stream of this StatisticsPerStream.


        :param per_title_result_stream: The per_title_result_stream of this StatisticsPerStream.
        :type: StatisticsPerTitleStream
        """

        if per_title_result_stream is not None:
            if not isinstance(per_title_result_stream, StatisticsPerTitleStream):
                raise TypeError("Invalid type for `per_title_result_stream`, type has to be `StatisticsPerTitleStream`")

        self._per_title_result_stream = per_title_result_stream

    @property
    def per_title_multiplicator(self):
        # type: () -> float
        """Gets the per_title_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for per-title

        :return: The per_title_multiplicator of this StatisticsPerStream.
        :rtype: float
        """
        return self._per_title_multiplicator

    @per_title_multiplicator.setter
    def per_title_multiplicator(self, per_title_multiplicator):
        # type: (float) -> None
        """Sets the per_title_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for per-title

        :param per_title_multiplicator: The per_title_multiplicator of this StatisticsPerStream.
        :type: float
        """

        if per_title_multiplicator is not None:
            if not isinstance(per_title_multiplicator, (float, int)):
                raise TypeError("Invalid type for `per_title_multiplicator`, type has to be `float`")

        self._per_title_multiplicator = per_title_multiplicator

    @property
    def psnr_mode(self):
        # type: () -> PsnrPerStreamMode
        """Gets the psnr_mode of this StatisticsPerStream.


        :return: The psnr_mode of this StatisticsPerStream.
        :rtype: PsnrPerStreamMode
        """
        return self._psnr_mode

    @psnr_mode.setter
    def psnr_mode(self, psnr_mode):
        # type: (PsnrPerStreamMode) -> None
        """Sets the psnr_mode of this StatisticsPerStream.


        :param psnr_mode: The psnr_mode of this StatisticsPerStream.
        :type: PsnrPerStreamMode
        """

        if psnr_mode is not None:
            if not isinstance(psnr_mode, PsnrPerStreamMode):
                raise TypeError("Invalid type for `psnr_mode`, type has to be `PsnrPerStreamMode`")

        self._psnr_mode = psnr_mode

    @property
    def psnr_multiplicator(self):
        # type: () -> float
        """Gets the psnr_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for psnr streams

        :return: The psnr_multiplicator of this StatisticsPerStream.
        :rtype: float
        """
        return self._psnr_multiplicator

    @psnr_multiplicator.setter
    def psnr_multiplicator(self, psnr_multiplicator):
        # type: (float) -> None
        """Sets the psnr_multiplicator of this StatisticsPerStream.

        The output minutes multiplicator for psnr streams

        :param psnr_multiplicator: The psnr_multiplicator of this StatisticsPerStream.
        :type: float
        """

        if psnr_multiplicator is not None:
            if not isinstance(psnr_multiplicator, (float, int)):
                raise TypeError("Invalid type for `psnr_multiplicator`, type has to be `float`")

        self._psnr_multiplicator = psnr_multiplicator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatisticsPerStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other