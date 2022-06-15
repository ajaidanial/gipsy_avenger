import itertools
from contextlib import suppress

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

    def get_all_results(
        self, client_method, results=None, pre_processor=None, **kwargs
    ) -> list:
        """
        When a listing `client_method` from AWS is triggered, it will only return the
        first page result. We use the `NextToken` to get other pages recursively.

        This is a central function used in listing methods, to get all
        pages data and return it, in the last page.

        Definitions:
            client_method       => Method to be invoked in the AWS EC2 Client
            results             => The output got by recursive querying
            pre_processor       => To pre-process each dict of data
            kwargs              => For passing in the api calls
        """

        if not pre_processor:
            pre_processor = lambda _: _  # noqa

        if not results:
            results = []

        # aws response
        response = getattr(self.client, client_method)(**kwargs)

        # pre-process & generate result
        for data in response[list(response.keys())[0]]:
            results.append(pre_processor(data))

        # next page token
        NextToken = response.get("NextToken", None)

        # end of result
        if not NextToken:
            return results

        # recursive query from aws
        return self.get_all_results(
            client_method=client_method,
            results=results,
            pre_processor=pre_processor,
            NextToken=NextToken,
        )

    def get_all_instances(self) -> list[dict]:
        """
        Returns the `InstanceId`, `InstanceType` and `Name` of the instances
        that is available, for the given AWS credentials on settings.
        """

        def _pre_processor(data):
            result = []

            for instance in data["Instances"]:
                name = None
                with suppress(IndexError):
                    name = [_["Value"] for _ in instance["Tags"] if _["Key"] == "Name"][
                        0
                    ]

                result.append(
                    {
                        "instance_id": instance["InstanceId"],
                        "name": name,
                        "instance_type": instance["InstanceType"],
                    }
                )

            return result

        return list(
            itertools.chain.from_iterable(
                self.get_all_results(
                    client_method="describe_instances", pre_processor=_pre_processor
                )
            )
        )

    def get_all_instance_types(self) -> list:
        """
        Returns all the available EC2 `instance_types` like r6gd.2xlarge etc.

        Ref:
            1. https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html
            2. https://aws.amazon.com/ec2/instance-types/
        """

        return self.get_all_results(
            client_method="describe_instance_types",
            pre_processor=lambda data: data["InstanceType"],
        )


def get_client():
    """Central adaptor function to return the app AWS client."""

    return AwsEc2Client()
