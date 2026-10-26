---
id: advanced.advanced-working-limits
title: "Working Limits"
section: advanced
path:
  - Advanced
  - Advanced - Working Limits
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 34 Advanced - Working Limits.odt
icon: error
summary: "There are some limits that you should take into account."
---
## Working Limits

There are some limits that you should take into account. Precision issues when working with mesh data for example.

### Space

While object positions, vertex locations are not clamped, larger values become increasingly imprecise.

To get an idea of the precision you can work with using different scales.

Here’s a table of scales and their associated accuracy.


|  |  |
| ---------- | --------------- |
| 10: | 1/1,048,576^th^ |
| 100: | 1/131,072^th^ |
| 1,000: | 1/16,384^th^ |
| 10,000: | 1/1,024^th^ |
| 100,000: | 1/128^th^ |
| 1,000,000: | 1/16^th^ |


> **Tip:** For a rough rule of thumb, values within -5,000/+5,000 are typically reliable (range of 10,000).
>
> Internally *single precision* floating point calculations are used.

### Time

The maximum number of frames for each scene is currently 500,000, and allows for continuous shots for duration's of:


|  |  |
| ------- | -------------------- |
| 24 fps: | 5 hours, 47 seconds. |
| 25 fps: | 5 hours, 33 seconds. |
| 30 fps: | 4 hours, 37 seconds. |
| 60 fps: | 2 hours, 18 seconds. |


> **Note:** In practice, a finished work is typically composed of output from many scenes. So this limit does not prevent you from creating longer works.

### Text Fields

Fixed strings are used internally, and while it is not useful to list all limits, here are some common limits. **Text fields are used for various things like data-block names, modifiers, vertex-groups, UV-layers…**


|  |  |
| ----------- | --------------- |
| directory: | 767 characters |
| file-name: | 255 characters |
| file-path: | 1023 characters |
| identifier: | 63 characters |


> **Note:** Multi-byte encoding means some Unicode characters use more than a single ASCII character.

