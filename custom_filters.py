def get_nav_item(context, key):
    return context.get(key)

def setup(env):
    env.filters['get_nav_item'] = get_nav_item
