###############################################################################
#   volumina: volume slicing and editing library
#
#       Copyright (C) 2011-2019, the ilastik developers
#                                <team@ilastik.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the Lesser GNU General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# See the files LICENSE.lgpl2 and LICENSE.lgpl3 for full text of the
# GNU Lesser General Public License version 2.1 and 3 respectively.
# This information is also available on the ilastik web site at:
# 		   http://ilastik.org/license/
###############################################################################
from .array import ArraySource, ArraySinkSource, RelabelingArraySource
from .constant import ConstantSource
from .minmax import MinMaxSource
from .halo import HaloAdjustedDataSource

__all__ = [
    "ArraySource",
    "ArraySinkSource",
    "RelabelingArraySource",
    "ConstantSource",
    "MinMaxSource",
    "HaloAdjustedDataSource",
]

try:
    from .lazyflow import LazyflowSource, LazyflowSinkSource

    __all__ += ["LazyflowSource", "LazyflowSinkSource"]
except ImportError:
    pass
