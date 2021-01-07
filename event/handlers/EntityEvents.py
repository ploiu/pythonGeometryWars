from event.Event import ENTITY_HURT_EVENT


def entity_hurt(hurt_event):
    hurt_entity = hurt_event.__dict__['hurt_entity']
    attacking_entity = hurt_event.__dict__['attacking_entity']
    hurt_entity.current_health -= int(hurt_event.__dict__['damage'])
    print('PAIN PEKO')


# export this list to register them all
handlers = {
    ENTITY_HURT_EVENT: [entity_hurt]
}
