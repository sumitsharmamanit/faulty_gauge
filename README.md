# Faulty Gauge
## Image processing to detect vibration in a pressure gauge


The gauge's vibration can be detected by counting the number of white pixels (after applying basic image processing), captured in the format of a timeseries/frame series. Timeseries data can be classified as stationary or non-stationary using the <b>Dickey-Fuller</b> test. In this test, a p-value is calculated to distinguish between stationary and non-stationary data.

In this case, if the gauge needle is faulty and found oscillating at its position, the auto-correlation of pixel data will be a fluctuating graph, whereas it will be a smooth curve in the case of a properly working or static needle.

Based on the sample data, a suitable threshold value can be used to compare the calculated p-value.

<em>NOTE: It is assumed that a gauge detector would provide bounding box coordinates for each frame.</em>

## Instructions
1. ```pip install -r requirements.txt```
2. execute test.py to test the sample cases
3. execute main.py by passing arguments [video_file path, boolean flag to save output plot, bounding box rectange xmin, ymin and xmax, ymax]
