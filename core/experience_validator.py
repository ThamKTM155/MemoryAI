class ExperienceValidator:

    REQUIRED_FIELDS = [
        "title",
        "topic",
    ]

    def validate(self, experience):

        for field in self.REQUIRED_FIELDS:

            value = getattr(experience, field, None)

            if value is None:
                raise ValueError(
                    f"{field} cannot be None"
                )

            if str(value).strip() == "":
                raise ValueError(
                    f"{field} cannot be empty"
                )

        return True