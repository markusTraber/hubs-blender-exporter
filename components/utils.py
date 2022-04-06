import bpy
from ..gizmos.gizmo_group import update_gizmos


def get_modules_in_folder(folder):
    from os.path import basename, isfile, join
    import glob
    modules = glob.glob(join(folder, "*.py"))
    return [basename(f)[:-3] for f in modules if isfile(f)
            and not f.endswith('__init__.py')]


def register_components_in_folder(modules, folder, registered_modules):
    import importlib
    for module_name in modules:
        if (module_name != folder):
            module = importlib.import_module(
                '.' + module_name, folder)
            registered_modules.append(module)
            print("Register component: " + module.__name__)
            module.register()


def unregister_components_in_folder(registered_modules):
    for module in registered_modules:
        print("Unregister component: " + module.__name__)
        module.unregister()


def add_component(obj, component_name):
    item = obj.hubs_component_list.items.add()
    item.name = component_name


def remove_component(obj, component_name):
    items = obj.hubs_component_list.items
    items.remove(items.find(component_name))
    del obj[component_name]


def has_component(obj, component_name):
    items = obj.hubs_component_list.items
    return component_name in items


def has_components(obj, component_names):
    items = obj.hubs_component_list.items
    for name in component_names:
        if name not in items:
            return False
    return True


def add_gizmo(obj, gizmo_id):
    if not gizmo_id:
        return
    gizmo = obj.hubs_object_gizmos.add()
    gizmo.name = gizmo_id
    update_gizmos(None, bpy.context)


def remove_gizmo(obj, gizmo_id):
    gizmos = obj.hubs_object_gizmos
    gizmos.remove(gizmos.find(gizmo_id))
    update_gizmos(None, bpy.context)


def get_object_source(context, panel_type):
    if panel_type == "material":
        return context.material
    elif panel_type == "bone":
        return context.bone or context.edit_bone
    elif panel_type == "scene":
        return context.scene
    else:
        return context.object


def dash_to_title(s):
    return s.replace("-", " ").title()
