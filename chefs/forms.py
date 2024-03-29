from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Profile, Comment


class UserProfileForm(forms.ModelForm):
    """
    - user profile form to update and set chef profile.
    - clean() Custom validation logic for form fields.

    """

    class Meta:
        model = Profile
        fields = [
            "name",
            "image",
            "email",
            "phone_number",
            "gender",
            "Region",
            "country",
            "city",
            "cuisine_specialization",
            "instructions",
            "facebook_link",
            "instagram_link",
            "tiktok_link",
            "youtube_link",
            "dish1",
            "dish2",
            "dish3",
            "dish4",
            "dish5",
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        city = cleaned_data.get("city")
        country = cleaned_data.get("country")
        cuisine = cleaned_data.get("cuisine_specialization")
        phone_number = cleaned_data.get("phone_number")
        instructions = cleaned_data.get("instructions")
        url_fields = [
            "facebook_link",
            "instagram_link",
            "youtube_link",
            "tiktok_link",
        ]

        valid_characters1 = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        )
        valid_characters2 = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,-/ "
        )
        valid_characters3 = set("0123456789 -()+")
        max_length = 5000

        if name and not all(char in valid_characters1 for char in name):
            self.add_error("name", "Name should contain only letters.")
        if city and not all(char in valid_characters1 for char in city):
            self.add_error("city", "City should contain only letters.")
        if country and not all(char in valid_characters1 for char in country):
            self.add_error("country", "Country should contain only letters.")
        if cuisine:
            if len(
                [char for char in cuisine if char.isalpha()]
            ) < 3 or not all(char in valid_characters2 for char in cuisine):
                self.add_error(
                    "cuisine_specialization",
                    "The cuisine should consist of letters and symbols , - /",
                )
        if phone_number:
            if len(
                [char for char in phone_number if char.isdigit()]
            ) < 6 or not all(
                char in valid_characters3 for char in phone_number
            ):
                self.add_error(
                    "phone_number",
                    "Phone Number should consist of digits and symbols -,+,()",
                )
        if len(instructions) > max_length:
            raise forms.ValidationError(
                f"schedules field exceeds a limit of {max_length} characters."
            )
        for field_name in url_fields:
            field_value = cleaned_data.get(field_name)
            if field_value:
                platform_name = field_name.split("_")[0]
                if platform_name not in field_value.lower():
                    self.add_error(
                        field_name,
                        f"Invalid {platform_name.capitalize()} URL.",
                    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Changes"))


class CommentForm(forms.ModelForm):
    """
    - comment form to submit a new comment on chef profile.
    - clean() Custom validation logic for form fields.
    """

    class Meta:
        model = Comment
        fields = ["name", "email", "comment"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        comment = cleaned_data.get("comment")

        valid_characters = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        )

        if name and not all(char in valid_characters for char in name):
            self.add_error("name", "Name should contain only letters.")
        if comment:
            letter_count = sum(char.isalpha() for char in comment)
            if letter_count < 10:
                self.add_error(
                    "comment",
                    "Comment must contain words please!.",
                )
