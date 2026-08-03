def create_entities(nodes, field, entity_type):

    entities = {}

    for node in nodes:

        value = node.get(field)

        if not value:

            continue

        # Nếu là list (ví dụ tags)
        if isinstance(value, list):

            values = value

        else:

            values = [value]

        for item in values:

            if item not in entities:

                entities[item] = {

                    "id": item,

                    "type": entity_type,

                    "name": item

                }

    return list(entities.values())