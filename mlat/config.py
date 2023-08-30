# -*- mode: python; indent-tabs-mode: nil -*-

# Part of mlat-server: a Mode S multilateration server
# Copyright (C) 2015  Oliver Jowett <oliver@mutability.co.uk>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Poor man's configuration system, because I'm lazy.."""

from mlat import constants

# Location at which _this copy_ of the server code may be found. This URL will
# be sent to network clients. Remember to uncomment this after updating it.
#
# See COPYING and README.md - the AGPL requires that you make your
# modified version of the server source code available to users that interact
# with the server over a network.
#
# Please remember that this needs to be _the code that the server is running_.
#
AGPL_SERVER_CODE_URL = "https://github.com/adsb-related-code/mlat-server/"

# minimum NUCp value to accept as a sync message
MIN_NUC = 6

# maximum number of planes we use for sync per receiver (randomly chosen every 15 seconds):
MAX_SYNC_AC = 15
# max sync rate
MAX_SYNC_RATE = 12

# minimum interval between trying to get an MLAT position
RESOLVE_INTERVAL = 0.15

# minimum time after successful position before trying to calculate the next one
RESOLVE_BACKOFF = 0.7

# maximum distance between even/odd DF17 messages, metres
MAX_INTERMESSAGE_RANGE = 10e3

# absolute maximum altitude, metres
MAX_ALT = 75000 * constants.FTOM
MIN_ALT = -1500 * constants.FTOM

# how long to wait to accumulate messages before doing multilateration, seconds
MLAT_DELAY = 0.9

# maxfev (maximum function evaluations) for the solver
SOLVER_MAXFEV = 165

# limit group size, discard the rest of message copies
# first pruning step before clock normalization
MAX_GROUP = 15

DEBUG_FOCUS='euerdorf'

if 'AGPL_SERVER_CODE_URL' not in globals():
    raise RuntimeError('Please update AGPL_SERVER_CODE_URL in mlat/server/config.py')
