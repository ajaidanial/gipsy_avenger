# Setup AWS Tokens

In order to downgrade or upgrade the EC2 instance we need a programmatic IAM user
with the necessary EC2 instance permissions. Follow the steps given
below to get the necessary tokens from AWS.

1. Login to your AWS account where the EC2 instances to modify are hosted.
2. Click on the `IAM` account management service, move to the `Users` section and click on `Add User`.
3. Provide the necessary name and make sure to check the `Access key - Programmatic access` option.
4. Now select `Attach existing policies directly`, from the permission make sure to check `AmazonEC2FullAccess`.
5. Save the user and make sure to copy the given `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` on completion.
6. The necessary `AWS_REGION_NAME` is the region name where your instances are hosted. Can be got from the region dropdown on the right-hand side top.

References:
1. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console
2. https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console
