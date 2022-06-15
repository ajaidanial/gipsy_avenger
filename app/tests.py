from app.aws_ec2 import get_client


def test_aws_ec2_client():
    """Runs necessary tests for `AwsEc2Client` to prevent breakages."""

    client = get_client()

    for method in ["get_all_instance_types", "get_all_instances"]:
        try:
            getattr(client, method)()
        except Exception as e:
            raise AssertionError(f"Error while executing: {method}. Error: {e}")
