# Copyright 2015 Jim Rosser
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from expects.matchers import Matcher


class be_greater(Matcher):
    def __init__(self, count):
        self._expected_count = count

    def _match(self, aws_object):
        return aws_object.count > self._expected_count

class be_less(Matcher):
    def __init__(self, count):
        self._expected_count = count

    def _match(self, aws_object):
        return aws_object.count < self._expected_count

class be_exactly(Matcher):
    def __init__(self, count):
        self._expected_count = count

    def _match(self, aws_object):
        return aws_object.count == self._expected_count

class be_less_or_equal_to(Matcher):
    def __init__(self, count):
        self._expected_count = count

    def _match(self, aws_object):
        return aws_object.count <= self._expected_count

class be_greater_or_equal_to(Matcher):
    def __init__(self, count):
        self._expected_count = count

    def _match(self, aws_object):
        return aws_object.count >= self._expected_count
