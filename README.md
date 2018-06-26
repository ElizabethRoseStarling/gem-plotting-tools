# gem-plotting-tools

Branch|[Travis CI](https://travis-ci.org)|[Coveralls](https://www.coveralls.io)|[Codecov](https://www.codecov.io)|[Codacy](https://www.codacy.com)|[Landscape](https://www.landscape.io)|[CodeClimate](https://www.codeclimate.com)
---|---|---|---|---|---|---
master|[![Build Status](https://travis-ci.org/cms-gem-daq-project/gem-plotting-tools.svg?branch=master)](https://travis-ci.org/cms-gem-daq-project/gem-plotting-tools)|[![Coveralls Status](https://coveralls.io/repos/github/cms-gem-daq-project/gem-plotting-tools/badge.svg?branch=master)](https://coveralls.io/github/cms-gem-daq-project/gem-plotting-tools?branch=master)|[![codecov](https://codecov.io/gh/cms-gem-daq-project/gem-plotting-tools/branch/master/graph/badge.svg)](https://codecov.io/gh/cms-gem-daq-project/gem-plotting-tools)|[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b81a9dc9270248b6b66155511369bec5)](https://www.codacy.com/app/cms-gem-daq-project/gem-plotting-tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cms-gem-daq-project/gem-plotting-tools&amp;utm_campaign=Badge_Grade)|[![Landscape Status](https://landscape.io/github/cms-gem-daq-project/gem-plotting-tools/master/landscape.svg)](https://landscape.io/github/cms-gem-daq-project/gem-plotting-tools/master)|[![Code Climate](https://codeclimate.com/github/cms-gem-daq-project/gem-plotting-tools/badges/gpa.svg)](https://codeclimate.com/github/cms-gem-daq-project/gem-plotting-tools)
develop|[![Build Status](https://travis-ci.org/cms-gem-daq-project/gem-plotting-tools.svg?branch=develop)](https://travis-ci.org/cms-gem-daq-project/gem-plotting-tools)|[![Coveralls Status](https://coveralls.io/repos/github/cms-gem-daq-project/gem-plotting-tools/badge.svg?branch=develop)](https://coveralls.io/github/cms-gem-daq-project/gem-plotting-tools?branch=develop)|[![codecov](https://codecov.io/gh/cms-gem-daq-project/gem-plotting-tools/branch/develop/graph/badge.svg)](https://codecov.io/gh/cms-gem-daq-project/gem-plotting-tools)|[![Codacy Badge](https://api.codacy.com/project/badge/Grade/00f0de54bcc94812b553ebeab74e9320)](https://www.codacy.com/app/cms-gem-daq-project/gem-plotting-tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cms-gem-daq-project/gem-plotting-tools&amp;utm_campaign=Badge_Grade)|[![Landscape Status](https://landscape.io/github/cms-gem-daq-project/gem-plotting-tools/develop/landscape.svg)](https://landscape.io/github/cms-gem-daq-project/gem-plotting-tools/develop)|[![Code Climate](https://codeclimate.com/github/cms-gem-daq-project/gem-plotting-tools/badges/issue_count.svg)](https://codeclimate.com/github/cms-gem-daq-project/gem-plotting-tools)


Table of Contents
=================

   * [gem-plotting-tools](#gem-plotting-tools)
      * [Setup](#setup)
        * [Setup at Point 5](#setup-at-point-5)
      * [Masking Channels Algorithmically](#masking-channels-algorithmically)
         * [Definitions](#definitions)
         * [Deriving Channel Configuration](#deriving-channel-configuration)
         * [Providing Cuts for maskReason at Runtime](#providing-cuts-for-maskreason-at-runtime)
      * [List Of Scandate Input Files](#list-of-scandate-input-files)
         * [Two Column Format](#two-column-format)
         * [Three Column Format](#three-column-format)
         * [Automatically Generating Set of listOfScanDates.txt](#automatically-generating-set-of-listofscandatestxt)
      * [Analyzing Scans:](#analyzing-scans)
         * [Analyzing Python Ultra Scan Data](#analyzing-python-ultra-scan-data)
            * [plot_eff.py](#plot_effpy)
            * [plot_eff.py Arguments](#plot_effpy-arguments)
            * [plot_eff.py Example](#plot_effpy-example)
            * [plot_eff.py Input File](#plot_effpy-input-file)
         * [Analyzing xDAQ Scan Data](#analyzing-xdaq-scan-data)
      * [Arbitray Plotting Tools](#arbitray-plotting-tools)
         * [gemPlotter.py](#gemplotterpy)
            * [gemPlotter.py Arguments](#gemplotterpy-arguments)
            * [gemPlotter.py Input File](#gemplotterpy-input-file)
            * [gemPlotter.py Example: Making a time series with plotTimeSeries.py](#gemplotterpy-example-making-a-time-series-with-plottimeseriespy)
            * [gemPlotter.py Example: Making a 1D Plot - Channel Level](#gemplotterpy-example-making-a-1d-plot---channel-level)
            * [gemPlotter.py Example: Making a 1D Plot - VFAT Level](#gemplotterpy-example-making-a-1d-plot---vfat-level)
            * [gemPlotter.py Example: Making a 2D Plot](#gemplotterpy-example-making-a-2d-plot)
         * [gemTreeDrawWrapper.py](#gemtreedrawwrapperpy)
            * [gemTreeDrawWrapper.py Arguments](#gemtreedrawwrapperpy-arguments)
            * [gemTreeDrawWrapper.py Input File](#gemtreedrawwrapperpy-input-file)
            * [gemTreeDrawWrapper.py Example: Making a Plot](#gemtreedrawwrapperpy-example-making-a-plot)
            * [gemTreeDrawWrapper.py Example: Fitting a Plot](#gemtreedrawwrapperpy-example-fitting-a-plot)
      * [Scurve Plotting Tools](#scurve-plotting-tools)
         * [gemSCurveAnaToolkit.py](#gemscurveanatoolkitpy)
            * [gemSCurveAnaToolkit.py Arguments](#gemscurveanatoolkitpy-arguments)
            * [gemSCurveAnaToolkit.py Input File](#gemscurveanatoolkitpy-input-file)
            * [gemSCurveAnaToolkit.py Example: Making a Plot](#gemscurveanatoolkitpy-example-making-a-plot)
         * [Comparing Scurves Results Across Scandates: plotSCurveFitResults.py](#comparing-scurves-results-across-scandates-plotscurvefitresultspy)
            * [plotSCurveFitResults.py Arguments](#plotscurvefitresultspy-arguments)
            * [plotSCurveFitResults.py Input File](#plotscurvefitresultspy-input-file)
            * [plotSCurveFitResults.py Example](#plotscurvefitresultspy-example)
         * [Analyzing the Time Evolution of Channels: timeHistoryAnalyzer.py](#analyzing-the-time-evolution-of-channels-timehistoryanalyzerpy)
            * [timeHistoryAnalyzer.py Arguments](#timehistoryanalyzerpy-arguments)
            * [timeHistoryAnalyzer.py Examples](#timehistoryanalyzerpy-examples)
      * [Packaging Tool: packageFiles4Docker.py](#packaging-tool-packagefiles4dockerpy)
         * [packageFiles4Docker.py Arguments](#packagefiles4dockerpy-arguments)
         * [packageFiles4Docker.py Input Files](#packagefiles4dockerpy-input-files)
         * [packageFiles4Docker.py Example](#packagefiles4dockerpy-example)
      * [Cluster Computing Tools](#cluster-computing-tools)
         * [Cluster Analysis of S-Curve Data: clusterAnaScurve.py](#cluster-analysis-of-s-curve-data-clusteranascurvepy)
            * [clusterAnaScurve.py: Arguments](#clusteranascurvepy-arguments)
            * [Full Example For P5 S-Curve Data](#full-example-for-p5-s-curve-data)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

## Setup

The `$SHELL` variable `$ELOG_PATH` should be defined:

```
export ELOG_PATH=/your/favorite/elog/path
```

Remove and download the setup script to ensure you have the most up-to-date version:

```
rm -f setup_gemdaq.sh
wget https://raw.githubusercontent.com/cms-gem-daq-project/sw_utils/master/scripts/setup_gemdaq.sh
```

Then execute:

```
source setup.sh -c <cmsgemos tag> -g <gem-plotting tag> -G <gem-plotting dev version optional>
```

Tags for each of the repo's can be found:

* [cmsgemos](https://github.com/cms-gem-daq-project/cmsgemos/tags) version X.Y.Z (`-c X.Y.Z`)
* [gemplotting](https://github.com/cms-gem-daq-project/gem-plotting-tools/tags) version X.Y.Z-dev**A** (`-g X.Y.Z -G A`)

Where `X`, `Y`, `Z`, and `A` are integers, and most likely will be different for each of the repositories. If a development version is not to be used (normal case), you can drop the `-G` option. If this is the first time you are executing the above command, it will create a Python `virtualenv` for you and install the `cmsgemos` and `gemplotting` packages. It may take some time to download them, so be patient and do not interrupt the installation.

> **Example**
>
> ```
> source setup_gemdaq.sh -c 0.3.1 -g 1.0.0 -G 5
> ```
>
> This command will install the following packages:
>
> * [cmsgemos](https://github.com/cms-gem-daq-project/cmsgemos/tags) version 0.3.1 (`-c 0.3.1`)
> * [gemplotting](https://github.com/cms-gem-daq-project/gem-plotting-tools/tags) version 1.0.0-dev5 (`-g 1.0.0 -G 5`)

In addition to installing the dependencies, the script will try to guess `$DATA_PATH` based on the machine you are using.

To disable the python env execute:

```
deactivate
```

To re-enable the python env, source the script again:

```
source setup_gemdaq.sh
```

Note that you should always source the setup script from the same directory.

### Setup at Point 5

Due to the limited Internet access, the setup at Point 5 is slightly more involved.

Create a SOCKS proxy that will allow `pip` to reach the outer world:

```
PORT=5000
ssh -D *:$PORT lxplus.cern.ch -N -f
```

If you get an error saying `bind: Address already in use`, try with `PORT=5001`, `5002`, ...

> **Note**
> The proxy expires after some time. Just create it again if `pip` complains about the network being unreachable.

Define `$ELOG_PATH`:

```
export ELOG_PATH=/your/favorite/elog/path
```

Remove and download the setup script to ensure you have the most up-to-date version:

```
rm -f setup_gemdaq.sh
ssh cmsusr wget https://raw.githubusercontent.com/cms-gem-daq-project/sw_utils/master/scripts/setup_gemdaq.sh
```
Then execute:

```
source setup.sh -c <cmsgemos tag> -g <gem-plotting tag> -G <gem-plotting dev version optional> -P $PORT
```

If a development version is not to be used (normal case), you can drop the `-G` option. If this is the first time you are executing the above command, it will create a Python `virtualenv` for you and install the `cmsgemos` and `gemplotting` packages. You will be asked for you `cmsusr` and `lxplus` passwords, possibly several times.

> **Example**
>
> ```
> source setup_gemdaq.sh -c 0.3.1 -g 1.0.0 -G 5 -P $PORT
> ```
>
> This command will install the following packages:
>
> * [cmsgemos](https://github.com/cms-gem-daq-project/cmsgemos/tags) version 0.3.1 (`-c 0.3.1`)
> * [gemplotting](https://github.com/cms-gem-daq-project/gem-plotting-tools/tags) version 1.0.0-dev5 (`-g 1.0.0 -G 5`)

After the script completes, you can use the usual commands to `deactivate` your `virtualenv` and activate it again (see above).

## Masking Channels Algorithmically

### Definitions
When the analysis software decides a channel should be masked it is because it falls under one of the categories defined in the `MaskReason` class of [anaInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/anaInfo.py). Multiple reasons can be assigned to a channel for why it is masked, and the total `maskReason` is a 5-bit binary number. Presently these reasons are:

| Name | Bit | Reason |
| :--: | :---: | :----- |
| `NotMasked` | (none set) | the channel is not masked. |
| `HotChannel` | 0 | the channel was identified as an outlier using the MAD algorithm, see talks by [B. Dorney](https://indico.cern.ch/event/638404/contributions/2643292/attachments/1483873/2302543/BDorney_OpsMtg_20170627.pdf) or [L. Moureaux](https://indico.cern.ch/event/659794/contributions/2691237/attachments/1508531/2351619/UpdateOnHotChannelIdentificationAlgo.pdf). |
| `FitFailed` | 1 | the s-curve fit of the channel failed. |
| `DeadChannel` | 2 | the channel has a burned or disconnected input. |
| `HighNoise` | 3 | the channel has an scurve sigma above the cut value. |
| `HighEffPed` | 4 | the channel has an effective pedestal above the cut value. |

The scurve sigma is the sigma of the modified error function used to fit the s-curve measurements.  It comes from the `TF1` object used to fit scurves in `ScanDataFitter::fit()` of [fitScanData.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/fitting/fitScanData.py).

A channel's effective pedestal is the percent of time a channel's comparator fires when injected charge is zero.  This is determined from an s-curve measurement via:

```
effPed = scurve_fit_func.Eval(0) / n_pulses
```

Where `n_pulses` are the number of charge injections for a given DAC value performed by the calibration module.

The analysis software will record the `maskReason` in decimal reprementation.  So for example a channel having `maskReason = 24` corresponds to `0b11000` which means the channel was assigned the `HighEffPed` and `HighNoise` maskReasons.

### Deriving Channel Configuration
The following procedure is used, note these steps must be executed one after another, without LV power cycle or action to cause a reset of the VFAT settings (e.g. SCA reset):

| Step | Tool v2b (v3) | VFAT Data | Input Config | Generates |
| :--: | :-----------: | :-------: | :----------: | :-------- |
| 1 | `trimChamber.py (trimChamberV3.py)` | Tracking | `VThreshold1 (CFG_THR_ARM_DAC) = 100`, `ztrim=4` | Initial channel configuration `chConfig.txt` and `trimRange` settings. |
| 2 | `confChamber.py` | N/A | `chConfig.txt`, `trimRange` in memory | Nothing |
| 3 | `ultraThreshold.py` | Tracking | Nothing | Generates updated channel config `chConfig_MasksUpdated.txt` and initial VFAT settings storing `VThreshold1` and `trimRange` in `vfatConfig.txt`. |
| 4 | `confChamber.py` | N/A | `chConfig_MasksUpdated.txt` and `vfatConfig.txt` | Nothing |
| 5 | `ultraThreshold.py (sbitThreshScanParallel.py)` | Trigger | Nothing | Generates updated VFAT settings `vfatConfig_Updated.txt` with final `VThreshold1` values. |

Please note that while `DeadChannel` is given in `maskReason` these channels are **never** masked such that they can be tracked overtime.

If a channel was masked at the time of acquisition of a test involving an s-curve measurement (e.g. `trimChamber(V3).py` or `ultraScurve.py`) then it will be assigned the `FitFailed` reason since the original reason is not known without referencing a previous scan.

### Providing Cuts for maskReason at Runtime
When analyzing the above s-curves taken by `trimChamber(V3).py` The following command line arguments are available for specifying the cut values for assigning the `DeadChannel`, `HighNoise`, and `HighEffPed` pedestal.

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--maxEffPedPercent` | float | Value from 0 to 1. Threshold for setting the `HighEffPed` mask reason, if channel `effPed > maxEffPedPercent * nevts` then `HighEffPed` is set. |
| `--highNoiseCut` | float | Threshold for setting the `HighNoise` `maskReason`, if channel `scurve_sigma > highNoiseCut` then `HighNoise` is set. |
| `--deadChanCutLow` | float | If channel `deadChanCutLow < scurve_sigma < deadChanCutHigh` then `DeadChannel` is set, see [Slide 22](https://indico.cern.ch/event/721622/contributions/2968019/attachments/1631961/2602748/BDorney_GEMDAQMtg_20180412_BurnedVFATInputs.pdf) for the origin of the default values in fC. |
| `--deadChanCutHigh` | float | If channel `deadChanCutHigh < scurve_sigma < deadChanCutHigh` then `DeadChannel` is set, , see [Slide 22](https://indico.cern.ch/event/721622/contributions/2968019/attachments/1631961/2602748/BDorney_GEMDAQMtg_20180412_BurnedVFATInputs.pdf) for the origin of the default values in fC. |

## List Of Scandate Input Files
Many of the tools found in the `macros/` directory require a `listOfScanDates.txt` file.  These come in either two or three column versions and the `parseListOfScanDatesFile(...)` of [anautilities.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/anautilities.py) is designed to parse either version and provide the tool with the correct information.  This means that, baring other command line arguments, the two formats are relatively interchangeable.

### Two Column Format
This should be a `tab` deliminited text file.  The first line of this file should be a list of column headers formatted as:

```
ChamberName scandate
```

Subsequent lines of this file are the values that correspond to these column headings.  The value of the `ChamberName` column must correspond to the value of one entry in the `chamber_config` dictionary found in `mapping/chamberInfo.py`.  The next column is for `scandate` values.  Please note the `#` character is  understood as a comment, lines starting with a `#` will be skipped.

A complete example for a single detector is given as:

```
ChamberName scandate
GE11-VI-L-CERN-0001    2017.08.11.16.30
GE11-VI-L-CERN-0001    2017.08.14.20.54
GE11-VI-L-CERN-0001    2017.08.30.15.03
GE11-VI-L-CERN-0001    2017.08.30.21.39
GE11-VI-L-CERN-0001    2017.08.31.08.28
GE11-VI-L-CERN-0001    2017.08.31.15.46
GE11-VI-L-CERN-0001    2017.09.05.11.41
GE11-VI-L-CERN-0001    2017.09.12.14.24
GE11-VI-L-CERN-0001    2017.09.13.16.45
```

### Three Column Format
This should be a `tab` deliminited text file.  The first line of this file should be a list of column headers formatted as:

```
ChamberName scandate    <Indep. Variable Name>
```

Subsequent lines of this file are the values that correspond to these column headings.  The value of the `ChamberName` column must correspond to the value of one entry in the `chamber_config` dictionary found in [mapping/chamberInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/master/mapping/chamberInfo.py).  The **Indep. Variable Name** is the independent variable that `--branchName` will be plotted against, if it is *not* numeric please use the `--alphaLabels` command line option.  Please note the `#` character is  understood as a comment, lines starting with a `#` will be skipped.

A complete example for a single detector is given as:

```
ChamberName scandate    VT_{1}
GE11-VI-L-CERN-0002 2017.09.04.20.12    10
GE11-VI-L-CERN-0002 2017.09.04.22.52    20
GE11-VI-L-CERN-0002 2017.09.05.01.33    30
GE11-VI-L-CERN-0002 2017.09.05.04.21    40
GE11-VI-L-CERN-0002 2017.09.05.07.11    50
```

Here the `ChamberName` is always `GE11-VI-L-CERN-0002` and `--branchName` will be plotted against `VT_{1}` which is the **Indep. Variable Name**.  Note the axis of interest will be assigned the label, with subscripts in this case, of `VT_{1}`.

A complete example for multiple detectors is given as:

```
ChamberName scandate    Layer
GEMINIm27L1 2019.09.04.20.12    GEMINIm27L1
GEMINIm27L2 2019.09.04.22.52    GEMINIm27L2
GEMINIm28L1 2019.09.05.01.33    GEMINIm28L1
GEMINIm28L2 2019.09.05.04.21    GEMINIm28L2
GEMINIp02L1 2019.09.05.07.11    GEMINIp02L1
GEMINIp02L2 2019.09.05.07.11    GEMINIp02L2
```

Here the `ChamberName` is different for each line and `--branchName` will be plotted against `Layer`.  Note since the **Indep. Variable Name** is not numeric the command line option `--alphaLabels` must be used.

### Automatically Generating Set of listOfScanDates.txt
To automatically generate a set of `listOfScanDates.txt` files for all s-curve measurements for each of the chambers defined in `chamber_config.values()` of [chamberInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/mapping/chamberInfo.py) execute:

```
plotTimeSeries.py --listOfScanDatesOnly --startDate=2017.01.01
```

For each detector defined in `chamber_config.values()` the `listOfScanDAtes.txt` file will be found at:

```
$DATA_PATH/<ChamberName>/scurve/
```

If you are interested in generating a set of `listOfScanDates.txt` files for measurements other than scurves supply the `--anaType` argument at the time of execution like:

```
plotTimeSeries.py --listOfScanDatesOnly --startDate=2017.01.01 --anaType=<type>
```

The list of supported `anaType`'s are from `ana_config.keys()` of [anaInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/anaInfo.py).  In this case the `listOfScanDAtes.txt` file for each chamber will be found at:

```
$DATA_PATH/<ChamberName>/<anaType>/
```

## Analyzing Scans:
Analysis is broken down into either analyzing data taken with the python ultra scan tools or with xdaq.

### Analyzing Python Ultra Scan Data
The following tools exist to help you to analyze scans taken with the ultra tools in the [vfatqc-python-scripts](https://github.com/cms-gem-daq-project/vfatqc-python-scripts) repository:

- `ana_scans.py`,
- `anaUltraLatency.py`,
- `anaUltraScurve.py`, and
- `anaUltraThreshold.py`.

See extensive documentation written on the [GEM DOC Twiki Page](https://twiki.cern.ch/twiki/bin/view/CMS/GEMDOCDoc#How_to_Produce_Scan_Plots).

#### plot_eff.py
For some test stands where you have configured the input L1A to pass only through a specific point of a detector you can use the data taken by `ultraLatency.py` to calculate the efficiency of the detector.  To help you perform this analysis the `plot_eff.py` tool has been created.

#### plot_eff.py Arguments
The following table shows the mandatory inputs that must be supplied to execute the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| ` --latSig` | int | Latency bin for which efficiency should be determined from. |
| `-i`, `--infilename` | string | physical filename of the input file to be passed to `plot_eff.py`.  The format of this input file should follow the [Three Column Format](#three-column-format). |
| `-p`, `--print` | none | Prints a comma separated table of the plot's data to the terminal.  The format of this table will be compatible with the `genericPlotter` executable of the [CMS_GEM_Analysis_Framework](https://github.com/cms-gem-detqc-project/CMS_GEM_Analysis_Framework#3b-genericplotter). | 
| `-v`, `--vfat` | int | Specify VFAT to use when calculating the efficiency. |

The following table shows the optional inputs that can be supplied when executing the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| ` --bkgSub` | none | Background subtraction is used to determine the efficiency instead of a single latency bin. May be used instead of the `--latSig` option. |
| `--vfatList` | Comma separated list of int's | List of VFATs to use when calculating the efficiency.  May be used instead of the `--vfat` option. |

Note if the `--bkgSub` option is used then you **must** first call `anaUltraLatency.py` for each of the scandates given in the `--infilename`.

#### plot_eff.py Input File
The format of this input file should follow the [Three Column Format](#three-column-format).

#### plot_eff.py Example
To calculate the efficiency using VFATs 12 & 13 in latency bin 39 for a list of scandates defined in `listOfScanDates.txt` call:

```
plot_eff.py --infilename=listOfScanDates.txt --vfatList=12,13 --latSig=39 --print
```

To calculate the efficiency using VFAT4 using background subtraction first call `anaUltraLatency.py` on each of the scandates given in `listOfScanDates.txt` and then call:

```
plot_eff.py --infilename=listOfScanDates.txt -v4 --bkgSub --print
```

### Analyzing xDAQ Scan Data
The following tools exist to help you to analyze scans taken with xDAQ:

- `anaXDAQLatency.py`

See documentation written on the [GEM DOC Twiki Page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/GEMDOCDoc#How_to_Produce_Scan_Plots_Ta_AN1).

## Arbitray Plotting Tools
There are two tools for helping you to make arbitrary plots from python scan data:

- `gemPlotter.py`
- `gemTreeDrawWrapper.py`

The first tool is for plotting from multiple different scandates. The second tool is for making a given plot from a list of scandates, for each scandate.

### gemPlotter.py
The `gemPlotter.py` tool is for making plots of an observable stored in one of the `TTree` objects produced by the (ana-) ultra scan scripts vs an arbitrary indepdent variable specified by the user.  Here each data point is from a different scandate.  This is useful if you run mulitple scans in which only a single parameter is changed (e.g. applied high voltage, or `VThreshold1`) and you want to track the dependency on this parameter.

Each plot produced will be stored as an output `*.png` file. Additionally an output `TFile` will be produced which will contain each of the plots, stored as `TGraph` objects, and canvases produced.

#### gemPlotter.py Arguments
The following table shows the mandatory inputs that must be supplied to execute the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--anaType` | string | Analysis type to be executed, see `tree_names.keys()` of [anaInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/master/anaInfo.py) for possible inputs |
| `--branchName` | string | Name of TBranch where dependent variable is found, note that this TBranch should be found in the `TTree` that corresponds to the value given to the `--anaType` argument |
| `-i`, `--infilename` | string | physical filename of the input file to be passed to `gemPlotter.py`.  See [Three Column Format](#three-column-format) for details on the format and contents of this file. |
| `-v`, `--vfat` | int | Specify VFAT to plot |

Note for those `anaType` values which have the substring `Ana` in their names it is expected that the user has already run `ana_scans.py` on the corresponding `scandate` to produce the necessary input file for `gemPlotter.py`.

The following table shows the optional inputs that can be supplied when executing the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `-a`, `--all` | none | When providing this flag data from all 24 VFATs will be plotted.  Additionally a summary plot in the typical 3x8 grid will be created showing the results of all 24 VFATs. May be used instead of the `--vfat` option. |
| `--alphaLabels` | none | When providing this flag `gemPlotter.py` will interpret the **Indep. Variable** as a string and modify the output X axis accordingly |
| `--axisMax` | float | Maximum value for the axis depicting `--branchName`. |
| `--axisMin` | float | Minimum value for the axis depicting `--branchName`. |
| `-c`, `--channels` | none | When providing this flag the `--strip` option is interpreted as VFAT channel number instead of readout board (ROB) strip number. |
| `-s`, `--strip` | int | Specific ROB strip number to plot for `--branchName`.  Note for ROB strip level `--branchName` values (e.g. `trimDAC`) if this option is *not* provided the data point (error bar) will represent the mean (standard deviation) of `--branchName` from all strips. |
| `--make2D` | none| When providing this flag a 2D plot of ROB strip/vfat channel vs. independent variable will be plotted whose z-axis value is `--branchName`. |
| `-p`, `--print` | none | Prints a comma separated table of the plot's data to the terminal.  The format of this table will be compatible with the `genericPlotter` executable of the [CMS_GEM_Analysis_Framework](https://github.com/cms-gem-detqc-project/CMS_GEM_Analysis_Framework#3b-genericplotter). | 
| `--rootOpt` | string | Option for creating the output `TFile`, e.g. {`RECREATE`,`UPDATE`} |
| `--skipBadFiles` | none | TFiles that fail to load, or where the TTree cannot be successfully loaded, will be skipped. |
| `--showStat` | none | Causes the statistics box to be drawn on created plots. Note only applicable when used with `--make2D`. |
| `--vfatList` | Comma separated list of int's | List of VFATs that should be plotted.  May be used instead of the `--vfat` option. |
| `--ztrim` | int | The ztrim value that was used when running the scans listed in `--infilename` |

#### gemPlotter.py Input File
The format of this input file should follow the [Three Column Format](#three-column-format).

#### gemPlotter.py Example: Making a time series with plotTimeSeries.py
To automatically consider the last two weeks worth of s-curve scans, run the script specifying `vt1bump` option like this:

```
plotTimeSeries.py --vt1bump=10
```

resulting plots will be stored under

```
$ELOG_PATH/timeSeriesPlots/<chamber name>/vt1bumpX/
```

#### gemPlotter.py Example: Making a 1D Plot - Channel Level
To make a 1D plot for a given strip of a given VFAT execute:

```
gemPlotter.py --infilename=<inputfilename> --anaType=<anaType> --branchName=<TBranch Name> --vfat=<VFAT No.> --strip=<Strip No.>
```

For example, to plot `trimDAC` vs. an **Indep. Variable Name** defined in `listOfScanDates.txt` for VFAT 12, strip number 49 execute:

```
gemPlotter.py -ilistOfScanDates.txt --anaType=trimAna --branchName=trimDAC --vfat=12 --strip=49
```

Additional VFATs could be plotted by either:
- Making successive calls of the above command and using the `--rootOpt=UPDATE`,
- Using the `--vfatList` argument instead of the `--vfat` argument, or
- Using the `-a` argument to make all VFATs.

#### gemPlotter.py Example: Making a 1D Plot - VFAT Level
To make a 1D plot for a given VFAT execute:

```
gemPlotter.py --infilename=<inputfilename> --anaType=<anaType> --branchName=<TBranch Name> --vfat=<VFAT No.> 
```

For example, to plot `trimRange` vs. an **Indep. Variable Name** defined in `listOfScanDates.txt` for VFAT 12 execute:

```
gemPlotter.py -ilistOfScanDates.txt --anaType=trimAna --branchName=trimRange --vfat=12
```

Note if **TBranch Name** is a strip level observable the data points (y-error bars) in the produced plot will represent the mean (standard deviation) from all of the VFAT's channels.

Additional VFATs could be plotted by either:
- Making successive calls of the above command and using the `--rootOpt=UPDATE`,
- Using the `--vfatList` argument instead of the `--vfat` argument, or
- Using the `-a` argument to make all VFATs.

To automatically extend this to all channels execute:

```
gemPlotterAllChannels.sh <InFile> <anaType> <branchName>
```

#### gemPlotter.py Example: Making a 2D Plot
To make a 2D plot for a given VFAT execute:

```
gemPlotter.py --infilename=<inputfilename> --anaType=<anaType> --branchName=<TBranch Name> --vfat=<VFAT No.> --make2D
```

Here the output plot will be of the form "ROB Strip/VFAT Channel vs. Indep. Variable Name" with the z-axis storing the value of `--branchName`.

For example to plot `trimDAC` for "ROB Strip vs. Indep. Variable Name" wher
For example to make a 2D plot with the z-axis as `trimDAC` and the **Indep. Variable Name** defined in `listOfScanDates.txt` for VFAT 12 execute:

```
gemPlotter.py -ilistOfScanDates.txt --anaType=trimAna --branchName=trimDAC --vfat=12 --make2D 
```

Additional VFATs could be plotted by either:
- Making successive calls of the above command and using the `--rootOpt=UPDATE`,
- Using the `--vfatList` argument instead of the `--vfat` argument, or
- Using the `-a` argument to make all VFATs.

### gemTreeDrawWrapper.py
The `gemTreeDrawWrapper.py` tool is for making a given 'Y vs. X' plot for each scandate of interest.  Here *Y* and *X* are quantities stored in `TBranches` of one of the `TTree` objects procued by the (ana-) ultra scan scripts.  This is designed to complement `gemPlotter.py` and should speed up plotting in general.  This tool is essesntially a wrapper for the `TTree::Draw()` method.  To make full use of this tool you should familiarize yourself with the `TTree::Draw()` [documentation](https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45).

Additionally `gemTreeDrawWrapper.py` can also fit produced plots with a function defined at runtime through the command line arguments.

Each plot produced will be stored as an output `*.png` file. Additionally an output `TFile` will be produced which will contain each of the plots, stored as `TGraph` objects, canvases, and fits produced. 

#### gemTreeDrawWrapper.py Arguments
The following table shows the mandatory inputs that must be supplied to execute the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--anaType` | string | Analysis type to be executed, see `tree_names.keys()` of [anaInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/master/anaInfo.py) for possible inputs |
| `-i`, `--infilename` | string | physical filename of the input file to be passed to `gemTreeDrawWrapper.py`.  See [Two Column Format](two-column-format) for details on the format and contents of this file. |
| `--treeExpress` | string | Expression to be drawn, corresponds to the `varexp` argument of [TTree::Draw()](https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45). |

Note for those `anaType` values which have the substring `Ana` in their names it is expected that the user has already run `ana_scans.py` on the corresponding `scandate` to produce the necessary input file for `gemTreeDrawWrapper.py`.

The following table shows the optional inputs that can be supplied when executing the script:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--axisMaxX` | float | Maximum value for X-axis range. |
| `--axisMinX` | float | Minimum value for X-axis range, note this parameter will default to 0 `--axisMaxX` is given. | 
| `--axisMaxY` | float | Maximum value for Y-axis range. |
| `--axisMinY` | float | Minimum value for Y-axis range, note this parameter will default to 0 `--axisMaxY` is given. | 
| `--drawLeg` | none | When used with `--summary` option draws a TLegend on the output plot. |
| `--fitFunc` | string | Expression following the [TFormula syntax](https://root.cern.ch/doc/master/classTFormula.html) for defining a TF1 to be fit to the plot. |
| `--fitGuess` | string | Initial guess for fit parameters defined in `--fitFunc`. Note, order of params here should match that of `--fitFunc`. |
| `--fitOpt` | string | Option to be used when fitting, a complete list can be found [here](https://root.cern.ch/doc/master/classTH1.html#a7e7d34c91d5ebab4fc9bba3ca47dabdd). |
| `--fitRange` | Comma separated list of float's | Defines the range the fit function is valid on. |
| `--rootOpt` | string | Option for creating the output `TFile`, e.g. {`RECREATE`,`UPDATE`} |
| `--showStat` | none | Causes the statistics box to be drawn on created plots. |
| `--summary` | none | Make a summary canvas with all created plots drawn on it. |
| `--treeSel` | string | Selection to be used when making the plot, corresponds to the `selection` argument of [TTree::Draw()](https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45). |
| `--treeDrawOpt` | string | Draw option to be used for the procued plots. |
| `--ztrim` | int | The ztrim value that was used when running the scans listed in `--infilename` |

#### gemTreeDrawWrapper.py Input File
The format of this input file should follow the [Two Column Format](#two-column-format).

#### gemTreeDrawWrapper.py Example: Making a Plot
For example to make a plot from a latency scan, `Nhits` vs. `lat` for VFAT12, use the following example:

```
gemTreeDrawWrapper.py -ilistOfScanDates_TreeDraw.txt --anaType=latency --summary --treeExpress="Nhits:lat" --treeDrawOpt=APE1 --treeSel="vfatN==12" --axisMaxY=1000 --axisMinX=39 --axisMaxX=49 --drawLeg
```

This will produce one `Nhits` vs. `lat` plot for VFAT12 for each (ChamberName,scandate) pair found in `listOfScanDates_TreeDraw.txt`.  Additionally it will make one summary plot with a legend drawn which contains all of the produced plots.

#### gemTreeDrawWrapper.py Example: Fitting a Plot
For example to plot and fit an scurve from an scurve scan, `Nhits` vs `vcal`, for VFAT12 channel 45, use the following example:

```
gemTreeDrawWrapper.py -ilistOfScanDates_TreeDraw.txt --anaType=scurve --treeExpress="Nhits:vcal" --treeDrawOpt=APE1 --treeSel="vfatN==12 && vfatCH==45" --fitFunc="500*TMath::Erf((TMath::Max([2],x)-[0])/(TMath::Sqrt(2)*[1]))+500" --fitRange=70,150 --fitOpt="RM" --fitGuess=110,10,10
```

Here the fit that will be applied will be equivalent too:
```
myFunc = r.TF1(strName,"500*TMath::Erf((TMath::Max([2],x)-[0])/(TMath::Sqrt(2)*[1]))+500",70,150)
myFunc.SetParameter(0,110)
myFunc.SetParameter(0,10)
myFunc.SetParameter(0,10)
```

The fit option that will be used will be `RM`.  This fit will be applied to the scurve generated from VFAT12 channel 45 for each (ChamberName,scandate) pair found in `listOfScanDates_TreeDraw.txt`.

## Scurve Plotting Tools
The following tools exist for helping to understand scurve data:

1. `gemSCurveAnaToolkit.py`
2. `plot_noise_vs_trim.py`
3. `plot_vfat_and_channel_Scurve.py`
4. `plot_vfat_summary.py`
5. `summary_plots.py`

These tools can all by found in the `macros/` subdirectory and are designed to be run on `TFile` objects containing the `scurveFitTree` `TTree` object (e.g. produced by `anaUltraScurve.py`).  The first tool `gemSCurveAnaToolkit.py` is for plotting the same (vfat,channel/ROBstr) scurve from a list of scandates and it is described in a dedicated subsection below. The rest of the tools above are for making plots from a single input file; the plots made by tools 2-4 are:

- `plot_noise_vs_trim.py`: Plots a channel/strip's scurve width (e.g. `noise`) vs. trimDAC as a `TH2D` on a `TCanvas`, 
- `plot_vfat_and_channel_Scurve.py`: Plots a channel/strip's scurve as a `TH1D` and its `TF1` on a `TCanvas`, and
- `plot_vfat_summary.py`: Plots all scurves from a given VFAT as a `TH2D` on a `TCanvas`.

Tool 5 `summary_plots.py` produces the following plots from a single input file for a given VFAT depending on the command line argument supplied:

- Plot of channel/strip scurve mean as a `TH1D`,
- Plot of channel/strip scurve width as a `TH1D`,
- Plot of channel/strip scurve pedestal as a `TH1D`,
- Plot of Chi<sup>2</sup> of the channel/strip scurve fits as a `TH1D`,
- Plot of channel/strip scurve mean vs. scurve width as a `TH2D`, and
- Plot of channel/strip scurve width vs. trimDAC as a `TH2D`.

The command line options for tools 2-5 are:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `-c`, `--channels` | none | Make plots vs VFAT channels instead of ROB strips. |
| `-i`, `--infilename` | string | Physical filename of the input file.  Note this must be a `TFile` which contains the `scurveFitTree` `TTree` object. |
| `-s`, `--strip` | int | If the `-c` option is (not) supplied this will be the VFAT channel (ROB strip) the plot will be made for. |
| `-v`, `--vfat` | int | The VFAT to plot. |

Additionally tool 5 `summary_plots.py` has the following additional command line options:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `-a`, `--all` | none | Equivalent to supplying `-f` and `-x` options. |
| `-f`, `--fit` | none | Make fit parameter plots. |
| `-x`, `--chi2` | none | Make Chi2 plots. |

Note that for tool 5 `summary_plots.py` you must supply at least one of these additional options {`-a`,`-f`,`-x`}.

### gemSCurveAnaToolkit.py
The `gemSCurveAnaToolkit.py` tool is for plotting scurves and their fits from a given (vfat, vfatCH/ROBstr) from a list of scandates that correspond to `TFile` objects which contain the `scurveFitTree` `TTree` (e.g. files produced by `anaUltraScurve.py`). Each plot produced will be stored as an output `*.png` file. Additionally an output `TFile` will be produced which will contain each of the scurves and their fits.

#### gemSCurveAnaToolkit.py Arguments

| Name | Type | Description |
| :--: | :--: | :---------- |
| `-c`, `--channels` | none | Make plots vs VFAT channels instead of ROB strips. |
| `-i`, `--infilename` | string | Physical filename of the input file to be passed to `gemSCurveAnaToolkit.py`.  The format of this input file should follow the [Two Column Format](two-column-format). |
| `-s`, `--strip` | int | If the `-c` option is (not) supplied this will be the VFAT channel (ROB strip) the plot will be made for. |
| `-v`, `--vfat` | int | The VFAT to plot. |
| `--anaType` | string | Analysis type to be executed, taken from the list {'scurveAna','trimAna'}. |
| `--drawLeg` | none | When used with `--summary` option draws a TLegend on the output plot. |
| `--rootOpt` | string | Option for creating the output `TFile`, e.g. {`RECREATE`,`UPDATE`} |
| `--summary` | none | Make a summary canvas with all created plots drawn on it. |
| `--ztrim` | int | The ztrim value that was used when running the scans listed in `--infilename` |

#### gemSCurveAnaToolkit.py Input File
The format of this input file should follow the [Two Column Format](two-column-format).

#### gemSCurveAnaToolkit.py Example: Making a Plot
To plot the scurves, and their fits, for VFAT0 channel 29 from a set of scandates defined in `listOfScanDates_Scurve.txt` taken by `ultraScurve.py` and analyzed with `anaUltraScurve.py` you would call:

```
gemSCurveAnaToolkit.py -ilistOfScanDates_Scurve.txt -v0 -s29 --anaType=scurveAna -c --summary --drawLeg
```

This will produce a `*.png` file for each of the scandates defined in `listOfScanDates_Scurve.txt` and one `*.png` file showing all the scurves with their fits drawn on it as a summary.  Additionally an output `TFile` will be produced containing each of the scurves and their fits.

### Comparing Scurves Results Across Scandates: plotSCurveFitResults.py
While `gemTreeDrawWrapper.py` and `gemPlotter.py` allow you to plot observables from multiple runs sometimes you are interested in seeing the results made from `anaUltraScurve.py`, from multiple scandates, on the same set of `TCanvas`es.  The tool `plotSCurveFitResults.py` allows you to do this.  The tool will create five output `*.png` files and one `TFile` which stores relevant plots for each VFAT from each of the input scandates.  These five `*.png` files are:

- `scurveFitSummaryGridAllScandates.png`, shows the `fitSummary` curves from all input scandates on one `TCanvas` in a 3-by-8 grid,
- `scurveMeanGridAllScandates.png`, shows the distribution of s-curve mean positions from each VFAT from all input scandates on one `TCanvas` in a 3-by-8 grid,
- `scurveSigmaGridAllScandates.png`, as `scurveMeanGridAllScandates.png` but for s-curve sigma,
- `canvSCurveSigmaDetSumAllScandates.png`, shows a summary distribution of s-curve sigma positions from all VFATs of the detector from all scandates on one `TCanvas`, and
- `canvSCurveMeanDetSumAllScandates.png`, as `canvSCurveSigmaDetSumAllScandates.png` but for s-curve mean.

The files will be found in `$ELOG_PATH` along with the output `TFile`, named `scurveFitResultPlots.root`.

#### plotSCurveFitResults.py Arguments

| Name | Type | Description |
| :--: | :--: | :---------- |
| `-i`, `--infilename` | string | Physical filename of the input file to be passed to `plotSCurveFitResults.py`.  The format of this input file should follow the [Three Column Format](#three-column-format). |
| `--alphaLabels` | none | When providing this flag `plotSCurveFitResults.py` will interpret the **Indep. Variable** as a string. |
| `--anaType` | string | Analysis type to be executed, taken from the list {'scurveAna','trimAna'}. |
| `--drawLeg` | none | Draws a TLegend on the output plots. For those 3x8 grid plots the legend will only be drawn on the plot for VFAT0. |
| `--rootName` | string | Name of output `TFile`.  This file will be found in `$ELOG_PATH`. |
| `--rootOpt` | string | Option for creating the output `TFile`, e.g. {`RECREATE`,`UPDATE`} |
| `--ztrim` | int | The ztrim value that was used when running the scans listed in `--infilename` |

#### plotSCurveFitResults.py Input File
The format of this input file should follow the [Three Column Format](#three-column-format).  Note that here the **Indep. Variable** for each row will be used as the `TLegend` entry if the `--drawLeg` argument is supplied.

#### plotSCurveFitResults.py Example
To plot results from a set of scandates defined in `listOfScanDates_Scurve.txt` taken by either `ultraScurve.py` or `trimChamber.py` and analyzed with `anaUltraScurve.py` you would call:

```
plotSCurveFitResults.py --anaType=scurveAna --drawLeg -i listOfScanDates_Scurve.txt --alphaLabels
```

This will produce the five `*.png` files mentioned above along with the output `TFile`.

### Analyzing the Time Evolution of Channels: timeHistoryAnalyzer.py

`timeHistoryAnalyzer.py` is a tool that finds when a channel turns bad (see below for the available definitions), and possibly when it is recovered. It takes as input a set of files produced by `plotTimeSeries.py`, and the results are printed to the terminal.

The analysis proceeds in three steps, executed in the following order:

1. [Bad scan removal](#bad-scan-removal): Scans that failed to produce consistent results are removed.
2. [Range detection](#range-detection): The time evolution of each channel is searched for successive scans with consistent "bad" behavior (see below). A set of such scans for a given channel is called a (time) range. What kind of behavior is searched for is used-defined.
3. [Analysis](#timehistoryanalyzerpy-output): The properties of "ranges" are computed and printed.

##### Bad scan removal

Scans that pass any the following cuts are removed:

* The average noise over the entire detector is lower than 0.1 fC (or `--minScanAvgNoise`). This cuts scans with no or very few channels responding.
* The fraction of masked channels is above 7% (or `--maxScanMaskedFrac`). This cuts e.g scans that produced no data and for which all fits failed.

Note that the options are named in the positive way, ie they tell which scans to *keep*.

##### Range detection

The time evolution of each channel is searched for successive scans with consistent behavior. A set of such scans "bad" scans for a given channel is called a (time) range; the definition of bad is user defined (see below).

Range finding starts with a list of scans, where each scan is marked as "good" or "bad". The definition of "bad" depends on what's being searched for (and "good" is always defined as "not bad"). The start of a range is determined by:

* Starts with a "bad" scan (see below)
* The channel wasn't "bad" in the previous scan (e.g going good to bad)

Then the range continues and the end of the range is determined by 5 consecutive good scans appearing (option: `--numEndScans`). To prevent the printing of spurious ranges due to transient effects ranges with less than 4 "bad" scans in total are suppressed (option: `--minBadScans`). A "range" found by this algorithm can have include some "good" scans.

As a side-effect, channels with sparse "bad" behavior are also extracted. This can be controlled by tightening the cuts in the algorithm above.

Three definitions of "bad" are currently available:

* `mask`: the channel under consideration is masked
* `maskReason`: the channel under consideration has a non-zero `maskReason`
*  `zeroInputCap`: the channel under consideration has an scurve width that is consistent with zero input capacitance (`4.14E-02 < scurevWidth < 1.09E-01 fC`). The precise values can be controlled using the `--minNoise` and `--maxNoise` options.

##### timeHistoryAnalyzer.py Output

For every "range" found in each of the VFATs, the following properties are computed and printed in a table:

| Column header | Meaning |
|:-|:-|
| `ROBstr` or `vfatCH` | Strip number and VFAT channel, respectively |
| Last known good | Date and time of the last good scan before the range ("never" if the range starts at the first scan) |
| Range begins | Start date and time |
| Range ends | End date and time ("never" if the range includes the lastest scan) |
| #scans | Total number of scans (good and bad) |
| masked% | Percentage of `#scans` where the channel is "masked" not to be confused with "bad (useful to investigate channels that behave badly once in a while) |
| Initial `maskReason` | `maskReason` for the first scan in the range |
| Other subsequent `maskReason`s | `maskReason` not present for the first scan but found in a later scan in the same range |

A summary table of initial `maskReason` vs VFAT is also printed at the end.

#### timeHistoryAnalyzer.py Arguments

##### General arguments

| Name | Type | Description |
|:-|:-|:-|
| `-i`, `--inputDir` | path | Input directory (=output directory of `plotTimeSeries.py`) |
| `--ranges` | string | Defines the range selection algorithm. Allowed values: `mask`, `maskReason`, `zeroInputCap` |
| `--onlyCurrent` | none | Only show ranges that extend until the last scan |

##### Options controlling bad scan removal

| Name | Type | Description |
|:-|:-|:-|
| `--minScanAvgNoise` | float | Minimum noise in fC, averaged over the whole detector, for a scan to be considered |
| `--maxScanMaskedFrac` | float | Maximum fraction of masked channel, over the whole detector, for a scan to be considered |

##### Options controlling the range finding algorithm

| Name | Type | Description |
|:-|:-|:-|
| `--numEndScans` | int | Number of 'good' scans to end a range |
| `--minBadScans` | int | Minimum number of 'bad' scans to keep a range |
| `--minNoise` | float | Lower bound on noise for the `zeroInputCap` range finder, in fC |
| `--maxNoise` | float | Upper bound on noise for the `zeroInputCap` range finder, in fC |

#### timeHistoryAnalyzer.py Examples

The examples below assume that you have analyzed S-curves
[using plotTimeSeries.py](#gemplotterpy-example-making-a-time-series-with-plottimeseriespy),
and that the output is located at:

```
$ELOG_PATH/timeSeriesPlots/<chamber name>/vt1bumpX/
```

Note that the above structure is created automatically by `plotTimeSeries.py`.

##### Simple analysis

The simplest possible call to `timeHistoryAnalyzer.py` is:

```
timeHistoryAnalyzer.py -i $ELOG_PATH/timeSeriesPlots/<chamber name>/vt1bumpX/
```

This will use the default range finder, `maskReason`, and settings. Depending on the detector and number of scans being analyzed, it may result in a lot of output being printed to the terminal. For every VFAT, you will get a table that looks like this:

|  `ROBstr`  | Last known good   | Range begins     | Range ends       |  #scans  |  Masked%  | Initial `maskReason`   | Other subsequent `maskReason`s   |
|:----------:|:------------------|:-----------------|:-----------------|:--------:|:---------:|:-----------------------|:---------------------------------|
|     18     | 2017.10.11.11.24  | 2017.10.13.12.53 | never            |   127    |    100    | HotChannel,FitFailed   |                                  |
|     31     | 2017.10.11.11.24  | 2017.10.13.12.53 | never            |   127    |     0     | DeadChannel            |                                  |
|     91     | 2017.06.15.15.10  | 2017.06.16.14.35 | 2018.02.06.12.07 |   107    |    47     | HotChannel             | HighNoise                        |
|     93     | 2017.03.27.16.22  | 2017.03.29.13.27 | 2017.05.31.14.48 |    46    |    56     | HotChannel             |                                  |
|     93     | 2017.06.15.15.10  | 2017.06.16.14.35 | 2018.02.06.12.07 |   107    |    50     | HotChannel             | HighNoise                        |

The meaning of the column headers is explained [above](#timehistoryanalyzerpy-output). Here's the information that we can extract from the table (take a look [here](#masking-channels-algorithmically) first if you're not confident with the meaning of `maskReason`):

* Strip number 18 became hot between 2017.10.11.11.24 and 2017.10.13.12.53. In the same period of time, strip number 31 died.
* Strip number 91 became hot in July 2017; afterwards, it was also found to have a high noise. It was recovered in February 2018. The masked fraction at 47% indicates that during this period, about half the scans didn't result in the corresponding channel being masked.
* Strip number 93 was hot during two periods: from the end of March to the end of May 2017, and afterwards from the beginning of April 2017 to the beginning of February 2018. Since both ranges have similar properties and the masked fraction is low, the split in two is likely an accident.

##### Using a different range finder

The example above used the `maskReason` range finder. Let's try with `zeroInputCap`:

```
timeHistoryAnalyzer.py -i $ELOG_PATH/timeSeriesPlots/<chamber name>/vt1bumpX/ --ranges zeroInputCap
```

Note that `--ranges zeroInputCap` typically produces in a lot less output than the default.

##### Reading the summary table

At the end of its output, `timeHistoryAnalyzer.py` prints the following table (some lines were stripped for concision):

|    |  HotChannel  |  FitFailed  |  DeadChannel  |  HighNoise  |  HighEffPed  |
|:--:|:------------:|:-----------:|:-------------:|:-----------:|:------------:|
| 0  |      0       |      0      |       2       |      0      |      0       |
| 7  |      2       |      0      |       3       |      0      |      0       |

The first column is the VFAT number; the others correspond to the possible entries in `maskReason`.

The table counts how many times a given `MaskReason` appears in the "Initial `maskReason`" column of each per-VFAT tables. Indeed, if we look at VFAT 0 for the above example, we find:

|  `ROBstr`  | Last known good   | Range begins     | Range ends   |  #scans  |  Masked%  | Initial `maskReason`   | Other subsequent `maskReason`s   |
|:----------:|:------------------|:-----------------|:-------------|:--------:|:---------:|:-----------------------|:---------------------------------|
|     63     | 2017.04.07.15.46  | 2017.04.09.14.27 | never        |   220    |     6     | DeadChannel            | HotChannel                       |
|     64     | never             | 2017.03.27.13.51 | never        |   229    |     0     | DeadChannel            |                                  |

The two entries in the DeadChannel column correspond to two ranges, that turn out to be from different strips (this may not be the case). Now VFAT 7:

|  `ROBstr`  | Last known good   | Range begins     | Range ends   |  #scans  |  Masked%  | Initial `maskReason`   | Other subsequent `maskReason`s   |
|:----------:|:------------------|:-----------------|:-------------|:--------:|:---------:|:-----------------------|:---------------------------------|
|     0      | 2017.05.10.20.41  | 2017.05.31.09.21 | never        |   182    |     0     | DeadChannel            |                                  |
|     2      | 2017.05.08.09.10  | 2017.05.10.19.57 | never        |   184    |     1     | HotChannel,DeadChannel |                                  |
|     3      | 2017.05.08.09.10  | 2017.05.10.19.57 | never        |   184    |     1     | HotChannel,DeadChannel |                                  |

We can see that the three entries in the DeadChannel column and the two in the HotChannel column come from the *same* ranges.

**Note** When using the `--onlyCurrent` option, there's only one range per channel, which makes the table easier to understand.

## Packaging Tool: packageFiles4Docker.py
You may occasionally need to update the `travis CI` docker which checks the code quality *or* you may want to transfer a number of files corresponding to a series of scandates from the P5 machine to another area.  The `packageFiles4Docker.py` tool enables you to do this.  The output of `packageFiles4Docker.py` will be a `*.tar` file that:

- mimics the file structure of `$DATA_PATH`, and 
- each of the input `listOfScandates.txt` files supplied at runtime, and 
- a temorary `chamberInfo.py` file which can be placed in the docker for testing.

### packageFiles4Docker.py Arguments

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--fileListLat` | string | Specify Input Filename for list of scandates for latency files. |
| `--fileListScurve` | string | Specify Input Filename for list of scandates for scurve files. |
| `--fileListThresh` | string | Specify Input Filename for list of scandates for threshold files. |
| `--fileListTrim` | string | Specify Input Filename for list of scandates for trim files. |
| `--ignoreFailedReads` | none | Ignores failed read errors in tarball creation, useful for ignoring scans that did not finish successfully. |
| `--onlyRawData` | none | Files produced by `anaUltra*.py` scripts will not be included. |
| `--tarBallName` | string | Specify the name of the output tarball. |
| `--ztrim` | int | The ztrim value of interest for scandates given in `--fileListTrim`. |
| `-d`, `--debug` | none | prints the tarball command but does not make one. |

Please note that multiple `--fileListX` arguments can be supplied at runtime, but at least one must be supplied.

### packageFiles4Docker.py Input Files
Each of the `--fileListX` arguments can be supplied with a `listOfScanDates.txt` file that follows either the [Two Column Format](#two-column-format) or the [Three Column Format](#three-column-format).

### packageFiles4Docker.py Example
To make a `tarball` of containing scurve scandates defined in `listOfScanDates.txt` for `GEMINIm01L1` execute:

```
packageFiles4Docker.py --ignoreFailedReads --fileListScurve=$DATA_PATH/GEMINIm01L1/scurve/listOfScanDates.txt --tarBallName=GEMINIm01L1_scurves.tar --ztrim=4 --onlyRawData
```

In this case failed read errors in the `tar` command will be ignored and only the raw data, e.g. `SCurveData.root` files, will be stored in the tarball following the appropriate file structure.

## Cluster Computing Tools
It may be that eventually you will need to re-analyze a large portion of the calibration dataset.  While this is expected to be rare it would be excessively time consuming to analyze the data by hand.  This section details the tools that exist to assist you in this process.  All tools below are designed to work with the lxplus batch submission system based on [LSF](https://cern.service-now.com/service-portal/service-element.do?name=batch).  Please note CERN IT plans to eventually transition from LSF to HTCondor.  When this occurs these tools will need to be migrated to the new system.  Instructions for doing so are available [here](http://batchdocs.web.cern.ch/batchdocs/).
 
### Cluster Analysis of S-Curve Data: clusterAnaScurve.py
This tool will allow you to re-analyze the scurve data in a straight forward way without the time consuming process of launching it by hand.

#### clusterAnaScurve.py: Arguments
The following table shows the mandatory inputs:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--anaType` | string | Analysis type to be executed, from list {'scurve','trim'} |
| `--chamberName` | string | Name of detector to be analyzed, must be present in `chamber_config.values()` of [mapping/chamberInfo.py](https://github.com/cms-gem-daq-project/gem-plotting-tools/blob/develop/mapping/chamberInfo.py). Either this option or `--infilename` must be supplied. |
| `-i`, `--infilename` | string | Physical filename of the input file to be passed to `clusterAnaScurve.py`.  The format of this input file should follow the [Two Column Format](two-column-format). Either this option or `--chamberName` must be supplied. |
| `-q`, `--queue` | string | queue to submit your jobs to.  Suggested options are {`8nm`, `1nh`} |
| ` -t`, `--type` | string | Specify GEB/detector type, e.g. "long" or "short" |

While the following table shows the optional additional inputs:

| Name | Type | Description |
| :--: | :--: | :---------- |
| `--calFile` | string | File specifying CAL_DAC/VCAL to fC equations per VFAT.  If this is not provided the analysis will default to hardcoded conversion for VFAT2 |
| `-c`, `--channels` | none | Output plots will be made vs VFAT channel instead of ROB strip |
| ` -d`, `--debug` | none | If provided all cluster files will be created for inspection, and job submission commands printed to terminal, but no jobs will be submitted to the cluster.  Strongly recommended calling with this option before submitting a large number of jobs. |
| `--endDate | string | If `--infilename` is not supplied this is the ending scandate, in YYYY.MM.DD formate, to be considered for job submission. Default is `None` so the default behavior will be whatever `datetime.today()` evaluates to. |
| `--extChanMapping` | string | Physical filename of a custom, non-default, channel mapping file.  If not provided the default slice test ROB strip to VFAT channel mapping will be used. |
| `-f`, `--fit` | none | Fit scurves and save fit information to output TFile |
| `-p`, `--panasonic` | none | Output plots will be made vs Panasonic pins instead of ROB strip |
| `--startDate | string | If `--infilename` is not supplied this is the starting scandate, in YYYY.MM.DD formate, to be considered for job submission.  Default is `2017.01.01` so the start of the slice test will be used. |
| `--zscore` | float | Z-Score for Outlier Identification in the MAD Algorithm.  For details see talks by [B. Dorney](https://indico.cern.ch/event/638404/contributions/2643292/attachments/1483873/2302543/BDorney_OpsMtg_20170627.pdf) or [L. Moureaux](https://indico.cern.ch/event/659794/contributions/2691237/attachments/1508531/2351619/UpdateOnHotChannelIdentificationAlgo.pdf) |
| `--ztrim` | float | Specify the p value of the trim in the quantity: `scurve_mean - ztrim * scurve_sigma` |

Finally `clusterAnaScurve.py` can also be passed the cut values used in assigning a maskReason described at [Providing Cuts for maskReason at Runtime](#providing-cuts-for-maskreason-at-runtime).

#### Full Example For P5 S-Curve Data
Before you start due to space limitations on `AFS` it is strongly recommended that your `$DATA_PATH` variable on lxplus point to the work area rather than the user area, e.g.:

```
export DATA_PATH=/afs/cern.ch/work/<first-letter-of-your-username>/<your-user-name>/<somepath>
```

In your work area you can have up to 100GB of space. If this is your first time using `lxplus` you may want to increase your storage quota by following instructions [here](https://resources.web.cern.ch/resources/Help/?kbid=067040).

Now connect to the P5 `dqm` machine. Then after setting up the env execute if you are intereted in a chamber ChamberName execute:

```
cd $HOME
python plotTimeSeries.py --listOfScanDatesOnly --startDate=2017.01.01
packageFiles4Docker.py --ignoreFailedReads --fileListScurve=/gemdata/<ChamberName>/scurve/listOfScanDates.txt --tarBallName=<ChamberName>_scurves.tar --ztrim=4 --onlyRawData
```

Then connect to `lxplus`.  Checkout the repository if you have not done so already. Then after setting up the env execute:

```
cd $DATA_PATH
scp <your-user-name>@cmsusr.cms:/nfshome0/<your-user-name>/<ChamberName>_scurves.tar .
tar -xf <ChamberName>_scurves.tar
mv gemdata/<ChamberName> .
clusterAnaScurve.py -i <ChamberName>/scurve/listOfScanDates.txt --anaType=scurve -f -q 1nh
```

It may take some time to finish the job submission.  Please pay attention to the output at the end of the `clusterAnaScurve.py` command as it provodes helpful information for managing jobs and undersanding what comes next.  Once your jobs are complete you should check that they all finished successfully.  One way to do this is to check if any of them exited with status `Exited` and check for the exit code.  To do this execute:

```
grep -R "exit code" <ChamberName>/scurve/*/stdout/jobOut.txt --color 
```

This will print a single line from all files where the string `exit code` appears.  For example:

```
% grep -R "exit code" GEMINIm01L1/scurve/*/stdout/jobOut.txt --color 
GEMINIm01L1/scurve/2017.04.10.20.33/stdout/jobOut.txt:Exited with exit code 255.
GEMINIm01L1/scurve/2017.04.26.12.25/stdout/jobOut.txt:Exited with exit code 255.
GEMINIm01L1/scurve/2017.04.27.13.27/stdout/jobOut.txt:Exited with exit code 255.
GEMINIm01L1/scurve/2017.06.07.12.17/stdout/jobOut.txt:Exited with exit code 255.
GEMINIm01L1/scurve/2017.07.18.11.09/stdout/jobOut.txt:Exited with exit code 255.
GEMINIm01L1/scurve/2017.07.18.18.34/stdout/jobOut.txt:Exited with exit code 255.
```

For those lines that appear in the `grep` output command you will need to check the standard err of the job which can be found in:

```
<ChamberName>/scurve/<scandate>/stderr/jobErr.txt
```

Note since some scans at P5 may have failed to complete successfully some jobs may intrinsically fail and be non-recoverable.  If you have questions about a particular job you can try to search in the e-log around the scandate in time to see if anything occurred around this time that might cause problems for the scan. If you would like to re-analyze a failed job you can do so by calling:

```
source $DATA_PATH/<ChamberName>/scurve/<scandate>/clusterJob.sh
```

If a large number of jobs have failed you should spend some time trying to understand why, and then re-submit to the cluster, rather than attempting to analyze them all by hand.

Finally after you are satisfied that all the jobs that could complete successfully have completed you can:

1. re-package the re-analyzed data into a tarball, and/or
2. create time series plots to summarize the entire dataset.

For case 1, re-packaging the re-analyzed files into a `tarball`, execute:

```
packageFiles4Docker.py --ignoreFailedReads --fileListScurve=<ChamberName>/scurve/listOfScanDates.txt --tarBallName=<ChamberName>_scurves_reanalyzed.tar --ztrim=4
mv <ChamberName>_scurves_reanalyzed.tar $HOME/public
chmod 755 $HOME/public/<ChamberName>_scurves_reanalyzed.tar
echo $HOME/public/<ChamberName>_scurves_reanalyzed.tar
```

Then provide the terminal output of this last command to one of the GEM DAQ Experts for mass-storage.

For case 2, create time series plots to summarize the entire dataset, execute:

```
<editor of your choice> $GEM_PLOTTING_PROJECT/mapping/chamberInfo.py
```

And ensure the only uncommented entries of the `chamber_config` dictionary match the set of `ChamberName`'s that you have submitted jobs for.  Then execute:

```
plotTimeSeries.py --startDate=2017.01.01 --anaType=scurve
```

Please note the above command may take some time to process depending on the number of detectors worth of data you are trying to analyze.  Then a series of output `*.png` and `*.root` files will be found at:

```
$ELOG_PATH/timeSeriesPlots/<ChamberName>/vt1bump0/
```

If you would prefer to analyze `ChamberName`'s one at a time, or to have an output `*.png` file for each VFAT, you can produce time series plots individually by executing the `gemPlotter.py` commands provided at the end of the `clusterAnaScurve.py` output.  This might be preferred as when analyzing a large period of time the 3-by-8 grid plots that `plotTimeSeries.py` will produce for you may be hard to read.  In either case `gemPlotter.py` or `plotTimeSeries.py` will produce a `TFile` for you in which the plots at the per VFAT level are stored for you to later investigate.

If you encounter issues in this procedure please spend some time trying to figure out what wrong on your side first.  If after studying the documentation and reviewing the commands you have exeuted you still do not understand the failure please ask on the `Software` channel of the `CMS GEM Ops` Mattermost team or submit an issue to the [github page](https://github.com/cms-gem-daq-project/gem-plotting-tools/issues/new).
