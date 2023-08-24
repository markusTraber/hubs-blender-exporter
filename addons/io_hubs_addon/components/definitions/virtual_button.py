from bpy.props import BoolProperty, StringProperty, EnumProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType

class VirtualButton(HubsComponent):
    _definition = {
        'name': 'virtual-btn',
        'display_name': 'Virtual Button',
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'OBJECT_DATA'
    }

    isPlaying: BoolProperty(
        name='Is Playing', description='The animations are already playing.', default=False)

    id: StringProperty(
        name="ID", description="An identifier for all related animations", default='btn1')

    loopType: EnumProperty(
        name="Loop Type",
        description="Defines how the animation should loop",
        items=[("loop-repeat", "Loop Repeat", "Playing the animation on repeat, each time jumping from the end of the clip directly to its beginning"),
               ("loop-once", "Loop Once", "Playing the animation once"),
               ("loop-once-reverse", "Loop Once Reverse (Door)", "Playing the animation once, then playing it in reverse. This is useful for doors."),
               ("loop-pingpong", "Loop Ping Pong", "Playing the animation on repeat forwards and backwards.")],
        default="loop-repeat")

    def draw(self, context, layout, panel):
        layout.prop(data=self, property="id")
        layout.prop(data=self, property="isPlaying")
        layout.prop(data=self, property="loopType")

        layout.separator()

        layout.label(text='1) Place this component onto the button object.')
        layout.label(text='2) Fill in a unique ID above for each Button (if multiple).')
        layout.label(text='3) Naming of Animations:')
        layout.label(text='    Button: VirtualButton-<id>')
        layout.label(text='    Other Animations: VirtualButton-<id>-*')
        layout.label(text='4) When exporting, activate "Group by NLA Track"')
        layout.label(text='See documentation for more details.', icon='INFO')