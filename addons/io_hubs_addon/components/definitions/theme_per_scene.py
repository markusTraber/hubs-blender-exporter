from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class ThemePerScene(HubsComponent):
    _definition = {
        'name': 'theme-per-scene',
        'display_name': 'Theme per scene',
        'category': Category.SCENE,
        'node_type': NodeType.SCENE,
        'panel_type': [PanelType.SCENE],
        'icon': 'LINKED',
    }

    themeId: StringProperty(name="Theme ID", description="Theme ID",
                         default="")
