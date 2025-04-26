  * [ FFmpeg](.)
  * [About](about.html)
  * [News](index.html#news)
  * [Download](download.html)
  * [Documentation](documentation.html)
  * [Community](community.html)
    * [Code of Conduct](community.html#CodeOfConduct)
    * [Mailing Lists](contact.html#MailingLists)
    * [IRC](contact.html#IRCChannels)
    * [Forums](contact.html#Forums)
    * [Bug Reports](bugreports.html)
    * [Wiki](https://trac.ffmpeg.org)
    * [Conferences](https://trac.ffmpeg.org/wiki/Conferences)
  * [Developers](developer.html)
    * [Source Code](download.html#get-sources)
    * [Contribute](developer.html#Introduction)
    * [FATE](http://fate.ffmpeg.org)
    * [Code Coverage](http://coverage.ffmpeg.org)
    * [Funding through SPI](spi.html)
  * More
    * [ Donate __](donations.html)
    * [Hire Developers](consulting.html)
    * [Contact](contact.html)
    * [Security](security.html)
    * [Legal](legal.html)

#  __FFmpeg Codecs Documentation

## Table of Contents

  * 1 Description
  * 2 Codec Options
  * 3 Decoders
  * 4 Video Decoders
    * 4.1 av1
      * 4.1.1 Options
    * 4.2 hevc
      * 4.2.1 Options
    * 4.3 rawvideo
      * 4.3.1 Options
    * 4.4 libdav1d
      * 4.4.1 Options
    * 4.5 libdavs2
    * 4.6 libuavs3d
      * 4.6.1 Options
    * 4.7 libxevd
      * 4.7.1 Options
    * 4.8 QSV Decoders
      * 4.8.1 Common Options
      * 4.8.2 HEVC Options
    * 4.9 v210
      * 4.9.1 Options
  * 5 Audio Decoders
    * 5.1 ac3
      * 5.1.1 AC-3 Decoder Options
    * 5.2 flac
      * 5.2.1 FLAC Decoder options
    * 5.3 ffwavesynth
    * 5.4 libcelt
    * 5.5 libgsm
    * 5.6 libilbc
      * 5.6.1 Options
    * 5.7 libopencore-amrnb
    * 5.8 libopencore-amrwb
    * 5.9 libopus
  * 6 Subtitles Decoders
    * 6.1 libaribb24
      * 6.1.1 libaribb24 Decoder Options
    * 6.2 libaribcaption
      * 6.2.1 libaribcaption Decoder Options
      * 6.2.2 libaribcaption decoder usage examples
    * 6.3 dvbsub
      * 6.3.1 Options
    * 6.4 dvdsub
      * 6.4.1 Options
    * 6.5 libzvbi-teletext
      * 6.5.1 Options
  * 7 Encoders
  * 8 Audio Encoders
    * 8.1 aac
      * 8.1.1 Options
    * 8.2 ac3 and ac3_fixed
      * 8.2.1 AC-3 Metadata
        * 8.2.1.1 Metadata Control Options
        * 8.2.1.2 Downmix Levels
        * 8.2.1.3 Audio Production Information
        * 8.2.1.4 Other Metadata Options
      * 8.2.2 Extended Bitstream Information
        * 8.2.2.1 Extended Bitstream Information - Part 1
        * 8.2.2.2 Extended Bitstream Information - Part 2
      * 8.2.3 Other AC-3 Encoding Options
      * 8.2.4 Floating-Point-Only AC-3 Encoding Options
    * 8.3 flac
      * 8.3.1 Options
    * 8.4 opus
      * 8.4.1 Options
    * 8.5 libfdk_aac
      * 8.5.1 Options
      * 8.5.2 Examples
    * 8.6 liblc3
      * 8.6.1 Options
    * 8.7 libmp3lame
      * 8.7.1 Options
    * 8.8 libopencore-amrnb
      * 8.8.1 Options
    * 8.9 libopus
      * 8.9.1 Option Mapping
    * 8.10 libshine
      * 8.10.1 Options
    * 8.11 libtwolame
      * 8.11.1 Options
    * 8.12 libvo-amrwbenc
      * 8.12.1 Options
    * 8.13 libvorbis
      * 8.13.1 Options
    * 8.14 mjpeg
      * 8.14.1 Options
    * 8.15 wavpack
      * 8.15.1 Options
        * 8.15.1.1 Shared options
        * 8.15.1.2 Private options
  * 9 Video Encoders
    * 9.1 a64_multi, a64_multi5
    * 9.2 Cinepak
      * 9.2.1 Options
    * 9.3 ffv1
      * 9.3.1 Options
    * 9.4 GIF
      * 9.4.1 Options
    * 9.5 Hap
      * 9.5.1 Options
    * 9.6 jpeg2000
      * 9.6.1 Options
    * 9.7 librav1e
      * 9.7.1 Options
    * 9.8 libaom-av1
      * 9.8.1 Options
    * 9.9 libsvtav1
      * 9.9.1 Options
    * 9.10 libjxl
      * 9.10.1 Options
    * 9.11 libkvazaar
      * 9.11.1 Options
    * 9.12 libopenh264
      * 9.12.1 Options
    * 9.13 libtheora
      * 9.13.1 Options
      * 9.13.2 Examples
    * 9.14 libvpx
      * 9.14.1 Options
    * 9.15 libvvenc
      * 9.15.1 Supported Pixel Formats
      * 9.15.2 Options
    * 9.16 libwebp
      * 9.16.1 Pixel Format
      * 9.16.2 Options
    * 9.17 libx264, libx264rgb
      * 9.17.1 Supported Pixel Formats
      * 9.17.2 Options
    * 9.18 libx265
      * 9.18.1 Options
    * 9.19 libxavs2
      * 9.19.1 Options
    * 9.20 libxeve
      * 9.20.1 Options
    * 9.21 libxvid
      * 9.21.1 Options
    * 9.22 MediaFoundation
    * 9.23 Microsoft RLE
      * 9.23.1 Options
    * 9.24 mpeg2
      * 9.24.1 Options
    * 9.25 png
      * 9.25.1 Options
      * 9.25.2 Private options
    * 9.26 ProRes
      * 9.26.1 Private Options for prores-ks
      * 9.26.2 Speed considerations
    * 9.27 QSV Encoders
      * 9.27.1 Ratecontrol Method
      * 9.27.2 Global Options -> MSDK Options
      * 9.27.3 Common Options
      * 9.27.4 Runtime Options
      * 9.27.5 H264 options
      * 9.27.6 HEVC Options
      * 9.27.7 MPEG2 Options
      * 9.27.8 VP9 Options
      * 9.27.9 AV1 Options
    * 9.28 snow
      * 9.28.1 Options
    * 9.29 VAAPI encoders
    * 9.30 vbn
      * 9.30.1 Options
    * 9.31 vc2
      * 9.31.1 Options
  * 10 Subtitles Encoders
    * 10.1 dvdsub
      * 10.1.1 Options
  * 11 See Also
  * 12 Authors

## 1 Description

This document describes the codecs (decoders and encoders) provided by the
libavcodec library.

## 2 Codec Options

libavcodec provides some generic global options, which can be set on all the
encoders and decoders. In addition, each codec may support so-called private
options, which are specific for a given codec.

Sometimes, a global option may only affect a specific kind of codec, and may
be nonsensical or ignored by another, so you need to be aware of the meaning
of the specified options. Also some options are meant only for decoding or
encoding.

Options may be set by specifying -option value in the FFmpeg tools, or by
setting the value explicitly in the `AVCodecContext` options or using the
libavutil/opt.h API for programmatic use.

The list of supported options follow:

b integer (_encoding,audio,video_)

    

Set bitrate in bits/s. Default value is 200K.

ab integer (_encoding,audio_)

    

Set audio bitrate (in bits/s). Default value is 128K.

bt integer (_encoding,video_)

    

Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance
specifies how far ratecontrol is willing to deviate from the target average
bitrate value. This is not related to min/max bitrate. Lowering tolerance too
much has an adverse effect on quality.

flags flags (_decoding/encoding,audio,video,subtitles_)

    

Set generic flags.

Possible values:

'mv4'

    

Use four motion vector by macroblock (mpeg4).

'qpel'

    

Use 1/4 pel motion compensation.

'loop'

    

Use loop filter.

'qscale'

    

Use fixed qscale.

'pass1'

    

Use internal 2pass ratecontrol in first pass mode.

'pass2'

    

Use internal 2pass ratecontrol in second pass mode.

'gray'

    

Only decode/encode grayscale.

'psnr'

    

Set error[?] variables during encoding.

'truncated'

    

Input bitstream might be randomly truncated.

'drop_changed'

    

Don't output frames whose parameters differ from first decoded frame in
stream. Error AVERROR_INPUT_CHANGED is returned when a frame is dropped.

'ildct'

    

Use interlaced DCT.

'low_delay'

    

Force low delay.

'global_header'

    

Place global headers in extradata instead of every keyframe.

'bitexact'

    

Only write platform-, build- and time-independent data. (except (I)DCT). This
ensures that file and data checksums are reproducible and match between
platforms. Its primary use is for regression testing.

'aic'

    

Apply H263 advanced intra coding / mpeg4 ac prediction.

'ilme'

    

Apply interlaced motion estimation.

'cgop'

    

Use closed gop.

'output_corrupt'

    

Output even potentially corrupted frames.

time_base rational number

    

Set codec time base.

It is the fundamental unit of time (in seconds) in terms of which frame
timestamps are represented. For fixed-fps content, timebase should be `1 /
frame_rate` and timestamp increments should be identically 1.

g integer (_encoding,video_)

    

Set the group of picture (GOP) size. Default value is 12.

ar integer (_decoding/encoding,audio_)

    

Set audio sampling rate (in Hz).

ac integer (_decoding/encoding,audio_)

    

Set number of audio channels.

cutoff integer (_encoding,audio_)

    

Set cutoff bandwidth. (Supported only by selected encoders, see their
respective documentation sections.)

frame_size integer (_encoding,audio_)

    

Set audio frame size.

Each submitted frame except the last must contain exactly frame_size samples
per channel. May be 0 when the codec has CODEC_CAP_VARIABLE_FRAME_SIZE set, in
that case the frame size is not restricted. It is set by some decoders to
indicate constant frame size.

frame_number integer

    

Set the frame number.

delay integer

qcomp float (_encoding,video_)

    

Set video quantizer scale compression (VBR). It is used as a constant in the
ratecontrol equation. Recommended range for default rc_eq: 0.0-1.0.

qblur float (_encoding,video_)

    

Set video quantizer scale blur (VBR).

qmin integer (_encoding,video_)

    

Set min video quantizer scale (VBR). Must be included between -1 and 69,
default value is 2.

qmax integer (_encoding,video_)

    

Set max video quantizer scale (VBR). Must be included between -1 and 1024,
default value is 31.

qdiff integer (_encoding,video_)

    

Set max difference between the quantizer scale (VBR).

bf integer (_encoding,video_)

    

Set max number of B frames between non-B-frames.

Must be an integer between -1 and 16. 0 means that B-frames are disabled. If a
value of -1 is used, it will choose an automatic value depending on the
encoder.

Default value is 0.

b_qfactor float (_encoding,video_)

    

Set qp factor between P and B frames.

codec_tag integer

bug flags (_decoding,video_)

    

Workaround not auto detected encoder bugs.

Possible values:

'autodetect'

'xvid_ilace'

    

Xvid interlacing bug (autodetected if fourcc==XVIX)

'ump4'

    

(autodetected if fourcc==UMP4)

'no_padding'

    

padding bug (autodetected)

'amv'

'qpel_chroma'

'std_qpel'

    

old standard qpel (autodetected per fourcc/version)

'qpel_chroma2'

'direct_blocksize'

    

direct-qpel-blocksize bug (autodetected per fourcc/version)

'edge'

    

edge padding bug (autodetected per fourcc/version)

'hpel_chroma'

'dc_clip'

'ms'

    

Workaround various bugs in microsoft broken decoders.

'trunc'

    

trancated frames

strict integer (_decoding/encoding,audio,video_)

    

Specify how strictly to follow the standards.

Possible values:

'very'

    

strictly conform to an older more strict version of the spec or reference
software

'strict'

    

strictly conform to all the things in the spec no matter what consequences

'normal'

'unofficial'

    

allow unofficial extensions

'experimental'

    

allow non standardized experimental things, experimental (unfinished/work in
progress/not well tested) decoders and encoders. Note: experimental decoders
can pose a security risk, do not use this for decoding untrusted input.

b_qoffset float (_encoding,video_)

    

Set QP offset between P and B frames.

err_detect flags (_decoding,audio,video_)

    

Set error detection flags.

Possible values:

'crccheck'

    

verify embedded CRCs

'bitstream'

    

detect bitstream specification deviations

'buffer'

    

detect improper bitstream length

'explode'

    

abort decoding on minor error detection

'ignore_err'

    

ignore decoding errors, and continue decoding. This is useful if you want to
analyze the content of a video and thus want everything to be decoded no
matter what. This option will not result in a video that is pleasing to watch
in case of errors.

'careful'

    

consider things that violate the spec and have not been seen in the wild as
errors

'compliant'

    

consider all spec non compliancies as errors

'aggressive'

    

consider things that a sane encoder should not do as an error

has_b_frames integer

block_align integer

rc_override_count integer

maxrate integer (_encoding,audio,video_)

    

Set max bitrate tolerance (in bits/s). Requires bufsize to be set.

minrate integer (_encoding,audio,video_)

    

Set min bitrate tolerance (in bits/s). Most useful in setting up a CBR encode.
It is of little use elsewise.

bufsize integer (_encoding,audio,video_)

    

Set ratecontrol buffer size (in bits).

i_qfactor float (_encoding,video_)

    

Set QP factor between P and I frames.

i_qoffset float (_encoding,video_)

    

Set QP offset between P and I frames.

dct integer (_encoding,video_)

    

Set DCT algorithm.

Possible values:

'auto'

    

autoselect a good one (default)

'fastint'

    

fast integer

'int'

    

accurate integer

'mmx'

'altivec'

'faan'

    

floating point AAN DCT

lumi_mask float (_encoding,video_)

    

Compress bright areas stronger than medium ones.

tcplx_mask float (_encoding,video_)

    

Set temporal complexity masking.

scplx_mask float (_encoding,video_)

    

Set spatial complexity masking.

p_mask float (_encoding,video_)

    

Set inter masking.

dark_mask float (_encoding,video_)

    

Compress dark areas stronger than medium ones.

idct integer (_decoding/encoding,video_)

    

Select IDCT implementation.

Possible values:

'auto'

'int'

'simple'

'simplemmx'

'simpleauto'

    

Automatically pick a IDCT compatible with the simple one

'arm'

'altivec'

'sh4'

'simplearm'

'simplearmv5te'

'simplearmv6'

'simpleneon'

'xvid'

'faani'

    

floating point AAN IDCT

slice_count integer

ec flags (_decoding,video_)

    

Set error concealment strategy.

Possible values:

'guess_mvs'

    

iterative motion vector (MV) search (slow)

'deblock'

    

use strong deblock filter for damaged MBs

'favor_inter'

    

favor predicting from the previous frame instead of the current

bits_per_coded_sample integer

aspect rational number (_encoding,video_)

    

Set sample aspect ratio.

sar rational number (_encoding,video_)

    

Set sample aspect ratio. Alias to aspect.

debug flags (_decoding/encoding,audio,video,subtitles_)

    

Print specific debug info.

Possible values:

'pict'

    

picture info

'rc'

    

rate control

'bitstream'

'mb_type'

    

macroblock (MB) type

'qp'

    

per-block quantization parameter (QP)

'dct_coeff'

'green_metadata'

    

display complexity metadata for the upcoming frame, GoP or for a given
duration.

'skip'

'startcode'

'er'

    

error recognition

'mmco'

    

memory management control operations (H.264)

'bugs'

'buffers'

    

picture buffer allocations

'thread_ops'

    

threading operations

'nomc'

    

skip motion compensation

cmp integer (_encoding,video_)

    

Set full pel me compare function.

Possible values:

'sad'

    

sum of absolute differences, fast (default)

'sse'

    

sum of squared errors

'satd'

    

sum of absolute Hadamard transformed differences

'dct'

    

sum of absolute DCT transformed differences

'psnr'

    

sum of squared quantization errors (avoid, low quality)

'bit'

    

number of bits needed for the block

'rd'

    

rate distortion optimal, slow

'zero'

    

0

'vsad'

    

sum of absolute vertical differences

'vsse'

    

sum of squared vertical differences

'nsse'

    

noise preserving sum of squared differences

'w53'

    

5/3 wavelet, only used in snow

'w97'

    

9/7 wavelet, only used in snow

'dctmax'

'chroma'

subcmp integer (_encoding,video_)

    

Set sub pel me compare function.

Possible values:

'sad'

    

sum of absolute differences, fast (default)

'sse'

    

sum of squared errors

'satd'

    

sum of absolute Hadamard transformed differences

'dct'

    

sum of absolute DCT transformed differences

'psnr'

    

sum of squared quantization errors (avoid, low quality)

'bit'

    

number of bits needed for the block

'rd'

    

rate distortion optimal, slow

'zero'

    

0

'vsad'

    

sum of absolute vertical differences

'vsse'

    

sum of squared vertical differences

'nsse'

    

noise preserving sum of squared differences

'w53'

    

5/3 wavelet, only used in snow

'w97'

    

9/7 wavelet, only used in snow

'dctmax'

'chroma'

mbcmp integer (_encoding,video_)

    

Set macroblock compare function.

Possible values:

'sad'

    

sum of absolute differences, fast (default)

'sse'

    

sum of squared errors

'satd'

    

sum of absolute Hadamard transformed differences

'dct'

    

sum of absolute DCT transformed differences

'psnr'

    

sum of squared quantization errors (avoid, low quality)

'bit'

    

number of bits needed for the block

'rd'

    

rate distortion optimal, slow

'zero'

    

0

'vsad'

    

sum of absolute vertical differences

'vsse'

    

sum of squared vertical differences

'nsse'

    

noise preserving sum of squared differences

'w53'

    

5/3 wavelet, only used in snow

'w97'

    

9/7 wavelet, only used in snow

'dctmax'

'chroma'

ildctcmp integer (_encoding,video_)

    

Set interlaced dct compare function.

Possible values:

'sad'

    

sum of absolute differences, fast (default)

'sse'

    

sum of squared errors

'satd'

    

sum of absolute Hadamard transformed differences

'dct'

    

sum of absolute DCT transformed differences

'psnr'

    

sum of squared quantization errors (avoid, low quality)

'bit'

    

number of bits needed for the block

'rd'

    

rate distortion optimal, slow

'zero'

    

0

'vsad'

    

sum of absolute vertical differences

'vsse'

    

sum of squared vertical differences

'nsse'

    

noise preserving sum of squared differences

'w53'

    

5/3 wavelet, only used in snow

'w97'

    

9/7 wavelet, only used in snow

'dctmax'

'chroma'

dia_size integer (_encoding,video_)

    

Set diamond type & size for motion estimation.

'(1024, INT_MAX)'

    

full motion estimation(slowest)

'(768, 1024]'

    

umh motion estimation

'(512, 768]'

    

hex motion estimation

'(256, 512]'

    

l2s diamond motion estimation

'[2,256]'

    

var diamond motion estimation

'(-1, 2)'

    

small diamond motion estimation

'-1'

    

funny diamond motion estimation

'(INT_MIN, -1)'

    

sab diamond motion estimation

last_pred integer (_encoding,video_)

    

Set amount of motion predictors from the previous frame.

precmp integer (_encoding,video_)

    

Set pre motion estimation compare function.

Possible values:

'sad'

    

sum of absolute differences, fast (default)

'sse'

    

sum of squared errors

'satd'

    

sum of absolute Hadamard transformed differences

'dct'

    

sum of absolute DCT transformed differences

'psnr'

    

sum of squared quantization errors (avoid, low quality)

'bit'

    

number of bits needed for the block

'rd'

    

rate distortion optimal, slow

'zero'

    

0

'vsad'

    

sum of absolute vertical differences

'vsse'

    

sum of squared vertical differences

'nsse'

    

noise preserving sum of squared differences

'w53'

    

5/3 wavelet, only used in snow

'w97'

    

9/7 wavelet, only used in snow

'dctmax'

'chroma'

pre_dia_size integer (_encoding,video_)

    

Set diamond type & size for motion estimation pre-pass.

subq integer (_encoding,video_)

    

Set sub pel motion estimation quality.

me_range integer (_encoding,video_)

    

Set limit motion vectors range (1023 for DivX player).

global_quality integer (_encoding,audio,video_)

slice_flags integer

mbd integer (_encoding,video_)

    

Set macroblock decision algorithm (high quality mode).

Possible values:

'simple'

    

use mbcmp (default)

'bits'

    

use fewest bits

'rd'

    

use best rate distortion

rc_init_occupancy integer (_encoding,video_)

    

Set number of bits which should be loaded into the rc buffer before decoding
starts.

flags2 flags (_decoding/encoding,audio,video,subtitles_)

    

Possible values:

'fast'

    

Allow non spec compliant speedup tricks.

'noout'

    

Skip bitstream encoding.

'ignorecrop'

    

Ignore cropping information from sps.

'local_header'

    

Place global headers at every keyframe instead of in extradata.

'chunks'

    

Frame data might be split into multiple chunks.

'showall'

    

Show all frames before the first keyframe.

'export_mvs'

    

Export motion vectors into frame side-data (see
`AV_FRAME_DATA_MOTION_VECTORS`) for codecs that support it. See also
doc/examples/export_mvs.c.

'skip_manual'

    

Do not skip samples and export skip information as frame side data.

'ass_ro_flush_noop'

    

Do not reset ASS ReadOrder field on flush.

'icc_profiles'

    

Generate/parse embedded ICC profiles from/to colorimetry tags.

export_side_data flags (_decoding/encoding,audio,video,subtitles_)

    

Possible values:

'mvs'

    

Export motion vectors into frame side-data (see
`AV_FRAME_DATA_MOTION_VECTORS`) for codecs that support it. See also
doc/examples/export_mvs.c.

'prft'

    

Export encoder Producer Reference Time into packet side-data (see
`AV_PKT_DATA_PRFT`) for codecs that support it.

'venc_params'

    

Export video encoding parameters through frame side data (see
`AV_FRAME_DATA_VIDEO_ENC_PARAMS`) for codecs that support it. At present,
those are H.264 and VP9.

'film_grain'

    

Export film grain parameters through frame side data (see
`AV_FRAME_DATA_FILM_GRAIN_PARAMS`). Supported at present by AV1 decoders.

'enhancements'

    

Export picture enhancement metadata through frame side data, e.g. LCEVC (see
`AV_FRAME_DATA_LCEVC`).

threads integer (_decoding/encoding,video_)

    

Set the number of threads to be used, in case the selected codec
implementation supports multi-threading.

Possible values:

'auto, 0'

    

automatically select the number of threads to set

Default value is 'auto'.

dc integer (_encoding,video_)

    

Set intra_dc_precision.

nssew integer (_encoding,video_)

    

Set nsse weight.

skip_top integer (_decoding,video_)

    

Set number of macroblock rows at the top which are skipped.

skip_bottom integer (_decoding,video_)

    

Set number of macroblock rows at the bottom which are skipped.

profile integer (_encoding,audio,video_)

    

Set encoder codec profile. Default value is 'unknown'. Encoder specific
profiles are documented in the relevant encoder documentation.

level integer (_encoding,audio,video_)

    

Set the encoder level. This level depends on the specific codec, and might
correspond to the profile level. It is set by default to 'unknown'.

Possible values:

'unknown'

lowres integer (_decoding,audio,video_)

    

Decode at 1= 1/2, 2=1/4, 3=1/8 resolutions.

mblmin integer (_encoding,video_)

    

Set min macroblock lagrange factor (VBR).

mblmax integer (_encoding,video_)

    

Set max macroblock lagrange factor (VBR).

skip_loop_filter integer (_decoding,video_)

skip_idct integer (_decoding,video_)

skip_frame integer (_decoding,video_)

    

Make decoder discard processing depending on the frame type selected by the
option value.

skip_loop_filter skips frame loop filtering, skip_idct skips frame
IDCT/dequantization, skip_frame skips decoding.

Possible values:

'none'

    

Discard no frame.

'default'

    

Discard useless frames like 0-sized frames.

'noref'

    

Discard all non-reference frames.

'bidir'

    

Discard all bidirectional frames.

'nokey'

    

Discard all frames excepts keyframes.

'nointra'

    

Discard all frames except I frames.

'all'

    

Discard all frames.

Default value is 'default'.

bidir_refine integer (_encoding,video_)

    

Refine the two motion vectors used in bidirectional macroblocks.

keyint_min integer (_encoding,video_)

    

Set minimum interval between IDR-frames.

refs integer (_encoding,video_)

    

Set reference frames to consider for motion compensation.

trellis integer (_encoding,audio,video_)

    

Set rate-distortion optimal quantization.

mv0_threshold integer (_encoding,video_)

compression_level integer (_encoding,audio,video_)

bits_per_raw_sample integer

channel_layout integer (_decoding/encoding,audio_)

    

See [(ffmpeg-utils)the Channel Layout section in the ffmpeg-utils(1)
manual](ffmpeg-utils.html#channel-layout-syntax) for the required syntax.

rc_max_vbv_use float (_encoding,video_)

rc_min_vbv_use float (_encoding,video_)

color_primaries integer (_decoding/encoding,video_)

    

Possible values:

'bt709'

    

BT.709

'bt470m'

    

BT.470 M

'bt470bg'

    

BT.470 BG

'smpte170m'

    

SMPTE 170 M

'smpte240m'

    

SMPTE 240 M

'film'

    

Film

'bt2020'

    

BT.2020

'smpte428'

'smpte428_1'

    

SMPTE ST 428-1

'smpte431'

    

SMPTE 431-2

'smpte432'

    

SMPTE 432-1

'jedec-p22'

    

JEDEC P22

color_trc integer (_decoding/encoding,video_)

    

Possible values:

'bt709'

    

BT.709

'gamma22'

    

BT.470 M

'gamma28'

    

BT.470 BG

'smpte170m'

    

SMPTE 170 M

'smpte240m'

    

SMPTE 240 M

'linear'

    

Linear

'log'

'log100'

    

Log

'log_sqrt'

'log316'

    

Log square root

'iec61966_2_4'

'iec61966-2-4'

    

IEC 61966-2-4

'bt1361'

'bt1361e'

    

BT.1361

'iec61966_2_1'

'iec61966-2-1'

    

IEC 61966-2-1

'bt2020_10'

'bt2020_10bit'

    

BT.2020 - 10 bit

'bt2020_12'

'bt2020_12bit'

    

BT.2020 - 12 bit

'smpte2084'

    

SMPTE ST 2084

'smpte428'

'smpte428_1'

    

SMPTE ST 428-1

'arib-std-b67'

    

ARIB STD-B67

colorspace integer (_decoding/encoding,video_)

    

Possible values:

'rgb'

    

RGB

'bt709'

    

BT.709

'fcc'

    

FCC

'bt470bg'

    

BT.470 BG

'smpte170m'

    

SMPTE 170 M

'smpte240m'

    

SMPTE 240 M

'ycocg'

    

YCOCG

'bt2020nc'

'bt2020_ncl'

    

BT.2020 NCL

'bt2020c'

'bt2020_cl'

    

BT.2020 CL

'smpte2085'

    

SMPTE 2085

'chroma-derived-nc'

    

Chroma-derived NCL

'chroma-derived-c'

    

Chroma-derived CL

'ictcp'

    

ICtCp

color_range integer (_decoding/encoding,video_)

    

If used as input parameter, it serves as a hint to the decoder, which
color_range the input has. Possible values:

'tv'

'mpeg'

'limited'

    

MPEG (219*2^(n-8))

'pc'

'jpeg'

'full'

    

JPEG (2^n-1)

chroma_sample_location integer (_decoding/encoding,video_)

    

Possible values:

'left'

'center'

'topleft'

'top'

'bottomleft'

'bottom'

log_level_offset integer

    

Set the log level offset.

slices integer (_encoding,video_)

    

Number of slices, used in parallelized encoding.

thread_type flags (_decoding/encoding,video_)

    

Select which multithreading methods to use.

Use of 'frame' will increase decoding delay by one frame per thread, so
clients which cannot provide future frames should not use it.

Possible values:

'slice'

    

Decode more than one part of a single frame at once.

Multithreading using slices works only when the video was encoded with slices.

'frame'

    

Decode more than one frame at once.

Default value is 'slice+frame'.

audio_service_type integer (_encoding,audio_)

    

Set audio service type.

Possible values:

'ma'

    

Main Audio Service

'ef'

    

Effects

'vi'

    

Visually Impaired

'hi'

    

Hearing Impaired

'di'

    

Dialogue

'co'

    

Commentary

'em'

    

Emergency

'vo'

    

Voice Over

'ka'

    

Karaoke

request_sample_fmt sample_fmt (_decoding,audio_)

    

Set sample format audio decoders should prefer. Default value is `none`.

pkt_timebase rational number

sub_charenc encoding (_decoding,subtitles_)

    

Set the input subtitles character encoding.

field_order field_order (_video_)

    

Set/override the field order of the video. Possible values:

'progressive'

    

Progressive video

'tt'

    

Interlaced video, top field coded and displayed first

'bb'

    

Interlaced video, bottom field coded and displayed first

'tb'

    

Interlaced video, top coded first, bottom displayed first

'bt'

    

Interlaced video, bottom coded first, top displayed first

skip_alpha bool (_decoding,video_)

    

Set to 1 to disable processing alpha (transparency). This works like the
'gray' flag in the flags option which skips chroma information instead of
alpha. Default is 0.

codec_whitelist list (_input_)

    

"," separated list of allowed decoders. By default all are allowed.

dump_separator string (_input_)

    

Separator used to separate the fields printed on the command line about the
Stream parameters. For example, to separate the fields with newlines and
indentation:

    
    
    ffprobe -dump_separator "
                              "  -i ~/videos/matrixbench_mpeg2.mpg
    

max_pixels integer (_decoding/encoding,video_)

    

Maximum number of pixels per image. This value can be used to avoid out of
memory failures due to large images.

apply_cropping bool (_decoding,video_)

    

Enable cropping if cropping parameters are multiples of the required alignment
for the left and top parameters. If the alignment is not met the cropping will
be partially applied to maintain alignment. Default is 1 (enabled). Note: The
required alignment depends on if `AV_CODEC_FLAG_UNALIGNED` is set and the CPU.
`AV_CODEC_FLAG_UNALIGNED` cannot be changed from the command line. Also
hardware decoders will not apply left/top Cropping.

## 3 Decoders

Decoders are configured elements in FFmpeg which allow the decoding of
multimedia streams.

When you configure your FFmpeg build, all the supported native decoders are
enabled by default. Decoders requiring an external library must be enabled
manually via the corresponding `--enable-lib` option. You can list all
available decoders using the configure option `--list-decoders`.

You can disable all the decoders with the configure option `--disable-
decoders` and selectively enable / disable single decoders with the options
`--enable-decoder=DECODER` / `--disable-decoder=DECODER`.

The option `-decoders` of the ff* tools will display the list of enabled
decoders.

## 4 Video Decoders

A description of some of the currently available video decoders follows.

### 4.1 av1

AOMedia Video 1 (AV1) decoder.

#### 4.1.1 Options

operating_point

    

Select an operating point of a scalable AV1 bitstream (0 - 31). Default is 0.

### 4.2 hevc

HEVC (AKA ITU-T H.265 or ISO/IEC 23008-2) decoder.

The decoder supports MV-HEVC multiview streams with at most two views. Views
to be output are selected by supplying a list of view IDs to the decoder (the
view_ids option). This option may be set either statically before decoder
init, or from the `get_format()` callback - useful for the case when the view
count or IDs change dynamically during decoding.

Only the base layer is decoded by default.

Note that if you are using the `ffmpeg` CLI tool, you should be using view
specifiers as documented in its manual, rather than the options documented
here.

#### 4.2.1 Options

view_ids (MV-HEVC)

    

Specify a list of view IDs that should be output. This option can also be set
to a single '-1', which will cause all views defined in the VPS to be decoded
and output.

view_ids_available (MV-HEVC)

    

This option may be read by the caller to retrieve an array of view IDs
available in the active VPS. The array is empty for single-layer video.

The value of this option is guaranteed to be accurate when read from the
`get_format()` callback. It may also be set at other times (e.g. after opening
the decoder), but the value is informational only and may be incorrect (e.g.
when the stream contains multiple distinct VPS NALUs).

view_pos_available (MV-HEVC)

    

This option may be read by the caller to retrieve an array of view positions
(left, right, or unspecified) available in the active VPS, as `AVStereo3DView`
values. When the array is available, its elements apply to the corresponding
elements of view_ids_available, i.e. `view_pos_available[i]` contains the
position of view with ID `view_ids_available[i]`.

Same validity restrictions as for view_ids_available apply to this option.

### 4.3 rawvideo

Raw video decoder.

This decoder decodes rawvideo streams.

#### 4.3.1 Options

top top_field_first

    

Specify the assumed field type of the input video.

-1
    

the video is assumed to be progressive (default)

0

    

bottom-field-first is assumed

1

    

top-field-first is assumed

### 4.4 libdav1d

dav1d AV1 decoder.

libdav1d allows libavcodec to decode the AOMedia Video 1 (AV1) codec. Requires
the presence of the libdav1d headers and library during configuration. You
need to explicitly configure the build with `--enable-libdav1d`.

#### 4.4.1 Options

The following options are supported by the libdav1d wrapper.

framethreads

    

Set amount of frame threads to use during decoding. The default value is 0
(autodetect). This option is deprecated for libdav1d >= 1.0 and will be
removed in the future. Use the option `max_frame_delay` and the global option
`threads` instead.

tilethreads

    

Set amount of tile threads to use during decoding. The default value is 0
(autodetect). This option is deprecated for libdav1d >= 1.0 and will be
removed in the future. Use the global option `threads` instead.

max_frame_delay

    

Set max amount of frames the decoder may buffer internally. The default value
is 0 (autodetect).

filmgrain

    

Apply film grain to the decoded video if present in the bitstream. Defaults to
the internal default of the library. This option is deprecated and will be
removed in the future. See the global option `export_side_data` to export Film
Grain parameters instead of applying it.

oppoint

    

Select an operating point of a scalable AV1 bitstream (0 - 31). Defaults to
the internal default of the library.

alllayers

    

Output all spatial layers of a scalable AV1 bitstream. The default value is
false.

### 4.5 libdavs2

AVS2-P2/IEEE1857.4 video decoder wrapper.

This decoder allows libavcodec to decode AVS2 streams with davs2 library.

### 4.6 libuavs3d

AVS3-P2/IEEE1857.10 video decoder.

libuavs3d allows libavcodec to decode AVS3 streams. Requires the presence of
the libuavs3d headers and library during configuration. You need to explicitly
configure the build with `--enable-libuavs3d`.

#### 4.6.1 Options

The following option is supported by the libuavs3d wrapper.

frame_threads

    

Set amount of frame threads to use during decoding. The default value is 0
(autodetect).

### 4.7 libxevd

eXtra-fast Essential Video Decoder (XEVD) MPEG-5 EVC decoder wrapper.

This decoder requires the presence of the libxevd headers and library during
configuration. You need to explicitly configure the build with \--enable-
libxevd.

The xevd project website is at <https://github.com/mpeg5/xevd>.

#### 4.7.1 Options

The following options are supported by the libxevd wrapper. The xevd-
equivalent options or values are listed in parentheses for easy migration.

To get a more accurate and extensive documentation of the libxevd options,
invoke the command `xevd_app --help` or consult the libxevd documentation.

threads (_threads_)

    

Force to use a specific number of threads

### 4.8 QSV Decoders

The family of Intel QuickSync Video decoders (VC1, MPEG-2, H.264, HEVC,
JPEG/MJPEG, VP8, VP9, AV1, VVC).

#### 4.8.1 Common Options

The following options are supported by all qsv decoders.

async_depth

    

Internal parallelization depth, the higher the value the higher the latency.

gpu_copy

    

A GPU-accelerated copy between video and system memory

'default'

'on'

'off'

#### 4.8.2 HEVC Options

Extra options for hevc_qsv.

load_plugin

    

A user plugin to load in an internal session

'none'

'hevc_sw'

'hevc_hw'

load_plugins

    

A :-separate list of hexadecimal plugin UIDs to load in an internal session

### 4.9 v210

Uncompressed 4:2:2 10-bit decoder.

#### 4.9.1 Options

custom_stride

    

Set the line size of the v210 data in bytes. The default value is 0
(autodetect). You can use the special -1 value for a strideless v210 as seen
in BOXX files.

## 5 Audio Decoders

A description of some of the currently available audio decoders follows.

### 5.1 ac3

AC-3 audio decoder.

This decoder implements part of ATSC A/52:2010 and ETSI TS 102 366, as well as
the undocumented RealAudio 3 (a.k.a. dnet).

#### 5.1.1 AC-3 Decoder Options

-drc_scale value
    

Dynamic Range Scale Factor. The factor to apply to dynamic range values from
the AC-3 stream. This factor is applied exponentially. The default value is 1.
There are 3 notable scale factor ranges:

drc_scale == 0

    

DRC disabled. Produces full range audio.

0 < drc_scale <= 1

    

DRC enabled. Applies a fraction of the stream DRC value. Audio reproduction is
between full range and full compression.

drc_scale > 1

    

DRC enabled. Applies drc_scale asymmetrically. Loud sounds are fully
compressed. Soft sounds are enhanced.

### 5.2 flac

FLAC audio decoder.

This decoder aims to implement the complete FLAC specification from Xiph.

#### 5.2.1 FLAC Decoder options

-use_buggy_lpc
    

The lavc FLAC encoder used to produce buggy streams with high lpc values (like
the default value). This option makes it possible to decode such streams
correctly by using lavc's old buggy lpc logic for decoding.

### 5.3 ffwavesynth

Internal wave synthesizer.

This decoder generates wave patterns according to predefined sequences. Its
use is purely internal and the format of the data it accepts is not publicly
documented.

### 5.4 libcelt

libcelt decoder wrapper.

libcelt allows libavcodec to decode the Xiph CELT ultra-low delay audio codec.
Requires the presence of the libcelt headers and library during configuration.
You need to explicitly configure the build with `--enable-libcelt`.

### 5.5 libgsm

libgsm decoder wrapper.

libgsm allows libavcodec to decode the GSM full rate audio codec. Requires the
presence of the libgsm headers and library during configuration. You need to
explicitly configure the build with `--enable-libgsm`.

This decoder supports both the ordinary GSM and the Microsoft variant.

### 5.6 libilbc

libilbc decoder wrapper.

libilbc allows libavcodec to decode the Internet Low Bitrate Codec (iLBC)
audio codec. Requires the presence of the libilbc headers and library during
configuration. You need to explicitly configure the build with `--enable-
libilbc`.

#### 5.6.1 Options

The following option is supported by the libilbc wrapper.

enhance

    

Enable the enhancement of the decoded audio when set to 1. The default value
is 0 (disabled).

### 5.7 libopencore-amrnb

libopencore-amrnb decoder wrapper.

libopencore-amrnb allows libavcodec to decode the Adaptive Multi-Rate
Narrowband audio codec. Using it requires the presence of the libopencore-
amrnb headers and library during configuration. You need to explicitly
configure the build with `--enable-libopencore-amrnb`.

An FFmpeg native decoder for AMR-NB exists, so users can decode AMR-NB without
this library.

### 5.8 libopencore-amrwb

libopencore-amrwb decoder wrapper.

libopencore-amrwb allows libavcodec to decode the Adaptive Multi-Rate Wideband
audio codec. Using it requires the presence of the libopencore-amrwb headers
and library during configuration. You need to explicitly configure the build
with `--enable-libopencore-amrwb`.

An FFmpeg native decoder for AMR-WB exists, so users can decode AMR-WB without
this library.

### 5.9 libopus

libopus decoder wrapper.

libopus allows libavcodec to decode the Opus Interactive Audio Codec. Requires
the presence of the libopus headers and library during configuration. You need
to explicitly configure the build with `--enable-libopus`.

An FFmpeg native decoder for Opus exists, so users can decode Opus without
this library.

## 6 Subtitles Decoders

### 6.1 libaribb24

ARIB STD-B24 caption decoder.

Implements profiles A and C of the ARIB STD-B24 standard.

#### 6.1.1 libaribb24 Decoder Options

-aribb24-base-path path
    

Sets the base path for the libaribb24 library. This is utilized for reading of
configuration files (for custom unicode conversions), and for dumping of non-
text symbols as images under that location.

Unset by default.

-aribb24-skip-ruby-text boolean
    

Tells the decoder wrapper to skip text blocks that contain half-height ruby
text.

Enabled by default.

### 6.2 libaribcaption

Yet another ARIB STD-B24 caption decoder using external _libaribcaption_
library.

Implements profiles A and C of the Japanse ARIB STD-B24 standard, Brazilian
ABNT NBR 15606-1, and Philippines version of ISDB-T.

Requires the presence of the libaribcaption headers and library
(<https://github.com/xqq/libaribcaption>) during configuration. You need to
explicitly configure the build with `--enable-libaribcaption`. If both
_libaribb24_ and _libaribcaption_ are enabled, _libaribcaption_ decoder
precedes.

#### 6.2.1 libaribcaption Decoder Options

-sub_type subtitle_type
    

Specifies the format of the decoded subtitles.

'bitmap'

    

Graphical image.

'ass'

    

ASS formatted text.

'text'

    

Simple text based output without formatting.

The default is _ass_ as same as _libaribb24_ decoder. Some present players
(e.g., _mpv_) expect ASS format for ARIB caption.

-caption_encoding encoding_scheme
    

Specifies the encoding scheme of input subtitle text.

'auto'

    

Automatically detect text encoding (default).

'jis'

    

8bit-char JIS encoding defined in ARIB STD B24. This encoding used in Japan
for ISDB captions.

'utf8'

    

UTF-8 encoding defined in ARIB STD B24. This encoding is used in Philippines
for ISDB-T captions.

'latin'

    

Latin character encoding defined in ABNT NBR 15606-1. This encoding is used in
South America for SBTVD / ISDB-Tb captions.

-font font_name[,font_name2,...]
    

Specify comma-separated list of font family names to be used for _bitmap_ or
_ass_ type subtitle rendering. Only first font name is used for _ass_ type
subtitle.

If not specified, use internaly defined default font family.

-ass_single_rect boolean
    

ARIB STD-B24 specifies that some captions may be displayed at different
positions at a time (multi-rectangle subtitle). Since some players (e.g., old
_mpv_) can't handle multiple ASS rectangles in a single AVSubtitle, or
multiple ASS rectangles of indeterminate duration with the same start
timestamp, this option can change the behavior so that all the texts are
displayed in a single ASS rectangle.

The default is false.

If your player cannot handle AVSubtitles with multiple ASS rectangles
properly, set this option to true or define `ASS_SINGLE_RECT=1` to change
default behavior at compilation.

-force_outline_text boolean
    

Specify whether always render outline text for all characters regardless of
the indication by charactor style.

The default is false.

-outline_width number (0.0 - 3.0)
    

Specify width for outline text, in dots (relative).

The default is 1.5.

-ignore_background boolean
    

Specify whether to ignore background color rendering.

The default is false.

-ignore_ruby boolean
    

Specify whether to ignore rendering for ruby-like (furigana) characters.

The default is false.

-replace_drcs boolean
    

Specify whether to render replaced DRCS characters as Unicode characters.

The default is true.

-replace_msz_ascii boolean
    

Specify whether to replace MSZ (Middle Size; half width) fullwidth
alphanumerics with halfwidth alphanumerics.

The default is true.

-replace_msz_japanese boolean
    

Specify whether to replace some MSZ (Middle Size; half width) fullwidth
japanese special characters with halfwidth ones.

The default is true.

-replace_msz_glyph boolean
    

Specify whether to replace MSZ (Middle Size; half width) characters with
halfwidth glyphs if the fonts supports it. This option works under FreeType or
DirectWrite renderer with Adobe-Japan1 compliant fonts. e.g., IBM Plex Sans
JP, Morisawa BIZ UDGothic, Morisawa BIZ UDMincho, Yu Gothic, Yu Mincho, and
Meiryo.

The default is true.

-canvas_size image_size
    

Specify the resolution of the canvas to render subtitles to; usually, this
should be frame size of input video. This only applies when `-subtitle_type`
is set to bitmap.

The libaribcaption decoder assumes input frame size for bitmap rendering as
below:

  1. PROFILE_A : 1440 x 1080 with SAR (PAR) 4:3 
  2. PROFILE_C : 320 x 180 with SAR (PAR) 1:1 

If actual frame size of input video does not match above assumption, the
rendered captions may be distorted. To make the captions undistorted, add
`-canvas_size` option to specify actual input video size.

Note that the `-canvas_size` option is not required for video with different
size but same aspect ratio. In such cases, the caption will be stretched or
shrunk to actual video size if `-canvas_size` option is not specified. If
`-canvas_size` option is specified with different size, the caption will be
stretched or shrunk as specified size with calculated SAR.

#### 6.2.2 libaribcaption decoder usage examples

Display MPEG-TS file with ARIB subtitle by `ffplay` tool:

    
    
    ffplay -sub_type bitmap MPEG.TS
    

Display MPEG-TS file with input frame size 1920x1080 by `ffplay` tool:

    
    
    ffplay -sub_type bitmap -canvas_size 1920x1080 MPEG.TS
    

Embed ARIB subtitle in transcoded video:

    
    
    ffmpeg -sub_type bitmap -i src.m2t -filter_complex "[0:v][0:s]overlay" -vcodec h264 dest.mp4
    

### 6.3 dvbsub

#### 6.3.1 Options

compute_clut

    

-2
    

Compute clut once if no matching CLUT is in the stream.

-1
    

Compute clut if no matching CLUT is in the stream.

0

    

Never compute CLUT

1

    

Always compute CLUT and override the one provided in the stream.

dvb_substream

    

Selects the dvb substream, or all substreams if -1 which is default.

### 6.4 dvdsub

This codec decodes the bitmap subtitles used in DVDs; the same subtitles can
also be found in VobSub file pairs and in some Matroska files.

#### 6.4.1 Options

palette

    

Specify the global palette used by the bitmaps. When stored in VobSub, the
palette is normally specified in the index file; in Matroska, the palette is
stored in the codec extra-data in the same format as in VobSub. In DVDs, the
palette is stored in the IFO file, and therefore not available when reading
from dumped VOB files.

The format for this option is a string containing 16 24-bits hexadecimal
numbers (without 0x prefix) separated by commas, for example `0d00ee, ee450d,
101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e,
0d950c, 0f007b, cf0dec, cfa80c, 7c127b`.

ifo_palette

    

Specify the IFO file from which the global palette is obtained. (experimental)

forced_subs_only

    

Only decode subtitle entries marked as forced. Some titles have forced and
non-forced subtitles in the same track. Setting this flag to `1` will only
keep the forced subtitles. Default value is `0`.

### 6.5 libzvbi-teletext

Libzvbi allows libavcodec to decode DVB teletext pages and DVB teletext
subtitles. Requires the presence of the libzvbi headers and library during
configuration. You need to explicitly configure the build with `--enable-
libzvbi`.

#### 6.5.1 Options

txt_page

    

List of teletext page numbers to decode. Pages that do not match the specified
list are dropped. You may use the special `*` string to match all pages, or
`subtitle` to match all subtitle pages. Default value is *.

txt_default_region

    

Set default character set used for decoding, a value between 0 and 87 (see ETS
300 706, Section 15, Table 32). Default value is -1, which does not override
the libzvbi default. This option is needed for some legacy level 1.0
transmissions which cannot signal the proper charset.

txt_chop_top

    

Discards the top teletext line. Default value is 1.

txt_format

    

Specifies the format of the decoded subtitles.

bitmap

    

The default format, you should use this for teletext pages, because certain
graphics and colors cannot be expressed in simple text or even ASS.

text

    

Simple text based output without formatting.

ass

    

Formatted ASS output, subtitle pages and teletext pages are returned in
different styles, subtitle pages are stripped down to text, but an effort is
made to keep the text alignment and the formatting.

txt_left

    

X offset of generated bitmaps, default is 0.

txt_top

    

Y offset of generated bitmaps, default is 0.

txt_chop_spaces

    

Chops leading and trailing spaces and removes empty lines from the generated
text. This option is useful for teletext based subtitles where empty spaces
may be present at the start or at the end of the lines or empty lines may be
present between the subtitle lines because of double-sized teletext
characters. Default value is 1.

txt_duration

    

Sets the display duration of the decoded teletext pages or subtitles in
milliseconds. Default value is -1 which means infinity or until the next
subtitle event comes.

txt_transparent

    

Force transparent background of the generated teletext bitmaps. Default value
is 0 which means an opaque background.

txt_opacity

    

Sets the opacity (0-255) of the teletext background. If txt_transparent is not
set, it only affects characters between a start box and an end box, typically
subtitles. Default value is 0 if txt_transparent is set, 255 otherwise.

## 7 Encoders

Encoders are configured elements in FFmpeg which allow the encoding of
multimedia streams.

When you configure your FFmpeg build, all the supported native encoders are
enabled by default. Encoders requiring an external library must be enabled
manually via the corresponding `--enable-lib` option. You can list all
available encoders using the configure option `--list-encoders`.

You can disable all the encoders with the configure option `--disable-
encoders` and selectively enable / disable single encoders with the options
`--enable-encoder=ENCODER` / `--disable-encoder=ENCODER`.

The option `-encoders` of the ff* tools will display the list of enabled
encoders.

## 8 Audio Encoders

A description of some of the currently available audio encoders follows.

### 8.1 aac

Advanced Audio Coding (AAC) encoder.

This encoder is the default AAC encoder, natively implemented into FFmpeg.

#### 8.1.1 Options

b

    

Set bit rate in bits/s. Setting this automatically activates constant bit rate
(CBR) mode. If this option is unspecified it is set to 128kbps.

q

    

Set quality for variable bit rate (VBR) mode. This option is valid only using
the `ffmpeg` command-line tool. For library interface users, use
global_quality.

cutoff

    

Set cutoff frequency. If unspecified will allow the encoder to dynamically
adjust the cutoff to improve clarity on low bitrates.

aac_coder

    

Set AAC encoder coding method. Possible values:

'twoloop'

    

Two loop searching (TLS) method. This is the default method.

This method first sets quantizers depending on band thresholds and then tries
to find an optimal combination by adding or subtracting a specific value from
all quantizers and adjusting some individual quantizer a little. Will tune
itself based on whether aac_is, aac_ms and aac_pns are enabled.

'anmr'

    

Average noise to mask ratio (ANMR) trellis-based solution.

This is an experimental coder which currently produces a lower quality, is
more unstable and is slower than the default twoloop coder but has potential.
Currently has no support for the aac_is or aac_pns options. Not currently
recommended.

'fast'

    

Constant quantizer method.

Uses a cheaper version of twoloop algorithm that doesn't try to do as many
clever adjustments. Worse with low bitrates (less than 64kbps), but is better
and much faster at higher bitrates.

aac_ms

    

Sets mid/side coding mode. The default value of "auto" will automatically use
M/S with bands which will benefit from such coding. Can be forced for all
bands using the value "enable", which is mainly useful for debugging or
disabled using "disable".

aac_is

    

Sets intensity stereo coding tool usage. By default, it's enabled and will
automatically toggle IS for similar pairs of stereo bands if it's beneficial.
Can be disabled for debugging by setting the value to "disable".

aac_pns

    

Uses perceptual noise substitution to replace low entropy high frequency bands
with imperceptible white noise during the decoding process. By default, it's
enabled, but can be disabled for debugging purposes by using "disable".

aac_tns

    

Enables the use of a multitap FIR filter which spans through the high
frequency bands to hide quantization noise during the encoding process and is
reverted by the decoder. As well as decreasing unpleasant artifacts in the
high range this also reduces the entropy in the high bands and allows for more
bits to be used by the mid-low bands. By default it's enabled but can be
disabled for debugging by setting the option to "disable".

aac_ltp

    

Enables the use of the long term prediction extension which increases coding
efficiency in very low bandwidth situations such as encoding of voice or solo
piano music by extending constant harmonic peaks in bands throughout frames.
This option is implied by profile:a aac_low. Use in conjunction with -ar to
decrease the samplerate.

profile

    

Sets the encoding profile, possible values:

'aac_low'

    

The default, AAC "Low-complexity" profile. Is the most compatible and produces
decent quality.

'mpeg2_aac_low'

    

Equivalent to `-profile:a aac_low -aac_pns 0`. PNS was introduced with the
MPEG4 specifications.

'aac_ltp'

    

Long term prediction profile, is enabled by and will enable the aac_ltp
option. Introduced in MPEG4.

If this option is unspecified it is set to 'aac_low'.

### 8.2 ac3 and ac3_fixed

AC-3 audio encoders.

These encoders implement part of ATSC A/52:2010 and ETSI TS 102 366.

The ac3 encoder uses floating-point math, while the ac3_fixed encoder only
uses fixed-point integer math. This does not mean that one is always faster,
just that one or the other may be better suited to a particular system. The
ac3_fixed encoder is not the default codec for any of the output formats, so
it must be specified explicitly using the option `-acodec ac3_fixed` in order
to use it.

#### 8.2.1 AC-3 Metadata

The AC-3 metadata options are used to set parameters that describe the audio,
but in most cases do not affect the audio encoding itself. Some of the options
do directly affect or influence the decoding and playback of the resulting
bitstream, while others are just for informational purposes. A few of the
options will add bits to the output stream that could otherwise be used for
audio data, and will thus affect the quality of the output. Those will be
indicated accordingly with a note in the option list below.

These parameters are described in detail in several publicly-available
documents.

  * [A/52:2010 - Digital Audio Compression (AC-3) (E-AC-3) Standard](http://www.atsc.org/cms/standards/a_52-2010.pdf)
  * [A/54 - Guide to the Use of the ATSC Digital Television Standard](http://www.atsc.org/cms/standards/a_54a_with_corr_1.pdf)
  * [Dolby Metadata Guide](http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/18_Metadata.Guide.pdf)
  * [Dolby Digital Professional Encoding Guidelines](http://www.dolby.com/uploadedFiles/zz-_Shared_Assets/English_PDFs/Professional/46_DDEncodingGuidelines.pdf)

#### 8.2.1.1 Metadata Control Options

-per_frame_metadata boolean
    

Allow Per-Frame Metadata. Specifies if the encoder should check for changing
metadata for each frame.

0

    

The metadata values set at initialization will be used for every frame in the
stream. (default)

1

    

Metadata values can be changed before encoding each frame.

#### 8.2.1.2 Downmix Levels

-center_mixlev level
    

Center Mix Level. The amount of gain the decoder should apply to the center
channel when downmixing to stereo. This field will only be written to the
bitstream if a center channel is present. The value is specified as a scale
factor. There are 3 valid values:

0.707

    

Apply -3dB gain

0.595

    

Apply -4.5dB gain (default)

0.500

    

Apply -6dB gain

-surround_mixlev level
    

Surround Mix Level. The amount of gain the decoder should apply to the
surround channel(s) when downmixing to stereo. This field will only be written
to the bitstream if one or more surround channels are present. The value is
specified as a scale factor. There are 3 valid values:

0.707

    

Apply -3dB gain

0.500

    

Apply -6dB gain (default)

0.000

    

Silence Surround Channel(s)

#### 8.2.1.3 Audio Production Information

Audio Production Information is optional information describing the mixing
environment. Either none or both of the fields are written to the bitstream.

-mixing_level number
    

Mixing Level. Specifies peak sound pressure level (SPL) in the production
environment when the mix was mastered. Valid values are 80 to 111, or -1 for
unknown or not indicated. The default value is -1, but that value cannot be
used if the Audio Production Information is written to the bitstream.
Therefore, if the `room_type` option is not the default value, the
`mixing_level` option must not be -1.

-room_type type
    

Room Type. Describes the equalization used during the final mixing session at
the studio or on the dubbing stage. A large room is a dubbing stage with the
industry standard X-curve equalization; a small room has flat equalization.
This field will not be written to the bitstream if both the `mixing_level`
option and the `room_type` option have the default values.

0

notindicated

    

Not Indicated (default)

1

large

    

Large Room

2

small

    

Small Room

#### 8.2.1.4 Other Metadata Options

-copyright boolean
    

Copyright Indicator. Specifies whether a copyright exists for this audio.

0

off

    

No Copyright Exists (default)

1

on

    

Copyright Exists

-dialnorm value
    

Dialogue Normalization. Indicates how far the average dialogue level of the
program is below digital 100% full scale (0 dBFS). This parameter determines a
level shift during audio reproduction that sets the average volume of the
dialogue to a preset level. The goal is to match volume level between program
sources. A value of -31dB will result in no volume level change, relative to
the source volume, during audio reproduction. Valid values are whole numbers
in the range -31 to -1, with -31 being the default.

-dsur_mode mode
    

Dolby Surround Mode. Specifies whether the stereo signal uses Dolby Surround
(Pro Logic). This field will only be written to the bitstream if the audio
stream is stereo. Using this option does **NOT** mean the encoder will
actually apply Dolby Surround processing.

0

notindicated

    

Not Indicated (default)

1

off

    

Not Dolby Surround Encoded

2

on

    

Dolby Surround Encoded

-original boolean
    

Original Bit Stream Indicator. Specifies whether this audio is from the
original source and not a copy.

0

off

    

Not Original Source

1

on

    

Original Source (default)

#### 8.2.2 Extended Bitstream Information

The extended bitstream options are part of the Alternate Bit Stream Syntax as
specified in Annex D of the A/52:2010 standard. It is grouped into 2 parts. If
any one parameter in a group is specified, all values in that group will be
written to the bitstream. Default values are used for those that are written
but have not been specified. If the mixing levels are written, the decoder
will use these values instead of the ones specified in the `center_mixlev` and
`surround_mixlev` options if it supports the Alternate Bit Stream Syntax.

#### 8.2.2.1 Extended Bitstream Information - Part 1

-dmix_mode mode
    

Preferred Stereo Downmix Mode. Allows the user to select either Lt/Rt (Dolby
Surround) or Lo/Ro (normal stereo) as the preferred stereo downmix mode.

0

notindicated

    

Not Indicated (default)

1

ltrt

    

Lt/Rt Downmix Preferred

2

loro

    

Lo/Ro Downmix Preferred

-ltrt_cmixlev level
    

Lt/Rt Center Mix Level. The amount of gain the decoder should apply to the
center channel when downmixing to stereo in Lt/Rt mode.

1.414

    

Apply +3dB gain

1.189

    

Apply +1.5dB gain

1.000

    

Apply 0dB gain

0.841

    

Apply -1.5dB gain

0.707

    

Apply -3.0dB gain

0.595

    

Apply -4.5dB gain (default)

0.500

    

Apply -6.0dB gain

0.000

    

Silence Center Channel

-ltrt_surmixlev level
    

Lt/Rt Surround Mix Level. The amount of gain the decoder should apply to the
surround channel(s) when downmixing to stereo in Lt/Rt mode.

0.841

    

Apply -1.5dB gain

0.707

    

Apply -3.0dB gain

0.595

    

Apply -4.5dB gain

0.500

    

Apply -6.0dB gain (default)

0.000

    

Silence Surround Channel(s)

-loro_cmixlev level
    

Lo/Ro Center Mix Level. The amount of gain the decoder should apply to the
center channel when downmixing to stereo in Lo/Ro mode.

1.414

    

Apply +3dB gain

1.189

    

Apply +1.5dB gain

1.000

    

Apply 0dB gain

0.841

    

Apply -1.5dB gain

0.707

    

Apply -3.0dB gain

0.595

    

Apply -4.5dB gain (default)

0.500

    

Apply -6.0dB gain

0.000

    

Silence Center Channel

-loro_surmixlev level
    

Lo/Ro Surround Mix Level. The amount of gain the decoder should apply to the
surround channel(s) when downmixing to stereo in Lo/Ro mode.

0.841

    

Apply -1.5dB gain

0.707

    

Apply -3.0dB gain

0.595

    

Apply -4.5dB gain

0.500

    

Apply -6.0dB gain (default)

0.000

    

Silence Surround Channel(s)

#### 8.2.2.2 Extended Bitstream Information - Part 2

-dsurex_mode mode
    

Dolby Surround EX Mode. Indicates whether the stream uses Dolby Surround EX
(7.1 matrixed to 5.1). Using this option does **NOT** mean the encoder will
actually apply Dolby Surround EX processing.

0

notindicated

    

Not Indicated (default)

1

on

    

Dolby Surround EX Off

2

off

    

Dolby Surround EX On

-dheadphone_mode mode
    

Dolby Headphone Mode. Indicates whether the stream uses Dolby Headphone
encoding (multi-channel matrixed to 2.0 for use with headphones). Using this
option does **NOT** mean the encoder will actually apply Dolby Headphone
processing.

0

notindicated

    

Not Indicated (default)

1

on

    

Dolby Headphone Off

2

off

    

Dolby Headphone On

-ad_conv_type type
    

A/D Converter Type. Indicates whether the audio has passed through HDCD A/D
conversion.

0

standard

    

Standard A/D Converter (default)

1

hdcd

    

HDCD A/D Converter

#### 8.2.3 Other AC-3 Encoding Options

-stereo_rematrixing boolean
    

Stereo Rematrixing. Enables/Disables use of rematrixing for stereo input. This
is an optional AC-3 feature that increases quality by selectively encoding the
left/right channels as mid/side. This option is enabled by default, and it is
highly recommended that it be left as enabled except for testing purposes.

cutoff frequency

    

Set lowpass cutoff frequency. If unspecified, the encoder selects a default
determined by various other encoding parameters.

#### 8.2.4 Floating-Point-Only AC-3 Encoding Options

These options are only valid for the floating-point encoder and do not exist
for the fixed-point encoder due to the corresponding features not being
implemented in fixed-point.

-channel_coupling boolean
    

Enables/Disables use of channel coupling, which is an optional AC-3 feature
that increases quality by combining high frequency information from multiple
channels into a single channel. The per-channel high frequency information is
sent with less accuracy in both the frequency and time domains. This allows
more bits to be used for lower frequencies while preserving enough information
to reconstruct the high frequencies. This option is enabled by default for the
floating-point encoder and should generally be left as enabled except for
testing purposes or to increase encoding speed.

-1
auto

    

Selected by Encoder (default)

0

off

    

Disable Channel Coupling

1

on

    

Enable Channel Coupling

-cpl_start_band number
    

Coupling Start Band. Sets the channel coupling start band, from 1 to 15. If a
value higher than the bandwidth is used, it will be reduced to 1 less than the
coupling end band. If auto is used, the start band will be determined by the
encoder based on the bit rate, sample rate, and channel layout. This option
has no effect if channel coupling is disabled.

-1
auto

    

Selected by Encoder (default)

### 8.3 flac

FLAC (Free Lossless Audio Codec) Encoder

#### 8.3.1 Options

The following options are supported by FFmpeg's flac encoder.

compression_level

    

Sets the compression level, which chooses defaults for many other options if
they are not set explicitly. Valid values are from 0 to 12, 5 is the default.

frame_size

    

Sets the size of the frames in samples per channel.

lpc_coeff_precision

    

Sets the LPC coefficient precision, valid values are from 1 to 15, 15 is the
default.

lpc_type

    

Sets the first stage LPC algorithm

'none'

    

LPC is not used

'fixed'

    

fixed LPC coefficients

'levinson'

'cholesky'

lpc_passes

    

Number of passes to use for Cholesky factorization during LPC analysis

min_partition_order

    

The minimum partition order

max_partition_order

    

The maximum partition order

prediction_order_method

    

'estimation'

'2level'

'4level'

'8level'

'search'

    

Bruteforce search

'log'

ch_mode

    

Channel mode

'auto'

    

The mode is chosen automatically for each frame

'indep'

    

Channels are independently coded

'left_side'

'right_side'

'mid_side'

exact_rice_parameters

    

Chooses if rice parameters are calculated exactly or approximately. if set to
1 then they are chosen exactly, which slows the code down slightly and
improves compression slightly.

multi_dim_quant

    

Multi Dimensional Quantization. If set to 1 then a 2nd stage LPC algorithm is
applied after the first stage to finetune the coefficients. This is quite slow
and slightly improves compression.

### 8.4 opus

Opus encoder.

This is a native FFmpeg encoder for the Opus format. Currently, it's in
development and only implements the CELT part of the codec. Its quality is
usually worse and at best is equal to the libopus encoder.

#### 8.4.1 Options

b

    

Set bit rate in bits/s. If unspecified it uses the number of channels and the
layout to make a good guess.

opus_delay

    

Sets the maximum delay in milliseconds. Lower delays than 20ms will very
quickly decrease quality.

### 8.5 libfdk_aac

libfdk-aac AAC (Advanced Audio Coding) encoder wrapper.

The libfdk-aac library is based on the Fraunhofer FDK AAC code from the
Android project.

Requires the presence of the libfdk-aac headers and library during
configuration. You need to explicitly configure the build with `--enable-
libfdk-aac`. The library is also incompatible with GPL, so if you allow the
use of GPL, you should configure with `--enable-gpl --enable-nonfree --enable-
libfdk-aac`.

This encoder has support for the AAC-HE profiles.

VBR encoding, enabled through the vbr or flags +qscale options, is
experimental and only works with some combinations of parameters.

Support for encoding 7.1 audio is only available with libfdk-aac 0.1.3 or
higher.

For more information see the fdk-aac project at
<http://sourceforge.net/p/opencore-amr/fdk-aac/>.

#### 8.5.1 Options

The following options are mapped on the shared FFmpeg codec options.

b

    

Set bit rate in bits/s. If the bitrate is not explicitly specified, it is
automatically set to a suitable value depending on the selected profile.

In case VBR mode is enabled the option is ignored.

ar

    

Set audio sampling rate (in Hz).

channels

    

Set the number of audio channels.

flags +qscale

    

Enable fixed quality, VBR (Variable Bit Rate) mode. Note that VBR is
implicitly enabled when the vbr value is positive.

cutoff

    

Set cutoff frequency. If not specified (or explicitly set to 0) it will use a
value automatically computed by the library. Default value is 0.

profile

    

Set audio profile.

The following profiles are recognized:

'aac_low'

    

Low Complexity AAC (LC)

'aac_he'

    

High Efficiency AAC (HE-AAC)

'aac_he_v2'

    

High Efficiency AAC version 2 (HE-AACv2)

'aac_ld'

    

Low Delay AAC (LD)

'aac_eld'

    

Enhanced Low Delay AAC (ELD)

If not specified it is set to 'aac_low'.

The following are private options of the libfdk_aac encoder.

afterburner

    

Enable afterburner feature if set to 1, disabled if set to 0. This improves
the quality but also the required processing power.

Default value is 1.

eld_sbr

    

Enable SBR (Spectral Band Replication) for ELD if set to 1, disabled if set to
0.

Default value is 0.

eld_v2

    

Enable ELDv2 (LD-MPS extension for ELD stereo signals) for ELDv2 if set to 1,
disabled if set to 0.

Note that option is available when fdk-aac version
(AACENCODER_LIB_VL0.AACENCODER_LIB_VL1.AACENCODER_LIB_VL2) > (4.0.0).

Default value is 0.

signaling

    

Set SBR/PS signaling style.

It can assume one of the following values:

'default'

    

choose signaling implicitly (explicit hierarchical by default, implicit if
global header is disabled)

'implicit'

    

implicit backwards compatible signaling

'explicit_sbr'

    

explicit SBR, implicit PS signaling

'explicit_hierarchical'

    

explicit hierarchical signaling

Default value is 'default'.

latm

    

Output LATM/LOAS encapsulated data if set to 1, disabled if set to 0.

Default value is 0.

header_period

    

Set StreamMuxConfig and PCE repetition period (in frames) for sending in-band
configuration buffers within LATM/LOAS transport layer.

Must be a 16-bits non-negative integer.

Default value is 0.

vbr

    

Set VBR mode, from 1 to 5. 1 is lowest quality (though still pretty good) and
5 is highest quality. A value of 0 will disable VBR, and CBR (Constant Bit
Rate) is enabled.

Currently only the 'aac_low' profile supports VBR encoding.

VBR modes 1-5 correspond to roughly the following average bit rates:

'1'

    

32 kbps/channel

'2'

    

40 kbps/channel

'3'

    

48-56 kbps/channel

'4'

    

64 kbps/channel

'5'

    

about 80-96 kbps/channel

Default value is 0.

frame_length

    

Set the audio frame length in samples. Default value is the internal default
of the library. Refer to the library's documentation for information about
supported values.

#### 8.5.2 Examples

  * Use `ffmpeg` to convert an audio file to VBR AAC in an M4A (MP4) container: 
        
        ffmpeg -i input.wav -codec:a libfdk_aac -vbr 3 output.m4a
        

  * Use `ffmpeg` to convert an audio file to CBR 64k kbps AAC, using the High-Efficiency AAC profile: 
        
        ffmpeg -i input.wav -c:a libfdk_aac -profile:a aac_he -b:a 64k output.m4a
        

### 8.6 liblc3

liblc3 LC3 (Low Complexity Communication Codec) encoder wrapper.

Requires the presence of the liblc3 headers and library during configuration.
You need to explicitly configure the build with `--enable-liblc3`.

This encoder has support for the Bluetooth SIG LC3 codec for the LE Audio
protocol, and the following features of LC3plus:

  * Frame duration of 2.5 and 5ms. 
  * High-Resolution mode, 48 KHz, and 96 kHz sampling rates. 

For more information see the liblc3 project at
<https://github.com/google/liblc3>.

#### 8.6.1 Options

The following options are mapped on the shared FFmpeg codec options.

b bitrate

    

Set the bit rate in bits/s. This will determine the fixed size of the encoded
frames, for a selected frame duration.

ar frequency

    

Set the audio sampling rate (in Hz).

channels

    

Set the number of audio channels.

frame_duration

    

Set the audio frame duration in milliseconds. Default value is 10ms. Allowed
frame durations are 2.5ms, 5ms, 7.5ms and 10ms. LC3 (Bluetooth LE Audio),
allows 7.5ms and 10ms; and LC3plus 2.5ms, 5ms and 10ms.

The 10ms frame duration is available in LC3 and LC3 plus standard. In this
mode, the produced bitstream can be referenced either as LC3 or LC3plus.

high_resolution boolean

    

Enable the high-resolution mode if set to 1. The high-resolution mode is
available with all LC3plus frame durations and for a sampling rate of 48 KHz,
and 96 KHz.

The encoder automatically turns off this mode at lower sampling rates and
activates it at 96 KHz.

This mode should be preferred at high bitrates. In this mode, the audio
bandwidth is always up to the Nyquist frequency, compared to LC3 at 48 KHz,
which limits the bandwidth to 20 KHz.

### 8.7 libmp3lame

LAME (Lame Ain't an MP3 Encoder) MP3 encoder wrapper.

Requires the presence of the libmp3lame headers and library during
configuration. You need to explicitly configure the build with `--enable-
libmp3lame`.

See libshine for a fixed-point MP3 encoder, although with a lower quality.

#### 8.7.1 Options

The following options are supported by the libmp3lame wrapper. The
`lame`-equivalent of the options are listed in parentheses.

b (_-b_)

    

Set bitrate expressed in bits/s for CBR or ABR. LAME `bitrate` is expressed in
kilobits/s.

q (_-V_)

    

Set constant quality setting for VBR. This option is valid only using the
`ffmpeg` command-line tool. For library interface users, use global_quality.

compression_level (_-q_)

    

Set algorithm quality. Valid arguments are integers in the 0-9 range, with 0
meaning highest quality but slowest, and 9 meaning fastest while producing the
worst quality.

cutoff (_\--lowpass_)

    

Set lowpass cutoff frequency. If unspecified, the encoder dynamically adjusts
the cutoff.

reservoir

    

Enable use of bit reservoir when set to 1. Default value is 1. LAME has this
enabled by default, but can be overridden by use \--nores option.

joint_stereo (_-m j_)

    

Enable the encoder to use (on a frame by frame basis) either L/R stereo or
mid/side stereo. Default value is 1.

abr (_\--abr_)

    

Enable the encoder to use ABR when set to 1. The `lame` \--abr sets the target
bitrate, while this options only tells FFmpeg to use ABR still relies on b to
set bitrate.

copyright (_-c_)

    

Set MPEG audio copyright flag when set to 1. The default value is 0
(disabled).

original (_-o_)

    

Set MPEG audio original flag when set to 1. The default value is 1 (enabled).

### 8.8 libopencore-amrnb

OpenCORE Adaptive Multi-Rate Narrowband encoder.

Requires the presence of the libopencore-amrnb headers and library during
configuration. You need to explicitly configure the build with `--enable-
libopencore-amrnb --enable-version3`.

This is a mono-only encoder. Officially it only supports 8000Hz sample rate,
but you can override it by setting strict to 'unofficial' or lower.

#### 8.8.1 Options

b

    

Set bitrate in bits per second. Only the following bitrates are supported,
otherwise libavcodec will round to the nearest valid bitrate.

4750

5150

5900

6700

7400

7950

10200

12200

dtx

    

Allow discontinuous transmission (generate comfort noise) when set to 1. The
default value is 0 (disabled).

### 8.9 libopus

libopus Opus Interactive Audio Codec encoder wrapper.

Requires the presence of the libopus headers and library during configuration.
You need to explicitly configure the build with `--enable-libopus`.

#### 8.9.1 Option Mapping

Most libopus options are modelled after the `opusenc` utility from opus-tools.
The following is an option mapping chart describing options supported by the
libopus wrapper, and their `opusenc`-equivalent in parentheses.

b (_bitrate_)

    

Set the bit rate in bits/s. FFmpeg's b option is expressed in bits/s, while
`opusenc`'s bitrate in kilobits/s.

vbr (_vbr_ , _hard-cbr_ , and _cvbr_)

    

Set VBR mode. The FFmpeg vbr option has the following valid arguments, with
the `opusenc` equivalent options in parentheses:

'off (_hard-cbr_)'

    

Use constant bit rate encoding.

'on (_vbr_)'

    

Use variable bit rate encoding (the default).

'constrained (_cvbr_)'

    

Use constrained variable bit rate encoding.

compression_level (_comp_)

    

Set encoding algorithm complexity. Valid options are integers in the 0-10
range. 0 gives the fastest encodes but lower quality, while 10 gives the
highest quality but slowest encoding. The default is 10.

frame_duration (_framesize_)

    

Set maximum frame size, or duration of a frame in milliseconds. The argument
must be exactly the following: 2.5, 5, 10, 20, 40, 60. Smaller frame sizes
achieve lower latency but less quality at a given bitrate. Sizes greater than
20ms are only interesting at fairly low bitrates. The default is 20ms.

packet_loss (_expect-loss_)

    

Set expected packet loss percentage. The default is 0.

fec (_n/a_)

    

Enable inband forward error correction. packet_loss must be non-zero to take
advantage - frequency of FEC 'side-data' is proportional to expected packet
loss. Default is disabled.

application (N.A.)

    

Set intended application type. Valid options are listed below:

'voip'

    

Favor improved speech intelligibility.

'audio'

    

Favor faithfulness to the input (the default).

'lowdelay'

    

Restrict to only the lowest delay modes by disabling voice-optimized modes.

cutoff (N.A.)

    

Set cutoff bandwidth in Hz. The argument must be exactly one of the following:
4000, 6000, 8000, 12000, or 20000, corresponding to narrowband, mediumband,
wideband, super wideband, and fullband respectively. The default is 0 (cutoff
disabled). Note that libopus forces a wideband cutoff for bitrates < 15 kbps,
unless CELT-only (application set to 'lowdelay') mode is used.

mapping_family (_mapping_family_)

    

Set channel mapping family to be used by the encoder. The default value of -1
uses mapping family 0 for mono and stereo inputs, and mapping family 1
otherwise. The default also disables the surround masking and LFE bandwidth
optimzations in libopus, and requires that the input contains 8 channels or
fewer.

Other values include 0 for mono and stereo, 1 for surround sound with masking
and LFE bandwidth optimizations, and 255 for independent streams with an
unspecified channel layout.

apply_phase_inv (N.A.) (requires libopus >= 1.2)

    

If set to 0, disables the use of phase inversion for intensity stereo,
improving the quality of mono downmixes, but slightly reducing normal stereo
quality. The default is 1 (phase inversion enabled).

### 8.10 libshine

Shine Fixed-Point MP3 encoder wrapper.

Shine is a fixed-point MP3 encoder. It has a far better performance on
platforms without an FPU, e.g. armel CPUs, and some phones and tablets.
However, as it is more targeted on performance than quality, it is not on par
with LAME and other production-grade encoders quality-wise. Also, according to
the project's homepage, this encoder may not be free of bugs as the code was
written a long time ago and the project was dead for at least 5 years.

This encoder only supports stereo and mono input. This is also CBR-only.

The original project (last updated in early 2007) is at
<http://sourceforge.net/projects/libshine-fxp/>. We only support the updated
fork by the Savonet/Liquidsoap project at <https://github.com/savonet/shine>.

Requires the presence of the libshine headers and library during
configuration. You need to explicitly configure the build with `--enable-
libshine`.

See also libmp3lame.

#### 8.10.1 Options

The following options are supported by the libshine wrapper. The
`shineenc`-equivalent of the options are listed in parentheses.

b (_-b_)

    

Set bitrate expressed in bits/s for CBR. `shineenc` -b option is expressed in
kilobits/s.

### 8.11 libtwolame

TwoLAME MP2 encoder wrapper.

Requires the presence of the libtwolame headers and library during
configuration. You need to explicitly configure the build with `--enable-
libtwolame`.

#### 8.11.1 Options

The following options are supported by the libtwolame wrapper. The
`twolame`-equivalent options follow the FFmpeg ones and are in parentheses.

b (_-b_)

    

Set bitrate expressed in bits/s for CBR. `twolame` b option is expressed in
kilobits/s. Default value is 128k.

q (_-V_)

    

Set quality for experimental VBR support. Maximum value range is from -50 to
50, useful range is from -10 to 10. The higher the value, the better the
quality. This option is valid only using the `ffmpeg` command-line tool. For
library interface users, use global_quality.

mode (_\--mode_)

    

Set the mode of the resulting audio. Possible values:

'auto'

    

Choose mode automatically based on the input. This is the default.

'stereo'

    

Stereo

'joint_stereo'

    

Joint stereo

'dual_channel'

    

Dual channel

'mono'

    

Mono

psymodel (_\--psyc-mode_)

    

Set psychoacoustic model to use in encoding. The argument must be an integer
between -1 and 4, inclusive. The higher the value, the better the quality. The
default value is 3.

energy_levels (_\--energy_)

    

Enable energy levels extensions when set to 1. The default value is 0
(disabled).

error_protection (_\--protect_)

    

Enable CRC error protection when set to 1. The default value is 0 (disabled).

copyright (_\--copyright_)

    

Set MPEG audio copyright flag when set to 1. The default value is 0
(disabled).

original (_\--original_)

    

Set MPEG audio original flag when set to 1. The default value is 0 (disabled).

### 8.12 libvo-amrwbenc

VisualOn Adaptive Multi-Rate Wideband encoder.

Requires the presence of the libvo-amrwbenc headers and library during
configuration. You need to explicitly configure the build with `--enable-
libvo-amrwbenc --enable-version3`.

This is a mono-only encoder. Officially it only supports 16000Hz sample rate,
but you can override it by setting strict to 'unofficial' or lower.

#### 8.12.1 Options

b

    

Set bitrate in bits/s. Only the following bitrates are supported, otherwise
libavcodec will round to the nearest valid bitrate.

'6600'

'8850'

'12650'

'14250'

'15850'

'18250'

'19850'

'23050'

'23850'

dtx

    

Allow discontinuous transmission (generate comfort noise) when set to 1. The
default value is 0 (disabled).

### 8.13 libvorbis

libvorbis encoder wrapper.

Requires the presence of the libvorbisenc headers and library during
configuration. You need to explicitly configure the build with `--enable-
libvorbis`.

#### 8.13.1 Options

The following options are supported by the libvorbis wrapper. The
`oggenc`-equivalent of the options are listed in parentheses.

To get a more accurate and extensive documentation of the libvorbis options,
consult the libvorbisenc's and `oggenc`'s documentations. See
<http://xiph.org/vorbis/>, <http://wiki.xiph.org/Vorbis-tools>, and oggenc(1).

b (_-b_)

    

Set bitrate expressed in bits/s for ABR. `oggenc` -b is expressed in
kilobits/s.

q (_-q_)

    

Set constant quality setting for VBR. The value should be a float number in
the range of -1.0 to 10.0. The higher the value, the better the quality. The
default value is '3.0'.

This option is valid only using the `ffmpeg` command-line tool. For library
interface users, use global_quality.

cutoff (_\--advanced-encode-option lowpass_frequency=N_)

    

Set cutoff bandwidth in Hz, a value of 0 disables cutoff. `oggenc`'s related
option is expressed in kHz. The default value is '0' (cutoff disabled).

minrate (_-m_)

    

Set minimum bitrate expressed in bits/s. `oggenc` -m is expressed in
kilobits/s.

maxrate (_-M_)

    

Set maximum bitrate expressed in bits/s. `oggenc` -M is expressed in
kilobits/s. This only has effect on ABR mode.

iblock (_\--advanced-encode-option impulse_noisetune=N_)

    

Set noise floor bias for impulse blocks. The value is a float number from
-15.0 to 0.0. A negative bias instructs the encoder to pay special attention
to the crispness of transients in the encoded audio. The tradeoff for better
transient response is a higher bitrate.

### 8.14 mjpeg

Motion JPEG encoder.

#### 8.14.1 Options

huffman

    

Set the huffman encoding strategy. Possible values:

'default'

    

Use the default huffman tables. This is the default strategy.

'optimal'

    

Compute and use optimal huffman tables.

### 8.15 wavpack

WavPack lossless audio encoder.

#### 8.15.1 Options

The equivalent options for `wavpack` command line utility are listed in
parentheses.

#### 8.15.1.1 Shared options

The following shared options are effective for this encoder. Only special
notes about this particular encoder will be documented here. For the general
meaning of the options, see the Codec Options chapter.

frame_size (_\--blocksize_)

    

For this encoder, the range for this option is between 128 and 131072. Default
is automatically decided based on sample rate and number of channel.

For the complete formula of calculating default, see libavcodec/wavpackenc.c.

compression_level (_-f_ , _-h_ , _-hh_ , and _-x_)

#### 8.15.1.2 Private options

joint_stereo (_-j_)

    

Set whether to enable joint stereo. Valid values are:

'on (_1_)'

    

Force mid/side audio encoding.

'off (_0_)'

    

Force left/right audio encoding.

'auto'

    

Let the encoder decide automatically.

optimize_mono

    

Set whether to enable optimization for mono. This option is only effective for
non-mono streams. Available values:

'on'

    

enabled

'off'

    

disabled

## 9 Video Encoders

A description of some of the currently available video encoders follows.

### 9.1 a64_multi, a64_multi5

A64 / Commodore 64 multicolor charset encoder. `a64_multi5` is extended with
5th color (colram).

### 9.2 Cinepak

Cinepak aka CVID encoder. Compatible with Windows 3.1 and vintage MacOS.

#### 9.2.1 Options

g integer

    

Keyframe interval. A keyframe is inserted at least every `-g` frames,
sometimes sooner.

q:v integer

    

Quality factor. Lower is better. Higher gives lower bitrate. The following
table lists bitrates when encoding akiyo_cif.y4m for various values of `-q:v`
with `-g 100`:

`-q:v 1` 1918 kb/s

`-q:v 2` 1735 kb/s

`-q:v 4` 1500 kb/s

`-q:v 10` 1041 kb/s

`-q:v 20` 826 kb/s

`-q:v 40` 553 kb/s

`-q:v 100` 394 kb/s

`-q:v 200` 312 kb/s

`-q:v 400` 266 kb/s

`-q:v 1000` 237 kb/s

max_extra_cb_iterations integer

    

Max extra codebook recalculation passes, more is better and slower.

skip_empty_cb boolean

    

Avoid wasting bytes, ignore vintage MacOS decoder.

max_strips integer

min_strips integer

    

The minimum and maximum number of strips to use. Wider range sometimes
improves quality. More strips is generally better quality but costs more bits.
Fewer strips tend to yield more keyframes. Vintage compatible is 1..3.

strip_number_adaptivity integer

    

How much number of strips is allowed to change between frames. Higher is
better but slower.

### 9.3 ffv1

FFv1 Encoder

#### 9.3.1 Options

The following options are supported by FFmpeg's FFv1 encoder.

context

    

Sets the context size, 0 (default) is small, 1 is big.

coder

    

Set the coder,

'rice'

    

Golomb rice coder

'range_def'

    

Range coder with default table

'range_tab'

    

Range coder with custom table

slicecrc

    

-1 (default, automatic), 1 use crc with zero initial and final state, 2 use crc with non zero initial and final state 

qtable

    

'default'

    

default, automatic

'8bit'

    

use 8bit default

'greater8bit'

    

use >8bit default

remap_optimizer

    

0 - 5, default 3, how much effort the encoder puts into optimizing the remap
table.

### 9.4 GIF

GIF image/animation encoder.

#### 9.4.1 Options

gifflags integer

    

Sets the flags used for GIF encoding.

offsetting

    

Enables picture offsetting.

Default is enabled.

transdiff

    

Enables transparency detection between frames.

Default is enabled.

gifimage integer

    

Enables encoding one full GIF image per frame, rather than an animated GIF.

Default value is 0.

global_palette integer

    

Writes a palette to the global GIF header where feasible.

If disabled, every frame will always have a palette written, even if there is
a global palette supplied.

Default value is 1.

### 9.5 Hap

Vidvox Hap video encoder.

#### 9.5.1 Options

format integer

    

Specifies the Hap format to encode.

hap

hap_alpha

hap_q

Default value is hap.

chunks integer

    

Specifies the number of chunks to split frames into, between 1 and 64. This
permits multithreaded decoding of large frames, potentially at the cost of
data-rate. The encoder may modify this value to divide frames evenly.

Default value is 1.

compressor integer

    

Specifies the second-stage compressor to use. If set to none, chunks will be
limited to 1, as chunked uncompressed frames offer no benefit.

none

snappy

Default value is snappy.

### 9.6 jpeg2000

The native jpeg 2000 encoder is lossy by default, the `-q:v` option can be
used to set the encoding quality. Lossless encoding can be selected with
`-pred 1`.

#### 9.6.1 Options

format integer

    

Can be set to either `j2k` or `jp2` (the default) that makes it possible to
store non-rgb pix_fmts.

tile_width integer

    

Sets tile width. Range is 1 to 1073741824. Default is 256.

tile_height integer

    

Sets tile height. Range is 1 to 1073741824. Default is 256.

pred integer

    

Allows setting the discrete wavelet transform (DWT) type

dwt97int (Lossy)

dwt53 (Lossless)

Default is `dwt97int`

sop boolean

    

Enable this to add SOP marker at the start of each packet. Disabled by
default.

eph boolean

    

Enable this to add EPH marker at the end of each packet header. Disabled by
default.

prog integer

    

Sets the progression order to be used by the encoder. Possible values are:

lrcp

rlcp

rpcl

pcrl

cprl

Set to `lrcp` by default.

layer_rates string

    

By default, when this option is not used, compression is done using the
quality metric. This option allows for compression using compression ratio.
The compression ratio for each level could be specified. The compression ratio
of a layer `l` species the what ratio of total file size is contained in the
first `l` layers.

Example usage:

    
    
    ffmpeg -i input.bmp -c:v jpeg2000 -layer_rates "100,10,1" output.j2k
    

This would compress the image to contain 3 layers, where the data contained in
the first layer would be compressed by 1000 times, compressed by 100 in the
first two layers, and shall contain all data while using all 3 layers.

### 9.7 librav1e

rav1e AV1 encoder wrapper.

Requires the presence of the rav1e headers and library during configuration.
You need to explicitly configure the build with `--enable-librav1e`.

#### 9.7.1 Options

qmax

    

Sets the maximum quantizer to use when using bitrate mode.

qmin

    

Sets the minimum quantizer to use when using bitrate mode.

qp

    

Uses quantizer mode to encode at the given quantizer (0-255).

speed

    

Selects the speed preset (0-10) to encode with.

tiles

    

Selects how many tiles to encode with.

tile-rows

    

Selects how many rows of tiles to encode with.

tile-columns

    

Selects how many columns of tiles to encode with.

rav1e-params

    

Set rav1e options using a list of key=value pairs separated by ":". See `rav1e
--help` for a list of options.

For example to specify librav1e encoding options with -rav1e-params:

    
    
    ffmpeg -i input -c:v librav1e -b:v 500K -rav1e-params speed=5:low_latency=true output.mp4
    

### 9.8 libaom-av1

libaom AV1 encoder wrapper.

Requires the presence of the libaom headers and library during configuration.
You need to explicitly configure the build with `--enable-libaom`.

#### 9.8.1 Options

The wrapper supports the following standard libavcodec options:

b

    

Set bitrate target in bits/second. By default this will use variable-bitrate
mode. If maxrate and minrate are also set to the same value then it will use
constant-bitrate mode, otherwise if crf is set as well then it will use
constrained-quality mode.

g keyint_min

    

Set key frame placement. The GOP size sets the maximum distance between key
frames; if zero the output stream will be intra-only. The minimum distance is
ignored unless it is the same as the GOP size, in which case key frames will
always appear at a fixed interval. Not set by default, so without this option
the library has completely free choice about where to place key frames.

qmin qmax

    

Set minimum/maximum quantisation values. Valid range is from 0 to 63 (warning:
this does not match the quantiser values actually used by AV1 \- divide by
four to map real quantiser values to this range). Defaults to min/max (no
constraint).

minrate maxrate bufsize rc_init_occupancy

    

Set rate control buffering parameters. Not used if not set - defaults to
unconstrained variable bitrate.

threads

    

Set the number of threads to use while encoding. This may require the tiles or
row-mt options to also be set to actually use the specified number of threads
fully. Defaults to the number of hardware threads supported by the host
machine.

profile

    

Set the encoding profile. Defaults to using the profile which matches the bit
depth and chroma subsampling of the input.

The wrapper also has some specific options:

cpu-used

    

Set the quality/encoding speed tradeoff. Valid range is from 0 to 8, higher
numbers indicating greater speed and lower quality. The default value is 1,
which will be slow and high quality.

auto-alt-ref

    

Enable use of alternate reference frames. Defaults to the internal default of
the library.

arnr-max-frames (_frames_)

    

Set altref noise reduction max frame count. Default is -1.

arnr-strength (_strength_)

    

Set altref noise reduction filter strength. Range is -1 to 6. Default is -1.

aq-mode (_aq-mode_)

    

Set adaptive quantization mode. Possible values:

'none (_0_)'

    

Disabled.

'variance (_1_)'

    

Variance-based.

'complexity (_2_)'

    

Complexity-based.

'cyclic (_3_)'

    

Cyclic refresh.

tune (_tune_)

    

Set the distortion metric the encoder is tuned with. Default is `psnr`.

'psnr (_0_)'

'ssim (_1_)'

lag-in-frames

    

Set the maximum number of frames which the encoder may keep in flight at any
one time for lookahead purposes. Defaults to the internal default of the
library.

error-resilience

    

Enable error resilience features:

default

    

Improve resilience against losses of whole frames.

Not enabled by default.

crf

    

Set the quality/size tradeoff for constant-quality (no bitrate target) and
constrained-quality (with maximum bitrate target) modes. Valid range is 0 to
63, higher numbers indicating lower quality and smaller output size. Only used
if set; by default only the bitrate target is used.

static-thresh

    

Set a change threshold on blocks below which they will be skipped by the
encoder. Defined in arbitrary units as a nonnegative integer, defaulting to
zero (no blocks are skipped).

drop-threshold

    

Set a threshold for dropping frames when close to rate control bounds. Defined
as a percentage of the target buffer - when the rate control buffer falls
below this percentage, frames will be dropped until it has refilled above the
threshold. Defaults to zero (no frames are dropped).

denoise-noise-level (_level_)

    

Amount of noise to be removed for grain synthesis. Grain synthesis is disabled
if this option is not set or set to 0.

denoise-block-size (_pixels_)

    

Block size used for denoising for grain synthesis. If not set, AV1 codec uses
the default value of 32.

undershoot-pct (_pct_)

    

Set datarate undershoot (min) percentage of the target bitrate. Range is -1 to
100. Default is -1.

overshoot-pct (_pct_)

    

Set datarate overshoot (max) percentage of the target bitrate. Range is -1 to
1000. Default is -1.

minsection-pct (_pct_)

    

Minimum percentage variation of the GOP bitrate from the target bitrate. If
minsection-pct is not set, the libaomenc wrapper computes it as follows:
`(minrate * 100 / bitrate)`. Range is -1 to 100. Default is -1 (unset).

maxsection-pct (_pct_)

    

Maximum percentage variation of the GOP bitrate from the target bitrate. If
maxsection-pct is not set, the libaomenc wrapper computes it as follows:
`(maxrate * 100 / bitrate)`. Range is -1 to 5000. Default is -1 (unset).

frame-parallel (_boolean_)

    

Enable frame parallel decodability features. Default is true.

tiles

    

Set the number of tiles to encode the input video with, as columns x rows.
Larger numbers allow greater parallelism in both encoding and decoding, but
may decrease coding efficiency. Defaults to the minimum number of tiles
required by the size of the input video (this is 1x1 (that is, a single tile)
for sizes up to and including 4K).

tile-columns tile-rows

    

Set the number of tiles as log2 of the number of tile rows and columns.
Provided for compatibility with libvpx/VP9.

row-mt (Requires libaom >= 1.0.0-759-g90a15f4f2)

    

Enable row based multi-threading. Disabled by default.

enable-cdef (_boolean_)

    

Enable Constrained Directional Enhancement Filter. The libaom-av1 encoder
enables CDEF by default.

enable-restoration (_boolean_)

    

Enable Loop Restoration Filter. Default is true for libaom-av1.

enable-global-motion (_boolean_)

    

Enable the use of global motion for block prediction. Default is true.

enable-intrabc (_boolean_)

    

Enable block copy mode for intra block prediction. This mode is useful for
screen content. Default is true.

enable-rect-partitions (_boolean_) (Requires libaom >= v2.0.0)

    

Enable rectangular partitions. Default is true.

enable-1to4-partitions (_boolean_) (Requires libaom >= v2.0.0)

    

Enable 1:4/4:1 partitions. Default is true.

enable-ab-partitions (_boolean_) (Requires libaom >= v2.0.0)

    

Enable AB shape partitions. Default is true.

enable-angle-delta (_boolean_) (Requires libaom >= v2.0.0)

    

Enable angle delta intra prediction. Default is true.

enable-cfl-intra (_boolean_) (Requires libaom >= v2.0.0)

    

Enable chroma predicted from luma intra prediction. Default is true.

enable-filter-intra (_boolean_) (Requires libaom >= v2.0.0)

    

Enable filter intra predictor. Default is true.

enable-intra-edge-filter (_boolean_) (Requires libaom >= v2.0.0)

    

Enable intra edge filter. Default is true.

enable-smooth-intra (_boolean_) (Requires libaom >= v2.0.0)

    

Enable smooth intra prediction mode. Default is true.

enable-paeth-intra (_boolean_) (Requires libaom >= v2.0.0)

    

Enable paeth predictor in intra prediction. Default is true.

enable-palette (_boolean_) (Requires libaom >= v2.0.0)

    

Enable palette prediction mode. Default is true.

enable-flip-idtx (_boolean_) (Requires libaom >= v2.0.0)

    

Enable extended transform type, including FLIPADST_DCT, DCT_FLIPADST,
FLIPADST_FLIPADST, ADST_FLIPADST, FLIPADST_ADST, IDTX, V_DCT, H_DCT, V_ADST,
H_ADST, V_FLIPADST, H_FLIPADST. Default is true.

enable-tx64 (_boolean_) (Requires libaom >= v2.0.0)

    

Enable 64-pt transform. Default is true.

reduced-tx-type-set (_boolean_) (Requires libaom >= v2.0.0)

    

Use reduced set of transform types. Default is false.

use-intra-dct-only (_boolean_) (Requires libaom >= v2.0.0)

    

Use DCT only for INTRA modes. Default is false.

use-inter-dct-only (_boolean_) (Requires libaom >= v2.0.0)

    

Use DCT only for INTER modes. Default is false.

use-intra-default-tx-only (_boolean_) (Requires libaom >= v2.0.0)

    

Use Default-transform only for INTRA modes. Default is false.

enable-ref-frame-mvs (_boolean_) (Requires libaom >= v2.0.0)

    

Enable temporal mv prediction. Default is true.

enable-reduced-reference-set (_boolean_) (Requires libaom >= v2.0.0)

    

Use reduced set of single and compound references. Default is false.

enable-obmc (_boolean_) (Requires libaom >= v2.0.0)

    

Enable obmc. Default is true.

enable-dual-filter (_boolean_) (Requires libaom >= v2.0.0)

    

Enable dual filter. Default is true.

enable-diff-wtd-comp (_boolean_) (Requires libaom >= v2.0.0)

    

Enable difference-weighted compound. Default is true.

enable-dist-wtd-comp (_boolean_) (Requires libaom >= v2.0.0)

    

Enable distance-weighted compound. Default is true.

enable-onesided-comp (_boolean_) (Requires libaom >= v2.0.0)

    

Enable one sided compound. Default is true.

enable-interinter-wedge (_boolean_) (Requires libaom >= v2.0.0)

    

Enable interinter wedge compound. Default is true.

enable-interintra-wedge (_boolean_) (Requires libaom >= v2.0.0)

    

Enable interintra wedge compound. Default is true.

enable-masked-comp (_boolean_) (Requires libaom >= v2.0.0)

    

Enable masked compound. Default is true.

enable-interintra-comp (_boolean_) (Requires libaom >= v2.0.0)

    

Enable interintra compound. Default is true.

enable-smooth-interintra (_boolean_) (Requires libaom >= v2.0.0)

    

Enable smooth interintra mode. Default is true.

aom-params

    

Set libaom options using a list of key=value pairs separated by ":". For a
list of supported options, see `aomenc --help` under the section "AV1 Specific
Options".

For example to specify libaom encoding options with -aom-params:

    
    
    ffmpeg -i input -c:v libaom-av1 -b:v 500K -aom-params tune=psnr:enable-tpl-model=1 output.mp4
    

### 9.9 libsvtav1

SVT-AV1 encoder wrapper.

Requires the presence of the SVT-AV1 headers and library during configuration.
You need to explicitly configure the build with `--enable-libsvtav1`.

#### 9.9.1 Options

profile

    

Set the encoding profile.

'main'

'high'

'professional'

level

    

Set the operating point level. For example: '4.0'

hielevel

    

Set the Hierarchical prediction levels.

'3level'

'4level'

    

This is the default.

tier

    

Set the operating point tier.

'main'

    

This is the default.

'high'

qmax

    

Set the maximum quantizer to use when using a bitrate mode.

qmin

    

Set the minimum quantizer to use when using a bitrate mode.

crf

    

Constant rate factor value used in crf rate control mode (0-63).

qp

    

Set the quantizer used in cqp rate control mode (0-63).

sc_detection

    

Enable scene change detection.

la_depth

    

Set number of frames to look ahead (0-120).

preset

    

Set the quality-speed tradeoff, in the range 0 to 13. Higher values are faster
but lower quality.

tile_rows

    

Set log2 of the number of rows of tiles to use (0-6).

tile_columns

    

Set log2 of the number of columns of tiles to use (0-4).

svtav1-params

    

Set SVT-AV1 options using a list of key=value pairs separated by ":". See the
SVT-AV1 encoder user guide for a list of accepted parameters.

### 9.10 libjxl

libjxl JPEG XL encoder wrapper.

Requires the presence of the libjxl headers and library during configuration.
You need to explicitly configure the build with `--enable-libjxl`.

#### 9.10.1 Options

The libjxl wrapper supports the following options:

distance

    

Set the target Butteraugli distance. This is a quality setting: lower distance
yields higher quality, with distance=1.0 roughly comparable to libjpeg Quality
90 for photographic content. Setting distance=0.0 yields true lossless
encoding. Valid values range between 0.0 and 15.0, and sane values rarely
exceed 5.0. Setting distance=0.1 usually attains transparency for most input.
The default is 1.0.

effort

    

Set the encoding effort used. Higher effort values produce more consistent
quality and usually produces a better quality/bpp curve, at the cost of more
CPU time required. Valid values range from 1 to 9, and the default is 7.

modular

    

Force the encoder to use Modular mode instead of choosing automatically. The
default is to use VarDCT for lossy encoding and Modular for lossless. VarDCT
is generally superior to Modular for lossy encoding but does not support
lossless encoding.

### 9.11 libkvazaar

Kvazaar H.265/HEVC encoder.

Requires the presence of the libkvazaar headers and library during
configuration. You need to explicitly configure the build with \--enable-
libkvazaar.

#### 9.11.1 Options

b

    

Set target video bitrate in bit/s and enable rate control.

kvazaar-params

    

Set kvazaar parameters as a list of name=value pairs separated by commas (,).
See kvazaar documentation for a list of options.

### 9.12 libopenh264

Cisco libopenh264 H.264/MPEG-4 AVC encoder wrapper.

This encoder requires the presence of the libopenh264 headers and library
during configuration. You need to explicitly configure the build with
`--enable-libopenh264`. The library is detected using `pkg-config`.

For more information about the library see <http://www.openh264.org>.

#### 9.12.1 Options

The following FFmpeg global options affect the configurations of the
libopenh264 encoder.

b

    

Set the bitrate (as a number of bits per second).

g

    

Set the GOP size.

maxrate

    

Set the max bitrate (as a number of bits per second).

flags +global_header

    

Set global header in the bitstream.

slices

    

Set the number of slices, used in parallelized encoding. Default value is 0.
This is only used when slice_mode is set to 'fixed'.

loopfilter

    

Enable loop filter, if set to 1 (automatically enabled). To disable set a
value of 0.

profile

    

Set profile restrictions. If set to the value of 'main' enable CABAC (set the
`SEncParamExt.iEntropyCodingModeFlag` flag to 1).

max_nal_size

    

Set maximum NAL size in bytes.

allow_skip_frames

    

Allow skipping frames to hit the target bitrate if set to 1.

### 9.13 libtheora

libtheora Theora encoder wrapper.

Requires the presence of the libtheora headers and library during
configuration. You need to explicitly configure the build with `--enable-
libtheora`.

For more information about the libtheora project see <http://www.theora.org/>.

#### 9.13.1 Options

The following global options are mapped to internal libtheora options which
affect the quality and the bitrate of the encoded stream.

b

    

Set the video bitrate in bit/s for CBR (Constant Bit Rate) mode. In case VBR
(Variable Bit Rate) mode is enabled this option is ignored.

flags

    

Used to enable constant quality mode (VBR) encoding through the qscale flag,
and to enable the `pass1` and `pass2` modes.

g

    

Set the GOP size.

global_quality

    

Set the global quality as an integer in lambda units.

Only relevant when VBR mode is enabled with `flags +qscale`. The value is
converted to QP units by dividing it by `FF_QP2LAMBDA`, clipped in the [0 -
10] range, and then multiplied by 6.3 to get a value in the native libtheora
range [0-63]. A higher value corresponds to a higher quality.

q

    

Enable VBR mode when set to a non-negative value, and set constant quality
value as a double floating point value in QP units.

The value is clipped in the [0-10] range, and then multiplied by 6.3 to get a
value in the native libtheora range [0-63].

This option is valid only using the `ffmpeg` command-line tool. For library
interface users, use global_quality.

#### 9.13.2 Examples

  * Set maximum constant quality (VBR) encoding with `ffmpeg`: 
        
        ffmpeg -i INPUT -codec:v libtheora -q:v 10 OUTPUT.ogg
        

  * Use `ffmpeg` to convert a CBR 1000 kbps Theora video stream: 
        
        ffmpeg -i INPUT -codec:v libtheora -b:v 1000k OUTPUT.ogg
        

### 9.14 libvpx

VP8/VP9 format supported through libvpx.

Requires the presence of the libvpx headers and library during configuration.
You need to explicitly configure the build with `--enable-libvpx`.

#### 9.14.1 Options

The following options are supported by the libvpx wrapper. The
`vpxenc`-equivalent options or values are listed in parentheses for easy
migration.

To reduce the duplication of documentation, only the private options and some
others requiring special attention are documented here. For the documentation
of the undocumented generic options, see the Codec Options chapter.

To get more documentation of the libvpx options, invoke the command `ffmpeg -h
encoder=libvpx`, `ffmpeg -h encoder=libvpx-vp9` or `vpxenc --help`. Further
information is available in the libvpx API documentation.

b (_target-bitrate_)

    

Set bitrate in bits/s. Note that FFmpeg's b option is expressed in bits/s,
while `vpxenc`'s target-bitrate is in kilobits/s.

g (_kf-max-dist_)

keyint_min (_kf-min-dist_)

qmin (_min-q_)

    

Minimum (Best Quality) Quantizer.

qmax (_max-q_)

    

Maximum (Worst Quality) Quantizer. Can be changed per-frame.

bufsize (_buf-sz_ , _buf-optimal-sz_)

    

Set ratecontrol buffer size (in bits). Note `vpxenc`'s options are specified
in milliseconds, the libvpx wrapper converts this value as follows: `buf-sz =
bufsize * 1000 / bitrate`, `buf-optimal-sz = bufsize * 1000 / bitrate * 5 /
6`.

rc_init_occupancy (_buf-initial-sz_)

    

Set number of bits which should be loaded into the rc buffer before decoding
starts. Note `vpxenc`'s option is specified in milliseconds, the libvpx
wrapper converts this value as follows: `rc_init_occupancy * 1000 / bitrate`.

undershoot-pct

    

Set datarate undershoot (min) percentage of the target bitrate.

overshoot-pct

    

Set datarate overshoot (max) percentage of the target bitrate.

skip_threshold (_drop-frame_)

qcomp (_bias-pct_)

maxrate (_maxsection-pct_)

    

Set GOP max bitrate in bits/s. Note `vpxenc`'s option is specified as a
percentage of the target bitrate, the libvpx wrapper converts this value as
follows: `(maxrate * 100 / bitrate)`.

minrate (_minsection-pct_)

    

Set GOP min bitrate in bits/s. Note `vpxenc`'s option is specified as a
percentage of the target bitrate, the libvpx wrapper converts this value as
follows: `(minrate * 100 / bitrate)`.

minrate, maxrate, b _end-usage=cbr_

    

`(minrate == maxrate == bitrate)`.

crf (_end-usage=cq_ , _cq-level_)

tune (_tune_)

    

'psnr (_psnr_)'

'ssim (_ssim_)'

quality, deadline (_deadline_)

    

'best'

    

Use best quality deadline. Poorly named and quite slow, this option should be
avoided as it may give worse quality output than good.

'good'

    

Use good quality deadline. This is a good trade-off between speed and quality
when used with the cpu-used option.

'realtime'

    

Use realtime quality deadline.

speed, cpu-used (_cpu-used_)

    

Set quality/speed ratio modifier. Higher values speed up the encode at the
cost of quality.

nr (_noise-sensitivity_)

static-thresh

    

Set a change threshold on blocks below which they will be skipped by the
encoder.

slices (_token-parts_)

    

Note that FFmpeg's slices option gives the total number of partitions, while
`vpxenc`'s token-parts is given as `log2(partitions)`.

max-intra-rate

    

Set maximum I-frame bitrate as a percentage of the target bitrate. A value of
0 means unlimited.

force_key_frames

    

`VPX_EFLAG_FORCE_KF`

Alternate reference frame related

    

auto-alt-ref

    

Enable use of alternate reference frames (2-pass only). Values greater than 1
enable multi-layer alternate reference frames (VP9 only).

arnr-maxframes

    

Set altref noise reduction max frame count.

arnr-type

    

Set altref noise reduction filter type: backward, forward, centered.

arnr-strength

    

Set altref noise reduction filter strength.

rc-lookahead, lag-in-frames (_lag-in-frames_)

    

Set number of frames to look ahead for frametype and ratecontrol.

min-gf-interval

    

Set minimum golden/alternate reference frame interval (VP9 only).

error-resilient

    

Enable error resiliency features.

sharpness integer

    

Increase sharpness at the expense of lower PSNR. The valid range is [0, 7].

ts-parameters

    

Sets the temporal scalability configuration using a :-separated list of
key=value pairs. For example, to specify temporal scalability parameters with
`ffmpeg`:

    
    
    ffmpeg -i INPUT -c:v libvpx -ts-parameters ts_number_layers=3:\
    ts_target_bitrate=250,500,1000:ts_rate_decimator=4,2,1:\
    ts_periodicity=4:ts_layer_id=0,2,1,2:ts_layering_mode=3 OUTPUT
    

Below is a brief explanation of each of the parameters, please refer to
`struct vpx_codec_enc_cfg` in `vpx/vpx_encoder.h` for more details.

ts_number_layers

    

Number of temporal coding layers.

ts_target_bitrate

    

Target bitrate for each temporal layer (in kbps). (bitrate should be inclusive
of the lower temporal layer).

ts_rate_decimator

    

Frame rate decimation factor for each temporal layer.

ts_periodicity

    

Length of the sequence defining frame temporal layer membership.

ts_layer_id

    

Template defining the membership of frames to temporal layers.

ts_layering_mode

    

(optional) Selecting the temporal structure from a set of pre-defined temporal
layering modes. Currently supports the following options.

0

    

No temporal layering flags are provided internally, relies on flags being
passed in using `metadata` field in `AVFrame` with following keys.

vp8-flags

    

Sets the flags passed into the encoder to indicate the referencing scheme for
the current frame. Refer to function `vpx_codec_encode` in `vpx/vpx_encoder.h`
for more details.

temporal_id

    

Explicitly sets the temporal id of the current frame to encode.

2

    

Two temporal layers. 0-1...

3

    

Three temporal layers. 0-2-1-2...; with single reference frame.

4

    

Same as option "3", except there is a dependency between the two temporal
layer 2 frames within the temporal period.

VP8-specific options

    

screen-content-mode

    

Screen content mode, one of: 0 (off), 1 (screen), 2 (screen with more
aggressive rate control).

VP9-specific options

    

lossless

    

Enable lossless mode.

tile-columns

    

Set number of tile columns to use. Note this is given as `log2(tile_columns)`.
For example, 8 tile columns would be requested by setting the tile-columns
option to 3.

tile-rows

    

Set number of tile rows to use. Note this is given as `log2(tile_rows)`. For
example, 4 tile rows would be requested by setting the tile-rows option to 2.

frame-parallel

    

Enable frame parallel decodability features.

aq-mode

    

Set adaptive quantization mode (0: off (default), 1: variance 2: complexity,
3: cyclic refresh, 4: equator360).

colorspace _color-space_

    

Set input color space. The VP9 bitstream supports signaling the following
colorspaces:

'rgb' _sRGB_

'bt709' _bt709_

'unspecified' _unknown_

'bt470bg' _bt601_

'smpte170m' _smpte170_

'smpte240m' _smpte240_

'bt2020_ncl' _bt2020_

row-mt boolean

    

Enable row based multi-threading.

tune-content

    

Set content type: default (0), screen (1), film (2).

corpus-complexity

    

Corpus VBR mode is a variant of standard VBR where the complexity distribution
midpoint is passed in rather than calculated for a specific clip or chunk.

The valid range is [0, 10000]. 0 (default) uses standard VBR.

enable-tpl boolean

    

Enable temporal dependency model.

ref-frame-config

    

Using per-frame metadata, set members of the structure
`vpx_svc_ref_frame_config_t` in `vpx/vp8cx.h` to fine-control referencing
schemes and frame buffer management.  
Use a :-separated list of key=value pairs. For example,

    
    
    av_dict_set(&av_frame->metadata, "ref-frame-config", \
    "rfc_update_buffer_slot=7:rfc_lst_fb_idx=0:rfc_gld_fb_idx=1:rfc_alt_fb_idx=2:rfc_reference_last=0:rfc_reference_golden=0:rfc_reference_alt_ref=0");
    

rfc_update_buffer_slot

    

Indicates the buffer slot number to update

rfc_update_last

    

Indicates whether to update the LAST frame

rfc_update_golden

    

Indicates whether to update GOLDEN frame

rfc_update_alt_ref

    

Indicates whether to update ALT_REF frame

rfc_lst_fb_idx

    

LAST frame buffer index

rfc_gld_fb_idx

    

GOLDEN frame buffer index

rfc_alt_fb_idx

    

ALT_REF frame buffer index

rfc_reference_last

    

Indicates whether to reference LAST frame

rfc_reference_golden

    

Indicates whether to reference GOLDEN frame

rfc_reference_alt_ref

    

Indicates whether to reference ALT_REF frame

rfc_reference_duration

    

Indicates frame duration

For more information about libvpx see: <http://www.webmproject.org/>

### 9.15 libvvenc

VVenC H.266/VVC encoder wrapper.

This encoder requires the presence of the libvvenc headers and library during
configuration. You need to explicitly configure the build with \--enable-
libvvenc.

The VVenC project website is at <https://github.com/fraunhoferhhi/vvenc>.

#### 9.15.1 Supported Pixel Formats

VVenC supports only 10-bit color spaces as input. But the internal (encoded)
bit depth can be set to 8-bit or 10-bit at runtime.

#### 9.15.2 Options

b

    

Sets target video bitrate.

g

    

Set the GOP size. Currently support for g=1 (Intra only) or default.

preset

    

Set the VVenC preset.

levelidc

    

Set level idc.

tier

    

Set vvc tier.

qp

    

Set constant quantization parameter.

subopt boolean

    

Set subjective (perceptually motivated) optimization. Default is 1 (on).

bitdepth8 boolean

    

Set 8bit coding mode instead of using 10bit. Default is 0 (off).

period

    

set (intra) refresh period in seconds.

vvenc-params

    

Set vvenc options using a list of key=value couples separated by ":". See
`vvencapp --fullhelp` or `vvencFFapp --fullhelp` for a list of options.

For example, the options might be provided as:

    
    
    intraperiod=64:decodingrefreshtype=idr:poc0idr=1:internalbitdepth=8
    

For example the encoding options might be provided with -vvenc-params:

    
    
    ffmpeg -i input -c:v libvvenc -b 1M -vvenc-params intraperiod=64:decodingrefreshtype=idr:poc0idr=1:internalbitdepth=8 output.mp4
    

### 9.16 libwebp

libwebp WebP Image encoder wrapper

libwebp is Google's official encoder for WebP images. It can encode in either
lossy or lossless mode. Lossy images are essentially a wrapper around a VP8
frame. Lossless images are a separate codec developed by Google.

#### 9.16.1 Pixel Format

Currently, libwebp only supports YUV420 for lossy and RGB for lossless due to
limitations of the format and libwebp. Alpha is supported for either mode.
Because of API limitations, if RGB is passed in when encoding lossy or YUV is
passed in for encoding lossless, the pixel format will automatically be
converted using functions from libwebp. This is not ideal and is done only for
convenience.

#### 9.16.2 Options

-lossless boolean
    

Enables/Disables use of lossless mode. Default is 0.

-compression_level integer
    

For lossy, this is a quality/speed tradeoff. Higher values give better quality
for a given size at the cost of increased encoding time. For lossless, this is
a size/speed tradeoff. Higher values give smaller size at the cost of
increased encoding time. More specifically, it controls the number of extra
algorithms and compression tools used, and varies the combination of these
tools. This maps to the method option in libwebp. The valid range is 0 to 6.
Default is 4.

-quality float
    

For lossy encoding, this controls image quality. For lossless encoding, this
controls the effort and time spent in compression. Range is 0 to 100. Default
is 75.

-preset type
    

Configuration preset. This does some automatic settings based on the general
type of the image.

none

    

Do not use a preset.

default

    

Use the encoder default.

picture

    

Digital picture, like portrait, inner shot

photo

    

Outdoor photograph, with natural lighting

drawing

    

Hand or line drawing, with high-contrast details

icon

    

Small-sized colorful images

text

    

Text-like

### 9.17 libx264, libx264rgb

x264 H.264/MPEG-4 AVC encoder wrapper.

This encoder requires the presence of the libx264 headers and library during
configuration. You need to explicitly configure the build with `--enable-
libx264`.

libx264 supports an impressive number of features, including 8x8 and 4x4
adaptive spatial transform, adaptive B-frame placement, CAVLC/CABAC entropy
coding, interlacing (MBAFF), lossless mode, psy optimizations for detail
retention (adaptive quantization, psy-RD, psy-trellis).

Many libx264 encoder options are mapped to FFmpeg global codec options, while
unique encoder options are provided through private options. Additionally the
x264opts and x264-params private options allows one to pass a list of
key=value tuples as accepted by the libx264 `x264_param_parse` function.

The x264 project website is at <http://www.videolan.org/developers/x264.html>.

The libx264rgb encoder is the same as libx264, except it accepts packed RGB
pixel formats as input instead of YUV.

#### 9.17.1 Supported Pixel Formats

x264 supports 8- to 10-bit color spaces. The exact bit depth is controlled at
x264's configure time.

#### 9.17.2 Options

The following options are supported by the libx264 wrapper. The
`x264`-equivalent options or values are listed in parentheses for easy
migration.

To reduce the duplication of documentation, only the private options and some
others requiring special attention are documented here. For the documentation
of the undocumented generic options, see the Codec Options chapter.

To get a more accurate and extensive documentation of the libx264 options,
invoke the command `x264 --fullhelp` or consult the libx264 documentation.

In the list below, note that the `x264` option name is shown in parentheses
after the libavcodec corresponding name, in case there is a direct mapping.

b (_bitrate_)

    

Set bitrate in bits/s. Note that FFmpeg's b option is expressed in bits/s,
while `x264`'s bitrate is in kilobits/s.

bf (_bframes_)

    

Number of B-frames between I and P-frames

g (_keyint_)

    

Maximum GOP size

qmin (_qpmin_)

    

Minimum quantizer scale

qmax (_qpmax_)

    

Maximum quantizer scale

qdiff (_qpstep_)

    

Maximum difference between quantizer scales

qblur (_qblur_)

    

Quantizer curve blur

qcomp (_qcomp_)

    

Quantizer curve compression factor

refs (_ref_)

    

Number of reference frames each P-frame can use. The range is 0-16.

level (_level_)

    

Set the `x264_param_t.i_level_idc` value in case the value is positive, it is
ignored otherwise.

This value can be set using the `AVCodecContext` API (e.g. by setting the
`AVCodecContext` value directly), and is specified as an integer mapped on a
corresponding level (e.g. the value 31 maps to H.264 level IDC "3.1", as
defined in the `x264_levels` table). It is ignored when set to a non positive
value.

Alternatively it can be set as a private option, overriding the value set in
`AVCodecContext`, and in this case must be specified as the level IDC
identifier (e.g. "3.1"), as defined by H.264 Annex A.

sc_threshold (_scenecut_)

    

Sets the threshold for the scene change detection.

trellis (_trellis_)

    

Performs Trellis quantization to increase efficiency. Enabled by default.

nr (_nr_)

    

Noise reduction

me_range (_merange_)

    

Maximum range of the motion search in pixels.

me_method (_me_)

    

Set motion estimation method. Possible values in the decreasing order of
speed:

'dia (_dia_)'

'epzs (_dia_)'

    

Diamond search with radius 1 (fastest). 'epzs' is an alias for 'dia'.

'hex (_hex_)'

    

Hexagonal search with radius 2.

'umh (_umh_)'

    

Uneven multi-hexagon search.

'esa (_esa_)'

    

Exhaustive search.

'tesa (_tesa_)'

    

Hadamard exhaustive search (slowest).

forced-idr

    

Normally, when forcing a I-frame type, the encoder can select any type of
I-frame. This option forces it to choose an IDR-frame.

subq (_subme_)

    

Sub-pixel motion estimation method.

b_strategy (_b-adapt_)

    

Adaptive B-frame placement decision algorithm. Use only on first-pass.

keyint_min (_min-keyint_)

    

Minimum GOP size.

coder

    

Set entropy encoder. Possible values:

'ac'

    

Enable CABAC.

'vlc'

    

Enable CAVLC and disable CABAC. It generates the same effect as `x264`'s
\--no-cabac option.

cmp

    

Set full pixel motion estimation comparison algorithm. Possible values:

'chroma'

    

Enable chroma in motion estimation.

'sad'

    

Ignore chroma in motion estimation. It generates the same effect as `x264`'s
\--no-chroma-me option.

threads (_threads_)

    

Number of encoding threads.

thread_type

    

Set multithreading technique. Possible values:

'slice'

    

Slice-based multithreading. It generates the same effect as `x264`'s
\--sliced-threads option.

'frame'

    

Frame-based multithreading.

flags

    

Set encoding flags. It can be used to disable closed GOP and enable open GOP
by setting it to `-cgop`. The result is similar to the behavior of `x264`'s
\--open-gop option.

rc_init_occupancy (_vbv-init_)

    

Initial VBV buffer occupancy

preset (_preset_)

    

Set the encoding preset.

tune (_tune_)

    

Set tuning of the encoding params.

profile (_profile_)

    

Set profile restrictions.

fastfirstpass

    

Enable fast settings when encoding first pass, when set to 1. When set to 0,
it has the same effect of `x264`'s \--slow-firstpass option.

crf (_crf_)

    

Set the quality for constant quality mode.

crf_max (_crf-max_)

    

In CRF mode, prevents VBV from lowering quality beyond this point.

qp (_qp_)

    

Set constant quantization rate control method parameter.

aq-mode (_aq-mode_)

    

Set AQ method. Possible values:

'none (_0_)'

    

Disabled.

'variance (_1_)'

    

Variance AQ (complexity mask).

'autovariance (_2_)'

    

Auto-variance AQ (experimental).

aq-strength (_aq-strength_)

    

Set AQ strength, reduce blocking and blurring in flat and textured areas.

psy

    

Use psychovisual optimizations when set to 1. When set to 0, it has the same
effect as `x264`'s \--no-psy option.

psy-rd (_psy-rd_)

    

Set strength of psychovisual optimization, in psy-rd:psy-trellis format.

rc-lookahead (_rc-lookahead_)

    

Set number of frames to look ahead for frametype and ratecontrol.

weightb

    

Enable weighted prediction for B-frames when set to 1. When set to 0, it has
the same effect as `x264`'s \--no-weightb option.

weightp (_weightp_)

    

Set weighted prediction method for P-frames. Possible values:

'none (_0_)'

    

Disabled

'simple (_1_)'

    

Enable only weighted refs

'smart (_2_)'

    

Enable both weighted refs and duplicates

ssim (_ssim_)

    

Enable calculation and printing SSIM stats after the encoding.

intra-refresh (_intra-refresh_)

    

Enable the use of Periodic Intra Refresh instead of IDR frames when set to 1.

avcintra-class (_class_)

    

Configure the encoder to generate AVC-Intra. Valid values are 50, 100 and 200

bluray-compat (_bluray-compat_)

    

Configure the encoder to be compatible with the bluray standard. It is a
shorthand for setting "bluray-compat=1 force-cfr=1".

b-bias (_b-bias_)

    

Set the influence on how often B-frames are used.

b-pyramid (_b-pyramid_)

    

Set method for keeping of some B-frames as references. Possible values:

'none (_none_)'

    

Disabled.

'strict (_strict_)'

    

Strictly hierarchical pyramid.

'normal (_normal_)'

    

Non-strict (not Blu-ray compatible).

mixed-refs

    

Enable the use of one reference per partition, as opposed to one reference per
macroblock when set to 1. When set to 0, it has the same effect as `x264`'s
\--no-mixed-refs option.

8x8dct

    

Enable adaptive spatial transform (high profile 8x8 transform) when set to 1.
When set to 0, it has the same effect as `x264`'s \--no-8x8dct option.

fast-pskip

    

Enable early SKIP detection on P-frames when set to 1. When set to 0, it has
the same effect as `x264`'s \--no-fast-pskip option.

aud (_aud_)

    

Enable use of access unit delimiters when set to 1.

mbtree

    

Enable use macroblock tree ratecontrol when set to 1. When set to 0, it has
the same effect as `x264`'s \--no-mbtree option.

deblock (_deblock_)

    

Set loop filter parameters, in alpha:beta form.

cplxblur (_cplxblur_)

    

Set fluctuations reduction in QP (before curve compression).

partitions (_partitions_)

    

Set partitions to consider as a comma-separated list of values. Possible
values in the list:

'p8x8'

    

8x8 P-frame partition.

'p4x4'

    

4x4 P-frame partition.

'b8x8'

    

4x4 B-frame partition.

'i8x8'

    

8x8 I-frame partition.

'i4x4'

    

4x4 I-frame partition. (Enabling 'p4x4' requires 'p8x8' to be enabled.
Enabling 'i8x8' requires adaptive spatial transform (8x8dct option) to be
enabled.)

'none (_none_)'

    

Do not consider any partitions.

'all (_all_)'

    

Consider every partition.

direct-pred (_direct_)

    

Set direct MV prediction mode. Possible values:

'none (_none_)'

    

Disable MV prediction.

'spatial (_spatial_)'

    

Enable spatial predicting.

'temporal (_temporal_)'

    

Enable temporal predicting.

'auto (_auto_)'

    

Automatically decided.

slice-max-size (_slice-max-size_)

    

Set the limit of the size of each slice in bytes. If not specified but RTP
payload size (ps) is specified, that is used.

stats (_stats_)

    

Set the file name for multi-pass stats.

nal-hrd (_nal-hrd_)

    

Set signal HRD information (requires vbv-bufsize to be set). Possible values:

'none (_none_)'

    

Disable HRD information signaling.

'vbr (_vbr_)'

    

Variable bit rate.

'cbr (_cbr_)'

    

Constant bit rate (not allowed in MP4 container).

x264opts opts

x264-params opts

    

Override the x264 configuration using a :-separated list of key=value options.

The argument for both options is a list of key=value couples separated by ":".
With x264opts the value can be omitted, and the value `1` is assumed in that
case.

For filter and psy-rd options values that use ":" as a separator themselves,
use "," instead. They accept it as well since long ago but this is kept
undocumented for some reason.

For example, the options might be provided as:

    
    
    level=30:bframes=0:weightp=0:cabac=0:ref=1:vbv-maxrate=768:vbv-bufsize=2000:analyse=all:me=umh:no-fast-pskip=1:subq=6:8x8dct=0:trellis=0
    

For example to specify libx264 encoding options with `ffmpeg`:

    
    
    ffmpeg -i foo.mpg -c:v libx264 -x264opts keyint=123:min-keyint=20 -an out.mkv
    

To get the complete list of the libx264 options, invoke the command `x264
--fullhelp` or consult the libx264 documentation.

a53cc boolean

    

Import closed captions (which must be ATSC compatible format) into output.
Only the mpeg2 and h264 decoders provide these. Default is 1 (on).

udu_sei boolean

    

Import user data unregistered SEI if available into output. Default is 0
(off).

mb_info boolean

    

Set mb_info data through AVFrameSideData, only useful when used from the API.
Default is 0 (off).

Encoding ffpresets for common usages are provided so they can be used with the
general presets system (e.g. passing the pre option).

### 9.18 libx265

x265 H.265/HEVC encoder wrapper.

This encoder requires the presence of the libx265 headers and library during
configuration. You need to explicitly configure the build with \--enable-
libx265.

#### 9.18.1 Options

b

    

Sets target video bitrate.

bf

g

    

Set the GOP size.

keyint_min

    

Minimum GOP size.

refs

    

Number of reference frames each P-frame can use. The range is from 1-16.

preset

    

Set the x265 preset.

tune

    

Set the x265 tune parameter.

profile

    

Set profile restrictions.

crf

    

Set the quality for constant quality mode.

qp

    

Set constant quantization rate control method parameter.

qmin

    

Minimum quantizer scale.

qmax

    

Maximum quantizer scale.

qdiff

    

Maximum difference between quantizer scales.

qblur

    

Quantizer curve blur

qcomp

    

Quantizer curve compression factor

i_qfactor

b_qfactor

forced-idr

    

Normally, when forcing a I-frame type, the encoder can select any type of
I-frame. This option forces it to choose an IDR-frame.

udu_sei boolean

    

Import user data unregistered SEI if available into output. Default is 0
(off).

x265-params

    

Set x265 options using a list of key=value couples separated by ":". See `x265
--help` for a list of options.

For example to specify libx265 encoding options with -x265-params:

    
    
    ffmpeg -i input -c:v libx265 -x265-params crf=26:psy-rd=1 output.mp4
    

### 9.19 libxavs2

xavs2 AVS2-P2/IEEE1857.4 encoder wrapper.

This encoder requires the presence of the libxavs2 headers and library during
configuration. You need to explicitly configure the build with \--enable-
libxavs2.

The following standard libavcodec options are used:

  * b / bit_rate
  * g / gop_size
  * bf / max_b_frames

The encoder also has its own specific options:

#### 9.19.1 Options

lcu_row_threads

    

Set the number of parallel threads for rows from 1 to 8 (default 5).

initial_qp

    

Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used
to set the initial qp for the first frame.

qp

    

Set the xavs2 quantization parameter from 1 to 63 (default 34). This is used
to set the qp value under constant-QP mode.

max_qp

    

Set the max qp for rate control from 1 to 63 (default 55).

min_qp

    

Set the min qp for rate control from 1 to 63 (default 20).

speed_level

    

Set the Speed level from 0 to 9 (default 0). Higher is better but slower.

log_level

    

Set the log level from -1 to 3 (default 0). -1: none, 0: error, 1: warning, 2:
info, 3: debug.

xavs2-params

    

Set xavs2 options using a list of key=value couples separated by ":".

For example to specify libxavs2 encoding options with -xavs2-params:

    
    
    ffmpeg -i input -c:v libxavs2 -xavs2-params RdoqLevel=0 output.avs2
    

### 9.20 libxeve

eXtra-fast Essential Video Encoder (XEVE) MPEG-5 EVC encoder wrapper. The
xeve-equivalent options or values are listed in parentheses for easy
migration.

This encoder requires the presence of the libxeve headers and library during
configuration. You need to explicitly configure the build with \--enable-
libxeve.

Many libxeve encoder options are mapped to FFmpeg global codec options, while
unique encoder options are provided through private options. Additionally the
xeve-params private options allows one to pass a list of key=value tuples as
accepted by the libxeve `parse_xeve_params` function.

The xeve project website is at <https://github.com/mpeg5/xeve>.

#### 9.20.1 Options

The following options are supported by the libxeve wrapper. The xeve-
equivalent options or values are listed in parentheses for easy migration.

To reduce the duplication of documentation, only the private options and some
others requiring special attention are documented here. For the documentation
of the undocumented generic options, see the Codec Options chapter.

To get a more accurate and extensive documentation of the libxeve options,
invoke the command `xeve_app --help` or consult the libxeve documentation.

b (_bitrate_)

    

Set target video bitrate in bits/s. Note that FFmpeg's b option is expressed
in bits/s, while xeve's bitrate is in kilobits/s.

bf (_bframes_)

    

Set the maximum number of B frames (1,3,7,15).

g (_keyint_)

    

Set the GOP size (I-picture period).

preset (_preset_)

    

Set the xeve preset. Set the encoder preset value to determine encoding speed
[fast, medium, slow, placebo]

tune (_tune_)

    

Set the encoder tune parameter [psnr, zerolatency]

profile (_profile_)

    

Set the encoder profile [0: baseline; 1: main]

crf (_crf_)

    

Set the quality for constant quality mode. Constant rate factor <10..49>
[default: 32]

qp (_qp_)

    

Set constant quantization rate control method parameter. Quantization
parameter qp <0..51> [default: 32]

threads (_threads_)

    

Force to use a specific number of threads

### 9.21 libxvid

Xvid MPEG-4 Part 2 encoder wrapper.

This encoder requires the presence of the libxvidcore headers and library
during configuration. You need to explicitly configure the build with
`--enable-libxvid --enable-gpl`.

The native `mpeg4` encoder supports the MPEG-4 Part 2 format, so users can
encode to this format without this library.

#### 9.21.1 Options

The following options are supported by the libxvid wrapper. Some of the
following options are listed but are not documented, and correspond to shared
codec options. See the Codec Options chapter for their documentation. The
other shared options which are not listed have no effect for the libxvid
encoder.

b

g

qmin

qmax

mpeg_quant

threads

bf

b_qfactor

b_qoffset

flags

    

Set specific encoding flags. Possible values:

'mv4'

    

Use four motion vector by macroblock.

'aic'

    

Enable high quality AC prediction.

'gray'

    

Only encode grayscale.

'qpel'

    

Enable quarter-pixel motion compensation.

'cgop'

    

Enable closed GOP.

'global_header'

    

Place global headers in extradata instead of every keyframe.

gmc

    

Enable the use of global motion compensation (GMC). Default is 0 (disabled).

me_quality

    

Set motion estimation quality level. Possible values in decreasing order of
speed and increasing order of quality:

'0'

    

Use no motion estimation (default).

'1, 2'

    

Enable advanced diamond zonal search for 16x16 blocks and half-pixel
refinement for 16x16 blocks.

'3, 4'

    

Enable all of the things described above, plus advanced diamond zonal search
for 8x8 blocks and half-pixel refinement for 8x8 blocks, also enable motion
estimation on chroma planes for P and B-frames.

'5, 6'

    

Enable all of the things described above, plus extended 16x16 and 8x8 blocks
search.

mbd

    

Set macroblock decision algorithm. Possible values in the increasing order of
quality:

'simple'

    

Use macroblock comparing function algorithm (default).

'bits'

    

Enable rate distortion-based half pixel and quarter pixel refinement for 16x16
blocks.

'rd'

    

Enable all of the things described above, plus rate distortion-based half
pixel and quarter pixel refinement for 8x8 blocks, and rate distortion-based
search using square pattern.

lumi_aq

    

Enable lumi masking adaptive quantization when set to 1. Default is 0
(disabled).

variance_aq

    

Enable variance adaptive quantization when set to 1. Default is 0 (disabled).

When combined with lumi_aq, the resulting quality will not be better than any
of the two specified individually. In other words, the resulting quality will
be the worse one of the two effects.

trellis

    

Set rate-distortion optimal quantization.

ssim

    

Set structural similarity (SSIM) displaying method. Possible values:

'off'

    

Disable displaying of SSIM information.

'avg'

    

Output average SSIM at the end of encoding to stdout. The format of showing
the average SSIM is:

    
    
    Average SSIM: %f
    

For users who are not familiar with C, %f means a float number, or a decimal
(e.g. 0.939232).

'frame'

    

Output both per-frame SSIM data during encoding and average SSIM at the end of
encoding to stdout. The format of per-frame information is:

    
    
           SSIM: avg: %1.3f min: %1.3f max: %1.3f
    

For users who are not familiar with C, %1.3f means a float number rounded to 3
digits after the dot (e.g. 0.932).

ssim_acc

    

Set SSIM accuracy. Valid options are integers within the range of 0-4, while 0
gives the most accurate result and 4 computes the fastest.

### 9.22 MediaFoundation

This provides wrappers to encoders (both audio and video) in the
MediaFoundation framework. It can access both SW and HW encoders. Video
encoders can take input in either of nv12 or yuv420p form (some encoders
support both, some support only either - in practice, nv12 is the safer
choice, especially among HW encoders).

### 9.23 Microsoft RLE

Microsoft RLE aka MSRLE encoder. Only 8-bit palette mode supported. Compatible
with Windows 3.1 and Windows 95.

#### 9.23.1 Options

g integer

    

Keyframe interval. A keyframe is inserted at least every `-g` frames,
sometimes sooner.

### 9.24 mpeg2

MPEG-2 video encoder.

#### 9.24.1 Options

profile

    

Select the mpeg2 profile to encode:

'422'

'high'

'ss'

    

Spatially Scalable

'snr'

    

SNR Scalable

'main'

'simple'

level

    

Select the mpeg2 level to encode:

'high'

'high1440'

'main'

'low'

seq_disp_ext integer

    

Specifies if the encoder should write a sequence_display_extension to the
output.

-1
auto

    

Decide automatically to write it or not (this is the default) by checking if
the data to be written is different from the default or unspecified values.

0

never

    

Never write it.

1

always

    

Always write it.

video_format integer

    

Specifies the video_format written into the sequence display extension
indicating the source of the video pictures. The default is 'unspecified', can
be 'component', 'pal', 'ntsc', 'secam' or 'mac'. For maximum compatibility,
use 'component'.

a53cc boolean

    

Import closed captions (which must be ATSC compatible format) into output.
Default is 1 (on).

### 9.25 png

PNG image encoder.

#### 9.25.1 Options

compression_level

    

Sets the compression level, from 0 to 9(default)

#### 9.25.2 Private options

dpi integer

    

Set physical density of pixels, in dots per inch, unset by default

dpm integer

    

Set physical density of pixels, in dots per meter, unset by default

pred method

    

Set prediction method (none, sub, up, avg, paeth, mixed), default is paeth

### 9.26 ProRes

Apple ProRes encoder.

FFmpeg contains 2 ProRes encoders, the prores-aw and prores-ks encoder. The
used encoder can be chosen with the `-vcodec` option.

#### 9.26.1 Private Options for prores-ks

profile integer

    

Select the ProRes profile to encode

'proxy'

'lt'

'standard'

'hq'

'4444'

'4444xq'

quant_mat integer

    

Select quantization matrix.

'auto'

'default'

'proxy'

'lt'

'standard'

'hq'

If set to auto, the matrix matching the profile will be picked. If not set,
the matrix providing the highest quality, default, will be picked.

bits_per_mb integer

    

How many bits to allot for coding one macroblock. Different profiles use
between 200 and 2400 bits per macroblock, the maximum is 8000.

mbs_per_slice integer

    

Number of macroblocks in each slice (1-8); the default value (8) should be
good in almost all situations.

vendor string

    

Override the 4-byte vendor ID. A custom vendor ID like apl0 would claim the
stream was produced by the Apple encoder.

alpha_bits integer

    

Specify number of bits for alpha component. Possible values are 0, 8 and 16.
Use 0 to disable alpha plane coding.

#### 9.26.2 Speed considerations

In the default mode of operation the encoder has to honor frame constraints
(i.e. not produce frames with size bigger than requested) while still making
output picture as good as possible. A frame containing a lot of small details
is harder to compress and the encoder would spend more time searching for
appropriate quantizers for each slice.

Setting a higher bits_per_mb limit will improve the speed.

For the fastest encoding speed set the qscale parameter (4 is the recommended
value) and do not set a size constraint.

### 9.27 QSV Encoders

The family of Intel QuickSync Video encoders (MPEG-2, H.264, HEVC, JPEG/MJPEG,
VP9, AV1)

#### 9.27.1 Ratecontrol Method

The ratecontrol method is selected as follows:

  * When global_quality is specified, a quality-based mode is used. Specifically this means either 
    * \- CQP \- constant quantizer scale, when the qscale codec flag is also set (the -qscale ffmpeg option). 
    * \- LA_ICQ \- intelligent constant quality with lookahead, when the look_ahead option is also set. 
    * \- ICQ - intelligent constant quality otherwise. For the ICQ modes, global quality range is 1 to 51, with 1 being the best quality. 
  * Otherwise when the desired average bitrate is specified with the b option, a bitrate-based mode is used. 
    * \- LA \- VBR with lookahead, when the look_ahead option is specified. 
    * \- VCM \- video conferencing mode, when the vcm option is set. 
    * \- CBR \- constant bitrate, when maxrate is specified and equal to the average bitrate. 
    * \- VBR \- variable bitrate, when maxrate is specified, but is higher than the average bitrate. 
    * \- AVBR \- average VBR mode, when maxrate is not specified, both avbr_accuracy and avbr_convergence are set to non-zero. This mode is available for H264 and HEVC on Windows. 
  * Otherwise the default ratecontrol method CQP is used. 

Note that depending on your system, a different mode than the one you
specified may be selected by the encoder. Set the verbosity level to verbose
or higher to see the actual settings used by the QSV runtime.

#### 9.27.2 Global Options -> MSDK Options

Additional libavcodec global options are mapped to MSDK options as follows:

  * g/gop_size -> GopPicSize
  * bf/max_b_frames+1 -> GopRefDist
  * rc_init_occupancy/rc_initial_buffer_occupancy -> InitialDelayInKB
  * slices -> NumSlice
  * refs -> NumRefFrame
  * b_strategy/b_frame_strategy -> BRefType
  * cgop/CLOSED_GOP codec flag -> GopOptFlag
  * For the CQP mode, the i_qfactor/i_qoffset and b_qfactor/b_qoffset set the difference between QPP and QPI, and QPP and QPB respectively. 
  * Setting the coder option to the value vlc will make the H.264 encoder use CAVLC instead of CABAC. 

#### 9.27.3 Common Options

Following options are used by all qsv encoders.

async_depth

    

Specifies how many asynchronous operations an application performs before the
application explicitly synchronizes the result. If zero, the value is not
specified.

preset

    

This option itemizes a range of choices from veryfast (best speed) to veryslow
(best quality).

'veryfast'

'faster'

'fast'

'medium'

'slow'

'slower'

'veryslow'

forced_idr

    

Forcing I frames as IDR frames.

low_power

    

For encoders set this flag to ON to reduce power consumption and GPU usage.

#### 9.27.4 Runtime Options

Following options can be used durning qsv encoding.

global_quality

i_quant_factor

i_quant_offset

b_quant_factor

b_quant_offset

    

Supported in h264_qsv and hevc_qsv. Change these value to reset qsv codec's qp
configuration.

max_frame_size

    

Supported in h264_qsv and hevc_qsv. Change this value to reset qsv codec's
MaxFrameSize configuration.

gop_size

    

Change this value to reset qsv codec's gop configuration.

int_ref_type

int_ref_cycle_size

int_ref_qp_delta

int_ref_cycle_dist

    

Supported in h264_qsv and hevc_qsv. Change these value to reset qsv codec's
Intra Refresh configuration.

qmax

qmin

max_qp_i

min_qp_i

max_qp_p

min_qp_p

max_qp_b

min_qp_b

    

Supported in h264_qsv. Change these value to reset qsv codec's max/min qp
configuration.

low_delay_brc

    

Supported in h264_qsv, hevc_qsv and av1_qsv. Change this value to reset qsv
codec's low_delay_brc configuration.

framerate

    

Change this value to reset qsv codec's framerate configuration.

bit_rate

rc_buffer_size

rc_initial_buffer_occupancy

rc_max_rate

    

Change these value to reset qsv codec's bitrate control configuration.

pic_timing_sei

    

Supported in h264_qsv and hevc_qsv. Change this value to reset qsv codec's
pic_timing_sei configuration.

qsv_params

    

Set QSV encoder parameters as a colon-separated list of key-value pairs.

The qsv_params should be formatted as `key1=value1:key2=value2:...`.

These parameters are passed directly to the underlying Intel Quick Sync Video
(QSV) encoder using the MFXSetParameter function.

Example:

    
    
    ffmpeg -i input.mp4 -c:v h264_qsv -qsv_params "CodingOption1=1:CodingOption2=2" output.mp4
    

This option allows fine-grained control over various encoder-specific settings
provided by the QSV encoder.

#### 9.27.5 H264 options

These options are used by h264_qsv

extbrc

    

Extended bitrate control.

recovery_point_sei

    

Set this flag to insert the recovery point SEI message at the beginning of
every intra refresh cycle.

rdo

    

Enable rate distortion optimization.

max_frame_size

    

Maximum encoded frame size in bytes.

max_frame_size_i

    

Maximum encoded frame size for I frames in bytes. If this value is set as
larger than zero, then for I frames the value set by max_frame_size is
ignored.

max_frame_size_p

    

Maximum encoded frame size for P frames in bytes. If this value is set as
larger than zero, then for P frames the value set by max_frame_size is
ignored.

max_slice_size

    

Maximum encoded slice size in bytes.

bitrate_limit

    

Toggle bitrate limitations. Modifies bitrate to be in the range imposed by the
QSV encoder. Setting this flag off may lead to violation of HRD conformance.
Mind that specifying bitrate below the QSV encoder range might significantly
affect quality. If on this option takes effect in non CQP modes: if bitrate is
not in the range imposed by the QSV encoder, it will be changed to be in the
range.

mbbrc

    

Setting this flag enables macroblock level bitrate control that generally
improves subjective visual quality. Enabling this flag may have negative
impact on performance and objective visual quality metric.

low_delay_brc

    

Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which
provides more accurate bitrate control to minimize the variance of bitstream
size frame by frame. Value: -1-default 0-off 1-on

adaptive_i

    

This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.

adaptive_b

    

This flag controls changing of frame type from B to P.

p_strategy

    

Enable P-pyramid: 0-default 1-simple 2-pyramid(bf need to be set to 0).

b_strategy

    

This option controls usage of B frames as reference.

dblk_idc

    

This option disable deblocking. It has value in range 0~2.

cavlc

    

If set, CAVLC is used; if unset, CABAC is used for encoding.

vcm

    

Video conferencing mode, please see ratecontrol method.

idr_interval

    

Distance (in I-frames) between IDR frames.

pic_timing_sei

    

Insert picture timing SEI with pic_struct_syntax element.

single_sei_nal_unit

    

Put all the SEI messages into one NALU.

max_dec_frame_buffering

    

Maximum number of frames buffered in the DPB.

look_ahead

    

Use VBR algorithm with look ahead.

look_ahead_depth

    

Depth of look ahead in number frames.

look_ahead_downsampling

    

Downscaling factor for the frames saved for the lookahead analysis.

'unknown'

'auto'

'off'

'2x'

'4x'

int_ref_type

    

Specifies intra refresh type. The major goal of intra refresh is improvement
of error resilience without significant impact on encoded bitstream size
caused by I frames. The SDK encoder achieves this by encoding part of each
frame in refresh cycle using intra MBs. none means no refresh. vertical means
vertical refresh, by column of MBs. horizontal means horizontal refresh, by
rows of MBs. slice means horizontal refresh by slices without overlapping. In
case of slice, in_ref_cycle_size is ignored. To enable intra refresh, B frame
should be set to 0.

int_ref_cycle_size

    

Specifies number of pictures within refresh cycle starting from 2. 0 and 1 are
invalid values.

int_ref_qp_delta

    

Specifies QP difference for inserted intra MBs. This is signed value in [-51,
51] range if target encoding bit-depth for luma samples is 8 and this range is
[-63, 63] for 10 bit-depth or [-75, 75] for 12 bit-depth respectively.

int_ref_cycle_dist

    

Distance between the beginnings of the intra-refresh cycles in frames.

profile

    

'unknown'

'baseline'

'main'

'high'

a53cc

    

Use A53 Closed Captions (if available).

aud

    

Insert the Access Unit Delimiter NAL.

mfmode

    

Multi-Frame Mode.

'off'

'auto'

repeat_pps

    

Repeat pps for every frame.

max_qp_i

    

Maximum video quantizer scale for I frame.

min_qp_i

    

Minimum video quantizer scale for I frame.

max_qp_p

    

Maximum video quantizer scale for P frame.

min_qp_p

    

Minimum video quantizer scale for P frame.

max_qp_b

    

Maximum video quantizer scale for B frame.

min_qp_b

    

Minimum video quantizer scale for B frame.

scenario

    

Provides a hint to encoder about the scenario for the encoding session.

'unknown'

'displayremoting'

'videoconference'

'archive'

'livestreaming'

'cameracapture'

'videosurveillance'

'gamestreaming'

'remotegaming'

avbr_accuracy

    

Accuracy of the AVBR ratecontrol (unit of tenth of percent).

avbr_convergence

    

Convergence of the AVBR ratecontrol (unit of 100 frames)

The parameters avbr_accuracy and avbr_convergence are for the average variable
bitrate control (AVBR) algorithm. The algorithm focuses on overall encoding
quality while meeting the specified bitrate, target_bitrate, within the
accuracy range avbr_accuracy, after a avbr_Convergence period. This method
does not follow HRD and the instant bitrate is not capped or padded.

skip_frame

    

Use per-frame metadata "qsv_skip_frame" to skip frame when encoding. This
option defines the usage of this metadata.

'no_skip'

    

Frame skipping is disabled.

'insert_dummy'

    

Encoder inserts into bitstream frame where all macroblocks are encoded as
skipped.

'insert_nothing'

    

Similar to insert_dummy, but encoder inserts nothing into bitstream. The
skipped frames are still used in brc. For example, gop still include skipped
frames, and the frames after skipped frames will be larger in size.

'brc_only'

    

skip_frame metadata indicates the number of missed frames before the current
frame.

#### 9.27.6 HEVC Options

These options are used by hevc_qsv

extbrc

    

Extended bitrate control.

recovery_point_sei

    

Set this flag to insert the recovery point SEI message at the beginning of
every intra refresh cycle.

rdo

    

Enable rate distortion optimization.

max_frame_size

    

Maximum encoded frame size in bytes.

max_frame_size_i

    

Maximum encoded frame size for I frames in bytes. If this value is set as
larger than zero, then for I frames the value set by max_frame_size is
ignored.

max_frame_size_p

    

Maximum encoded frame size for P frames in bytes. If this value is set as
larger than zero, then for P frames the value set by max_frame_size is
ignored.

max_slice_size

    

Maximum encoded slice size in bytes.

mbbrc

    

Setting this flag enables macroblock level bitrate control that generally
improves subjective visual quality. Enabling this flag may have negative
impact on performance and objective visual quality metric.

low_delay_brc

    

Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which
provides more accurate bitrate control to minimize the variance of bitstream
size frame by frame. Value: -1-default 0-off 1-on

adaptive_i

    

This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.

adaptive_b

    

This flag controls changing of frame type from B to P.

p_strategy

    

Enable P-pyramid: 0-default 1-simple 2-pyramid(bf need to be set to 0).

b_strategy

    

This option controls usage of B frames as reference.

dblk_idc

    

This option disable deblocking. It has value in range 0~2.

idr_interval

    

Distance (in I-frames) between IDR frames.

'begin_only'

    

Output an IDR-frame only at the beginning of the stream.

load_plugin

    

A user plugin to load in an internal session.

'none'

'hevc_sw'

'hevc_hw'

load_plugins

    

A :-separate list of hexadecimal plugin UIDs to load in an internal session.

look_ahead_depth

    

Depth of look ahead in number frames, available when extbrc option is enabled.

profile

    

Set the encoding profile (scc requires libmfx >= 1.32).

'unknown'

'main'

'main10'

'mainsp'

'rext'

'scc'

tier

    

Set the encoding tier (only level >= 4 can support high tier). This option
only takes effect when the level option is specified.

'main'

'high'

gpb

    

1: GPB (generalized P/B frame)

0: regular P frame.

tile_cols

    

Number of columns for tiled encoding.

tile_rows

    

Number of rows for tiled encoding.

aud

    

Insert the Access Unit Delimiter NAL.

pic_timing_sei

    

Insert picture timing SEI with pic_struct_syntax element.

transform_skip

    

Turn this option ON to enable transformskip. It is supported on platform equal
or newer than ICL.

int_ref_type

    

Specifies intra refresh type. The major goal of intra refresh is improvement
of error resilience without significant impact on encoded bitstream size
caused by I frames. The SDK encoder achieves this by encoding part of each
frame in refresh cycle using intra MBs. none means no refresh. vertical means
vertical refresh, by column of MBs. horizontal means horizontal refresh, by
rows of MBs. slice means horizontal refresh by slices without overlapping. In
case of slice, in_ref_cycle_size is ignored. To enable intra refresh, B frame
should be set to 0.

int_ref_cycle_size

    

Specifies number of pictures within refresh cycle starting from 2. 0 and 1 are
invalid values.

int_ref_qp_delta

    

Specifies QP difference for inserted intra MBs. This is signed value in [-51,
51] range if target encoding bit-depth for luma samples is 8 and this range is
[-63, 63] for 10 bit-depth or [-75, 75] for 12 bit-depth respectively.

int_ref_cycle_dist

    

Distance between the beginnings of the intra-refresh cycles in frames.

max_qp_i

    

Maximum video quantizer scale for I frame.

min_qp_i

    

Minimum video quantizer scale for I frame.

max_qp_p

    

Maximum video quantizer scale for P frame.

min_qp_p

    

Minimum video quantizer scale for P frame.

max_qp_b

    

Maximum video quantizer scale for B frame.

min_qp_b

    

Minimum video quantizer scale for B frame.

scenario

    

Provides a hint to encoder about the scenario for the encoding session.

'unknown'

'displayremoting'

'videoconference'

'archive'

'livestreaming'

'cameracapture'

'videosurveillance'

'gamestreaming'

'remotegaming'

avbr_accuracy

    

Accuracy of the AVBR ratecontrol (unit of tenth of percent).

avbr_convergence

    

Convergence of the AVBR ratecontrol (unit of 100 frames)

The parameters avbr_accuracy and avbr_convergence are for the average variable
bitrate control (AVBR) algorithm. The algorithm focuses on overall encoding
quality while meeting the specified bitrate, target_bitrate, within the
accuracy range avbr_accuracy, after a avbr_Convergence period. This method
does not follow HRD and the instant bitrate is not capped or padded.

skip_frame

    

Use per-frame metadata "qsv_skip_frame" to skip frame when encoding. This
option defines the usage of this metadata.

'no_skip'

    

Frame skipping is disabled.

'insert_dummy'

    

Encoder inserts into bitstream frame where all macroblocks are encoded as
skipped.

'insert_nothing'

    

Similar to insert_dummy, but encoder inserts nothing into bitstream. The
skipped frames are still used in brc. For example, gop still include skipped
frames, and the frames after skipped frames will be larger in size.

'brc_only'

    

skip_frame metadata indicates the number of missed frames before the current
frame.

#### 9.27.7 MPEG2 Options

These options are used by mpeg2_qsv

profile

    

'unknown'

'simple'

'main'

'high'

#### 9.27.8 VP9 Options

These options are used by vp9_qsv

profile

    

'unknown'

'profile0'

'profile1'

'profile2'

'profile3'

tile_cols

    

Number of columns for tiled encoding (requires libmfx >= 1.29).

tile_rows

    

Number of rows for tiled encoding (requires libmfx >= 1.29).

#### 9.27.9 AV1 Options

These options are used by av1_qsv (requires libvpl).

profile

    

'unknown'

'main'

tile_cols

    

Number of columns for tiled encoding.

tile_rows

    

Number of rows for tiled encoding.

adaptive_i

    

This flag controls insertion of I frames by the QSV encoder. Turn ON this flag
to allow changing of frame type from P and B to I.

adaptive_b

    

This flag controls changing of frame type from B to P.

b_strategy

    

This option controls usage of B frames as reference.

extbrc

    

Extended bitrate control.

look_ahead_depth

    

Depth of look ahead in number frames, available when extbrc option is enabled.

low_delay_brc

    

Setting this flag turns on or off LowDelayBRC feautre in qsv plugin, which
provides more accurate bitrate control to minimize the variance of bitstream
size frame by frame. Value: -1-default 0-off 1-on

max_frame_size

    

Set the allowed max size in bytes for each frame. If the frame size exceeds
the limitation, encoder will adjust the QP value to control the frame size.
Invalid in CQP rate control mode.

max_frame_size_i

    

Maximum encoded frame size for I frames in bytes. If this value is set as
larger than zero, then for I frames the value set by max_frame_size is
ignored.

max_frame_size_p

    

Maximum encoded frame size for P frames in bytes. If this value is set as
larger than zero, then for P frames the value set by max_frame_size is
ignored.

### 9.28 snow

#### 9.28.1 Options

iterative_dia_size

    

dia size for the iterative motion estimation

### 9.29 VAAPI encoders

Wrappers for hardware encoders accessible via VAAPI.

These encoders only accept input in VAAPI hardware surfaces. If you have input
in software frames, use the hwupload filter to upload them to the GPU.

The following standard libavcodec options are used:

  * g / gop_size
  * bf / max_b_frames
  * profile

If not set, this will be determined automatically from the format of the input
frames and the profiles supported by the driver.

  * level
  * b / bit_rate
  * maxrate / rc_max_rate
  * bufsize / rc_buffer_size
  * rc_init_occupancy / rc_initial_buffer_occupancy
  * compression_level

Speed / quality tradeoff: higher values are faster / worse quality.

  * q / global_quality

Size / quality tradeoff: higher values are smaller / worse quality.

  * qmin
  * qmax
  * i_qfactor / i_quant_factor
  * i_qoffset / i_quant_offset
  * b_qfactor / b_quant_factor
  * b_qoffset / b_quant_offset
  * slices

All encoders support the following options:

low_power

    

Some drivers/platforms offer a second encoder for some codecs intended to use
less power than the default encoder; setting this option will attempt to use
that encoder. Note that it may support a reduced feature set, so some other
options may not be available in this mode.

idr_interval

    

Set the number of normal intra frames between full-refresh (IDR) frames in
open-GOP mode. The intra frames are still IRAPs, but will not include global
headers and may have non-decodable leading pictures.

b_depth

    

Set the B-frame reference depth. When set to one (the default), all B-frames
will refer only to P- or I-frames. When set to greater values multiple layers
of B-frames will be present, frames in each layer only referring to frames in
higher layers.

async_depth

    

Maximum processing parallelism. Increase this to improve single channel
performance. This option doesn't work if driver doesn't implement vaSyncBuffer
function. Please make sure there are enough hw_frames allocated if a large
number of async_depth is used.

max_frame_size

    

Set the allowed max size in bytes for each frame. If the frame size exceeds
the limitation, encoder will adjust the QP value to control the frame size.
Invalid in CQP rate control mode.

rc_mode

    

Set the rate control mode to use. A given driver may only support a subset of
modes.

Possible modes:

auto

    

Choose the mode automatically based on driver support and the other options.
This is the default.

CQP

    

Constant-quality.

CBR

    

Constant-bitrate.

VBR

    

Variable-bitrate.

ICQ

    

Intelligent constant-quality.

QVBR

    

Quality-defined variable-bitrate.

AVBR

    

Average variable bitrate.

blbrc

    

Enable block level rate control, which assigns different bitrate block by
block. Invalid for CQP mode.

Each encoder also has its own specific options:

av1_vaapi

    

profile sets the value of _seq_profile_. tier sets the value of _seq_tier_.
level sets the value of _seq_level_idx_.

tiles

    

Set the number of tiles to encode the input video with, as columns x rows.
(default is auto, which means use minimal tile column/row number).

tile_groups

    

Set tile groups number. All the tiles will be distributed as evenly as
possible to each tile group. (default is 1).

h264_vaapi

    

profile sets the value of _profile_idc_ and the _constraint_set*_flag_ s.
level sets the value of _level_idc_.

coder

    

Set entropy encoder (default is _cabac_). Possible values:

'ac'

'cabac'

    

Use CABAC.

'vlc'

'cavlc'

    

Use CAVLC.

aud

    

Include access unit delimiters in the stream (not included by default).

sei

    

Set SEI message types to include. Some combination of the following values:

'identifier'

    

Include a _user_data_unregistered_ message containing information about the
encoder.

'timing'

    

Include picture timing parameters (_buffering_period_ and _pic_timing_
messages).

'recovery_point'

    

Include recovery points where appropriate (_recovery_point_ messages).

hevc_vaapi

    

profile and level set the values of _general_profile_idc_ and
_general_level_idc_ respectively.

aud

    

Include access unit delimiters in the stream (not included by default).

tier

    

Set _general_tier_flag_. This may affect the level chosen for the stream if it
is not explicitly specified.

sei

    

Set SEI message types to include. Some combination of the following values:

'hdr'

    

Include HDR metadata if the input frames have it
(_mastering_display_colour_volume_ and _content_light_level_ messages).

tiles

    

Set the number of tiles to encode the input video with, as columns x rows.
Larger numbers allow greater parallelism in both encoding and decoding, but
may decrease coding efficiency.

mjpeg_vaapi

    

Only baseline DCT encoding is supported. The encoder always uses the standard
quantisation and huffman tables - global_quality scales the standard
quantisation table (range 1-100).

For YUV, 4:2:0, 4:2:2 and 4:4:4 subsampling modes are supported. RGB is also
supported, and will create an RGB JPEG.

jfif

    

Include JFIF header in each frame (not included by default).

huffman

    

Include standard huffman tables (on by default). Turning this off will save a
few hundred bytes in each output frame, but may lose compatibility with some
JPEG decoders which don't fully handle MJPEG.

mpeg2_vaapi

    

profile and level set the value of _profile_and_level_indication_.

vp8_vaapi

    

B-frames are not supported.

global_quality sets the _q_idx_ used for non-key frames (range 0-127).

loop_filter_level

loop_filter_sharpness

    

Manually set the loop filter parameters.

vp9_vaapi

    

global_quality sets the _q_idx_ used for P-frames (range 0-255).

loop_filter_level

loop_filter_sharpness

    

Manually set the loop filter parameters.

B-frames are supported, but the output stream is always in encode order rather
than display order. If B-frames are enabled, it may be necessary to use the
vp9_raw_reorder bitstream filter to modify the output stream to display frames
in the correct order.

Only normal frames are produced - the vp9_superframe bitstream filter may be
required to produce a stream usable with all decoders.

### 9.30 vbn

Vizrt Binary Image encoder.

This format is used by the broadcast vendor Vizrt for quick texture streaming.
Advanced features of the format such as LZW compression of texture data or
generation of mipmaps are not supported.

#### 9.30.1 Options

format string

    

Sets the texture compression used by the VBN file. Can be dxt1, dxt5 or raw.
Default is dxt5.

### 9.31 vc2

SMPTE VC-2 (previously BBC Dirac Pro). This codec was primarily aimed at
professional broadcasting but since it supports yuv420, yuv422 and yuv444 at 8
(limited range or full range), 10 or 12 bits, this makes it suitable for other
tasks which require low overhead and low compression (like screen recording).

#### 9.31.1 Options

b

    

Sets target video bitrate. Usually that's around 1:6 of the uncompressed video
bitrate (e.g. for 1920x1080 50fps yuv422p10 that's around 400Mbps). Higher
values (close to the uncompressed bitrate) turn on lossless compression mode.

field_order

    

Enables field coding when set (e.g. to tt - top field first) for interlaced
inputs. Should increase compression with interlaced content as it splits the
fields and encodes each separately.

wavelet_depth

    

Sets the total amount of wavelet transforms to apply, between 1 and 5
(default). Lower values reduce compression and quality. Less capable decoders
may not be able to handle values of wavelet_depth over 3.

wavelet_type

    

Sets the transform type. Currently only 5_3 (LeGall) and 9_7 (Deslauriers-
Dubuc) are implemented, with 9_7 being the one with better compression and
thus is the default.

slice_width

slice_height

    

Sets the slice size for each slice. Larger values result in better
compression. For compatibility with other more limited decoders use
slice_width of 32 and slice_height of 8.

tolerance

    

Sets the undershoot tolerance of the rate control system in percent. This is
to prevent an expensive search from being run.

qm

    

Sets the quantization matrix preset to use by default or when wavelet_depth is
set to 5

  * \- default Uses the default quantization matrix from the specifications, extended with values for the fifth level. This provides a good balance between keeping detail and omitting artifacts. 
  * \- flat Use a completely zeroed out quantization matrix. This increases PSNR but might reduce perception. Use in bogus benchmarks. 
  * \- color Reduces detail but attempts to preserve color at extremely low bitrates. 

## 10 Subtitles Encoders

### 10.1 dvdsub

This codec encodes the bitmap subtitle format that is used in DVDs. Typically
they are stored in VOBSUB file pairs (*.idx + *.sub), and they can also be
used in Matroska files.

#### 10.1.1 Options

palette

    

Specify the global palette used by the bitmaps.

The format for this option is a string containing 16 24-bits hexadecimal
numbers (without 0x prefix) separated by commas, for example `0d00ee, ee450d,
101010, eaeaea, 0ce60b, ec14ed, ebff0b, 0d617a, 7b7b7b, d1d1d1, 7b2a0e,
0d950c, 0f007b, cf0dec, cfa80c, 7c127b`.

even_rows_fix

    

When set to 1, enable a work-around that makes the number of pixel rows even
in all subtitles. This fixes a problem with some players that cut off the
bottom row if the number is odd. The work-around just adds a fully transparent
row if needed. The overhead is low, typically one byte per subtitle on
average.

By default, this work-around is disabled.

## 11 See Also

[ffmpeg](ffmpeg.html), [ffplay](ffplay.html), [ffprobe](ffprobe.html),
[libavcodec](libavcodec.html)

## 12 Authors

The FFmpeg developers.

For details about the authorship, see the Git history of the project
(https://git.ffmpeg.org/ffmpeg), e.g. by typing the command `git log` in the
FFmpeg source directory, or browsing the online repository at
<https://git.ffmpeg.org/ffmpeg>.

Maintainers for the specific components are listed in the file MAINTAINERS in
the source code tree.

This document was generated on _April 25, 2025_ using
[_makeinfo_](http://www.gnu.org/software/texinfo/).

Hosting provided by [telepoint.bg](https://telepoint.bg)

