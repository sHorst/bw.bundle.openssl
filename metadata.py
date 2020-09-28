defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'ca-certificates': {'installed': True}
        }
    }
