# coding: utf-8

from __future__ import absolute_import

# import models into model package
from bitmovin.models.aac_audio_configuration import AacAudioConfiguration
from bitmovin.models.aac_channel_layout import AacChannelLayout
from bitmovin.models.abstract_condition import AbstractCondition
from bitmovin.models.abstract_conjunction import AbstractConjunction
from bitmovin.models.ac3_audio_configuration import Ac3AudioConfiguration
from bitmovin.models.ac3_channel_layout import Ac3ChannelLayout
from bitmovin.models.accessibility import Accessibility
from bitmovin.models.account_api_key import AccountApiKey
from bitmovin.models.account_information import AccountInformation
from bitmovin.models.acl import Acl
from bitmovin.models.acl_entry import AclEntry
from bitmovin.models.acl_permission import AclPermission
from bitmovin.models.adaptation_set import AdaptationSet
from bitmovin.models.adaptation_set_role import AdaptationSetRole
from bitmovin.models.adaptive_quant_mode import AdaptiveQuantMode
from bitmovin.models.aes_encryption_drm import AesEncryptionDrm
from bitmovin.models.aes_encryption_method import AesEncryptionMethod
from bitmovin.models.akamai_msl_output import AkamaiMslOutput
from bitmovin.models.akamai_msl_stream_format import AkamaiMslStreamFormat
from bitmovin.models.akamai_msl_version import AkamaiMslVersion
from bitmovin.models.akamai_net_storage_input import AkamaiNetStorageInput
from bitmovin.models.akamai_net_storage_output import AkamaiNetStorageOutput
from bitmovin.models.analytics_avg_query_request import AnalyticsAvgQueryRequest
from bitmovin.models.analytics_column_label import AnalyticsColumnLabel
from bitmovin.models.analytics_count_query_request import AnalyticsCountQueryRequest
from bitmovin.models.analytics_export_status import AnalyticsExportStatus
from bitmovin.models.analytics_export_task import AnalyticsExportTask
from bitmovin.models.analytics_export_task_output_target import AnalyticsExportTaskOutputTarget
from bitmovin.models.analytics_filter import AnalyticsFilter
from bitmovin.models.analytics_impression_details import AnalyticsImpressionDetails
from bitmovin.models.analytics_interval import AnalyticsInterval
from bitmovin.models.analytics_license import AnalyticsLicense
from bitmovin.models.analytics_max_query_request import AnalyticsMaxQueryRequest
from bitmovin.models.analytics_median_query_request import AnalyticsMedianQueryRequest
from bitmovin.models.analytics_min_query_request import AnalyticsMinQueryRequest
from bitmovin.models.analytics_operator import AnalyticsOperator
from bitmovin.models.analytics_order import AnalyticsOrder
from bitmovin.models.analytics_order_by_entry import AnalyticsOrderByEntry
from bitmovin.models.analytics_percentile_query_request import AnalyticsPercentileQueryRequest
from bitmovin.models.analytics_query_request import AnalyticsQueryRequest
from bitmovin.models.analytics_query_timeframe import AnalyticsQueryTimeframe
from bitmovin.models.analytics_response import AnalyticsResponse
from bitmovin.models.analytics_stddev_query_request import AnalyticsStddevQueryRequest
from bitmovin.models.analytics_sum_query_request import AnalyticsSumQueryRequest
from bitmovin.models.analytics_variance_query_request import AnalyticsVarianceQueryRequest
from bitmovin.models.and_conjunction import AndConjunction
from bitmovin.models.api_error_definition import ApiErrorDefinition
from bitmovin.models.applied_stream_settings import AppliedStreamSettings
from bitmovin.models.aspera_input import AsperaInput
from bitmovin.models.audio_adaptation_set import AudioAdaptationSet
from bitmovin.models.audio_configuration import AudioConfiguration
from bitmovin.models.audio_group import AudioGroup
from bitmovin.models.audio_group_configuration import AudioGroupConfiguration
from bitmovin.models.audio_media_info import AudioMediaInfo
from bitmovin.models.audio_mix_channel import AudioMixChannel
from bitmovin.models.audio_mix_channel_layout import AudioMixChannelLayout
from bitmovin.models.audio_mix_channel_type import AudioMixChannelType
from bitmovin.models.audio_mix_filter import AudioMixFilter
from bitmovin.models.audio_mix_input_channel_layout import AudioMixInputChannelLayout
from bitmovin.models.audio_mix_input_stream import AudioMixInputStream
from bitmovin.models.audio_mix_input_stream_channel import AudioMixInputStreamChannel
from bitmovin.models.audio_stream import AudioStream
from bitmovin.models.audio_video_sync_mode import AudioVideoSyncMode
from bitmovin.models.audio_volume_filter import AudioVolumeFilter
from bitmovin.models.audio_volume_unit import AudioVolumeUnit
from bitmovin.models.auto_representation import AutoRepresentation
from bitmovin.models.auto_restart_configuration import AutoRestartConfiguration
from bitmovin.models.av1_adaptive_quant_mode import Av1AdaptiveQuantMode
from bitmovin.models.av1_key_placement_mode import Av1KeyPlacementMode
from bitmovin.models.av1_video_configuration import Av1VideoConfiguration
from bitmovin.models.aws_account import AwsAccount
from bitmovin.models.aws_account_region_settings import AwsAccountRegionSettings
from bitmovin.models.aws_cloud_region import AwsCloudRegion
from bitmovin.models.azure_input import AzureInput
from bitmovin.models.azure_output import AzureOutput
from bitmovin.models.b_adapt import BAdapt
from bitmovin.models.backup_srt_inputs import BackupSrtInputs
from bitmovin.models.basic_media_info import BasicMediaInfo
from bitmovin.models.billable_encoding_feature_minutes import BillableEncodingFeatureMinutes
from bitmovin.models.billable_encoding_minutes import BillableEncodingMinutes
from bitmovin.models.billable_encoding_minutes_details import BillableEncodingMinutesDetails
from bitmovin.models.bitmovin_resource import BitmovinResource
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.bitmovin_response_list import BitmovinResponseList
from bitmovin.models.bitrate_selection_mode import BitrateSelectionMode
from bitmovin.models.broadcast_ts_audio_input_stream_configuration import BroadcastTsAudioInputStreamConfiguration
from bitmovin.models.broadcast_ts_input_stream_configuration import BroadcastTsInputStreamConfiguration
from bitmovin.models.broadcast_ts_muxing import BroadcastTsMuxing
from bitmovin.models.broadcast_ts_muxing_configuration import BroadcastTsMuxingConfiguration
from bitmovin.models.broadcast_ts_muxing_information import BroadcastTsMuxingInformation
from bitmovin.models.broadcast_ts_program_configuration import BroadcastTsProgramConfiguration
from bitmovin.models.broadcast_ts_transport_configuration import BroadcastTsTransportConfiguration
from bitmovin.models.broadcast_ts_video_input_stream_configuration import BroadcastTsVideoInputStreamConfiguration
from bitmovin.models.burn_in_subtitle_srt import BurnInSubtitleSrt
from bitmovin.models.caption_character_encoding import CaptionCharacterEncoding
from bitmovin.models.cea608708_subtitle_configuration import Cea608708SubtitleConfiguration
from bitmovin.models.cenc_drm import CencDrm
from bitmovin.models.cenc_fair_play import CencFairPlay
from bitmovin.models.cenc_marlin import CencMarlin
from bitmovin.models.cenc_play_ready import CencPlayReady
from bitmovin.models.cenc_widevine import CencWidevine
from bitmovin.models.channel_layout import ChannelLayout
from bitmovin.models.chroma_location import ChromaLocation
from bitmovin.models.chunk_length_mode import ChunkLengthMode
from bitmovin.models.clear_key_drm import ClearKeyDrm
from bitmovin.models.closed_captions_media_info import ClosedCaptionsMediaInfo
from bitmovin.models.cloud_region import CloudRegion
from bitmovin.models.cmaf_muxing import CmafMuxing
from bitmovin.models.codec_config_type import CodecConfigType
from bitmovin.models.codec_config_type_response import CodecConfigTypeResponse
from bitmovin.models.codec_configuration import CodecConfiguration
from bitmovin.models.color_config import ColorConfig
from bitmovin.models.color_primaries import ColorPrimaries
from bitmovin.models.color_range import ColorRange
from bitmovin.models.color_space import ColorSpace
from bitmovin.models.color_transfer import ColorTransfer
from bitmovin.models.concatenation_input_configuration import ConcatenationInputConfiguration
from bitmovin.models.concatenation_input_stream import ConcatenationInputStream
from bitmovin.models.condition import Condition
from bitmovin.models.condition_operator import ConditionOperator
from bitmovin.models.condition_type import ConditionType
from bitmovin.models.content_protection import ContentProtection
from bitmovin.models.convert_scc_caption import ConvertSccCaption
from bitmovin.models.convert_scc_caption_web_vtt_settings import ConvertSccCaptionWebVttSettings
from bitmovin.models.convert_scc_position_mode import ConvertSccPositionMode
from bitmovin.models.crop_filter import CropFilter
from bitmovin.models.custom_attribute import CustomAttribute
from bitmovin.models.custom_data import CustomData
from bitmovin.models.custom_player_build_details import CustomPlayerBuildDetails
from bitmovin.models.custom_player_build_download import CustomPlayerBuildDownload
from bitmovin.models.custom_player_build_status import CustomPlayerBuildStatus
from bitmovin.models.custom_tag import CustomTag
from bitmovin.models.custom_web_player_build_domain import CustomWebPlayerBuildDomain
from bitmovin.models.custom_xml_element import CustomXmlElement
from bitmovin.models.daily_statistics import DailyStatistics
from bitmovin.models.daily_statistics_per_label import DailyStatisticsPerLabel
from bitmovin.models.dash_cmaf_drm_representation import DashCmafDrmRepresentation
from bitmovin.models.dash_cmaf_representation import DashCmafRepresentation
from bitmovin.models.dash_fmp4_drm_representation import DashFmp4DrmRepresentation
from bitmovin.models.dash_fmp4_representation import DashFmp4Representation
from bitmovin.models.dash_manifest import DashManifest
from bitmovin.models.dash_manifest_default import DashManifestDefault
from bitmovin.models.dash_manifest_default_version import DashManifestDefaultVersion
from bitmovin.models.dash_mp4_drm_representation import DashMp4DrmRepresentation
from bitmovin.models.dash_mp4_representation import DashMp4Representation
from bitmovin.models.dash_profile import DashProfile
from bitmovin.models.dash_representation import DashRepresentation
from bitmovin.models.dash_representation_type import DashRepresentationType
from bitmovin.models.dash_representation_type_mode import DashRepresentationTypeMode
from bitmovin.models.dash_segmented_representation import DashSegmentedRepresentation
from bitmovin.models.dash_vtt_representation import DashVttRepresentation
from bitmovin.models.dash_webm_representation import DashWebmRepresentation
from bitmovin.models.decoding_error_mode import DecodingErrorMode
from bitmovin.models.deinterlace_filter import DeinterlaceFilter
from bitmovin.models.deinterlace_frame_selection_mode import DeinterlaceFrameSelectionMode
from bitmovin.models.deinterlace_mode import DeinterlaceMode
from bitmovin.models.denoise_hqdn3d_filter import DenoiseHqdn3dFilter
from bitmovin.models.domain import Domain
from bitmovin.models.domain_list import DomainList
from bitmovin.models.drm import Drm
from bitmovin.models.drm_type import DrmType
from bitmovin.models.eac3_audio_configuration import Eac3AudioConfiguration
from bitmovin.models.ebu_r128_single_pass_filter import EbuR128SinglePassFilter
from bitmovin.models.email_notification import EmailNotification
from bitmovin.models.email_notification_with_stream_conditions import EmailNotificationWithStreamConditions
from bitmovin.models.encoding import Encoding
from bitmovin.models.encoding_error_definition import EncodingErrorDefinition
from bitmovin.models.encoding_error_email_notification import EncodingErrorEmailNotification
from bitmovin.models.encoding_mode import EncodingMode
from bitmovin.models.encoding_output import EncodingOutput
from bitmovin.models.encoding_statistics import EncodingStatistics
from bitmovin.models.encoding_statistics_live import EncodingStatisticsLive
from bitmovin.models.encoding_statistics_vod import EncodingStatisticsVod
from bitmovin.models.encoding_stats import EncodingStats
from bitmovin.models.encoding_stream_input_details import EncodingStreamInputDetails
from bitmovin.models.encryption_mode import EncryptionMode
from bitmovin.models.encryption_type import EncryptionType
from bitmovin.models.enhanced_watermark_filter import EnhancedWatermarkFilter
from bitmovin.models.error_details import ErrorDetails
from bitmovin.models.error_retry_hint import ErrorRetryHint
from bitmovin.models.fair_play_drm import FairPlayDrm
from bitmovin.models.filter import Filter
from bitmovin.models.filter_type import FilterType
from bitmovin.models.filter_type_response import FilterTypeResponse
from bitmovin.models.fmp4_muxing import Fmp4Muxing
from bitmovin.models.force_flush_mode import ForceFlushMode
from bitmovin.models.fragmented_mp4_muxing_manifest_type import FragmentedMp4MuxingManifestType
from bitmovin.models.frame_id_id3_tag import FrameIdId3Tag
from bitmovin.models.ftp_input import FtpInput
from bitmovin.models.ftp_output import FtpOutput
from bitmovin.models.gcs_input import GcsInput
from bitmovin.models.gcs_output import GcsOutput
from bitmovin.models.generic_s3_input import GenericS3Input
from bitmovin.models.generic_s3_output import GenericS3Output
from bitmovin.models.google_cloud_region import GoogleCloudRegion
from bitmovin.models.group import Group
from bitmovin.models.h264_b_pyramid import H264BPyramid
from bitmovin.models.h264_interlace_mode import H264InterlaceMode
from bitmovin.models.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin.models.h264_nal_hrd import H264NalHrd
from bitmovin.models.h264_partition import H264Partition
from bitmovin.models.h264_per_title_configuration import H264PerTitleConfiguration
from bitmovin.models.h264_picture_timing_trimming_input_stream import H264PictureTimingTrimmingInputStream
from bitmovin.models.h264_sub_me import H264SubMe
from bitmovin.models.h264_trellis import H264Trellis
from bitmovin.models.h264_video_configuration import H264VideoConfiguration
from bitmovin.models.h265_per_title_configuration import H265PerTitleConfiguration
from bitmovin.models.h265_video_configuration import H265VideoConfiguration
from bitmovin.models.he_aac_v1_audio_configuration import HeAacV1AudioConfiguration
from bitmovin.models.he_aac_v2_audio_configuration import HeAacV2AudioConfiguration
from bitmovin.models.hls_manifest import HlsManifest
from bitmovin.models.hls_manifest_default import HlsManifestDefault
from bitmovin.models.hls_manifest_default_version import HlsManifestDefaultVersion
from bitmovin.models.hls_version import HlsVersion
from bitmovin.models.http_input import HttpInput
from bitmovin.models.https_input import HttpsInput
from bitmovin.models.i_frame_playlist import IFramePlaylist
from bitmovin.models.id3_tag import Id3Tag
from bitmovin.models.id3_tag_position_mode import Id3TagPositionMode
from bitmovin.models.id3_tag_type import Id3TagType
from bitmovin.models.ignored_by import IgnoredBy
from bitmovin.models.ignoring import Ignoring
from bitmovin.models.infrastructure_settings import InfrastructureSettings
from bitmovin.models.ingest_input_stream import IngestInputStream
from bitmovin.models.input import Input
from bitmovin.models.input_color_range import InputColorRange
from bitmovin.models.input_color_space import InputColorSpace
from bitmovin.models.input_path import InputPath
from bitmovin.models.input_stream import InputStream
from bitmovin.models.input_stream_type import InputStreamType
from bitmovin.models.input_stream_type_response import InputStreamTypeResponse
from bitmovin.models.input_type import InputType
from bitmovin.models.input_type_response import InputTypeResponse
from bitmovin.models.interlace_filter import InterlaceFilter
from bitmovin.models.interlace_mode import InterlaceMode
from bitmovin.models.internal_chunk_length import InternalChunkLength
from bitmovin.models.iv_size import IvSize
from bitmovin.models.keyframe import Keyframe
from bitmovin.models.kubernetes_cluster import KubernetesCluster
from bitmovin.models.kubernetes_cluster_configuration import KubernetesClusterConfiguration
from bitmovin.models.level_h264 import LevelH264
from bitmovin.models.level_h265 import LevelH265
from bitmovin.models.limit_references import LimitReferences
from bitmovin.models.limit_transform_unit_depth_recursion_mode import LimitTransformUnitDepthRecursionMode
from bitmovin.models.link import Link
from bitmovin.models.live_dash_manifest import LiveDashManifest
from bitmovin.models.live_encoding import LiveEncoding
from bitmovin.models.live_encoding_codec import LiveEncodingCodec
from bitmovin.models.live_encoding_event_name import LiveEncodingEventName
from bitmovin.models.live_encoding_stats import LiveEncodingStats
from bitmovin.models.live_encoding_stats_event import LiveEncodingStatsEvent
from bitmovin.models.live_encoding_stats_event_details import LiveEncodingStatsEventDetails
from bitmovin.models.live_encoding_status import LiveEncodingStatus
from bitmovin.models.live_hls_manifest import LiveHlsManifest
from bitmovin.models.local_input import LocalInput
from bitmovin.models.local_output import LocalOutput
from bitmovin.models.log_level import LogLevel
from bitmovin.models.login import Login
from bitmovin.models.manifest import Manifest
from bitmovin.models.manifest_resource import ManifestResource
from bitmovin.models.manifest_type import ManifestType
from bitmovin.models.manifest_type_response import ManifestTypeResponse
from bitmovin.models.marlin_drm import MarlinDrm
from bitmovin.models.max_ctu_size import MaxCtuSize
from bitmovin.models.max_transform_unit_size import MaxTransformUnitSize
from bitmovin.models.media_info_type import MediaInfoType
from bitmovin.models.media_info_type_response import MediaInfoTypeResponse
from bitmovin.models.media_stream import MediaStream
from bitmovin.models.media_type import MediaType
from bitmovin.models.message import Message
from bitmovin.models.message_type import MessageType
from bitmovin.models.min_coding_unit_size import MinCodingUnitSize
from bitmovin.models.mjpeg_video_configuration import MjpegVideoConfiguration
from bitmovin.models.motion_search import MotionSearch
from bitmovin.models.mp2_audio_configuration import Mp2AudioConfiguration
from bitmovin.models.mp3_audio_configuration import Mp3AudioConfiguration
from bitmovin.models.mp3_muxing import Mp3Muxing
from bitmovin.models.mp3_muxing_information import Mp3MuxingInformation
from bitmovin.models.mp4_muxing import Mp4Muxing
from bitmovin.models.mp4_muxing_information import Mp4MuxingInformation
from bitmovin.models.muxing import Muxing
from bitmovin.models.muxing_information_audio_track import MuxingInformationAudioTrack
from bitmovin.models.muxing_information_video_track import MuxingInformationVideoTrack
from bitmovin.models.muxing_stream import MuxingStream
from bitmovin.models.muxing_type import MuxingType
from bitmovin.models.mv_prediction_mode import MvPredictionMode
from bitmovin.models.notification import Notification
from bitmovin.models.notification_state_entry import NotificationStateEntry
from bitmovin.models.notification_states import NotificationStates
from bitmovin.models.object_detection_bounding_box import ObjectDetectionBoundingBox
from bitmovin.models.object_detection_configuration import ObjectDetectionConfiguration
from bitmovin.models.object_detection_result import ObjectDetectionResult
from bitmovin.models.opus_audio_configuration import OpusAudioConfiguration
from bitmovin.models.opus_channel_layout import OpusChannelLayout
from bitmovin.models.or_conjunction import OrConjunction
from bitmovin.models.organization import Organization
from bitmovin.models.output import Output
from bitmovin.models.output_type import OutputType
from bitmovin.models.output_type_response import OutputTypeResponse
from bitmovin.models.pagination_response import PaginationResponse
from bitmovin.models.per_title import PerTitle
from bitmovin.models.per_title_configuration import PerTitleConfiguration
from bitmovin.models.per_title_fixed_resolution_and_bitrate_configuration import PerTitleFixedResolutionAndBitrateConfiguration
from bitmovin.models.per_title_fixed_resolution_and_bitrate_configuration_mode import PerTitleFixedResolutionAndBitrateConfigurationMode
from bitmovin.models.period import Period
from bitmovin.models.permission import Permission
from bitmovin.models.picture_field_parity import PictureFieldParity
from bitmovin.models.pixel_format import PixelFormat
from bitmovin.models.plaintext_id3_tag import PlaintextId3Tag
from bitmovin.models.play_ready_drm import PlayReadyDrm
from bitmovin.models.play_ready_encryption_method import PlayReadyEncryptionMethod
from bitmovin.models.player_channel import PlayerChannel
from bitmovin.models.player_license import PlayerLicense
from bitmovin.models.player_license_analytics import PlayerLicenseAnalytics
from bitmovin.models.player_third_party_licensing import PlayerThirdPartyLicensing
from bitmovin.models.player_third_party_licensing_error_action import PlayerThirdPartyLicensingErrorAction
from bitmovin.models.player_version import PlayerVersion
from bitmovin.models.policy import Policy
from bitmovin.models.position_mode import PositionMode
from bitmovin.models.position_unit import PositionUnit
from bitmovin.models.preset_configuration import PresetConfiguration
from bitmovin.models.prewarm_encoder_settings import PrewarmEncoderSettings
from bitmovin.models.prime_time_drm import PrimeTimeDrm
from bitmovin.models.profile_h264 import ProfileH264
from bitmovin.models.profile_h265 import ProfileH265
from bitmovin.models.progressive_mov_muxing import ProgressiveMovMuxing
from bitmovin.models.progressive_mov_muxing_information import ProgressiveMovMuxingInformation
from bitmovin.models.progressive_muxing_information import ProgressiveMuxingInformation
from bitmovin.models.progressive_ts_muxing import ProgressiveTsMuxing
from bitmovin.models.progressive_ts_muxing_information import ProgressiveTsMuxingInformation
from bitmovin.models.progressive_ts_muxing_information_byte_ranges import ProgressiveTsMuxingInformationByteRanges
from bitmovin.models.progressive_webm_muxing import ProgressiveWebmMuxing
from bitmovin.models.progressive_webm_muxing_information import ProgressiveWebmMuxingInformation
from bitmovin.models.psnr_per_stream_mode import PsnrPerStreamMode
from bitmovin.models.psnr_quality_metric import PsnrQualityMetric
from bitmovin.models.quantization_group_size import QuantizationGroupSize
from bitmovin.models.rai_unit import RaiUnit
from bitmovin.models.rate_distortion_level_for_quantization import RateDistortionLevelForQuantization
from bitmovin.models.rate_distortion_penalty_mode import RateDistortionPenaltyMode
from bitmovin.models.raw_id3_tag import RawId3Tag
from bitmovin.models.redundant_rtmp_input import RedundantRtmpInput
from bitmovin.models.reprioritize_encoding_request import ReprioritizeEncodingRequest
from bitmovin.models.reschedule_encoding_request import RescheduleEncodingRequest
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.response_error_data import ResponseErrorData
from bitmovin.models.response_status import ResponseStatus
from bitmovin.models.result_wrapper import ResultWrapper
from bitmovin.models.retry_hint import RetryHint
from bitmovin.models.reupload_settings import ReuploadSettings
from bitmovin.models.rotate_filter import RotateFilter
from bitmovin.models.rtmp_ingest_point import RtmpIngestPoint
from bitmovin.models.rtmp_input import RtmpInput
from bitmovin.models.s3_input import S3Input
from bitmovin.models.s3_output import S3Output
from bitmovin.models.s3_role_based_input import S3RoleBasedInput
from bitmovin.models.s3_role_based_output import S3RoleBasedOutput
from bitmovin.models.s3_signature_version import S3SignatureVersion
from bitmovin.models.scale_filter import ScaleFilter
from bitmovin.models.scaling_algorithm import ScalingAlgorithm
from bitmovin.models.scc_caption import SccCaption
from bitmovin.models.scheduling import Scheduling
from bitmovin.models.segmented_raw_muxing import SegmentedRawMuxing
from bitmovin.models.segments_media_info import SegmentsMediaInfo
from bitmovin.models.sftp_input import SftpInput
from bitmovin.models.sftp_output import SftpOutput
from bitmovin.models.sidecar_error_mode import SidecarErrorMode
from bitmovin.models.sidecar_file import SidecarFile
from bitmovin.models.signature_type import SignatureType
from bitmovin.models.smooth_manifest_content_protection import SmoothManifestContentProtection
from bitmovin.models.smooth_manifest_default import SmoothManifestDefault
from bitmovin.models.smooth_manifest_default_version import SmoothManifestDefaultVersion
from bitmovin.models.smooth_streaming_manifest import SmoothStreamingManifest
from bitmovin.models.smooth_streaming_representation import SmoothStreamingRepresentation
from bitmovin.models.source_channel import SourceChannel
from bitmovin.models.source_channel_type import SourceChannelType
from bitmovin.models.sprite import Sprite
from bitmovin.models.sprite_unit import SpriteUnit
from bitmovin.models.srt_input import SrtInput
from bitmovin.models.srt_mode import SrtMode
from bitmovin.models.srt_statistic_link import SrtStatisticLink
from bitmovin.models.srt_statistic_recv import SrtStatisticRecv
from bitmovin.models.srt_statistic_send import SrtStatisticSend
from bitmovin.models.srt_statistic_window import SrtStatisticWindow
from bitmovin.models.srt_statistics import SrtStatistics
from bitmovin.models.standard_media_info import StandardMediaInfo
from bitmovin.models.start_encoding_request import StartEncodingRequest
from bitmovin.models.start_live_encoding_request import StartLiveEncodingRequest
from bitmovin.models.statistics import Statistics
from bitmovin.models.statistics_per_label import StatisticsPerLabel
from bitmovin.models.statistics_per_muxing import StatisticsPerMuxing
from bitmovin.models.statistics_per_stream import StatisticsPerStream
from bitmovin.models.statistics_per_title_stream import StatisticsPerTitleStream
from bitmovin.models.statistics_resolution import StatisticsResolution
from bitmovin.models.status import Status
from bitmovin.models.stream import Stream
from bitmovin.models.stream_caption_output_format import StreamCaptionOutputFormat
from bitmovin.models.stream_conditions_mode import StreamConditionsMode
from bitmovin.models.stream_details import StreamDetails
from bitmovin.models.stream_dvb_sub_subtitle import StreamDvbSubSubtitle
from bitmovin.models.stream_filter import StreamFilter
from bitmovin.models.stream_filter_list import StreamFilterList
from bitmovin.models.stream_info import StreamInfo
from bitmovin.models.stream_infos import StreamInfos
from bitmovin.models.stream_infos_details import StreamInfosDetails
from bitmovin.models.stream_input import StreamInput
from bitmovin.models.stream_metadata import StreamMetadata
from bitmovin.models.stream_mode import StreamMode
from bitmovin.models.stream_per_title_fixed_resolution_and_bitrate_settings import StreamPerTitleFixedResolutionAndBitrateSettings
from bitmovin.models.stream_per_title_settings import StreamPerTitleSettings
from bitmovin.models.stream_selection_mode import StreamSelectionMode
from bitmovin.models.subtask import Subtask
from bitmovin.models.subtitle_adaptation_set import SubtitleAdaptationSet
from bitmovin.models.subtitle_stream import SubtitleStream
from bitmovin.models.subtitles_media_info import SubtitlesMediaInfo
from bitmovin.models.task import Task
from bitmovin.models.tcp_input import TcpInput
from bitmovin.models.tenant import Tenant
from bitmovin.models.text_filter import TextFilter
from bitmovin.models.text_filter_font import TextFilterFont
from bitmovin.models.thumbnail import Thumbnail
from bitmovin.models.thumbnail_unit import ThumbnailUnit
from bitmovin.models.time_based_trimming_input_stream import TimeBasedTrimmingInputStream
from bitmovin.models.time_code import TimeCode
from bitmovin.models.time_span import TimeSpan
from bitmovin.models.timecode_track_trimming_input_stream import TimecodeTrackTrimmingInputStream
from bitmovin.models.transfer_version import TransferVersion
from bitmovin.models.transform_skip_mode import TransformSkipMode
from bitmovin.models.trimming import Trimming
from bitmovin.models.ts_muxing import TsMuxing
from bitmovin.models.ttml_embed import TtmlEmbed
from bitmovin.models.tu_inter_depth import TuInterDepth
from bitmovin.models.tu_intra_depth import TuIntraDepth
from bitmovin.models.tweaks import Tweaks
from bitmovin.models.udp_input import UdpInput
from bitmovin.models.udp_multicast_input import UdpMulticastInput
from bitmovin.models.unsharp_filter import UnsharpFilter
from bitmovin.models.utc_timing import UtcTiming
from bitmovin.models.variant_stream_dropping_mode import VariantStreamDroppingMode
from bitmovin.models.vertical_low_pass_filtering_mode import VerticalLowPassFilteringMode
from bitmovin.models.video_adaptation_set import VideoAdaptationSet
from bitmovin.models.video_configuration import VideoConfiguration
from bitmovin.models.video_format import VideoFormat
from bitmovin.models.video_media_info import VideoMediaInfo
from bitmovin.models.video_stream import VideoStream
from bitmovin.models.vorbis_audio_configuration import VorbisAudioConfiguration
from bitmovin.models.vorbis_channel_layout import VorbisChannelLayout
from bitmovin.models.vp8_arnr_type import Vp8ArnrType
from bitmovin.models.vp8_noise_sensitivity import Vp8NoiseSensitivity
from bitmovin.models.vp8_quality import Vp8Quality
from bitmovin.models.vp8_video_configuration import Vp8VideoConfiguration
from bitmovin.models.vp9_aq_mode import Vp9AqMode
from bitmovin.models.vp9_arnr_type import Vp9ArnrType
from bitmovin.models.vp9_per_title_configuration import Vp9PerTitleConfiguration
from bitmovin.models.vp9_quality import Vp9Quality
from bitmovin.models.vp9_video_configuration import Vp9VideoConfiguration
from bitmovin.models.vtt_media_info import VttMediaInfo
from bitmovin.models.watermark_filter import WatermarkFilter
from bitmovin.models.web_vtt_sidecar_file import WebVttSidecarFile
from bitmovin.models.web_vtt_sidecar_file_segmentation import WebVttSidecarFileSegmentation
from bitmovin.models.webhook import Webhook
from bitmovin.models.webhook_encryption import WebhookEncryption
from bitmovin.models.webhook_http_method import WebhookHttpMethod
from bitmovin.models.webhook_signature import WebhookSignature
from bitmovin.models.webm_muxing import WebmMuxing
from bitmovin.models.weighted_prediction_p_frames import WeightedPredictionPFrames
from bitmovin.models.widevine_drm import WidevineDrm
from bitmovin.models.xml_namespace import XmlNamespace
from bitmovin.models.zixi_input import ZixiInput
