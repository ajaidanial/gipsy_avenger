import boto3
from django.conf import settings


class AwsEc2Client:
    """
    Client class for handling the AWS.EC2 sdk. Contains all the app necessary
    handler methods. Used across the application.
    """

    def __init__(self):
        """On init create the client."""

        self.client = boto3.client(
            "ec2",
            region_name=settings.AWS_REGION_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    def get_all_instances(self, result=[], **kwargs) -> list[dict]:  # noqa
        """Returns all the `InstanceId` and `KeyName` of the instances."""

        # response
        response = self.client.describe_instances(**kwargs)

        # generate result
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                result.append(
                    {
                        "id": instance["InstanceId"],
                        "tags": [
                            _["Value"] for _ in instance["Tags"] if _["Key"] == "Name"
                        ],
                        "instance_type": instance["InstanceType"],
                    }
                )
        NextToken = response.get("NextToken", None)

        # end of result
        if not NextToken:
            return result

        # recursive query from aws
        return self.get_all_instances(result=result, NextToken=NextToken)

    def get_all_instance_types(self, result=[], **kwargs) -> list:  # noqa
        """
        Returns all the available EC2 `instance_types` like r6gd.2xlarge etc.

        Ref:
            1. https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html
            2. https://aws.amazon.com/ec2/instance-types/
        """

        # response
        response = self.client.describe_instance_types(**kwargs)

        # generate result
        for instance_type in response["InstanceTypes"]:
            result.append(instance_type["InstanceType"])
        NextToken = response.get("NextToken", None)

        # end of result
        if not NextToken:
            return result

        # recursive query from aws
        return self.get_all_instance_types(result=result, NextToken=NextToken)


def get_client():
    """Central adaptor function to return the app AWS client."""

    return AwsEc2Client()
