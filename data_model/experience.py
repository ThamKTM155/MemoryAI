class Experience:

    def __init__(
        self,
        title="",
        topic="",
        channel="",
        hook="",
        views=0,
        ctr=0.0,
        retention=0.0,
        status="",
        reason="",
        lessons=None,
        next_action="",
        date="",
        source="",
        version="V1",
        id=""
    ):

        self.title = title
        self.topic = topic
        self.channel = channel
        self.hook = hook

        self.views = views
        self.ctr = ctr
        self.retention = retention

        self.status = status
        self.reason = reason

        self.lessons = lessons or []

        self.next_action = next_action

        self.date = date
        self.source = source
        self.version = version
        self.id = id