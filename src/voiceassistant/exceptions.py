"""Host custom exceptions."""


class AssistantBaseException(Exception):
    """Base assistant exception."""


class NlpException(AssistantBaseException):
    """Natural Language Processor Error."""