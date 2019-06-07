# coding: utf-8

from bitmovin.models.muxing import Muxing
from bitmovin.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class TsMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(TsMuxing, self).openapi_types
        types.update({
            'segment_length': 'float',
            'segment_naming': 'str',
            'segment_naming_template': 'str',
            'start_offset': 'int',
            'segments_muxed': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(TsMuxing, self).attribute_map
        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'start_offset': 'startOffset',
            'segments_muxed': 'segmentsMuxed'
        })
        return attributes

    def __init__(self, segment_length=None, segment_naming=None, segment_naming_template=None, start_offset=None, segments_muxed=None, *args, **kwargs):
        super(TsMuxing, self).__init__(*args, **kwargs)

        self._segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._start_offset = None
        self._segments_muxed = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if start_offset is not None:
            self.start_offset = start_offset
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed

    @property
    def segment_length(self):
        """Gets the segment_length of this TsMuxing.

        Length of the fragments in seconds

        :return: The segment_length of this TsMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this TsMuxing.

        Length of the fragments in seconds

        :param segment_length: The segment_length of this TsMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length


    @property
    def segment_naming(self):
        """Gets the segment_naming of this TsMuxing.

        Segment naming policy

        :return: The segment_naming of this TsMuxing.
        :rtype: str
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        """Sets the segment_naming of this TsMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this TsMuxing.
        :type: str
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, str):
                raise TypeError("Invalid type for `segment_naming`, type has to be `str`")

        self._segment_naming = segment_naming


    @property
    def segment_naming_template(self):
        """Gets the segment_naming_template of this TsMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property. Intended to avoid re-use of segment names after restarting a live encoding. If segmentNamingTemplate is set, segmentNaming must not be set.

        :return: The segment_naming_template of this TsMuxing.
        :rtype: str
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        """Sets the segment_naming_template of this TsMuxing.

        Segment naming policy containing a placeholder of the format '{rand_chars:x}', which will be replaced by a random alphanumeric string of length x (default 32) on each (re)start of the encoding. The resulting string will be copied to the segmentNaming property. Intended to avoid re-use of segment names after restarting a live encoding. If segmentNamingTemplate is set, segmentNaming must not be set.

        :param segment_naming_template: The segment_naming_template of this TsMuxing.
        :type: str
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, str):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `str`")

        self._segment_naming_template = segment_naming_template


    @property
    def start_offset(self):
        """Gets the start_offset of this TsMuxing.

        Offset of MPEG-TS timestamps in seconds. E.g., first packet will start with PTS 900,000 for a 10 seconds offset (90,000 MPEG-TS timescale).

        :return: The start_offset of this TsMuxing.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this TsMuxing.

        Offset of MPEG-TS timestamps in seconds. E.g., first packet will start with PTS 900,000 for a 10 seconds offset (90,000 MPEG-TS timescale).

        :param start_offset: The start_offset of this TsMuxing.
        :type: int
        """

        if start_offset is not None:
            if not isinstance(start_offset, int):
                raise TypeError("Invalid type for `start_offset`, type has to be `int`")

        self._start_offset = start_offset


    @property
    def segments_muxed(self):
        """Gets the segments_muxed of this TsMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this TsMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        """Sets the segments_muxed of this TsMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this TsMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(TsMuxing, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(TsMuxing, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TsMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
