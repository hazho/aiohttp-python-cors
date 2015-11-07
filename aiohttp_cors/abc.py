# Copyright 2015 Vladimir Rutsky <vladimir@rutsky.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Abstract base classes.
"""

import abc


__all__ = ("AbstractRouterAdapter",)


class AbstractRouterAdapter(metaclass=abc.ABCMeta):
    """Router adapter is a minimal interface to router implementation that
    is required to implement CORS handling.
    """

    @abc.abstractmethod
    def route_methods(self, route):
        """Returns list of HTTP methods that route handles"""

    @abc.abstractmethod
    def add_options_method_handler(self, route, handler):
        """Add OPTIONS method request handler that will be issued at the same
        paths as provided `route`.

        :return: Newly added route.
        """
