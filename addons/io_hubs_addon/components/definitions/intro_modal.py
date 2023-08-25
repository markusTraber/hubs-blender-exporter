from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class IntroModal(HubsComponent):
    _definition = {
        'name': 'intro-modal',
        'display_name': 'Intro Modal',
        'category': Category.SCENE,
        'node_type': NodeType.SCENE,
        'panel_type': [PanelType.SCENE],
        'icon': 'LINKED',
    }

    href: StringProperty(name="Intro Modal URL", description="Intro Modal URL. '{lang}' is necessary and will be replaced with the language code.",
                         default="https://ternaty.com/?lang={lang}")
