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

import boto3

class ec2_instances(object):
    def __init__(self):
        self.count = 2
        self._filters = []

    def with_root_device_type(self, name):
        self._filters.append(
                {
                    'Name': 'root-device-type',
                    'Values': [name],
                }
            )
        return self._get_instances()

    def with_tenancy(self, tenancy):
        self._filters.append(
                {
                    'Name': 'tenancy',
                    'Values': [tenancy],
                }
            )
        return self._get_instances()

    def with_vpc_id(self, vpc_id):
        self._filters.append(
                {
                    'Name': 'vpc-id',
                    'Values': [vpc_id],
                }
            )
        return self._get_instances()

    def with_tags(self, tags):
        for key, val in tags.iteritems():
            if isinstance(val, basestring):
                val = [val]

            self._filters.append(
                {
                    'Name': ("tag:{}".format(key)),
                    'Values': val,
                }
            )
        return self._get_instances()

    def _get_instances(self):
        client = boto3.client('ec2')
        results = client.describe_instances(Filters=self._filters)
        reservations = results.get('Reservations')
        if reservations is None:
            self.count = 0
            return self

        instances = []
        for reservation in reservations:
            instances.append(reservation.get('Instances'))
        if not instances:
            self.count = 0
            return self

        self.count = len(instances)
        return self
