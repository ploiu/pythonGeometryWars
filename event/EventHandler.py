# a list of registered event handlers; key is event code and value is a list of functions that will execute the event
registered_handlers = {}


def register_event_handler(event_code, event_handler):
    if event_code in registered_handlers:
        current_handlers = registered_handlers[event_code]
        # now add the handler to the current handlers
        current_handlers.append(event_handler)
    else:
        # event code is not being used, create a new list of handlers for the code
        current_handlers = [event_handler]
        registered_handlers[event_code] = current_handlers


def process_event(event):
    # for each event handler we have registered for the event code, call the handler with the event
    if event.type in registered_handlers:
        event_handlers = registered_handlers[event.type]
        for handler in event_handlers:
            # invoke the handler with the event
            handler(event)


def register_event_handlers(event_code, event_handlers):
    for handler in event_handlers:
        register_event_handler(event_code, handler)
