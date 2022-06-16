from django.forms import ChoiceField, ModelForm

from app.aws_ec2 import get_client
from app.models import AlterEC2Request


class AlterEC2RequestForm(ModelForm):
    """Form which handles the creation of the `AlterEC2Request`."""

    class Meta:
        model = AlterEC2Request
        fields = [
            "name",
            "instance_for_action",
            "day_of_action",
            "time_of_action",
            "change_to_instance_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # load data from AWS client
        self.fields["instance_for_action"] = ChoiceField(
            choices=[
                (_["instance_id"], _["name"] if _["name"] else _["instance_id"])
                for _ in get_client().get_all_instances()
            ]
        )
        self.fields["change_to_instance_type"] = ChoiceField(
            choices=[(_, _) for _ in get_client().get_all_instance_types()]
        )

        # widget customisation
        self.fields["time_of_action"].widget.input_type = "time"
        self.fields["time_of_action"].widget.attrs["step"] = "1800"  # every 30 minutes

    def save(self, commit=True):
        """Custom data insert on save."""

        instance = super().save(commit=False)

        # set the name for user reference
        instance.instance_name = instance.instance_for_action
        for choice in self.fields["instance_for_action"].choices:
            if choice[0] == instance.instance_for_action:
                instance.instance_name = choice[1]
                break

        instance.save()
        return instance
