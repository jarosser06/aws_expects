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
        self._filters = []

    def with_affinity(self, affinity):
        self._filters.append(
                {
                    'Name': 'affinity',
                    'Values': [affinity],
                }
            )
        return self

    def with_architecture(self, architecture):
        self._filters.append(
                {
                    'Name': 'architecture',
                    'Values': [architecture],
                }
            )
        return self

    def with_image_id(self, image_id):
        self._filters.append(
                {
                    'Name': 'image-id',
                    'Values': [image_id],
                }
            )
        return self

    def with_root_device_type(self, name):
        self._filters.append(
                {
                    'Name': 'root-device-type',
                    'Values': [name],
                }
            )
        return self

    def with_instance_state(self, state):
        self._filters.append(
                {
                    'Name': 'instance-state-name',
                    'Values': [state],
                }
            )
        return self

    def with_tenancy(self, tenancy):
        self._filters.append(
                {
                    'Name': 'tenancy',
                    'Values': [tenancy],
                }
            )
        return self

    def with_vpc_id(self, vpc_id):
        self._filters.append(
                {
                    'Name': 'vpc-id',
                    'Values': [vpc_id],
                }
            )
        return self

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
        return self

    @property
    def count(self):
        client = boto3.client('ec2')
        results = client.describe_instances(Filters=self._filters)
        reservations = results.get('Reservations')
        if reservations is None:
            return 0

        instances = []
        for reservation in reservations:
            instances.append(reservation.get('Instances'))
        if not instances:
            return 0

        return len(instances)
