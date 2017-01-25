class APNsException(Exception):
    '''
    A base class for all exceptions raised by PyAPNs2.
    '''
    pass


class InternalException(APNsException):
    '''
    A base class for internal APNs exceptions which, if raised, can point to a bug in PyAPNs2.
    '''


class BadPayloadException(APNsException):
    '''
    A base class for exceptions which signify an error in the notification payload.
    '''


class PayloadEmpty(BadPayloadException):
    def __init__(self):
        super(PayloadEmpty, self).__init__('The message payload was empty.')


class PayloadTooLarge(BadPayloadException):
    def __init__(self):
        super(PayloadTooLarge, self).__init__(
            'The message payload was too large. The maximum payload size is 4096 bytes.'
        )


class BadTopic(BadPayloadException):
    def __init__(self):
        super(BadTopic, self).__init__('The apns-topic was invalid.')


class TopicDisallowed(BadPayloadException):
    def __init__(self):
        super(TopicDisallowed, self).__init__('Pushing to this topic is not allowed.')


class BadMessageId(InternalException):
    def __init__(self):
        super(BadMessageId, self).__init__('The apns-id value is bad.')


class BadExpirationDate(BadPayloadException):
    def __init__(self):
        super(BadExpirationDate, self).__init__('The apns-expiration value is bad.')


class BadPriority(InternalException):
    def __init__(self):
        super(BadPriority, self).__init__('The apns-priority value is bad.')


class MissingDeviceToken(APNsException):
    def __init__(self):
        super(MissingDeviceToken, self).__init__(
            'The device token is not specified in the request :path. Verify that the :path header '
            'contains the device token.'
        )


class BadDeviceToken(APNsException):
    def __init__(self):
        super(BadDeviceToken, self).__init__(
            'The specified device token was bad. Verify that the request contains a valid token '
            'and that the token matches the environment.'
        )


class DeviceTokenNotForTopic(APNsException):
    def __init__(self):
        super(DeviceTokenNotForTopic, self).__init__(
            'The device token does not match the specified topic.'
        )

class Unregistered(APNsException):
    def __init__(self):
        super(Unregistered, self).__init__(
            'The device token is inactive for the specified topic.'
        )


class DuplicateHeaders(InternalException):
    def __init__(self):
        super(DuplicateHeaders, self).__init__('One or more headers were repeated.')


class BadCertificateEnvironment(APNsException):
    def __init__(self):
        super(BadCertificateEnvironment, self).__init__(
            'The client certificate was for the wrong environment.'
        )


class BadCertificate(APNsException):
    def __init__(self):
        super(BadCertificate, self).__init__('The certificate was bad.')


class Forbidden(APNsException):
    def __init__(self):
        super(Forbidden, self).__init__('The specified action is not allowed.')


class BadPath(APNsException):
    def __init__(self):
        super(BadPath, self).__init__('The request contained a bad :path value.')


class MethodNotAllowed(InternalException):
    def __init__(self):
        super(MethodNotAllowed, self).__init__('The specified :method was not POST.')


class TooManyRequests(APNsException):
    def __init__(self):
        super(TooManyRequests, self).__init__(
            'Too many requests were made consecutively to the same device token.'
        )


class IdleTimeout(APNsException):
    def __init__(self):
        super(IdleTimeout, self).__init__('Idle time out.')


class Shutdown(APNsException):
    def __init__(self):
        super(Shutdown, self).__init__('The server is shutting down.')


class InternalServerError(APNsException):
    def __init__(self):
        super(InternalServerError, self).__init__('An internal server error occurred.')


class ServiceUnavailable(APNsException):
    def __init__(self):
        super(ServiceUnavailable, self).__init__('The service is unavailable.')


class MissingTopic(BadPayloadException):
    def __init__(self):
        super(MissingTopic, self).__init__(
            'The apns-topic header of the request was not specified and was required. '
            'The apns-topic header is mandatory when the client is connected using a certificate '
            'that supports multiple topics.'
        )


class ConnectionError(APNsException):
    def __init__(self):
        super(ConnectionError, self).__init__('There was an error connecting to APNs.')


def exception_class_for_reason(reason):
    return {
        'PayloadEmpty': PayloadEmpty,
        'PayloadTooLarge': PayloadTooLarge,
        'BadTopic': BadTopic,
        'TopicDisallowed': TopicDisallowed,
        'BadMessageId': BadMessageId,
        'BadExpirationDate': BadExpirationDate,
        'BadPriority': BadPriority,
        'MissingDeviceToken': MissingDeviceToken,
        'BadDeviceToken': BadDeviceToken,
        'DeviceTokenNotForTopic': DeviceTokenNotForTopic,
        'Unregistered': Unregistered,
        'DuplicateHeaders': DuplicateHeaders,
        'BadCertificateEnvironment': BadCertificateEnvironment,
        'BadCertificate': BadCertificate,
        'Forbidden': Forbidden,
        'BadPath': BadPath,
        'MethodNotAllowed': MethodNotAllowed,
        'TooManyRequests': TooManyRequests,
        'IdleTimeout': IdleTimeout,
        'Shutdown': Shutdown,
        'InternalServerError': InternalServerError,
        'ServiceUnavailable': ServiceUnavailable,
        'MissingTopic': MissingTopic,
    }[reason]
