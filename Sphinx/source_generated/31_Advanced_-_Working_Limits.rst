****************************
31 Advanced - Working Limits
****************************

.. contents:: Contents




Working Limits
==============

There are some limits that you should take into account.Precision issues when working with mesh data for example.



Space
-----

While object positions, vertex locations are not clamped, larger values become increasingly imprecise.

To get an idea of the precision you can work with using different scales.

Here’s a table of scales and their associated accuracy.

.. list-table::

	* - 10:
	  - 1/1,048,576th

	* - 100:
	  - 1/131,072th

	* - 1,000:
	  - 1/16,384th

	* - 10,000:
	  - 1/1,024th

	* - 100,000:
	  - 1/128th

	* - 1,000,000:
	  - 1/16th

.. Hint:: For a rough rule of thumb, values within -5,000/+5,000 are typically reliable (range of 10,000).



Time
----

The maximum number of frames for each scene is currently 500,000, and allows for continuous shots for durations of:

.. list-table::

	* - 24 fps:
	  - 5 hours, 47 seconds.

	* - 25 fps:
	  - 5 hours, 33 seconds.

	* - 30 fps:
	  - 4 hours, 37 seconds.

	* - 60 fps:
	  - 2 hours, 18 seconds.

.. Note:: In practice, a finished work is typically composed of output from many scenes. So this limit does not prevent you from creating longer works.



Text Fields
-----------

Fixed strings are used internally, and while it is not useful to list all limits, here are some common limits.**Text fields are used for various things like data-block names, modifiers, vertex-groups, UV-layers…**

.. list-table::

	* - directory:
	  - 767 characters

	* - file-name:
	  - 255 characters

	* - file-path:
	  - 1023 characters

	* - identifier:
	  - 63 characters

.. Note:: Multi-byte encoding means some unicode characters use more than a single ASCII character.

