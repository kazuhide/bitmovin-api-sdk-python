# coding: utf-8

from bitmovin.models.id3_tag import Id3Tag
from bitmovin.models.id3_tag_position_mode import Id3TagPositionMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class FrameIdId3Tag(Id3Tag):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(FrameIdId3Tag, self).openapi_types
        types.update({
            'bytes': 'str',
            'frame_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(FrameIdId3Tag, self).attribute_map
        attributes.update({
            'bytes': 'bytes',
            'frame_id': 'frameId'
        })
        return attributes

    def __init__(self, bytes=None, frame_id=None, *args, **kwargs):
        super(FrameIdId3Tag, self).__init__(*args, **kwargs)

        self._bytes = None
        self._frame_id = None
        self.discriminator = None

        if bytes is not None:
            self.bytes = bytes
        if frame_id is not None:
            self.frame_id = frame_id

    @property
    def bytes(self):
        """Gets the bytes of this FrameIdId3Tag.

        Base64 Encoded Data

        :return: The bytes of this FrameIdId3Tag.
        :rtype: str
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this FrameIdId3Tag.

        Base64 Encoded Data

        :param bytes: The bytes of this FrameIdId3Tag.
        :type: str
        """

        if bytes is not None:
            if not isinstance(bytes, str):
                raise TypeError("Invalid type for `bytes`, type has to be `str`")

        self._bytes = bytes


    @property
    def frame_id(self):
        """Gets the frame_id of this FrameIdId3Tag.

        4 character long Frame ID

        :return: The frame_id of this FrameIdId3Tag.
        :rtype: str
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        """Sets the frame_id of this FrameIdId3Tag.

        4 character long Frame ID

        :param frame_id: The frame_id of this FrameIdId3Tag.
        :type: str
        """

        if frame_id is not None:
            if not isinstance(frame_id, str):
                raise TypeError("Invalid type for `frame_id`, type has to be `str`")

        self._frame_id = frame_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(FrameIdId3Tag, self).to_dict()

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
            if issubclass(FrameIdId3Tag, dict):
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
        if not isinstance(other, FrameIdId3Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
