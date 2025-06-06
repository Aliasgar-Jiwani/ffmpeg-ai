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

#  __ffmpeg Documentation

## Table of Contents

  * 1 Synopsis
  * 2 Description
  * 3 Detailed description
    * 3.1 Streamcopy
    * 3.2 Trancoding
    * 3.3 Filtering
      * 3.3.1 Simple filtergraphs
      * 3.3.2 Complex filtergraphs
    * 3.4 Loopback decoders
  * 4 Stream selection
    * 4.1 Description
      * 4.1.1 Automatic stream selection
      * 4.1.2 Manual stream selection
      * 4.1.3 Complex filtergraphs
      * 4.1.4 Stream handling
    * 4.2 Examples
  * 5 Options
    * 5.1 Stream specifiers
    * 5.2 Generic options
    * 5.3 AVOptions
    * 5.4 Main options
    * 5.5 Video Options
    * 5.6 Advanced Video options
    * 5.7 Audio Options
    * 5.8 Advanced Audio options
    * 5.9 Subtitle options
    * 5.10 Advanced Subtitle options
    * 5.11 Advanced options
    * 5.12 Preset files
      * 5.12.1 ffpreset files
      * 5.12.2 avpreset files
    * 5.13 vstats file format
  * 6 Examples
    * 6.1 Video and Audio grabbing
    * 6.2 X11 grabbing
    * 6.3 Video and Audio file format conversion
  * 7 See Also
  * 8 Authors

## 1 Synopsis

ffmpeg [global_options] {[input_file_options] -i input_url} ...
{[output_file_options] output_url} ...

## 2 Description

`ffmpeg` is a universal media converter. It can read a wide variety of inputs
- including live grabbing/recording devices - filter, and transcode them into
a plethora of output formats.

`ffmpeg` reads from an arbitrary number of inputs (which can be regular files,
pipes, network streams, grabbing devices, etc.), specified by the `-i` option,
and writes to an arbitrary number of outputs, which are specified by a plain
output url. Anything found on the command line which cannot be interpreted as
an option is considered to be an output url.

Each input or output can, in principle, contain any number of elementary
streams of different types (video/audio/subtitle/attachment/data), though the
allowed stream counts and/or types may be limited by the container format.
Selecting which streams from which inputs will go into which output is either
done automatically or with the `-map` option (see the Stream selection
chapter).

To refer to inputs/outputs in options, you must use their indices (0-based).
E.g. the first input is `0`, the second is `1`, etc. Similarly, streams within
an input/output are referred to by their indices. E.g. `2:3` refers to the
fourth stream in the third input or output. Also see the Stream specifiers
chapter.

As a general rule, options are applied to the next specified file. Therefore,
order is important, and you can have the same option on the command line
multiple times. Each occurrence is then applied to the next input or output
file. Exceptions from this rule are the global options (e.g. verbosity level),
which should be specified first.

Do not mix input and output files - first specify all input files, then all
output files. Also do not mix options which belong to different files. All
options apply ONLY to the next input or output file and are reset between
files.

Some simple examples follow.

  * Convert an input media file to a different format, by re-encoding media streams: 
        
        ffmpeg -i input.avi output.mp4
        

  * Set the video bitrate of the output file to 64 kbit/s: 
        
        ffmpeg -i input.avi -b:v 64k -bufsize 64k output.mp4
        

  * Force the frame rate of the output file to 24 fps: 
        
        ffmpeg -i input.avi -r 24 output.mp4
        

  * Force the frame rate of the input file (valid for raw formats only) to 1 fps and the frame rate of the output file to 24 fps: 
        
        ffmpeg -r 1 -i input.m2v -r 24 output.mp4
        

The format option may be needed for raw input files.

## 3 Detailed description

`ffmpeg` builds a transcoding pipeline out of the components listed below. The
program's operation then consists of input data chunks flowing from the
sources down the pipes towards the sinks, while being transformed by the
components they encounter along the way.

The following kinds of components are available:

  * _Demuxers_ (short for "demultiplexers") read an input source in order to extract 
    * global properties such as metadata or chapters; 
    * list of input elementary streams and their properties 

One demuxer instance is created for each -i option, and sends encoded
_packets_ to _decoders_ or _muxers_.

In other literature, demuxers are sometimes called _splitters_ , because their
main function is splitting a file into elementary streams (though some files
only contain one elementary stream).

A schematic representation of a demuxer looks like this:

    
    ââââââââââââ¬ââââââââââââââââââââââââ
    â demuxer  â                       â packets for stream 0
    ââââââââââââ¡ elementary stream 0   ââââââââââââââââââââââââº
    â          â                       â
    â  global  âââââââââââââââââââââââââ¤
    âpropertiesâ                       â packets for stream 1
    â   and    â elementary stream 1   ââââââââââââââââââââââââº
    â metadata â                       â
    â          âââââââââââââââââââââââââ¤
    â          â                       â
    â          â     ...........       â
    â          â                       â
    â          âââââââââââââââââââââââââ¤
    â          â                       â packets for stream N
    â          â elementary stream N   ââââââââââââââââââââââââº
    â          â                       â
    ââââââââââââ´ââââââââââââââââââââââââ
         â²
         â
         â read from file, network stream,
         â     grabbing device, etc.
         â
    

  * _Decoders_ receive encoded (compressed) _packets_ for an audio, video, or subtitle elementary stream, and decode them into raw _frames_ (arrays of pixels for video, PCM for audio). A decoder is typically associated with (and receives its input from) an elementary stream in a _demuxer_ , but sometimes may also exist on its own (see Loopback decoders). 

A schematic representation of a decoder looks like this:

        
        âââââââââââ
         packets  â         â raw frames
        ââââââââââºâ decoder ââââââââââââââº
                  â         â
                  âââââââââââ
        

  * _Filtergraphs_ process and transform raw audio or video _frames_. A filtergraph consists of one or more individual _filters_ linked into a graph. Filtergraphs come in two flavors - _simple_ and _complex_ , configured with the -filter and -filter_complex options, respectively. 

A simple filtergraph is associated with an _output elementary stream_ ; it
receives the input to be filtered from a _decoder_ and sends filtered output
to that output stream's _encoder_.

A simple video filtergraph that performs deinterlacing (using the `yadif`
deinterlacer) followed by resizing (using the `scale` filter) can look like
this:

        
        ââââââââââââââââââââââââââ
                     â  simple filtergraph    â
         frames from ââââââââââââââââââââââââââ¡ frames for
         a decoder   â  âââââââââ  âââââââââ  â an encoder
        âââââââââââââºâââºâ yadif âââºâ scale âââºââââââââââââââº
                     â  âââââââââ  âââââââââ  â
                     ââââââââââââââââââââââââââ
        

A complex filtergraph is standalone and not associated with any specific
stream. It may have multiple (or zero) inputs, potentially of different types
(audio or video), each of which receiving data either from a decoder or
another complex filtergraph's output. It also has one or more outputs that
feed either an encoder or another complex filtergraph's input.

The following example diagram represents a complex filtergraph with 3 inputs
and 2 outputs (all video):

        
        âââââââââââââââââââââââââââââââââââââââââââââââââââ
                  â               complex filtergraph               â
                  âââââââââââââââââââââââââââââââââââââââââââââââââââ¡
         frames   âââââââââ  âââââââââââ      âââââââââââ  ââââââââââ¤ frames
        ââââââââââºâinput 0âââºâ overlay âââââââºâ overlay âââºâoutput 0ââââââââââº
                  âââââââââ  â         â      â         â  ââââââââââ¤
         frames   ââââââââââ­âºâ         â    â­âºâ         â           â
        ââââââââââºâinput 1ââ¯ âââââââââââ    â âââââââââââ           â
                  âââââââââ                 â                       â
         frames   âââââââââ âââââââ âââââââ¬ââ¯              ââââââââââ¤ frames
        ââââââââââºâinput 2ââºâscaleââºâsplitâââââââââââââââââºâoutput 1ââââââââââº
                  âââââââââ âââââââ âââââââ                ââââââââââ¤
                  âââââââââââââââââââââââââââââââââââââââââââââââââââ
        

Frames from second input are overlaid over those from the first. Frames from
the third input are rescaled, then the duplicated into two identical streams.
One of them is overlaid over the combined first two inputs, with the result
exposed as the filtergraph's first output. The other duplicate ends up being
the filtergraph's second output.

  * _Encoders_ receive raw audio, video, or subtitle _frames_ and encode them into encoded _packets_. The encoding (compression) process is typically _lossy_ \- it degrades stream quality to make the output smaller; some encoders are _lossless_ , but at the cost of much higher output size. A video or audio encoder receives its input from some filtergraph's output, subtitle encoders receive input from a decoder (since subtitle filtering is not supported yet). Every encoder is associated with some muxer's _output elementary stream_ and sends its output to that muxer. 

A schematic representation of an encoder looks like this:

        
        âââââââââââ
         raw frames  â         â packets
        âââââââââââââºâ encoder âââââââââââº
                     â         â
                     âââââââââââ
        

  * _Muxers_ (short for "multiplexers") receive encoded _packets_ for their elementary streams from encoders (the _transcoding_ path) or directly from demuxers (the _streamcopy_ path), interleave them (when there is more than one elementary stream), and write the resulting bytes into the output file (or pipe, network stream, etc.). 

A schematic representation of a muxer looks like this:

        
        ââââââââââââââââââââââââ¬ââââââââââââ
         packets for stream 0  â                      â   muxer   â
        âââââââââââââââââââââââºâ  elementary stream 0 âââââââââââââ¡
                               â                      â           â
                               ââââââââââââââââââââââââ¤  global   â
         packets for stream 1  â                      âproperties â
        âââââââââââââââââââââââºâ  elementary stream 1 â   and     â
                               â                      â metadata  â
                               ââââââââââââââââââââââââ¤           â
                               â                      â           â
                               â     ...........      â           â
                               â                      â           â
                               ââââââââââââââââââââââââ¤           â
         packets for stream N  â                      â           â
        âââââââââââââââââââââââºâ  elementary stream N â           â
                               â                      â           â
                               ââââââââââââââââââââââââ´ââââââ¬ââââââ
                                                            â
                             write to file, network stream, â
                                 grabbing device, etc.      â
                                                            â
                                                            â¼
        

### 3.1 Streamcopy

The simplest pipeline in `ffmpeg` is single-stream _streamcopy_ , that is
copying one _input elementary stream_ 's packets without decoding, filtering,
or encoding them. As an example, consider an input file called INPUT.mkv with
3 elementary streams, from which we take the second and write it to file
OUTPUT.mp4. A schematic representation of such a pipeline looks like this:

    
    
    ââââââââââââ¬ââââââââââââââââââââââ
    â demuxer  â                     â unused
    ââââââââââââ¡ elementary stream 0 ââââââââââ³
    â          â                     â
    âINPUT.mkv âââââââââââââââââââââââ¤          ââââââââââââââââââââââââ¬ââââââââââââ
    â          â                     â packets  â                      â   muxer   â
    â          â elementary stream 1 âââââââââââºâ  elementary stream 0 âââââââââââââ¡
    â          â                     â          â                      âOUTPUT.mp4 â
    â          âââââââââââââââââââââââ¤          ââââââââââââââââââââââââ´ââââââââââââ
    â          â                     â unused
    â          â elementary stream 2 ââââââââââ³
    â          â                     â
    ââââââââââââ´ââââââââââââââââââââââ
    

The above pipeline can be constructed with the following commandline:

    
    
    ffmpeg -i INPUT.mkv -map 0:1 -c copy OUTPUT.mp4
    

In this commandline

  * there is a single input INPUT.mkv; 
  * there are no input options for this input; 
  * there is a single output OUTPUT.mp4; 
  * there are two output options for this output: 
    * `-map 0:1` selects the input stream to be used - from input with index 0 (i.e. the first one) the stream with index 1 (i.e. the second one); 
    * `-c copy` selects the `copy` encoder, i.e. streamcopy with no decoding or encoding. 

Streamcopy is useful for changing the elementary stream count, container
format, or modifying container-level metadata. Since there is no decoding or
encoding, it is very fast and there is no quality loss. However, it might not
work in some cases because of a variety of factors (e.g. certain information
required by the target container is not available in the source). Applying
filters is obviously also impossible, since filters work on decoded frames.

More complex streamcopy scenarios can be constructed - e.g. combining streams
from two input files into a single output:

    
    
    ââââââââââââ¬âââââââââââââââââââââ         ââââââââââââââââââââââ¬ââââââââââââ
    â demuxer 0â                    â packets â                    â   muxer   â
    ââââââââââââ¡elementary stream 0 ââââââââââºâelementary stream 0 âââââââââââââ¡
    âINPUT0.mkvâ                    â         â                    âOUTPUT.mp4 â
    ââââââââââââ´âââââââââââââââââââââ         ââââââââââââââââââââââ¤           â
    ââââââââââââ¬âââââââââââââââââââââ         â                    â           â
    â demuxer 1â                    â packets âelementary stream 1 â           â
    ââââââââââââ¡elementary stream 0 ââââââââââºâ                    â           â
    âINPUT1.aacâ                    â         ââââââââââââââââââââââ´ââââââââââââ
    ââââââââââââ´âââââââââââââââââââââ
    

that can be built by the commandline

    
    
    ffmpeg -i INPUT0.mkv -i INPUT1.aac -map 0:0 -map 1:0 -c copy OUTPUT.mp4
    

The output -map option is used twice here, creating two streams in the output
file - one fed by the first input and one by the second. The single instance
of the -c option selects streamcopy for both of those streams. You could also
use multiple instances of this option together with Stream specifiers to apply
different values to each stream, as will be demonstrated in following
sections.

A converse scenario is splitting multiple streams from a single input into
multiple outputs:

    
    
    ââââââââââââ¬ââââââââââââââââââââââ          âââââââââââââââââââââ¬ââââââââââââ
    â demuxer  â                     â packets  â                   â muxer 0   â
    ââââââââââââ¡ elementary stream 0 âââââââââââºâelementary stream 0âââââââââââââ¡
    â          â                     â          â                   âOUTPUT0.mp4â
    âINPUT.mkv âââââââââââââââââââââââ¤          âââââââââââââââââââââ´ââââââââââââ
    â          â                     â packets  âââââââââââââââââââââ¬ââââââââââââ
    â          â elementary stream 1 âââââââââââºâ                   â muxer 1   â
    â          â                     â          âelementary stream 0âââââââââââââ¡
    ââââââââââââ´ââââââââââââââââââââââ          â                   âOUTPUT1.mp4â
                                                âââââââââââââââââââââ´ââââââââââââ
    

built with

    
    
    ffmpeg -i INPUT.mkv -map 0:0 -c copy OUTPUT0.mp4 -map 0:1 -c copy OUTPUT1.mp4
    

Note how a separate instance of the -c option is needed for every output file
even though their values are the same. This is because non-global options
(which is most of them) only apply in the context of the file before which
they are placed.

These examples can of course be further generalized into arbitrary remappings
of any number of inputs into any number of outputs.

### 3.2 Trancoding

_Transcoding_ is the process of decoding a stream and then encoding it again.
Since encoding tends to be computationally expensive and in most cases
degrades the stream quality (i.e. it is _lossy_), you should only transcode
when you need to and perform streamcopy otherwise. Typical reasons to
transcode are:

  * applying filters - e.g. resizing, deinterlacing, or overlaying video; resampling or mixing audio; 
  * you want to feed the stream to something that cannot decode the original codec. 

Note that `ffmpeg` will transcode all audio, video, and subtitle streams
unless you specify -c copy for them.

Consider an example pipeline that reads an input file with one audio and one
video stream, transcodes the video and copies the audio into a single output
file. This can be schematically represented as follows

    
    
    ââââââââââââ¬ââââââââââââââââââââââ
    â demuxer  â                     â       audio packets
    ââââââââââââ¡ stream 0 (audio)    âââââââââââââââââââââââââââââââââââââââ®
    â          â                     â                                     â
    âINPUT.mkv âââââââââââââââââââââââ¤ video    âââââââââââ     raw        â
    â          â                     â packets  â  video  â video frames   â
    â          â stream 1 (video)    âââââââââââºâ decoder ââââââââââââââââ® â
    â          â                     â          â         â              â â
    ââââââââââââ´ââââââââââââââââââââââ          âââââââââââ              â â
                                                                         â¼ â¼
                                                                         â â
    ââââââââââââ¬ââââââââââââââââââââââ video    âââââââââââ              â â
    â muxer    â                     â packets  â  video  â              â â
    ââââââââââââ¡ stream 0 (video)    ââââââââââââ¤ encoder ââââââââââââââââ¯ â
    â          â                     â          â(libx264)â                â
    âOUTPUT.mp4âââââââââââââââââââââââ¤          âââââââââââ                â
    â          â                     â                                     â
    â          â stream 1 (audio)    âââââââââââââââââââââââââââââââââââââââ¯
    â          â                     â
    ââââââââââââ´ââââââââââââââââââââââ
    

and implemented with the following commandline:

    
    
    ffmpeg -i INPUT.mkv -map 0:v -map 0:a -c:v libx264 -c:a copy OUTPUT.mp4
    

Note how it uses stream specifiers `:v` and `:a` to select input streams and
apply different values of the -c option to them; see the Stream specifiers
section for more details.

### 3.3 Filtering

When transcoding, audio and video streams can be filtered before encoding,
with either a _simple_ or _complex_ filtergraph.

#### 3.3.1 Simple filtergraphs

Simple filtergraphs are those that have exactly one input and output, both of
the same type (audio or video). They are configured with the per-stream
-filter option (with -vf and -af aliases for -filter:v (video) and -filter:a
(audio) respectively). Note that simple filtergraphs are tied to their output
stream, so e.g. if you have multiple audio streams, -af will create a separate
filtergraph for each one.

Taking the trancoding example from above, adding filtering (and omitting
audio, for clarity) makes it look like this:

    
    
    ââââââââââââ¬ââââââââââââââââ
    â demuxer  â               â          âââââââââââ
    ââââââââââââ¡ video stream  â packets  â  video  â frames
    âINPUT.mkv â               âââââââââââºâ decoder âââââââºââââ®
    â          â               â          âââââââââââ         â
    ââââââââââââ´ââââââââââââââââ                              â
                                      â­ââââââââââââââââââââââââ¯
                                      â   ââââââââââââââââââââââââââ
                                      â   â  simple filtergraph    â
                                      â   ââââââââââââââââââââââââââ¡
                                      â   â  âââââââââ  âââââââââ  â
                                      â°âââºâââºâ yadif âââºâ scale âââºââ®
                                          â  âââââââââ  âââââââââ  ââ
                                          âââââââââââââââââââââââââââ
                                                                    â
                                                                    â
    ââââââââââââ¬ââââââââââââââââ video    âââââââââââ               â
    â muxer    â               â packets  â  video  â               â
    ââââââââââââ¡ video stream  ââââââââââââ¤ encoder âââââââââââââââââ¯
    âOUTPUT.mp4â               â          â         â
    â          â               â          âââââââââââ
    ââââââââââââ´ââââââââââââââââ
    

#### 3.3.2 Complex filtergraphs

Complex filtergraphs are those which cannot be described as simply a linear
processing chain applied to one stream. This is the case, for example, when
the graph has more than one input and/or output, or when output stream type is
different from input. Complex filtergraphs are configured with the
-filter_complex option. Note that this option is global, since a complex
filtergraph, by its nature, cannot be unambiguously associated with a single
stream or file. Each instance of -filter_complex creates a new complex
filtergraph, and there can be any number of them.

A trivial example of a complex filtergraph is the `overlay` filter, which has
two video inputs and one video output, containing one video overlaid on top of
the other. Its audio counterpart is the `amix` filter.

### 3.4 Loopback decoders

While decoders are normally associated with demuxer streams, it is also
possible to create "loopback" decoders that decode the output from some
encoder and allow it to be fed back to complex filtergraphs. This is done with
the `-dec` directive, which takes as a parameter the index of the output
stream that should be decoded. Every such directive creates a new loopback
decoder, indexed with successive integers starting at zero. These indices
should then be used to refer to loopback decoders in complex filtergraph link
labels, as described in the documentation for -filter_complex.

Decoding AVOptions can be passed to loopback decoders by placing them before
`-dec`, analogously to input/output options.

E.g. the following example:

    
    
    ffmpeg -i INPUT                                        \
      -map 0:v:0 -c:v libx264 -crf 45 -f null -            \
      -threads 3 -dec 0:0                                  \
      -filter_complex '[0:v][dec:0]hstack[stack]'          \
      -map '[stack]' -c:v ffv1 OUTPUT
    

reads an input video and

  * (line 2) encodes it with `libx264` at low quality; 
  * (line 3) decodes this encoded stream using 3 threads; 
  * (line 4) places decoded video side by side with the original input video; 
  * (line 5) combined video is then losslessly encoded and written into OUTPUT. 

Such a transcoding pipeline can be represented with the following diagram:

    
    
    ââââââââââââ¬ââââââââââââââââ
    â demuxer  â               â   âââââââââââ            âââââââââââ    ââââââââââââââââââââââ
    ââââââââââââ¡ video stream  â   â  video  â            â  video  â    â null muxer         â
    â   INPUT  â               ââââºâ decoder ââââ¬âââââââââºâ encoder âââ¬ââºâ(discards its input)â
    â          â               â   âââââââââââ  â         â(libx264)â â  ââââââââââââââââââââââ
    ââââââââââââ´ââââââââââââââââ                â         âââââââââââ â
                                     â­âââââââââââ¯   âââââââââââ       â
                                     â              âloopback â       â
                                     â â­âââââââââââââ¤ decoder âââââââââ¯
                                     â â            âââââââââââ
                                     â â
                                     â â
                                     â â  âââââââââââââââââââââ
                                     â â  âcomplex filtergraphâ
                                     â â  âââââââââââââââââââââ¡
                                     â â  â  âââââââââââââââ  â
                                     â°ââ«ââºâââºâ   hstack    âââºââ®
                                       â°ââºâââºâ             â  ââ
                                          â  âââââââââââââââ  ââ
                                          ââââââââââââââââââââââ
                                                               â
    ââââââââââââ¬ââââââââââââââââ  âââââââââââ                  â
    â muxer    â               â  â  video  â                  â
    ââââââââââââ¡ video stream  ââââ¤ encoder ââââââââââââââââââââ¯
    â  OUTPUT  â               â  â (ffv1)  â
    â          â               â  âââââââââââ
    ââââââââââââ´ââââââââââââââââ
    

## 4 Stream selection

`ffmpeg` provides the `-map` option for manual control of stream selection in
each output file. Users can skip `-map` and let ffmpeg perform automatic
stream selection as described below. The `-vn / -an / -sn / -dn` options can
be used to skip inclusion of video, audio, subtitle and data streams
respectively, whether manually mapped or automatically selected, except for
those streams which are outputs of complex filtergraphs.

### 4.1 Description

The sub-sections that follow describe the various rules that are involved in
stream selection. The examples that follow next show how these rules are
applied in practice.

While every effort is made to accurately reflect the behavior of the program,
FFmpeg is under continuous development and the code may have changed since the
time of this writing.

#### 4.1.1 Automatic stream selection

In the absence of any map options for a particular output file, ffmpeg
inspects the output format to check which type of streams can be included in
it, viz. video, audio and/or subtitles. For each acceptable stream type,
ffmpeg will pick one stream, when available, from among all the inputs.

It will select that stream based upon the following criteria:

  * for video, it is the stream with the highest resolution, 
  * for audio, it is the stream with the most channels, 
  * for subtitles, it is the first subtitle stream found but there's a caveat. The output format's default subtitle encoder can be either text-based or image-based, and only a subtitle stream of the same type will be chosen. 

In the case where several streams of the same type rate equally, the stream
with the lowest index is chosen.

Data or attachment streams are not automatically selected and can only be
included using `-map`.

#### 4.1.2 Manual stream selection

When `-map` is used, only user-mapped streams are included in that output
file, with one possible exception for filtergraph outputs described below.

#### 4.1.3 Complex filtergraphs

If there are any complex filtergraph output streams with unlabeled pads, they
will be added to the first output file. This will lead to a fatal error if the
stream type is not supported by the output format. In the absence of the map
option, the inclusion of these streams leads to the automatic stream selection
of their types being skipped. If map options are present, these filtergraph
streams are included in addition to the mapped streams.

Complex filtergraph output streams with labeled pads must be mapped once and
exactly once.

#### 4.1.4 Stream handling

Stream handling is independent of stream selection, with an exception for
subtitles described below. Stream handling is set via the `-codec` option
addressed to streams within a specific _output_ file. In particular, codec
options are applied by ffmpeg after the stream selection process and thus do
not influence the latter. If no `-codec` option is specified for a stream
type, ffmpeg will select the default encoder registered by the output file
muxer.

An exception exists for subtitles. If a subtitle encoder is specified for an
output file, the first subtitle stream found of any type, text or image, will
be included. ffmpeg does not validate if the specified encoder can convert the
selected stream or if the converted stream is acceptable within the output
format. This applies generally as well: when the user sets an encoder
manually, the stream selection process cannot check if the encoded stream can
be muxed into the output file. If it cannot, ffmpeg will abort and _all_
output files will fail to be processed.

### 4.2 Examples

The following examples illustrate the behavior, quirks and limitations of
ffmpeg's stream selection methods.

They assume the following three input files.

    
    
    input file 'A.avi'
          stream 0: video 640x360
          stream 1: audio 2 channels
    
    input file 'B.mp4'
          stream 0: video 1920x1080
          stream 1: audio 2 channels
          stream 2: subtitles (text)
          stream 3: audio 5.1 channels
          stream 4: subtitles (text)
    
    input file 'C.mkv'
          stream 0: video 1280x720
          stream 1: audio 2 channels
          stream 2: subtitles (image)
    

#### Example: automatic stream selection

    
    
    ffmpeg -i A.avi -i B.mp4 out1.mkv out2.wav -map 1:a -c:a copy out3.mov
    

There are three output files specified, and for the first two, no `-map`
options are set, so ffmpeg will select streams for these two files
automatically.

out1.mkv is a Matroska container file and accepts video, audio and subtitle
streams, so ffmpeg will try to select one of each type.  
For video, it will select `stream 0` from B.mp4, which has the highest
resolution among all the input video streams.  
For audio, it will select `stream 3` from B.mp4, since it has the greatest
number of channels.  
For subtitles, it will select `stream 2` from B.mp4, which is the first
subtitle stream from among A.avi and B.mp4.

out2.wav accepts only audio streams, so only `stream 3` from B.mp4 is
selected.

For out3.mov, since a `-map` option is set, no automatic stream selection will
occur. The `-map 1:a` option will select all audio streams from the second
input B.mp4. No other streams will be included in this output file.

For the first two outputs, all included streams will be transcoded. The
encoders chosen will be the default ones registered by each output format,
which may not match the codec of the selected input streams.

For the third output, codec option for audio streams has been set to `copy`,
so no decoding-filtering-encoding operations will occur, or _can_ occur.
Packets of selected streams shall be conveyed from the input file and muxed
within the output file.

#### Example: automatic subtitles selection

    
    
    ffmpeg -i C.mkv out1.mkv -c:s dvdsub -an out2.mkv
    

Although out1.mkv is a Matroska container file which accepts subtitle streams,
only a video and audio stream shall be selected. The subtitle stream of C.mkv
is image-based and the default subtitle encoder of the Matroska muxer is text-
based, so a transcode operation for the subtitles is expected to fail and
hence the stream isn't selected. However, in out2.mkv, a subtitle encoder is
specified in the command and so, the subtitle stream is selected, in addition
to the video stream. The presence of `-an` disables audio stream selection for
out2.mkv.

#### Example: unlabeled filtergraph outputs

    
    
    ffmpeg -i A.avi -i C.mkv -i B.mp4 -filter_complex "overlay" out1.mp4 out2.srt
    

A filtergraph is setup here using the `-filter_complex` option and consists of
a single video filter. The `overlay` filter requires exactly two video inputs,
but none are specified, so the first two available video streams are used,
those of A.avi and C.mkv. The output pad of the filter has no label and so is
sent to the first output file out1.mp4. Due to this, automatic selection of
the video stream is skipped, which would have selected the stream in B.mp4.
The audio stream with most channels viz. `stream 3` in B.mp4, is chosen
automatically. No subtitle stream is chosen however, since the MP4 format has
no default subtitle encoder registered, and the user hasn't specified a
subtitle encoder.

The 2nd output file, out2.srt, only accepts text-based subtitle streams. So,
even though the first subtitle stream available belongs to C.mkv, it is image-
based and hence skipped. The selected stream, `stream 2` in B.mp4, is the
first text-based subtitle stream.

#### Example: labeled filtergraph outputs

    
    
    ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0[outv];overlay;aresample" \
           -map '[outv]' -an        out1.mp4 \
                                    out2.mkv \
           -map '[outv]' -map 1:a:0 out3.mkv
    

The above command will fail, as the output pad labelled `[outv]` has been
mapped twice. None of the output files shall be processed.

    
    
    ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0[outv];overlay;aresample" \
           -an        out1.mp4 \
                      out2.mkv \
           -map 1:a:0 out3.mkv
    

This command above will also fail as the hue filter output has a label,
`[outv]`, and hasn't been mapped anywhere.

The command should be modified as follows,

    
    
    ffmpeg -i A.avi -i B.mp4 -i C.mkv -filter_complex "[1:v]hue=s=0,split=2[outv1][outv2];overlay;aresample" \
            -map '[outv1]' -an        out1.mp4 \
                                      out2.mkv \
            -map '[outv2]' -map 1:a:0 out3.mkv
    

The video stream from B.mp4 is sent to the hue filter, whose output is cloned
once using the split filter, and both outputs labelled. Then a copy each is
mapped to the first and third output files.

The overlay filter, requiring two video inputs, uses the first two unused
video streams. Those are the streams from A.avi and C.mkv. The overlay output
isn't labelled, so it is sent to the first output file out1.mp4, regardless of
the presence of the `-map` option.

The aresample filter is sent the first unused audio stream, that of A.avi.
Since this filter output is also unlabelled, it too is mapped to the first
output file. The presence of `-an` only suppresses automatic or manual stream
selection of audio streams, not outputs sent from filtergraphs. Both these
mapped streams shall be ordered before the mapped stream in out1.mp4.

The video, audio and subtitle streams mapped to `out2.mkv` are entirely
determined by automatic stream selection.

out3.mkv consists of the cloned video output from the hue filter and the first
audio stream from B.mp4.  

## 5 Options

All the numerical options, if not specified otherwise, accept a string
representing a number as input, which may be followed by one of the SI unit
prefixes, for example: 'K', 'M', or 'G'.

If 'i' is appended to the SI unit prefix, the complete prefix will be
interpreted as a unit prefix for binary multiples, which are based on powers
of 1024 instead of powers of 1000. Appending 'B' to the SI unit prefix
multiplies the value by 8. This allows using, for example: 'KB', 'MiB', 'G'
and 'B' as number suffixes.

Options which do not take arguments are boolean options, and set the
corresponding value to true. They can be set to false by prefixing the option
name with "no". For example using "-nofoo" will set the boolean option with
name "foo" to false.

Options that take arguments support a special syntax where the argument given
on the command line is interpreted as a path to the file from which the actual
argument value is loaded. To use this feature, add a forward slash '/'
immediately before the option name (after the leading dash). E.g.

    
    
    ffmpeg -i INPUT -/filter:v filter.script OUTPUT
    

will load a filtergraph description from the file named filter.script.

### 5.1 Stream specifiers

Some options are applied per-stream, e.g. bitrate or codec. Stream specifiers
are used to precisely specify which stream(s) a given option belongs to.

A stream specifier is a string generally appended to the option name and
separated from it by a colon. E.g. `-codec:a:1 ac3` contains the `a:1` stream
specifier, which matches the second audio stream. Therefore, it would select
the ac3 codec for the second audio stream.

A stream specifier can match several streams, so that the option is applied to
all of them. E.g. the stream specifier in `-b:a 128k` matches all audio
streams.

An empty stream specifier matches all streams. For example, `-codec copy` or
`-codec: copy` would copy all the streams without reencoding.

Possible forms of stream specifiers are:

stream_index

    

Matches the stream with this index. E.g. `-threads:1 4` would set the thread
count for the second stream to 4. If stream_index is used as an additional
stream specifier (see below), then it selects stream number stream_index from
the matching streams. Stream numbering is based on the order of the streams as
detected by libavformat except when a stream group specifier or program ID is
also specified. In this case it is based on the ordering of the streams in the
group or program.

stream_type[:additional_stream_specifier]

    

stream_type is one of following: 'v' or 'V' for video, 'a' for audio, 's' for
subtitle, 'd' for data, and 't' for attachments. 'v' matches all video
streams, 'V' only matches video streams which are not attached pictures, video
thumbnails or cover arts. If additional_stream_specifier is used, then it
matches streams which both have this type and match the
additional_stream_specifier. Otherwise, it matches all streams of the
specified type.

g:group_specifier[:additional_stream_specifier]

    

Matches streams which are in the group with the specifier group_specifier. if
additional_stream_specifier is used, then it matches streams which both are
part of the group and match the additional_stream_specifier. group_specifier
may be one of the following:

group_index

    

Match the stream with this group index.

#group_id or i:group_id

    

Match the stream with this group id.

p:program_id[:additional_stream_specifier]

    

Matches streams which are in the program with the id program_id. If
additional_stream_specifier is used, then it matches streams which both are
part of the program and match the additional_stream_specifier.

#stream_id or i:stream_id

    

Match the stream by stream id (e.g. PID in MPEG-TS container).

m:key[:value]

    

Matches streams with the metadata tag key having the specified value. If value
is not given, matches streams that contain the given tag with any value. The
colon character ':' in key or value needs to be backslash-escaped.

disp:dispositions[:additional_stream_specifier]

    

Matches streams with the given disposition(s). dispositions is a list of one
or more dispositions (as printed by the -dispositions option) joined with '+'.

u

    

Matches streams with usable configuration, the codec must be defined and the
essential information such as video dimension or audio sample rate must be
present.

Note that in `ffmpeg`, matching by metadata will only work properly for input
files.

### 5.2 Generic options

These options are shared amongst the ff* tools.

-L
    

Show license.

-h, -?, -help, --help [arg]
    

Show help. An optional parameter may be specified to print help about a
specific item. If no argument is specified, only basic (non advanced) tool
options are shown.

Possible values of arg are:

long

    

Print advanced tool options in addition to the basic tool options.

full

    

Print complete list of options, including shared and private options for
encoders, decoders, demuxers, muxers, filters, etc.

decoder=decoder_name

    

Print detailed information about the decoder named decoder_name. Use the
-decoders option to get a list of all decoders.

encoder=encoder_name

    

Print detailed information about the encoder named encoder_name. Use the
-encoders option to get a list of all encoders.

demuxer=demuxer_name

    

Print detailed information about the demuxer named demuxer_name. Use the
-formats option to get a list of all demuxers and muxers.

muxer=muxer_name

    

Print detailed information about the muxer named muxer_name. Use the -formats
option to get a list of all muxers and demuxers.

filter=filter_name

    

Print detailed information about the filter named filter_name. Use the
-filters option to get a list of all filters.

bsf=bitstream_filter_name

    

Print detailed information about the bitstream filter named
bitstream_filter_name. Use the -bsfs option to get a list of all bitstream
filters.

protocol=protocol_name

    

Print detailed information about the protocol named protocol_name. Use the
-protocols option to get a list of all protocols.

-version
    

Show version.

-buildconf
    

Show the build configuration, one option per line.

-formats
    

Show available formats (including devices).

-demuxers
    

Show available demuxers.

-muxers
    

Show available muxers.

-devices
    

Show available devices.

-codecs
    

Show all codecs known to libavcodec.

Note that the term 'codec' is used throughout this documentation as a shortcut
for what is more correctly called a media bitstream format.

-decoders
    

Show available decoders.

-encoders
    

Show all available encoders.

-bsfs
    

Show available bitstream filters.

-protocols
    

Show available protocols.

-filters
    

Show available libavfilter filters.

-pix_fmts
    

Show available pixel formats.

-sample_fmts
    

Show available sample formats.

-layouts
    

Show channel names and standard channel layouts.

-dispositions
    

Show stream dispositions.

-colors
    

Show recognized color names.

-sources device[,opt1=val1[,opt2=val2]...]
    

Show autodetected sources of the input device. Some devices may provide
system-dependent source names that cannot be autodetected. The returned list
cannot be assumed to be always complete.

    
    
    ffmpeg -sources pulse,server=192.168.0.4
    

-sinks device[,opt1=val1[,opt2=val2]...]
    

Show autodetected sinks of the output device. Some devices may provide system-
dependent sink names that cannot be autodetected. The returned list cannot be
assumed to be always complete.

    
    
    ffmpeg -sinks pulse,server=192.168.0.4
    

-loglevel [flags+]loglevel | -v [flags+]loglevel
    

Set logging level and flags used by the library.

The optional flags prefix can consist of the following values:

'repeat'

    

Indicates that repeated log output should not be compressed to the first line
and the "Last message repeated n times" line will be omitted.

'level'

    

Indicates that log output should add a `[level]` prefix to each message line.
This can be used as an alternative to log coloring, e.g. when dumping the log
to file.

'time'

    

Indicates that log lines should be prefixed with time information.

'datetime'

    

Indicates that log lines should be prefixed with date and time information.

Flags can also be used alone by adding a '+'/'-' prefix to set/reset a single
flag without affecting other flags or changing loglevel. When setting both
flags and loglevel, a '+' separator is expected between the last flags value
and before loglevel.

loglevel is a string or a number containing one of the following values:

'quiet, -8'

    

Show nothing at all; be silent.

'panic, 0'

    

Only show fatal errors which could lead the process to crash, such as an
assertion failure. This is not currently used for anything.

'fatal, 8'

    

Only show fatal errors. These are errors after which the process absolutely
cannot continue.

'error, 16'

    

Show all errors, including ones which can be recovered from.

'warning, 24'

    

Show all warnings and errors. Any message related to possibly incorrect or
unexpected events will be shown.

'info, 32'

    

Show informative messages during processing. This is in addition to warnings
and errors. This is the default value.

'verbose, 40'

    

Same as `info`, except more verbose.

'debug, 48'

    

Show everything, including debugging information.

'trace, 56'

For example to enable repeated log output, add the `level` prefix, and set
loglevel to `verbose`:

    
    
    ffmpeg -loglevel repeat+level+verbose -i input output
    

Another example that enables repeated log output without affecting current
state of `level` prefix flag or loglevel:

    
    
    ffmpeg [...] -loglevel +repeat
    

By default the program logs to stderr. If coloring is supported by the
terminal, colors are used to mark errors and warnings. Log coloring can be
disabled setting the environment variable `AV_LOG_FORCE_NOCOLOR`, or can be
forced setting the environment variable `AV_LOG_FORCE_COLOR`.

-report
    

Dump full command line and log output to a file named `program-YYYYMMDD-
HHMMSS.log` in the current directory. This file can be useful for bug reports.
It also implies `-loglevel debug`.

Setting the environment variable `FFREPORT` to any value has the same effect.
If the value is a ':'-separated key=value sequence, these options will affect
the report; option values must be escaped if they contain special characters
or the options delimiter ':' (see the "Quoting and escaping" section in the
ffmpeg-utils manual).

The following options are recognized:

file

    

set the file name to use for the report; `%p` is expanded to the name of the
program, `%t` is expanded to a timestamp, `%%` is expanded to a plain `%`

level

    

set the log verbosity level using a numerical value (see `-loglevel`).

For example, to output a report to a file named ffreport.log using a log level
of `32` (alias for log level `info`):

    
    
    FFREPORT=file=ffreport.log:level=32 ffmpeg -i input output
    

Errors in parsing the environment variable are not fatal, and will not appear
in the report.

-hide_banner
    

Suppress printing banner.

All FFmpeg tools will normally show a copyright notice, build options and
library versions. This option can be used to suppress printing this
information.

-cpuflags flags (_global_)
    

Allows setting and clearing cpu flags. This option is intended for testing. Do
not use it unless you know what you're doing.

    
    
    ffmpeg -cpuflags -sse+mmx ...
    ffmpeg -cpuflags mmx ...
    ffmpeg -cpuflags 0 ...
    

Possible flags for this option are:

'x86'

    

'mmx'

'mmxext'

'sse'

'sse2'

'sse2slow'

'sse3'

'sse3slow'

'ssse3'

'atom'

'sse4.1'

'sse4.2'

'avx'

'avx2'

'xop'

'fma3'

'fma4'

'3dnow'

'3dnowext'

'bmi1'

'bmi2'

'cmov'

'ARM'

    

'armv5te'

'armv6'

'armv6t2'

'vfp'

'vfpv3'

'neon'

'setend'

'AArch64'

    

'armv8'

'vfp'

'neon'

'PowerPC'

    

'altivec'

'Specific Processors'

    

'pentium2'

'pentium3'

'pentium4'

'k6'

'k62'

'athlon'

'athlonxp'

'k8'

-cpucount count (_global_)
    

Override detection of CPU count. This option is intended for testing. Do not
use it unless you know what you're doing.

    
    
    ffmpeg -cpucount 2
    

-max_alloc bytes
    

Set the maximum size limit for allocating a block on the heap by ffmpeg's
family of malloc functions. Exercise **extreme caution** when using this
option. Don't use if you do not understand the full consequence of doing so.
Default is INT_MAX.

### 5.3 AVOptions

These options are provided directly by the libavformat, libavdevice and
libavcodec libraries. To see the list of available AVOptions, use the -help
option. They are separated into two categories:

generic

    

These options can be set for any container, codec or device. Generic options
are listed under AVFormatContext options for containers/devices and under
AVCodecContext options for codecs.

private

    

These options are specific to the given container, device or codec. Private
options are listed under their corresponding containers/devices/codecs.

For example to write an ID3v2.3 header instead of a default ID3v2.4 to an MP3
file, use the id3v2_version private option of the MP3 muxer:

    
    
    ffmpeg -i input.flac -id3v2_version 3 out.mp3
    

All codec AVOptions are per-stream, and thus a stream specifier should be
attached to them:

    
    
    ffmpeg -i multichannel.mxf -map 0:v:0 -map 0:a:0 -map 0:a:0 -c:a:0 ac3 -b:a:0 640k -ac:a:1 2 -c:a:1 aac -b:2 128k out.mp4
    

In the above example, a multichannel audio stream is mapped twice for output.
The first instance is encoded with codec ac3 and bitrate 640k. The second
instance is downmixed to 2 channels and encoded with codec aac. A bitrate of
128k is specified for it using absolute index of the output stream.

Note: the -nooption syntax cannot be used for boolean AVOptions, use -option
0/-option 1.

Note: the old undocumented way of specifying per-stream AVOptions by
prepending v/a/s to the options name is now obsolete and will be removed soon.

### 5.4 Main options

-f fmt (_input/output_)
    

Force input or output file format. The format is normally auto detected for
input files and guessed from the file extension for output files, so this
option is not needed in most cases.

-i url (_input_)
    

input file url

-y (_global_)
    

Overwrite output files without asking.

-n (_global_)
    

Do not overwrite output files, and exit immediately if a specified output file
already exists.

-stream_loop number (_input_)
    

Set number of times input stream shall be looped. Loop 0 means no loop, loop
-1 means infinite loop.

-recast_media (_global_)
    

Allow forcing a decoder of a different media type than the one detected or
designated by the demuxer. Useful for decoding media data muxed as data
streams.

-c[:stream_specifier] codec (_input/output,per-stream_)
-codec[:stream_specifier] codec (_input/output,per-stream_)
    

Select an encoder (when used before an output file) or a decoder (when used
before an input file) for one or more streams. codec is the name of a
decoder/encoder or a special value `copy` (output only) to indicate that the
stream is not to be re-encoded.

For example

    
    
    ffmpeg -i INPUT -map 0 -c:v libx264 -c:a copy OUTPUT
    

encodes all video streams with libx264 and copies all audio streams.

For each stream, the last matching `c` option is applied, so

    
    
    ffmpeg -i INPUT -map 0 -c copy -c:v:1 libx264 -c:a:137 libvorbis OUTPUT
    

will copy all the streams except the second video, which will be encoded with
libx264, and the 138th audio, which will be encoded with libvorbis.

-t duration (_input/output_)
    

When used as an input option (before `-i`), limit the duration of data read
from the input file.

When used as an output option (before an output url), stop writing the output
after its duration reaches duration.

duration must be a time duration specification, see [(ffmpeg-utils)the Time
duration section in the ffmpeg-utils(1) manual](ffmpeg-utils.html#time-
duration-syntax).

-to and -t are mutually exclusive and -t has priority. 

-to position (_input/output_)
    

Stop writing the output or reading the input at position. position must be a
time duration specification, see [(ffmpeg-utils)the Time duration section in
the ffmpeg-utils(1) manual](ffmpeg-utils.html#time-duration-syntax).

-to and -t are mutually exclusive and -t has priority. 

-fs limit_size (_output_)
    

Set the file size limit, expressed in bytes. No further chunk of bytes is
written after the limit is exceeded. The size of the output file is slightly
more than the requested file size.

-ss position (_input/output_)
    

When used as an input option (before `-i`), seeks in this input file to
position. Note that in most formats it is not possible to seek exactly, so
`ffmpeg` will seek to the closest seek point before position. When transcoding
and -accurate_seek is enabled (the default), this extra segment between the
seek point and position will be decoded and discarded. When doing stream copy
or when -noaccurate_seek is used, it will be preserved.

When used as an output option (before an output url), decodes but discards
input until the timestamps reach position.

position must be a time duration specification, see [(ffmpeg-utils)the Time
duration section in the ffmpeg-utils(1) manual](ffmpeg-utils.html#time-
duration-syntax).

-sseof position (_input_)
    

Like the `-ss` option but relative to the "end of file". That is negative
values are earlier in the file, 0 is at EOF.

-isync input_index (_input_)
    

Assign an input as a sync source.

This will take the difference between the start times of the target and
reference inputs and offset the timestamps of the target file by that
difference. The source timestamps of the two inputs should derive from the
same clock source for expected results. If `copyts` is set then
`start_at_zero` must also be set. If either of the inputs has no starting
timestamp then no sync adjustment is made.

Acceptable values are those that refer to a valid ffmpeg input index. If the
sync reference is the target index itself or -1, then no adjustment is made to
target timestamps. A sync reference may not itself be synced to any other
input.

Default value is -1.

-itsoffset offset (_input_)
    

Set the input time offset.

offset must be a time duration specification, see [(ffmpeg-utils)the Time
duration section in the ffmpeg-utils(1) manual](ffmpeg-utils.html#time-
duration-syntax).

The offset is added to the timestamps of the input files. Specifying a
positive offset means that the corresponding streams are delayed by the time
duration specified in offset.

-itsscale scale (_input,per-stream_)
    

Rescale input timestamps. scale should be a floating point number.

-timestamp date (_output_)
    

Set the recording timestamp in the container.

date must be a date specification, see [(ffmpeg-utils)the Date section in the
ffmpeg-utils(1) manual](ffmpeg-utils.html#date-syntax).

-metadata[:metadata_specifier] key=value (_output,per-metadata_)
    

Set a metadata key/value pair.

An optional metadata_specifier may be given to set metadata on streams,
chapters or programs. See `-map_metadata` documentation for details.

This option overrides metadata set with `-map_metadata`. It is also possible
to delete metadata by using an empty value.

For example, for setting the title in the output file:

    
    
    ffmpeg -i in.avi -metadata title="my title" out.flv
    

To set the language of the first audio stream:

    
    
    ffmpeg -i INPUT -metadata:s:a:0 language=eng OUTPUT
    

-disposition[:stream_specifier] value (_output,per-stream_)
    

Sets the disposition flags for a stream.

Default value: by default, all disposition flags are copied from the input
stream, unless the output stream this option applies to is fed by a complex
filtergraph \- in that case no disposition flags are set by default.

value is a sequence of disposition flags separated by '+' or '-'. A '+' prefix
adds the given disposition, '-' removes it. If the first flag is also prefixed
with '+' or '-', the resulting disposition is the default value updated by
value. If the first flag is not prefixed, the resulting disposition is value.
It is also possible to clear the disposition by setting it to 0.

If no `-disposition` options were specified for an output file, ffmpeg will
automatically set the 'default' disposition flag on the first stream of each
type, when there are multiple streams of this type in the output file and no
stream of that type is already marked as default.

The `-dispositions` option lists the known disposition flags.

For example, to make the second audio stream the default stream:

    
    
    ffmpeg -i in.mkv -c copy -disposition:a:1 default out.mkv
    

To make the second subtitle stream the default stream and remove the default
disposition from the first subtitle stream:

    
    
    ffmpeg -i in.mkv -c copy -disposition:s:0 0 -disposition:s:1 default out.mkv
    

To add an embedded cover/thumbnail:

    
    
    ffmpeg -i in.mp4 -i IMAGE -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic out.mp4
    

To add the 'original' and remove the 'comment' disposition flag from the first
audio stream without removing its other disposition flags:

    
    
    ffmpeg -i in.mkv -c copy -disposition:a:0 +original-comment out.mkv
    

To remove the 'original' and add the 'comment' disposition flag to the first
audio stream without removing its other disposition flags:

    
    
    ffmpeg -i in.mkv -c copy -disposition:a:0 -original+comment out.mkv
    

To set only the 'original' and 'comment' disposition flags on the first audio
stream (and remove its other disposition flags):

    
    
    ffmpeg -i in.mkv -c copy -disposition:a:0 original+comment out.mkv
    

To remove all disposition flags from the first audio stream:

    
    
    ffmpeg -i in.mkv -c copy -disposition:a:0 0 out.mkv
    

Not all muxers support embedded thumbnails, and those who do, only support a
few formats, like JPEG or PNG.

-program [title=title:][program_num=program_num:]st=stream[:st=stream...] (_output_)
    

Creates a program with the specified title, program_num and adds the specified
stream(s) to it.

-stream_group [map=input_file_id=stream_group][type=type:]st=stream[:st=stream][:stg=stream_group][:id=stream_group_id...] (_output_)
    

Creates a stream group of the specified type and stream_group_id, or by
mapping an input group, adding the specified stream(s) and/or previously
defined stream_group(s) to it.

type can be one of the following:

iamf_audio_element

    

Groups streams that belong to the same IAMF Audio Element

For this group type, the following options are available

audio_element_type

    

The Audio Element type. The following values are supported:

channel

    

Scalable channel audio representation

scene

    

Ambisonics representation

demixing

    

Demixing information used to reconstruct a scalable channel audio
representation. This option must be separated from the rest with a ',', and
takes the following key=value options

parameter_id

    

An identifier parameters blocks in frames may refer to

dmixp_mode

    

A pre-defined combination of demixing parameters

recon_gain

    

Recon gain information used to reconstruct a scalable channel audio
representation. This option must be separated from the rest with a ',', and
takes the following key=value options

parameter_id

    

An identifier parameters blocks in frames may refer to

layer

    

A layer defining a Channel Layout in the Audio Element. This option must be
separated from the rest with a ','. Several ',' separated entries can be
defined, and at least one must be set.

It takes the following ":"-separated key=value options

ch_layout

    

The layer's channel layout

flags

    

The following flags are available:

recon_gain

    

Wether to signal if recon_gain is present as metadata in parameter blocks
within frames

output_gain

output_gain_flags

    

Which channels output_gain applies to. The following flags are available:

FL

FR

BL

BR

TFL

TFR

ambisonics_mode

    

The ambisonics mode. This has no effect if audio_element_type is set to
channel.

The following values are supported:

mono

    

Each ambisonics channel is coded as an individual mono stream in the group

default_w

    

Default weight value

iamf_mix_presentation

    

Groups streams that belong to all IAMF Audio Element the same IAMF Mix
Presentation references

For this group type, the following options are available

submix

    

A sub-mix within the Mix Presentation. This option must be separated from the
rest with a ','. Several ',' separated entries can be defined, and at least
one must be set.

It takes the following ":"-separated key=value options

parameter_id

    

An identifier parameters blocks in frames may refer to, for post-processing
the mixed audio signal to generate the audio signal for playback

parameter_rate

    

The sample rate duration fields in parameters blocks in frames that refer to
this parameter_id are expressed as

default_mix_gain

    

Default mix gain value to apply when there are no parameter blocks sharing the
same parameter_id for a given frame

element

    

References an Audio Element used in this Mix Presentation to generate the
final output audio signal for playback. This option must be separated from the
rest with a '|'. Several '|' separated entries can be defined, and at least
one must be set.

It takes the following ":"-separated key=value options:

stg

    

The stream_group_id for an Audio Element which this sub-mix refers to

parameter_id

    

An identifier parameters blocks in frames may refer to, for applying any
processing to the referenced and rendered Audio Element before being summed
with other processed Audio Elements

parameter_rate

    

The sample rate duration fields in parameters blocks in frames that refer to
this parameter_id are expressed as

default_mix_gain

    

Default mix gain value to apply when there are no parameter blocks sharing the
same parameter_id for a given frame

annotations

    

A key=value string describing the sub-mix element where "key" is a string
conforming to BCP-47 that specifies the language for the "value" string. "key"
must be the same as the one in the mix's annotations

headphones_rendering_mode

    

Indicates whether the input channel-based Audio Element is rendered to stereo
loudspeakers or spatialized with a binaural renderer when played back on
headphones. This has no effect if the referenced Audio Element's
audio_element_type is set to channel.

The following values are supported:

stereo

binaural

layout

    

Specifies the layouts for this sub-mix on which the loudness information was
measured. This option must be separated from the rest with a '|'. Several '|'
separated entries can be defined, and at least one must be set.

It takes the following ":"-separated key=value options:

layout_type

    

loudspeakers

    

The layout follows the loudspeaker sound system convention of ITU-2051-3.

binaural

    

The layout is binaural.

sound_system

    

Channel layout matching one of Sound Systems A to J of ITU-2051-3, plus 7.1.2
and 3.1.2 This has no effect if layout_type is set to binaural.

integrated_loudness

    

The program integrated loudness information, as defined in ITU-1770-4.

digital_peak

    

The digital (sampled) peak value of the audio signal, as defined in
ITU-1770-4.

true_peak

    

The true peak of the audio signal, as defined in ITU-1770-4.

dialog_anchored_loudness

    

The Dialogue loudness information, as defined in ITU-1770-4.

album_anchored_loudness

    

The Album loudness information, as defined in ITU-1770-4.

annotations

    

A key=value string string describing the mix where "key" is a string
conforming to BCP-47 that specifies the language for the "value" string. "key"
must be the same as the ones in all sub-mix element's annotationss

E.g. to create an scalable 5.1 IAMF file from several WAV input files

    
    
    ffmpeg -i front.wav -i back.wav -i center.wav -i lfe.wav
    -map 0:0 -map 1:0 -map 2:0 -map 3:0 -c:a opus
    -stream_group type=iamf_audio_element:id=1:st=0:st=1:st=2:st=3,
    demixing=parameter_id=998,
    recon_gain=parameter_id=101,
    layer=ch_layout=stereo,
    layer=ch_layout=5.1(side),
    -stream_group type=iamf_mix_presentation:id=2:stg=0:annotations=en-us=Mix_Presentation,
    submix=parameter_id=100:parameter_rate=48000|element=stg=0:parameter_id=100:annotations=en-us=Scalable_Submix|layout=sound_system=stereo|layout=sound_system=5.1(side)
    -streamid 0:0 -streamid 1:1 -streamid 2:2 -streamid 3:3 output.iamf
    

To copy the two stream groups (Audio Element and Mix Presentation) from an
input IAMF file with four streams into an mp4 output

    
    
    ffmpeg -i input.iamf -c:a copy -stream_group map=0=0:st=0:st=1:st=2:st=3 -stream_group map=0=1:stg=0
    -streamid 0:0 -streamid 1:1 -streamid 2:2 -streamid 3:3 output.mp4
    

-target type (_output_)
    

Specify target file type (`vcd`, `svcd`, `dvd`, `dv`, `dv50`). type may be
prefixed with `pal-`, `ntsc-` or `film-` to use the corresponding standard.
All the format options (bitrate, codecs, buffer sizes) are then set
automatically. You can just type:

    
    
    ffmpeg -i myfile.avi -target vcd /tmp/vcd.mpg
    

Nevertheless you can specify additional options as long as you know they do
not conflict with the standard, as in:

    
    
    ffmpeg -i myfile.avi -target vcd -bf 2 /tmp/vcd.mpg
    

The parameters set for each target are as follows.

**VCD**

    
    
    pal:
    -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
    -s 352x288 -r 25
    -codec:v mpeg1video -g 15 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
    -ar 44100 -ac 2
    -codec:a mp2 -b:a 224k
    
    ntsc:
    -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
    -s 352x240 -r 30000/1001
    -codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
    -ar 44100 -ac 2
    -codec:a mp2 -b:a 224k
    
    film:
    -f vcd -muxrate 1411200 -muxpreload 0.44 -packetsize 2324
    -s 352x240 -r 24000/1001
    -codec:v mpeg1video -g 18 -b:v 1150k -maxrate:v 1150k -minrate:v 1150k -bufsize:v 327680
    -ar 44100 -ac 2
    -codec:a mp2 -b:a 224k
    

**SVCD**

    
    
    pal:
    -f svcd -packetsize 2324
    -s 480x576 -pix_fmt yuv420p -r 25
    -codec:v mpeg2video -g 15 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
    -ar 44100
    -codec:a mp2 -b:a 224k
    
    ntsc:
    -f svcd -packetsize 2324
    -s 480x480 -pix_fmt yuv420p -r 30000/1001
    -codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
    -ar 44100
    -codec:a mp2 -b:a 224k
    
    film:
    -f svcd -packetsize 2324
    -s 480x480 -pix_fmt yuv420p -r 24000/1001
    -codec:v mpeg2video -g 18 -b:v 2040k -maxrate:v 2516k -minrate:v 0 -bufsize:v 1835008 -scan_offset 1
    -ar 44100
    -codec:a mp2 -b:a 224k
    

**DVD**

    
    
    pal:
    -f dvd -muxrate 10080k -packetsize 2048
    -s 720x576 -pix_fmt yuv420p -r 25
    -codec:v mpeg2video -g 15 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
    -ar 48000
    -codec:a ac3 -b:a 448k
    
    ntsc:
    -f dvd -muxrate 10080k -packetsize 2048
    -s 720x480 -pix_fmt yuv420p -r 30000/1001
    -codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
    -ar 48000
    -codec:a ac3 -b:a 448k
    
    film:
    -f dvd -muxrate 10080k -packetsize 2048
    -s 720x480 -pix_fmt yuv420p -r 24000/1001
    -codec:v mpeg2video -g 18 -b:v 6000k -maxrate:v 9000k -minrate:v 0 -bufsize:v 1835008
    -ar 48000
    -codec:a ac3 -b:a 448k
    

**DV**

    
    
    pal:
    -f dv
    -s 720x576 -pix_fmt yuv420p -r 25
    -ar 48000 -ac 2
    
    ntsc:
    -f dv
    -s 720x480 -pix_fmt yuv411p -r 30000/1001
    -ar 48000 -ac 2
    
    film:
    -f dv
    -s 720x480 -pix_fmt yuv411p -r 24000/1001
    -ar 48000 -ac 2
    

The `dv50` target is identical to the `dv` target except that the pixel format
set is `yuv422p` for all three standards.

Any user-set value for a parameter above will override the target preset
value. In that case, the output may not comply with the target standard.

-dn (_input/output_)
    

As an input option, blocks all data streams of a file from being filtered or
being automatically selected or mapped for any output. See `-discard` option
to disable streams individually.

As an output option, disables data recording i.e. automatic selection or
mapping of any data stream. For full manual control see the `-map` option.

-dframes number (_output_)
    

Set the number of data frames to output. This is an obsolete alias for
`-frames:d`, which you should use instead.

-frames[:stream_specifier] framecount (_output,per-stream_)
    

Stop writing to the stream after framecount frames.

-q[:stream_specifier] q (_output,per-stream_)
-qscale[:stream_specifier] q (_output,per-stream_)
    

Use fixed quality scale (VBR). The meaning of q/qscale is codec-dependent. If
qscale is used without a stream_specifier then it applies only to the video
stream, this is to maintain compatibility with previous behavior and as
specifying the same codec specific value to 2 different codecs that is audio
and video generally is not what is intended when no stream_specifier is used.

-filter[:stream_specifier] filtergraph (_output,per-stream_)
    

Create the filtergraph specified by filtergraph and use it to filter the
stream.

filtergraph is a description of the filtergraph to apply to the stream, and
must have a single input and a single output of the same type of the stream.
In the filtergraph, the input is associated to the label `in`, and the output
to the label `out`. See the ffmpeg-filters manual for more information about
the filtergraph syntax.

See the -filter_complex option if you want to create filtergraphs with
multiple inputs and/or outputs.

-reinit_filter[:stream_specifier] integer (_input,per-stream_)
    

This boolean option determines if the filtergraph(s) to which this stream is
fed gets reinitialized when input frame parameters change mid-stream. This
option is enabled by default as most video and all audio filters cannot handle
deviation in input frame properties. Upon reinitialization, existing filter
state is lost, like e.g. the frame count `n` reference available in some
filters. Any frames buffered at time of reinitialization are lost. The
properties where a change triggers reinitialization are, for video, frame
resolution or pixel format; for audio, sample format, sample rate, channel
count or channel layout.

-drop_changed[:stream_specifier] integer (_input,per-stream_)
    

This boolean option determines whether a frame with differing frame parameters
mid-stream gets dropped instead of leading to filtergraph reinitialization, as
that would lead to loss of filter state. Generally useful to avoid corrupted
yet decodable packets in live streaming inputs. Default is false.

-filter_threads nb_threads (_global_)
    

Defines how many threads are used to process a filter pipeline. Each pipeline
will produce a thread pool with this many threads available for parallel
processing. The default is the number of available CPUs.

-pre[:stream_specifier] preset_name (_output,per-stream_)
    

Specify the preset for matching stream(s).

-stats (_global_)
    

Log encoding progress/statistics as "info"-level log (see `-loglevel`). It is
on by default, to explicitly disable it you need to specify `-nostats`.

-stats_period time (_global_)
    

Set period at which encoding progress/statistics are updated. Default is 0.5
seconds.

-print_graphs (_global_)
    

Prints execution graph details to stderr in the format set via
-print_graphs_format.

-print_graphs_file filename (_global_)
    

Writes execution graph details to the specified file in the format set via
-print_graphs_format.

-print_graphs_format format (_global_)
    

Sets the output format (available formats are: default, compact, csv, flat,
ini, json, xml, mermaid, mermaidhtml) The default format is json.

-progress url (_global_)
    

Send program-friendly progress information to url.

Progress information is written periodically and at the end of the encoding
process. It is made of "key=value" lines. key consists of only alphanumeric
characters. The last key of a sequence of progress information is always
"progress" with the value "continue" or "end".

The update period is set using `-stats_period`.

For example, log progress information to stdout:

    
    
    ffmpeg -progress pipe:1 -i in.mkv out.mkv
    

-stdin
    

Enable interaction on standard input. On by default unless standard input is
used as an input. To explicitly disable interaction you need to specify
`-nostdin`.

Disabling interaction on standard input is useful, for example, if ffmpeg is
in the background process group. Roughly the same result can be achieved with
`ffmpeg ... < /dev/null` but it requires a shell.

-debug_ts (_global_)
    

Print timestamp/latency information. It is off by default. This option is
mostly useful for testing and debugging purposes, and the output format may
change from one version to another, so it should not be employed by portable
scripts.

See also the option `-fdebug ts`.

-attach filename (_output_)
    

Add an attachment to the output file. This is supported by a few formats like
Matroska for e.g. fonts used in rendering subtitles. Attachments are
implemented as a specific type of stream, so this option will add a new stream
to the file. It is then possible to use per-stream options on this stream in
the usual way. Attachment streams created with this option will be created
after all the other streams (i.e. those created with `-map` or automatic
mappings).

Note that for Matroska you also have to set the mimetype metadata tag:

    
    
    ffmpeg -i INPUT -attach DejaVuSans.ttf -metadata:s:2 mimetype=application/x-truetype-font out.mkv
    

(assuming that the attachment stream will be third in the output file).

-dump_attachment[:stream_specifier] filename (_input,per-stream_)
    

Extract the matching attachment stream into a file named filename. If filename
is empty, then the value of the `filename` metadata tag will be used.

E.g. to extract the first attachment to a file named 'out.ttf':

    
    
    ffmpeg -dump_attachment:t:0 out.ttf -i INPUT
    

To extract all attachments to files determined by the `filename` tag:

    
    
    ffmpeg -dump_attachment:t "" -i INPUT
    

Technical note - attachments are implemented as codec extradata, so this
option can actually be used to extract extradata from any stream, not just
attachments.

### 5.5 Video Options

-vframes number (_output_)
    

Set the number of video frames to output. This is an obsolete alias for
`-frames:v`, which you should use instead.

-r[:stream_specifier] fps (_input/output,per-stream_)
    

Set frame rate (Hz value, fraction or abbreviation).

As an input option, ignore any timestamps stored in the file and instead
generate timestamps assuming constant frame rate fps. This is not the same as
the -framerate option used for some input formats like image2 or v4l2 (it used
to be the same in older versions of FFmpeg). If in doubt use -framerate
instead of the input option -r.

As an output option:

video encoding

    

Duplicate or drop frames right before encoding them to achieve constant output
frame rate fps.

video streamcopy

    

Indicate to the muxer that fps is the stream frame rate. No data is dropped or
duplicated in this case. This may produce invalid files if fps does not match
the actual stream frame rate as determined by packet timestamps. See also the
`setts` bitstream filter.

-fpsmax[:stream_specifier] fps (_output,per-stream_)
    

Set maximum frame rate (Hz value, fraction or abbreviation).

Clamps output frame rate when output framerate is auto-set and is higher than
this value. Useful in batch processing or when input framerate is wrongly
detected as very high. It cannot be set together with `-r`. It is ignored
during streamcopy.

-s[:stream_specifier] size (_input/output,per-stream_)
    

Set frame size.

As an input option, this is a shortcut for the video_size private option,
recognized by some demuxers for which the frame size is either not stored in
the file or is configurable - e.g. raw video or video grabbers.

As an output option, this inserts the `scale` video filter to the _end_ of the
corresponding filtergraph. Please use the `scale` filter directly to insert it
at the beginning or some other place.

The format is 'wxh' (default - same as source).

-aspect[:stream_specifier] aspect (_output,per-stream_)
    

Set the video display aspect ratio specified by aspect.

aspect can be a floating point number string, or a string of the form num:den,
where num and den are the numerator and denominator of the aspect ratio. For
example "4:3", "16:9", "1.3333", and "1.7777" are valid argument values.

If used together with -vcodec copy, it will affect the aspect ratio stored at
container level, but not the aspect ratio stored in encoded frames, if it
exists.

-display_rotation[:stream_specifier] rotation (_input,per-stream_)
    

Set video rotation metadata.

rotation is a decimal number specifying the amount in degree by which the
video should be rotated counter-clockwise before being displayed.

This option overrides the rotation/display transform metadata stored in the
file, if any. When the video is being transcoded (rather than copied) and
`-autorotate` is enabled, the video will be rotated at the filtering stage.
Otherwise, the metadata will be written into the output file if the muxer
supports it.

If the `-display_hflip` and/or `-display_vflip` options are given, they are
applied after the rotation specified by this option.

-display_hflip[:stream_specifier] (_input,per-stream_)
    

Set whether on display the image should be horizontally flipped.

See the `-display_rotation` option for more details.

-display_vflip[:stream_specifier] (_input,per-stream_)
    

Set whether on display the image should be vertically flipped.

See the `-display_rotation` option for more details.

-vn (_input/output_)
    

As an input option, blocks all video streams of a file from being filtered or
being automatically selected or mapped for any output. See `-discard` option
to disable streams individually.

As an output option, disables video recording i.e. automatic selection or
mapping of any video stream. For full manual control see the `-map` option.

-vcodec codec (_output_)
    

Set the video codec. This is an alias for `-codec:v`.

-pass[:stream_specifier] n (_output,per-stream_)
    

Select the pass number (1 or 2). It is used to do two-pass video encoding. The
statistics of the video are recorded in the first pass into a log file (see
also the option -passlogfile), and in the second pass that log file is used to
generate the video at the exact requested bitrate. On pass 1, you may just
deactivate audio and set output to null, examples for Windows and Unix:

    
    
    ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y NUL
    ffmpeg -i foo.mov -c:v libxvid -pass 1 -an -f rawvideo -y /dev/null
    

-passlogfile[:stream_specifier] prefix (_output,per-stream_)
    

Set two-pass log file name prefix to prefix, the default file name prefix is
"ffmpeg2pass". The complete file name will be PREFIX-N.log, where N is a
number specific to the output stream

-vf filtergraph (_output_)
    

Create the filtergraph specified by filtergraph and use it to filter the
stream.

This is an alias for `-filter:v`, see the -filter option.

-autorotate
    

Automatically rotate the video according to file metadata. Enabled by default,
use -noautorotate to disable it.

-autoscale
    

Automatically scale the video according to the resolution of first frame.
Enabled by default, use -noautoscale to disable it. When autoscale is
disabled, all output frames of filter graph might not be in the same
resolution and may be inadequate for some encoder/muxer. Therefore, it is not
recommended to disable it unless you really know what you are doing. Disable
autoscale at your own risk.

### 5.6 Advanced Video options

-pix_fmt[:stream_specifier] format (_input/output,per-stream_)
    

Set pixel format. Use `-pix_fmts` to show all the supported pixel formats. If
the selected pixel format can not be selected, ffmpeg will print a warning and
select the best pixel format supported by the encoder. If pix_fmt is prefixed
by a `+`, ffmpeg will exit with an error if the requested pixel format can not
be selected, and automatic conversions inside filtergraphs are disabled. If
pix_fmt is a single `+`, ffmpeg selects the same pixel format as the input (or
graph output) and automatic conversions are disabled.

-sws_flags flags (_input/output_)
    

Set default flags for the libswscale library. These flags are used by
automatically inserted `scale` filters and those within simple filtergraphs,
if not overridden within the filtergraph definition.

See the [(ffmpeg-scaler)ffmpeg-scaler manual](ffmpeg-
scaler.html#scaler_005foptions) for a list of scaler options.

-rc_override[:stream_specifier] override (_output,per-stream_)
    

Rate control override for specific intervals, formatted as "int,int,int" list
separated with slashes. Two first values are the beginning and end frame
numbers, last one is quantizer to use if positive, or quality factor if
negative.

-vstats
    

Dump video coding statistics to vstats_HHMMSS.log. See the vstats file format
section for the format description.

-vstats_file file
    

Dump video coding statistics to file. See the vstats file format section for
the format description.

-vstats_version file
    

Specify which version of the vstats format to use. Default is `2`. See the
vstats file format section for the format description.

-vtag fourcc/tag (_output_)
    

Force video tag/fourcc. This is an alias for `-tag:v`.

-force_key_frames[:stream_specifier] time[,time...] (_output,per-stream_)
-force_key_frames[:stream_specifier] expr:expr (_output,per-stream_)
-force_key_frames[:stream_specifier] source (_output,per-stream_)
    

force_key_frames can take arguments of the following form:

time[,time...]

    

If the argument consists of timestamps, ffmpeg will round the specified times
to the nearest output timestamp as per the encoder time base and force a
keyframe at the first frame having timestamp equal or greater than the
computed timestamp. Note that if the encoder time base is too coarse, then the
keyframes may be forced on frames with timestamps lower than the specified
time. The default encoder time base is the inverse of the output framerate but
may be set otherwise via `-enc_time_base`.

If one of the times is "`chapters`[delta]", it is expanded into the time of
the beginning of all chapters in the file, shifted by delta, expressed as a
time in seconds. This option can be useful to ensure that a seek point is
present at a chapter mark or any other designated place in the output file.

For example, to insert a key frame at 5 minutes, plus key frames 0.1 second
before the beginning of every chapter:

    
    
    -force_key_frames 0:05:00,chapters-0.1
    

expr:expr

    

If the argument is prefixed with `expr:`, the string expr is interpreted like
an expression and is evaluated for each frame. A key frame is forced in case
the evaluation is non-zero.

The expression in expr can contain the following constants:

n

    

the number of current processed frame, starting from 0

n_forced

    

the number of forced frames

prev_forced_n

    

the number of the previous forced frame, it is `NAN` when no keyframe was
forced yet

prev_forced_t

    

the time of the previous forced frame, it is `NAN` when no keyframe was forced
yet

t

    

the time of the current processed frame

For example to force a key frame every 5 seconds, you can specify:

    
    
    -force_key_frames expr:gte(t,n_forced*5)
    

To force a key frame 5 seconds after the time of the last forced one, starting
from second 13:

    
    
    -force_key_frames expr:if(isnan(prev_forced_t),gte(t,13),gte(t,prev_forced_t+5))
    

source

    

If the argument is `source`, ffmpeg will force a key frame if the current
frame being encoded is marked as a key frame in its source. In cases where
this particular source frame has to be dropped, enforce the next available
frame to become a key frame instead.

Note that forcing too many keyframes is very harmful for the lookahead
algorithms of certain encoders: using fixed-GOP options or similar would be
more efficient.

-apply_cropping[:stream_specifier] source (_input,per-stream_)
    

Automatically crop the video after decoding according to file metadata.
Default is _all_.

none (0)

    

Don't apply any cropping metadata.

all (1)

    

Apply both codec and container level croppping. This is the default mode.

codec (2)

    

Apply codec level croppping.

container (3)

    

Apply container level croppping.

-copyinkf[:stream_specifier] (_output,per-stream_)
    

When doing stream copy, copy also non-key frames found at the beginning.

-init_hw_device type[=name][:device[,key=value...]]
    

Initialise a new hardware device of type type called name, using the given
device parameters. If no name is specified it will receive a default name of
the form "type%d".

The meaning of device and the following arguments depends on the device type:

cuda

    

device is the number of the CUDA device.

The following options are recognized:

primary_ctx

    

If set to 1, uses the primary device context instead of creating a new one.

Examples:

_-init_hw_device cuda:1_

    

Choose the second device on the system.

_-init_hw_device cuda:0,primary_ctx=1_

    

Choose the first device and use the primary device context.

dxva2

    

device is the number of the Direct3D 9 display adapter.

d3d11va

    

device is the number of the Direct3D 11 display adapter. If not specified, it
will attempt to use the default Direct3D 11 display adapter or the first
Direct3D 11 display adapter whose hardware VendorId is specified by
'vendor_id'.

Examples:

_-init_hw_device d3d11va_

    

Create a d3d11va device on the default Direct3D 11 display adapter.

_-init_hw_device d3d11va:1_

    

Create a d3d11va device on the Direct3D 11 display adapter specified by index
1.

_-init_hw_device d3d11va:,vendor_id=0x8086_

    

Create a d3d11va device on the first Direct3D 11 display adapter whose
hardware VendorId is 0x8086.

vaapi

    

device is either an X11 display name, a DRM render node or a DirectX adapter
index. If not specified, it will attempt to open the default X11 display
(_$DISPLAY_) and then the first DRM render node (_/dev/dri/renderD128_), or
the default DirectX adapter on Windows.

The following options are recognized:

kernel_driver

    

When device is not specified, use this option to specify the name of the
kernel driver associated with the desired device. This option is available
only when the hardware acceleration method _drm_ and _vaapi_ are enabled.

vendor_id

    

When device and kernel_driver are not specified, use this option to specify
the vendor id associated with the desired device. This option is available
only when the hardware acceleration method _drm_ and _vaapi_ are enabled and
_kernel_driver_ is not specified.

Examples:

_-init_hw_device vaapi_

    

Create a vaapi device on the default device.

_-init_hw_device vaapi:/dev/dri/renderD129_

    

Create a vaapi device on DRM render node /dev/dri/renderD129.

_-init_hw_device vaapi:1_

    

Create a vaapi device on DirectX adapter 1.

_-init_hw_device vaapi:,kernel_driver=i915_

    

Create a vaapi device on a device associated with kernel driver 'i915'.

_-init_hw_device vaapi:,vendor_id=0x8086_

    

Create a vaapi device on a device associated with vendor id '0x8086'.

vdpau

    

device is an X11 display name. If not specified, it will attempt to open the
default X11 display (_$DISPLAY_).

qsv

    

device selects a value in 'MFX_IMPL_*'. Allowed values are:

auto

sw

hw

auto_any

hw_any

hw2

hw3

hw4

If not specified, 'auto_any' is used. (Note that it may be easier to achieve
the desired result for QSV by creating the platform-appropriate subdevice
('dxva2' or 'd3d11va' or 'vaapi') and then deriving a QSV device from that.)

The following options are recognized:

child_device

    

Specify a DRM render node on Linux or DirectX adapter on Windows.

child_device_type

    

Choose platform-appropriate subdevice type. On Windows 'd3d11va' is used as
default subdevice type when `--enable-libvpl` is specified at configuration
time, 'dxva2' is used as default subdevice type when `--enable-libmfx` is
specified at configuration time. On Linux user can use 'vaapi' only as
subdevice type.

Examples:

_-init_hw_device qsv:hw,child_device=/dev/dri/renderD129_

    

Create a QSV device with 'MFX_IMPL_HARDWARE' on DRM render node
/dev/dri/renderD129.

_-init_hw_device qsv:hw,child_device=1_

    

Create a QSV device with 'MFX_IMPL_HARDWARE' on DirectX adapter 1.

_-init_hw_device qsv:hw,child_device_type=d3d11va_

    

Choose the GPU subdevice with type 'd3d11va' and create QSV device with
'MFX_IMPL_HARDWARE'.

_-init_hw_device qsv:hw,child_device_type=dxva2_

    

Choose the GPU subdevice with type 'dxva2' and create QSV device with
'MFX_IMPL_HARDWARE'.

_-init_hw_device qsv:hw,child_device=1,child_device_type=d3d11va_

    

Create a QSV device with 'MFX_IMPL_HARDWARE' on DirectX adapter 1 with
subdevice type 'd3d11va'.

_-init_hw_device vaapi=va:/dev/dri/renderD129 -init_hw_device qsv=hw1@ va_

    

Create a VAAPI device called 'va' on /dev/dri/renderD129, then derive a QSV
device called 'hw1' from device 'va'.

opencl

    

device selects the platform and device as _platform_index.device_index_.

The set of devices can also be filtered using the key-value pairs to find only
devices matching particular platform or device strings.

The strings usable as filters are:

platform_profile

platform_version

platform_name

platform_vendor

platform_extensions

device_name

device_vendor

driver_version

device_version

device_profile

device_extensions

device_type

The indices and filters must together uniquely select a device.

Examples:

_-init_hw_device opencl:0.1_

    

Choose the second device on the first platform.

_-init_hw_device opencl:,device_name=Foo9000_

    

Choose the device with a name containing the string _Foo9000_.

_-init_hw_device opencl:1,device_type=gpu,device_extensions=cl_khr_fp16_

    

Choose the GPU device on the second platform supporting the _cl_khr_fp16_
extension.

vulkan

    

If device is an integer, it selects the device by its index in a system-
dependent list of devices. If device is any other string, it selects the first
device with a name containing that string as a substring.

The following options are recognized:

debug

    

If set to 1, enables the validation layer, if installed.

linear_images

    

If set to 1, images allocated by the hwcontext will be linear and locally
mappable.

instance_extensions

    

A plus separated list of additional instance extensions to enable.

device_extensions

    

A plus separated list of additional device extensions to enable.

Examples:

_-init_hw_device vulkan:1_

    

Choose the second device on the system.

_-init_hw_device vulkan:RADV_

    

Choose the first device with a name containing the string _RADV_.

_-init_hw_device
vulkan:0,instance_extensions=VK_KHR_wayland_surface+VK_KHR_xcb_surface_

    

Choose the first device and enable the Wayland and XCB instance extensions.

-init_hw_device type[=name]@source
    

Initialise a new hardware device of type type called name, deriving it from
the existing device with the name source.

-init_hw_device list
    

List all hardware device types supported in this build of ffmpeg.

-filter_hw_device name
    

Pass the hardware device called name to all filters in any filter graph. This
can be used to set the device to upload to with the `hwupload` filter, or the
device to map to with the `hwmap` filter. Other filters may also make use of
this parameter when they require a hardware device. Note that this is
typically only required when the input is not already in hardware frames -
when it is, filters will derive the device they require from the context of
the frames they receive as input.

This is a global setting, so all filters will receive the same device.

-hwaccel[:stream_specifier] hwaccel (_input,per-stream_)
    

Use hardware acceleration to decode the matching stream(s). The allowed values
of hwaccel are:

none

    

Do not use any hardware acceleration (the default).

auto

    

Automatically select the hardware acceleration method.

vdpau

    

Use VDPAU (Video Decode and Presentation API for Unix) hardware acceleration.

dxva2

    

Use DXVA2 (DirectX Video Acceleration) hardware acceleration.

d3d11va

    

Use D3D11VA (DirectX Video Acceleration) hardware acceleration.

vaapi

    

Use VAAPI (Video Acceleration API) hardware acceleration.

qsv

    

Use the Intel QuickSync Video acceleration for video transcoding.

Unlike most other values, this option does not enable accelerated decoding
(that is used automatically whenever a qsv decoder is selected), but
accelerated transcoding, without copying the frames into the system memory.

For it to work, both the decoder and the encoder must support QSV acceleration
and no filters must be used.

videotoolbox

    

Use Video Toolbox hardware acceleration.

This option has no effect if the selected hwaccel is not available or not
supported by the chosen decoder.

Note that most acceleration methods are intended for playback and will not be
faster than software decoding on modern CPUs. Additionally, `ffmpeg` will
usually need to copy the decoded frames from the GPU memory into the system
memory, resulting in further performance loss. This option is thus mainly
useful for testing.

-hwaccel_device[:stream_specifier] hwaccel_device (_input,per-stream_)
    

Select a device to use for hardware acceleration.

This option only makes sense when the -hwaccel option is also specified. It
can either refer to an existing device created with -init_hw_device by name,
or it can create a new device as if '-init_hw_device' type:hwaccel_device were
called immediately before.

-hwaccels
    

List all hardware acceleration components enabled in this build of ffmpeg.
Actual runtime availability depends on the hardware and its suitable driver
being installed.

-fix_sub_duration_heartbeat[:stream_specifier]
    

Set a specific output video stream as the heartbeat stream according to which
to split and push through currently in-progress subtitle upon receipt of a
random access packet.

This lowers the latency of subtitles for which the end packet or the following
subtitle has not yet been received. As a drawback, this will most likely lead
to duplication of subtitle events in order to cover the full duration, so when
dealing with use cases where latency of when the subtitle event is passed on
to output is not relevant this option should not be utilized.

Requires -fix_sub_duration to be set for the relevant input subtitle stream
for this to have any effect, as well as for the input subtitle stream having
to be directly mapped to the same output in which the heartbeat stream
resides.

### 5.7 Audio Options

-aframes number (_output_)
    

Set the number of audio frames to output. This is an obsolete alias for
`-frames:a`, which you should use instead.

-ar[:stream_specifier] freq (_input/output,per-stream_)
    

Set the audio sampling frequency. For output streams it is set by default to
the frequency of the corresponding input stream. For input streams this option
only makes sense for audio grabbing devices and raw demuxers and is mapped to
the corresponding demuxer options.

-aq q (_output_)
    

Set the audio quality (codec-specific, VBR). This is an alias for -q:a.

-ac[:stream_specifier] channels (_input/output,per-stream_)
    

Set the number of audio channels. For output streams it is set by default to
the number of input audio channels. For input streams this option only makes
sense for audio grabbing devices and raw demuxers and is mapped to the
corresponding demuxer options.

-an (_input/output_)
    

As an input option, blocks all audio streams of a file from being filtered or
being automatically selected or mapped for any output. See `-discard` option
to disable streams individually.

As an output option, disables audio recording i.e. automatic selection or
mapping of any audio stream. For full manual control see the `-map` option.

-acodec codec (_input/output_)
    

Set the audio codec. This is an alias for `-codec:a`.

-sample_fmt[:stream_specifier] sample_fmt (_output,per-stream_)
    

Set the audio sample format. Use `-sample_fmts` to get a list of supported
sample formats.

-af filtergraph (_output_)
    

Create the filtergraph specified by filtergraph and use it to filter the
stream.

This is an alias for `-filter:a`, see the -filter option.

### 5.8 Advanced Audio options

-atag fourcc/tag (_output_)
    

Force audio tag/fourcc. This is an alias for `-tag:a`.

-ch_layout[:stream_specifier] layout (_input/output,per-stream_)
    

Alias for `-channel_layout`.

-channel_layout[:stream_specifier] layout (_input/output,per-stream_)
    

Set the audio channel layout. For output streams it is set by default to the
input channel layout. For input streams it overrides the channel layout of the
input. Not all decoders respect the overridden channel layout. This option
also sets the channel layout for audio grabbing devices and raw demuxers and
is mapped to the corresponding demuxer option.

-guess_layout_max channels (_input,per-stream_)
    

If some input channel layout is not known, try to guess only if it corresponds
to at most the specified number of channels. For example, 2 tells to `ffmpeg`
to recognize 1 channel as mono and 2 channels as stereo but not 6 channels as
5.1. The default is to always try to guess. Use 0 to disable all guessing.
Using the `-channel_layout` option to explicitly specify an input layout also
disables guessing.

### 5.9 Subtitle options

-scodec codec (_input/output_)
    

Set the subtitle codec. This is an alias for `-codec:s`.

-sn (_input/output_)
    

As an input option, blocks all subtitle streams of a file from being filtered
or being automatically selected or mapped for any output. See `-discard`
option to disable streams individually.

As an output option, disables subtitle recording i.e. automatic selection or
mapping of any subtitle stream. For full manual control see the `-map` option.

### 5.10 Advanced Subtitle options

-fix_sub_duration
    

Fix subtitles durations. For each subtitle, wait for the next packet in the
same stream and adjust the duration of the first to avoid overlap. This is
necessary with some subtitles codecs, especially DVB subtitles, because the
duration in the original packet is only a rough estimate and the end is
actually marked by an empty subtitle frame. Failing to use this option when
necessary can result in exaggerated durations or muxing failures due to non-
monotonic timestamps.

Note that this option will delay the output of all data until the next
subtitle packet is decoded: it may increase memory consumption and latency a
lot.

-canvas_size size
    

Set the size of the canvas used to render subtitles.

### 5.11 Advanced options

-map [-]input_file_id[:stream_specifier][:view_specifier][:?] | [linklabel] (_output_)
    

Create one or more streams in the output file. This option has two forms for
specifying the data source(s): the first selects one or more streams from some
input file (specified with `-i`), the second takes an output from some complex
filtergraph (specified with `-filter_complex`).

In the first form, an output stream is created for every stream from the input
file with the index input_file_id. If stream_specifier is given, only those
streams that match the specifier are used (see the Stream specifiers section
for the stream_specifier syntax).

A `-` character before the stream identifier creates a "negative" mapping. It
disables matching streams from already created mappings.

An optional view_specifier may be given after the stream specifier, which for
multiview video specifies the view to be used. The view specifier may have one
of the following formats:

view:view_id

    

select a view by its ID; view_id may be set to 'all' to use all the views
interleaved into one stream;

vidx:view_idx

    

select a view by its index; i.e. 0 is the base view, 1 is the first non-base
view, etc.

vpos:position

    

select a view by its display position; position may be `left` or `right`

The default for transcoding is to only use the base view, i.e. the equivalent
of `vidx:0`. For streamcopy, view specifiers are not supported and all views
are always copied.

A trailing `?` after the stream index will allow the map to be optional: if
the map matches no streams the map will be ignored instead of failing. Note
the map will still fail if an invalid input file index is used; such as if the
map refers to a non-existent input.

An alternative [linklabel] form will map outputs from complex filter graphs
(see the -filter_complex option) to the output file. linklabel must correspond
to a defined output link label in the graph.

This option may be specified multiple times, each adding more streams to the
output file. Any given input stream may also be mapped any number of times as
a source for different output streams, e.g. in order to use different encoding
options and/or filters. The streams are created in the output in the same
order in which the `-map` options are given on the commandline.

Using this option disables the default mappings for this output file.

Examples:

_map everything_

    

To map ALL streams from the first input file to output

    
    
    ffmpeg -i INPUT -map 0 output
    

_select specific stream_

    

If you have two audio streams in the first input file, these streams are
identified by 0:0 and 0:1. You can use `-map` to select which streams to place
in an output file. For example:

    
    
    ffmpeg -i INPUT -map 0:1 out.wav
    

will map the second input stream in INPUT to the (single) output stream in
out.wav.

_create multiple streams_

    

To select the stream with index 2 from input file a.mov (specified by the
identifier 0:2), and stream with index 6 from input b.mov (specified by the
identifier 1:6), and copy them to the output file out.mov:

    
    
    ffmpeg -i a.mov -i b.mov -c copy -map 0:2 -map 1:6 out.mov
    

_create multiple streams 2_

    

To select all video and the third audio stream from an input file:

    
    
    ffmpeg -i INPUT -map 0:v -map 0:a:2 OUTPUT
    

_negative map_

    

To map all the streams except the second audio, use negative mappings

    
    
    ffmpeg -i INPUT -map 0 -map -0:a:1 OUTPUT
    

_optional map_

    

To map the video and audio streams from the first input, and using the
trailing `?`, ignore the audio mapping if no audio streams exist in the first
input:

    
    
    ffmpeg -i INPUT -map 0:v -map 0:a? OUTPUT
    

_map by language_

    

To pick the English audio stream:

    
    
    ffmpeg -i INPUT -map 0:m:language:eng OUTPUT
    

-ignore_unknown
    

Ignore input streams with unknown type instead of failing if copying such
streams is attempted.

-copy_unknown
    

Allow input streams with unknown type to be copied instead of failing if
copying such streams is attempted.

-map_metadata[:metadata_spec_out] infile[:metadata_spec_in] (_output,per-metadata_)
    

Set metadata information of the next output file from infile. Note that those
are file indices (zero-based), not filenames. Optional metadata_spec_in/out
parameters specify, which metadata to copy. A metadata specifier can have the
following forms:

g

    

global metadata, i.e. metadata that applies to the whole file

s[:stream_spec]

    

per-stream metadata. stream_spec is a stream specifier as described in the
Stream specifiers chapter. In an input metadata specifier, the first matching
stream is copied from. In an output metadata specifier, all matching streams
are copied to.

c:chapter_index

    

per-chapter metadata. chapter_index is the zero-based chapter index.

p:program_index

    

per-program metadata. program_index is the zero-based program index.

If metadata specifier is omitted, it defaults to global.

By default, global metadata is copied from the first input file, per-stream
and per-chapter metadata is copied along with streams/chapters. These default
mappings are disabled by creating any mapping of the relevant type. A negative
file index can be used to create a dummy mapping that just disables automatic
copying.

For example to copy metadata from the first stream of the input file to global
metadata of the output file:

    
    
    ffmpeg -i in.ogg -map_metadata 0:s:0 out.mp3
    

To do the reverse, i.e. copy global metadata to all audio streams:

    
    
    ffmpeg -i in.mkv -map_metadata:s:a 0:g out.mkv
    

Note that simple `0` would work as well in this example, since global metadata
is assumed by default.

-map_chapters input_file_index (_output_)
    

Copy chapters from input file with index input_file_index to the next output
file. If no chapter mapping is specified, then chapters are copied from the
first input file with at least one chapter. Use a negative file index to
disable any chapter copying.

-benchmark (_global_)
    

Show benchmarking information at the end of an encode. Shows real, system and
user time used and maximum memory consumption. Maximum memory consumption is
not supported on all systems, it will usually display as 0 if not supported.

-benchmark_all (_global_)
    

Show benchmarking information during the encode. Shows real, system and user
time used in various steps (audio/video encode/decode).

-timelimit duration (_global_)
    

Exit after ffmpeg has been running for duration seconds in CPU user time.

-dump (_global_)
    

Dump each input packet to stderr.

-hex (_global_)
    

When dumping packets, also dump the payload.

-readrate speed (_input_)
    

Limit input read speed.

Its value is a floating-point positive number which represents the maximum
duration of media, in seconds, that should be ingested in one second of
wallclock time. Default value is zero and represents no imposed limitation on
speed of ingestion. Value `1` represents real-time speed and is equivalent to
`-re`.

Mainly used to simulate a capture device or live input stream (e.g. when
reading from a file). Should not be used with a low value when input is an
actual capture device or live stream as it may cause packet loss.

It is useful for when flow speed of output packets is important, such as live
streaming.

-re (_input_)
    

Read input at native frame rate. This is equivalent to setting `-readrate 1`.

-readrate_initial_burst seconds
    

Set an initial read burst time, in seconds, after which -re/-readrate will be
enforced.

-readrate_catchup speed (_input_)
    

If either the input or output is blocked leading to actual read speed falling
behind the specified readrate, then this rate takes effect till the input
catches up with the specified readrate. Must not be lower than the primary
readrate.

-vsync parameter (_global_)
-fps_mode[:stream_specifier] parameter (_output,per-stream_)
    

Set video sync method / framerate mode. vsync is applied to all output video
streams but can be overridden for a stream by setting fps_mode. vsync is
deprecated and will be removed in the future.

For compatibility reasons some of the values for vsync can be specified as
numbers (shown in parentheses in the following table).

passthrough (0)

    

Each frame is passed with its timestamp from the demuxer to the muxer.

cfr (1)

    

Frames will be duplicated and dropped to achieve exactly the requested
constant frame rate.

vfr (2)

    

Frames are passed through with their timestamp or dropped so as to prevent 2
frames from having the same timestamp.

auto (-1)

    

Chooses between cfr and vfr depending on muxer capabilities. This is the
default method.

Note that the timestamps may be further modified by the muxer, after this. For
example, in the case that the format option avoid_negative_ts is enabled.

With -map you can select from which stream the timestamps should be taken. You
can leave either video or audio unchanged and sync the remaining stream(s) to
the unchanged one.

-frame_drop_threshold parameter
    

Frame drop threshold, which specifies how much behind video frames can be
before they are dropped. In frame rate units, so 1.0 is one frame. The default
is -1.1. One possible usecase is to avoid framedrops in case of noisy
timestamps or to increase frame drop precision in case of exact timestamps.

-apad parameters (_output,per-stream_)
    

Pad the output audio stream(s). This is the same as applying `-af apad`.
Argument is a string of filter parameters composed the same as with the `apad`
filter. `-shortest` must be set for this output for the option to take effect.

-copyts
    

Do not process input timestamps, but keep their values without trying to
sanitize them. In particular, do not remove the initial start time offset
value.

Note that, depending on the vsync option or on specific muxer processing (e.g.
in case the format option avoid_negative_ts is enabled) the output timestamps
may mismatch with the input timestamps even when this option is selected.

-start_at_zero
    

When used with copyts, shift input timestamps so they start at zero.

This means that using e.g. `-ss 50` will make output timestamps start at 50
seconds, regardless of what timestamp the input file started at.

-copytb mode
    

Specify how to set the encoder timebase when stream copying. mode is an
integer numeric value, and can assume one of the following values:

1

    

Use the demuxer timebase.

The time base is copied to the output encoder from the corresponding input
demuxer. This is sometimes required to avoid non monotonically increasing
timestamps when copying video streams with variable frame rate.

0

    

Use the decoder timebase.

The time base is copied to the output encoder from the corresponding input
decoder.

-1
    

Try to make the choice automatically, in order to generate a sane output.

Default value is -1.

-enc_time_base[:stream_specifier] timebase (_output,per-stream_)
    

Set the encoder timebase. timebase can assume one of the following values:

0

    

Assign a default value according to the media type.

For video - use 1/framerate, for audio - use 1/samplerate.

demux

    

Use the timebase from the demuxer.

filter

    

Use the timebase from the filtergraph.

a positive number

    

Use the provided number as the timebase.

This field can be provided as a ratio of two integers (e.g. 1:24, 1:48000) or
as a decimal number (e.g. 0.04166, 2.0833e-5)

Default value is 0.

-bitexact (_input/output_)
    

Enable bitexact mode for (de)muxer and (de/en)coder

-shortest (_output_)
    

Finish encoding when the shortest output stream ends.

Note that this option may require buffering frames, which introduces extra
latency. The maximum amount of this latency may be controlled with the
`-shortest_buf_duration` option.

-shortest_buf_duration duration (_output_)
    

The `-shortest` option may require buffering potentially large amounts of data
when at least one of the streams is "sparse" (i.e. has large gaps between
frames â this is typically the case for subtitles).

This option controls the maximum duration of buffered frames in seconds.
Larger values may allow the `-shortest` option to produce more accurate
results, but increase memory use and latency.

The default value is 10 seconds.

-dts_delta_threshold threshold
    

Timestamp discontinuity delta threshold, expressed as a decimal number of
seconds.

The timestamp discontinuity correction enabled by this option is only applied
to input formats accepting timestamp discontinuity (for which the
`AVFMT_TS_DISCONT` flag is enabled), e.g. MPEG-TS and HLS, and is
automatically disabled when employing the `-copyts` option (unless wrapping is
detected).

If a timestamp discontinuity is detected whose absolute value is greater than
threshold, ffmpeg will remove the discontinuity by decreasing/increasing the
current DTS and PTS by the corresponding delta value.

The default value is 10.

-dts_error_threshold threshold
    

Timestamp error delta threshold, expressed as a decimal number of seconds.

The timestamp correction enabled by this option is only applied to input
formats not accepting timestamp discontinuity (for which the
`AVFMT_TS_DISCONT` flag is not enabled).

If a timestamp discontinuity is detected whose absolute value is greater than
threshold, ffmpeg will drop the PTS/DTS timestamp value.

The default value is `3600*30` (30 hours), which is arbitrarily picked and
quite conservative.

-muxdelay seconds (_output_)
    

Set the maximum demux-decode delay.

-muxpreload seconds (_output_)
    

Set the initial demux-decode delay.

-streamid output-stream-index:new-value (_output_)
    

Assign a new stream-id value to an output stream. This option should be
specified prior to the output filename to which it applies. For the situation
where multiple output files exist, a streamid may be reassigned to a different
value.

For example, to set the stream 0 PID to 33 and the stream 1 PID to 36 for an
output mpegts file:

    
    
    ffmpeg -i inurl -streamid 0:33 -streamid 1:36 out.ts
    

-bsf[:stream_specifier] bitstream_filters (_input/output,per-stream_)
    

Apply bitstream filters to matching streams. The filters are applied to each
packet as it is received from the demuxer (when used as an input option) or
before it is sent to the muxer (when used as an output option).

bitstream_filters is a comma-separated list of bitstream filter
specifications, each of the form

    
    
    filter[=optname0=optval0:optname1=optval1:...]
    

Any of the ',=:' characters that are to be a part of an option value need to
be escaped with a backslash.

Use the `-bsfs` option to get the list of bitstream filters.

E.g.

    
    
    ffmpeg -bsf:v h264_mp4toannexb -i h264.mp4 -c:v copy -an out.h264
    

applies the `h264_mp4toannexb` bitstream filter (which converts
MP4-encapsulated H.264 stream to Annex B) to the _input_ video stream.

On the other hand,

    
    
    ffmpeg -i file.mov -an -vn -bsf:s mov2textsub -c:s copy -f rawvideo sub.txt
    

applies the `mov2textsub` bitstream filter (which extracts text from MOV
subtitles) to the _output_ subtitle stream. Note, however, that since both
examples use `-c copy`, it matters little whether the filters are applied on
input or output - that would change if transcoding was happening.

-tag[:stream_specifier] codec_tag (_input/output,per-stream_)
    

Force a tag/fourcc for matching streams.

-timecode hh:mm:ssSEPff
    

Specify Timecode for writing. SEP is ':' for non drop timecode and ';' (or
'.') for drop.

    
    
    ffmpeg -i input.mpg -timecode 01:02:03.04 -r 30000/1001 -s ntsc output.mpg
    

-filter_complex filtergraph (_global_)
    

Define a complex filtergraph, i.e. one with arbitrary number of inputs and/or
outputs. For simple graphs - those with one input and one output of the same
type - see the -filter options. filtergraph is a description of the
filtergraph, as described in the "Filtergraph syntax" section of the ffmpeg-
filters manual. This option may be specified multiple times - each use creates
a new complex filtergraph.

Inputs to a complex filtergraph may come from different source types,
distinguished by the format of the corresponding link label:

  * To connect an input stream, use `[file_index:stream_specifier]` (i.e. the same syntax as -map). If stream_specifier matches multiple streams, the first one will be used. For multiview video, the stream specifier may be followed by the view specifier, see documentation for the -map option for its syntax. 
  * To connect a loopback decoder use [dec:dec_idx], where dec_idx is the index of the loopback decoder to be connected to given input. For multiview video, the decoder index may be followed by the view specifier, see documentation for the -map option for its syntax. 
  * To connect an output from another complex filtergraph, use its link label. E.g the following example: 
        
        ffmpeg -i input.mkv \
          -filter_complex '[0:v]scale=size=hd1080,split=outputs=2[for_enc][orig_scaled]' \
          -c:v libx264 -map '[for_enc]' output.mkv \
          -dec 0:0 \
          -filter_complex '[dec:0][orig_scaled]hstack[stacked]' \
          -map '[stacked]' -c:v ffv1 comparison.mkv
        

reads an input video and

    * (line 2) uses a complex filtergraph with one input and two outputs to scale the video to 1920x1080 and duplicate the result to both outputs; 
    * (line 3) encodes one scaled output with `libx264` and writes the result to output.mkv; 
    * (line 4) decodes this encoded stream with a loopback decoder; 
    * (line 5) places the output of the loopback decoder (i.e. the `libx264`-encoded video) side by side with the scaled original input; 
    * (line 6) combined video is then losslessly encoded and written into comparison.mkv. 

Note that the two filtergraphs cannot be combined into one, because then there
would be a cycle in the transcoding pipeline (filtergraph output goes to
encoding, from there to decoding, then back to the same graph), and such
cycles are not allowed.

An unlabeled input will be connected to the first unused input stream of the
matching type.

Output link labels are referred to with -map. Unlabeled outputs are added to
the first output file.

Note that with this option it is possible to use only lavfi sources without
normal input files.

For example, to overlay an image over video

    
    
    ffmpeg -i video.mkv -i image.png -filter_complex '[0:v][1:v]overlay[out]' -map
    '[out]' out.mkv
    

Here `[0:v]` refers to the first video stream in the first input file, which
is linked to the first (main) input of the overlay filter. Similarly the first
video stream in the second input is linked to the second (overlay) input of
overlay.

Assuming there is only one video stream in each input file, we can omit input
labels, so the above is equivalent to

    
    
    ffmpeg -i video.mkv -i image.png -filter_complex 'overlay[out]' -map
    '[out]' out.mkv
    

Furthermore we can omit the output label and the single output from the filter
graph will be added to the output file automatically, so we can simply write

    
    
    ffmpeg -i video.mkv -i image.png -filter_complex 'overlay' out.mkv
    

As a special exception, you can use a bitmap subtitle stream as input: it will
be converted into a video with the same size as the largest video in the file,
or 720x576 if no video is present. Note that this is an experimental and
temporary solution. It will be removed once libavfilter has proper support for
subtitles.

For example, to hardcode subtitles on top of a DVB-T recording stored in MPEG-
TS format, delaying the subtitles by 1 second:

    
    
    ffmpeg -i input.ts -filter_complex \
      '[#0x2ef] setpts=PTS+1/TB [sub] ; [#0x2d0] [sub] overlay' \
      -sn -map '#0x2dc' output.mkv
    

(0x2d0, 0x2dc and 0x2ef are the MPEG-TS PIDs of respectively the video, audio
and subtitles streams; 0:0, 0:3 and 0:7 would have worked too)

To generate 5 seconds of pure red video using lavfi `color` source:

    
    
    ffmpeg -filter_complex 'color=c=red' -t 5 out.mkv
    

-filter_complex_threads nb_threads (_global_)
    

Defines how many threads are used to process a filter_complex graph. Similar
to filter_threads but used for `-filter_complex` graphs only. The default is
the number of available CPUs.

-lavfi filtergraph (_global_)
    

Define a complex filtergraph, i.e. one with arbitrary number of inputs and/or
outputs. Equivalent to -filter_complex.

-accurate_seek (_input_)
    

This option enables or disables accurate seeking in input files with the -ss
option. It is enabled by default, so seeking is accurate when transcoding. Use
-noaccurate_seek to disable it, which may be useful e.g. when copying some
streams and transcoding the others.

-seek_timestamp (_input_)
    

This option enables or disables seeking by timestamp in input files with the
-ss option. It is disabled by default. If enabled, the argument to the -ss
option is considered an actual timestamp, and is not offset by the start time
of the file. This matters only for files which do not start from timestamp 0,
such as transport streams.

-thread_queue_size size (_input/output_)
    

For input, this option sets the maximum number of queued packets when reading
from the file or device. With low latency / high rate live streams, packets
may be discarded if they are not read in a timely manner; setting this value
can force ffmpeg to use a separate input thread and read packets as soon as
they arrive. By default ffmpeg only does this if multiple inputs are
specified.

For output, this option specified the maximum number of packets that may be
queued to each muxing thread.

-sdp_file file (_global_)
    

Print sdp information for an output stream to file. This allows dumping sdp
information when at least one output isn't an rtp stream. (Requires at least
one of the output formats to be rtp).

-discard (_input_)
    

Allows discarding specific streams or frames from streams. Any input stream
can be fully discarded, using value `all` whereas selective discarding of
frames from a stream occurs at the demuxer and is not supported by all
demuxers.

none

    

Discard no frame.

default

    

Default, which discards no frames.

noref

    

Discard all non-reference frames.

bidir

    

Discard all bidirectional frames.

nokey

    

Discard all frames excepts keyframes.

all

    

Discard all frames.

-abort_on flags (_global_)
    

Stop and abort on various conditions. The following flags are available:

empty_output

    

No packets were passed to the muxer, the output is empty.

empty_output_stream

    

No packets were passed to the muxer in some of the output streams.

-max_error_rate (_global_)
    

Set fraction of decoding frame failures across all inputs which when crossed
ffmpeg will return exit code 69. Crossing this threshold does not terminate
processing. Range is a floating-point number between 0 to 1. Default is 2/3.

-xerror (_global_)
    

Stop and exit on error

-max_muxing_queue_size packets (_output,per-stream_)
    

When transcoding audio and/or video streams, ffmpeg will not begin writing
into the output until it has one packet for each such stream. While waiting
for that to happen, packets for other streams are buffered. This option sets
the size of this buffer, in packets, for the matching output stream.

The default value of this option should be high enough for most uses, so only
touch this option if you are sure that you need it.

-muxing_queue_data_threshold bytes (_output,per-stream_)
    

This is a minimum threshold until which the muxing queue size is not taken
into account. Defaults to 50 megabytes per stream, and is based on the overall
size of packets passed to the muxer.

-auto_conversion_filters (_global_)
    

Enable automatically inserting format conversion filters in all filter graphs,
including those defined by -vf, -af, -filter_complex and -lavfi. If filter
format negotiation requires a conversion, the initialization of the filters
will fail. Conversions can still be performed by inserting the relevant
conversion filter (scale, aresample) in the graph. On by default, to
explicitly disable it you need to specify `-noauto_conversion_filters`.

-bits_per_raw_sample[:stream_specifier] value (_output,per-stream_)
    

Declare the number of bits per raw sample in the given output stream to be
value. Note that this option sets the information provided to the
encoder/muxer, it does not change the stream to conform to this value. Setting
values that do not match the stream properties may result in encoding failures
or invalid output files.

-stats_enc_pre[:stream_specifier] path (_output,per-stream_)
-stats_enc_post[:stream_specifier] path (_output,per-stream_)
-stats_mux_pre[:stream_specifier] path (_output,per-stream_)
    

Write per-frame encoding information about the matching streams into the file
given by path.

-stats_enc_pre writes information about raw video or audio frames right before they are sent for encoding, while -stats_enc_post writes information about encoded packets as they are received from the encoder. -stats_mux_pre writes information about packets just as they are about to be sent to the muxer. Every frame or packet produces one line in the specified file. The format of this line is controlled by -stats_enc_pre_fmt / -stats_enc_post_fmt / -stats_mux_pre_fmt. 

When stats for multiple streams are written into a single file, the lines
corresponding to different streams will be interleaved. The precise order of
this interleaving is not specified and not guaranteed to remain stable between
different invocations of the program, even with the same options.

-stats_enc_pre_fmt[:stream_specifier] format_spec (_output,per-stream_)
-stats_enc_post_fmt[:stream_specifier] format_spec (_output,per-stream_)
-stats_mux_pre_fmt[:stream_specifier] format_spec (_output,per-stream_)
    

Specify the format for the lines written with -stats_enc_pre / -stats_enc_post
/ -stats_mux_pre.

format_spec is a string that may contain directives of the form {fmt}.
format_spec is backslash-escaped -- use \\{, \\}, and \\\ to write a literal
{, }, or \, respectively, into the output.

The directives given with fmt may be one of the following:

fidx

    

Index of the output file.

sidx

    

Index of the output stream in the file.

n

    

Frame number. Pre-encoding: number of frames sent to the encoder so far. Post-
encoding: number of packets received from the encoder so far. Muxing: number
of packets submitted to the muxer for this stream so far.

ni

    

Input frame number. Index of the input frame (i.e. output by a decoder) that
corresponds to this output frame or packet. -1 if unavailable.

tb

    

Timebase in which this frame/packet's timestamps are expressed, as a rational
number num/den. Note that encoder and muxer may use different timebases.

tbi

    

Timebase for ptsi, as a rational number num/den. Available when ptsi is
available, 0/1 otherwise.

pts

    

Presentation timestamp of the frame or packet, as an integer. Should be
multiplied by the timebase to compute presentation time.

ptsi

    

Presentation timestamp of the input frame (see ni), as an integer. Should be
multiplied by tbi to compute presentation time. Printed as (2^63 - 1 =
9223372036854775807) when not available.

t

    

Presentation time of the frame or packet, as a decimal number. Equal to pts
multiplied by tb.

ti

    

Presentation time of the input frame (see ni), as a decimal number. Equal to
ptsi multiplied by tbi. Printed as inf when not available.

dts (_packet_)

    

Decoding timestamp of the packet, as an integer. Should be multiplied by the
timebase to compute presentation time.

dt (_packet_)

    

Decoding time of the frame or packet, as a decimal number. Equal to dts
multiplied by tb.

sn (_frame,audio_)

    

Number of audio samples sent to the encoder so far.

samp (_frame,audio_)

    

Number of audio samples in the frame.

size (_packet_)

    

Size of the encoded packet in bytes.

br (_packet_)

    

Current bitrate in bits per second.

abr (_packet_)

    

Average bitrate for the whole stream so far, in bits per second, -1 if it
cannot be determined at this point.

key (_packet_)

    

Character 'K' if the packet contains a keyframe, character 'N' otherwise.

Directives tagged with _packet_ may only be used with -stats_enc_post_fmt and
-stats_mux_pre_fmt.

Directives tagged with _frame_ may only be used with -stats_enc_pre_fmt.

Directives tagged with _audio_ may only be used with audio streams.

The default format strings are:

pre-encoding

    

{fidx} {sidx} {n} {t}

post-encoding

    

{fidx} {sidx} {n} {t}

In the future, new items may be added to the end of the default formatting
strings. Users who depend on the format staying exactly the same, should
prescribe it manually.

Note that stats for different streams written into the same file may have
different formats.

### 5.12 Preset files

A preset file contains a sequence of option=value pairs, one for each line,
specifying a sequence of options which would be awkward to specify on the
command line. Lines starting with the hash ('#') character are ignored and are
used to provide comments. Check the presets directory in the FFmpeg source
tree for examples.

There are two types of preset files: ffpreset and avpreset files.

#### 5.12.1 ffpreset files

ffpreset files are specified with the `vpre`, `apre`, `spre`, and `fpre`
options. The `fpre` option takes the filename of the preset instead of a
preset name as input and can be used for any kind of codec. For the `vpre`,
`apre`, and `spre` options, the options specified in a preset file are applied
to the currently selected codec of the same type as the preset option.

The argument passed to the `vpre`, `apre`, and `spre` preset options
identifies the preset file to use according to the following rules:

First ffmpeg searches for a file named arg.ffpreset in the directories
$FFMPEG_DATADIR (if set), and $HOME/.ffmpeg, and in the datadir defined at
configuration time (usually PREFIX/share/ffmpeg) or in a ffpresets folder
along the executable on win32, in that order. For example, if the argument is
`libvpx-1080p`, it will search for the file libvpx-1080p.ffpreset.

If no such file is found, then ffmpeg will search for a file named codec_name-
arg.ffpreset in the above-mentioned directories, where codec_name is the name
of the codec to which the preset file options will be applied. For example, if
you select the video codec with `-vcodec libvpx` and use `-vpre 1080p`, then
it will search for the file libvpx-1080p.ffpreset.

#### 5.12.2 avpreset files

avpreset files are specified with the `pre` option. They work similar to
ffpreset files, but they only allow encoder- specific options. Therefore, an
option=value pair specifying an encoder cannot be used.

When the `pre` option is specified, ffmpeg will look for files with the suffix
.avpreset in the directories $AVCONV_DATADIR (if set), and $HOME/.avconv, and
in the datadir defined at configuration time (usually PREFIX/share/ffmpeg), in
that order.

First ffmpeg searches for a file named codec_name-arg.avpreset in the above-
mentioned directories, where codec_name is the name of the codec to which the
preset file options will be applied. For example, if you select the video
codec with `-vcodec libvpx` and use `-pre 1080p`, then it will search for the
file libvpx-1080p.avpreset.

If no such file is found, then ffmpeg will search for a file named
arg.avpreset in the same directories.

### 5.13 vstats file format

The `-vstats` and `-vstats_file` options enable generation of a file
containing statistics about the generated video outputs.

The `-vstats_version` option controls the format version of the generated
file.

With version `1` the format is:

    
    
    frame= FRAME q= FRAME_QUALITY PSNR= PSNR f_size= FRAME_SIZE s_size= STREAM_SIZEkB time= TIMESTAMP br= BITRATEkbits/s avg_br= AVERAGE_BITRATEkbits/s
    

With version `2` the format is:

    
    
    out= OUT_FILE_INDEX st= OUT_FILE_STREAM_INDEX frame= FRAME_NUMBER q= FRAME_QUALITYf PSNR= PSNR f_size= FRAME_SIZE s_size= STREAM_SIZEkB time= TIMESTAMP br= BITRATEkbits/s avg_br= AVERAGE_BITRATEkbits/s
    

The value corresponding to each key is described below:

avg_br

    

average bitrate expressed in Kbits/s

br

    

bitrate expressed in Kbits/s

frame

    

number of encoded frame

out

    

out file index

PSNR

    

Peak Signal to Noise Ratio

q

    

quality of the frame

f_size

    

encoded packet size expressed as number of bytes

s_size

    

stream size expressed in KiB

st

    

out file stream index

time

    

time of the packet

type

    

picture type

See also the -stats_enc options for an alternative way to show encoding
statistics.

## 6 Examples

### 6.1 Video and Audio grabbing

If you specify the input format and device then ffmpeg can grab video and
audio directly.

    
    
    ffmpeg -f oss -i /dev/dsp -f video4linux2 -i /dev/video0 /tmp/out.mpg
    

Or with an ALSA audio source (mono input, card id 1) instead of OSS:

    
    
    ffmpeg -f alsa -ac 1 -i hw:1 -f video4linux2 -i /dev/video0 /tmp/out.mpg
    

Note that you must activate the right video source and channel before
launching ffmpeg with any TV viewer such as
[xawtv](http://linux.bytesex.org/xawtv/) by Gerd Knorr. You also have to set
the audio recording levels correctly with a standard mixer.

### 6.2 X11 grabbing

Grab the X11 display with ffmpeg via

    
    
    ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0 /tmp/out.mpg
    

0.0 is display.screen number of your X11 server, same as the DISPLAY
environment variable.

    
    
    ffmpeg -f x11grab -video_size cif -framerate 25 -i :0.0+10,20 /tmp/out.mpg
    

0.0 is display.screen number of your X11 server, same as the DISPLAY
environment variable. 10 is the x-offset and 20 the y-offset for the grabbing.

### 6.3 Video and Audio file format conversion

Any supported file format and protocol can serve as input to ffmpeg:

Examples:

  * You can use YUV files as input: 
        
        ffmpeg -i /tmp/test%d.Y /tmp/out.mpg
        

It will use the files:

        
        /tmp/test0.Y, /tmp/test0.U, /tmp/test0.V,
        /tmp/test1.Y, /tmp/test1.U, /tmp/test1.V, etc...
        

The Y files use twice the resolution of the U and V files. They are raw files,
without header. They can be generated by all decent video decoders. You must
specify the size of the image with the -s option if ffmpeg cannot guess it.

  * You can input from a raw YUV420P file: 
        
        ffmpeg -i /tmp/test.yuv /tmp/out.avi
        

test.yuv is a file containing raw YUV planar data. Each frame is composed of
the Y plane followed by the U and V planes at half vertical and horizontal
resolution.

  * You can output to a raw YUV420P file: 
        
        ffmpeg -i mydivx.avi hugefile.yuv
        

  * You can set several input files and output files: 
        
        ffmpeg -i /tmp/a.wav -s 640x480 -i /tmp/a.yuv /tmp/a.mpg
        

Converts the audio file a.wav and the raw YUV video file a.yuv to MPEG file
a.mpg.

  * You can also do audio and video conversions at the same time: 
        
        ffmpeg -i /tmp/a.wav -ar 22050 /tmp/a.mp2
        

Converts a.wav to MPEG audio at 22050 Hz sample rate.

  * You can encode to several formats at the same time and define a mapping from input stream to output streams: 
        
        ffmpeg -i /tmp/a.wav -map 0:a -b:a 64k /tmp/a.mp2 -map 0:a -b:a 128k /tmp/b.mp2
        

Converts a.wav to a.mp2 at 64 kbits and to b.mp2 at 128 kbits. '-map
file:index' specifies which input stream is used for each output stream, in
the order of the definition of output streams.

  * You can transcode decrypted VOBs: 
        
        ffmpeg -i snatch_1.vob -f avi -c:v mpeg4 -b:v 800k -g 300 -bf 2 -c:a libmp3lame -b:a 128k snatch.avi
        

This is a typical DVD ripping example; the input is a VOB file, the output an
AVI file with MPEG-4 video and MP3 audio. Note that in this command we use
B-frames so the MPEG-4 stream is DivX5 compatible, and GOP size is 300 which
means one intra frame every 10 seconds for 29.97fps input video. Furthermore,
the audio stream is MP3-encoded so you need to enable LAME support by passing
`--enable-libmp3lame` to configure. The mapping is particularly useful for DVD
transcoding to get the desired audio language.

NOTE: To see the supported input formats, use `ffmpeg -demuxers`.

  * You can extract images from a video, or create a video from many images: 

For extracting images from a video:

        
        ffmpeg -i foo.avi -r 1 -s WxH -f image2 foo-%03d.jpeg
        

This will extract one video frame per second from the video and will output
them in files named foo-001.jpeg, foo-002.jpeg, etc. Images will be rescaled
to fit the new WxH values.

If you want to extract just a limited number of frames, you can use the above
command in combination with the `-frames:v` or `-t` option, or in combination
with -ss to start extracting from a certain point in time.

For creating a video from many images:

        
        ffmpeg -f image2 -framerate 12 -i foo-%03d.jpeg -s WxH foo.avi
        

The syntax `foo-%03d.jpeg` specifies to use a decimal number composed of three
digits padded with zeroes to express the sequence number. It is the same
syntax supported by the C printf function, but only formats accepting a normal
integer are suitable.

When importing an image sequence, -i also supports expanding shell-like
wildcard patterns (globbing) internally, by selecting the image2-specific
`-pattern_type glob` option.

For example, for creating a video from filenames matching the glob pattern
`foo-*.jpeg`:

        
        ffmpeg -f image2 -pattern_type glob -framerate 12 -i 'foo-*.jpeg' -s WxH foo.avi
        

  * You can put many streams of the same type in the output: 
        
        ffmpeg -i test1.avi -i test2.avi -map 1:1 -map 1:0 -map 0:1 -map 0:0 -c copy -y test12.nut
        

The resulting output file test12.nut will contain the first four streams from
the input files in reverse order.

  * To force CBR video output: 
        
        ffmpeg -i myfile.avi -b 4000k -minrate 4000k -maxrate 4000k -bufsize 1835k out.m2v
        

  * The four options lmin, lmax, mblmin and mblmax use 'lambda' units, but you may use the QP2LAMBDA constant to easily convert from 'q' units: 
        
        ffmpeg -i src.ext -lmax 21*QP2LAMBDA dst.ext
        

## 7 See Also

[ffmpeg-all](ffmpeg-all.html), [ffplay](ffplay.html), [ffprobe](ffprobe.html),
[ffmpeg-utils](ffmpeg-utils.html), [ffmpeg-scaler](ffmpeg-scaler.html),
[ffmpeg-resampler](ffmpeg-resampler.html), [ffmpeg-codecs](ffmpeg-
codecs.html), [ffmpeg-bitstream-filters](ffmpeg-bitstream-filters.html),
[ffmpeg-formats](ffmpeg-formats.html), [ffmpeg-devices](ffmpeg-devices.html),
[ffmpeg-protocols](ffmpeg-protocols.html), [ffmpeg-filters](ffmpeg-
filters.html)

## 8 Authors

The FFmpeg developers.

For details about the authorship, see the Git history of the project
(https://git.ffmpeg.org/ffmpeg), e.g. by typing the command `git log` in the
FFmpeg source directory, or browsing the online repository at
<https://git.ffmpeg.org/ffmpeg>.

Maintainers for the specific components are listed in the file MAINTAINERS in
the source code tree.

This document was generated on _May 21, 2025_ using
[_makeinfo_](http://www.gnu.org/software/texinfo/).

Hosting provided by [telepoint.bg](https://telepoint.bg)

