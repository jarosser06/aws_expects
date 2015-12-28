from expects import expect
from aws_expects.ec2 import ec2_instances
from aws_expects import matchers

expect(ec2_instances()
        .with_tenancy('default')
        .with_tags({"foo": "bar"})
        .with_root_device_type('ebs')).to(matchers.be_greater_or_equal_to(1))
